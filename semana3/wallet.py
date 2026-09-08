import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1


def create_wallet():
    # Actividad 2.1: genera el par de llaves privada/pública
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key


def get_address(public_key):
    # Actividad 2.2: la "dirección" se deriva aplicando SHA-256 a la llave pública
    public_key_bytes = public_key.to_string()
    return hashlib.sha256(public_key_bytes).hexdigest()


def sign_transaction(private_key, transaction_data: str):
    # Actividad 2.3: firma la transacción con la llave privada del emisor
    return private_key.sign(transaction_data.encode())


def verify_transaction(public_key, transaction_data: str, signature) -> bool:
    # Actividad 2.4: cualquier nodo puede verificar con la llave pública
    try:
        return public_key.verify(signature, transaction_data.encode())
    except Exception:
        return False