from flask import Flask, jsonify, request
from blockchain import Blockchain
from wallet import verify_transaction, create_wallet, get_address
from ecdsa import VerifyingKey, SECP256k1, BadSignatureError

app = Flask(__name__)
criptonico = Blockchain()

# Wallet propia de este nodo (para recibir recompensa al minar)
mi_priv, mi_pub = create_wallet()
MI_DIRECCION = get_address(mi_pub)


@app.route('/transacciones/nueva', methods=['POST'])
def nueva_transaccion():
    datos = request.get_json()
    requeridos = ['de', 'para', 'monto', 'firma', 'llave_publica_hex']
    if not all(k in datos for k in requeridos):
        return jsonify({"error": "Faltan campos en la transacción"}), 400

    try:
        llave_publica = VerifyingKey.from_string(
            bytes.fromhex(datos['llave_publica_hex']), curve=SECP256k1
        )
        firma = bytes.fromhex(datos['firma'])
        datos_tx = f"{datos['de']}->{datos['para']}:{datos['monto']}"

        if not verify_transaction(llave_publica, datos_tx, firma):
            return jsonify({"error": "Firma inválida, transacción rechazada"}), 400

    except (BadSignatureError, ValueError, Exception) as e:
        return jsonify({"error": f"Firma inválida: {str(e)}"}), 400

    tx = {"de": datos['de'], "para": datos['para'], "monto": datos['monto']}
    criptonico.add_transaction_to_mempool(tx)
    return jsonify({"mensaje": "Transacción añadida al mempool", "transaccion": tx}), 201


@app.route('/cadena', methods=['GET'])
def obtener_cadena():
    cadena_data = []
    for block in criptonico.chain:
        cadena_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "transactions": block.transactions,
            "previous_hash": block.previous_hash,
            "nonce": block.nonce,
            "hash": block.hash
        })
    return jsonify({"longitud": len(cadena_data), "cadena": cadena_data}), 200


@app.route('/minar', methods=['GET'])
def minar():
    if not criptonico.mempool:
        return jsonify({"mensaje": "No hay transacciones pendientes para minar"}), 200

    nuevo_bloque = criptonico.mine_pending_transactions(MI_DIRECCION)
    return jsonify({
        "mensaje": "Bloque minado exitosamente",
        "index": nuevo_bloque.index,
        "hash": nuevo_bloque.hash,
        "nonce": nuevo_bloque.nonce
    }), 200


@app.route('/balance/<direccion>', methods=['GET'])
def balance(direccion):
    saldo = criptonico.get_balance(direccion)
    return jsonify({"direccion": direccion, "balance": saldo}), 200


@app.route('/mi-direccion', methods=['GET'])
def mi_direccion():
    return jsonify({"direccion_nodo": MI_DIRECCION}), 200


if __name__ == '__main__':
    print(f"Dirección de este nodo (minero): {MI_DIRECCION}")
    app.run(host='0.0.0.0', port=5000, debug=True)