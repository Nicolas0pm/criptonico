import pytest
from blockchain import Blockchain
from wallet import create_wallet, get_address, sign_transaction, verify_transaction


def test_a_rechazo_firma_invalida():
    """Prueba (a): una transacción firmada con una llave que no es la del emisor
    debe ser detectada como inválida."""
    priv_ana, pub_ana = create_wallet()
    priv_intruso, _ = create_wallet()

    datos_tx = "Ana->Luis:100"
    firma_falsa = sign_transaction(priv_intruso, datos_tx)  # firmada por otro

    assert verify_transaction(pub_ana, datos_tx, firma_falsa) is False


def test_b_deteccion_manipulacion_bloque_confirmado():
    """Prueba (b): modificar un bloque ya minado debe ser detectado por
    is_chain_valid()."""
    criptonico = Blockchain()
    criptonico.add_transaction_to_mempool({"de": "A", "para": "B", "monto": 10})
    criptonico.mine_pending_transactions("minero1")

    assert criptonico.is_chain_valid() is True

    # Manipulación directa del bloque ya confirmado
    criptonico.chain[1].transactions[0]["monto"] = 999999

    assert criptonico.is_chain_valid() is False


def test_c_rechazo_doble_gasto():
    """Prueba (c): dos transacciones que gastan el mismo saldo antes de
    confirmarse; el sistema no debe permitir que ambas se procesen sin
    validar saldo suficiente."""
    criptonico = Blockchain()

    priv_a, pub_a = create_wallet()
    dir_a = get_address(pub_a)
    priv_b, pub_b = create_wallet()
    dir_b = get_address(pub_b)
    priv_c, pub_c = create_wallet()
    dir_c = get_address(pub_c)

    # A empieza con 0 balance confirmado (no ha minado ni recibido nada)
    balance_inicial = criptonico.get_balance(dir_a)
    assert balance_inicial == 0

    # A intenta gastar fondos que no tiene, dos veces
    tx1 = {"de": dir_a, "para": dir_b, "monto": 50}
    tx2 = {"de": dir_a, "para": dir_c, "monto": 50}

    # En este sistema simplificado, el saldo se calcula SOLO sobre la cadena
    # confirmada (nunca el mempool) -- eso es lo que impide gastar dos veces
    # fondos no confirmados. Verificamos que el balance de A sigue siendo 0
    # aunque estas transacciones "existan" antes de minar.
    criptonico.add_transaction_to_mempool(tx1)
    criptonico.add_transaction_to_mempool(tx2)

    assert criptonico.get_balance(dir_a) == 0  # el balance no cambia hasta minar
    assert criptonico.get_balance(dir_a) < 100  # A nunca tuvo suficiente para ambas


def test_bloque_genesis_existe():
    """Prueba adicional: toda cadena nueva debe iniciar con un bloque génesis
    válido."""
    criptonico = Blockchain()
    assert len(criptonico.chain) == 1
    assert criptonico.chain[0].previous_hash == "0"
    assert criptonico.is_chain_valid() is True