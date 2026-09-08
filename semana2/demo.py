import time
from blockchain import Blockchain
from wallet import create_wallet, get_address, sign_transaction, verify_transaction

criptonico = Blockchain()

# --- Crear 2 wallets ---
priv_nico, pub_nico = create_wallet()
priv_ana, pub_ana = create_wallet()

dir_nico = get_address(pub_nico)
dir_ana = get_address(pub_ana)

print("Dirección de Nico:", dir_nico)
print("Dirección de Ana:", dir_ana)

# --- Transacción válida: Nico envía a Ana ---
datos_tx = f"{dir_nico}->{dir_ana}:20"
firma = sign_transaction(priv_nico, datos_tx)

if verify_transaction(pub_nico, datos_tx, firma):
    tx = {"de": dir_nico, "para": dir_ana, "monto": 20}
    criptonico.add_transaction_to_mempool(tx)
    print("\nTransacción válida añadida al mempool.")
else:
    print("\nTransacción rechazada: firma inválida.")

# --- Minar el bloque (Nico mina y recibe recompensa) ---
print("\nMinando bloque...")
criptonico.mine_pending_transactions(dir_nico)

# --- Consultar balances actualizados ---
print("\nBalance de Nico:", criptonico.get_balance(dir_nico))
print("Balance de Ana:", criptonico.get_balance(dir_ana))

# --- Actividad 2.8: prueba de rechazo de firma inválida ---
print("\n>>> Probando una firma falsificada (Ana intenta gastar en nombre de Nico) <<<")
datos_falsos = f"{dir_nico}->{dir_ana}:1000"
firma_falsa = sign_transaction(priv_ana, datos_falsos)  # firmado con la llave equivocada

if verify_transaction(pub_nico, datos_falsos, firma_falsa):
    print("ERROR: el sistema aceptó una firma inválida (no debería pasar).")
else:
    print("Correcto: el sistema RECHAZÓ la firma inválida antes de entrar al mempool.")

# --- Tabla comparativa de tiempos de minado con distintas dificultades ---
print("\n=== Comparación de tiempos de minado ===")
from block import Block
for dificultad in [2, 3, 4]:
    bloque_prueba = Block(99, ["prueba"], "0")
    inicio = time.time()
    bloque_prueba.mine_block(dificultad)
    duracion = time.time() - inicio
    print(f"Dificultad {dificultad}: {duracion:.4f} segundos, nonce final = {bloque_prueba.nonce}")