import requests
from wallet import create_wallet, get_address, sign_transaction

NODO = "http://127.0.0.1:5000"

# Crear una wallet de prueba (simula a "Ana")
priv_ana, pub_ana = create_wallet()
dir_ana = get_address(pub_ana)

# Obtener la dirección del nodo (el minero) para enviarle fondos
respuesta = requests.get(f"{NODO}/mi-direccion")
dir_nodo = respuesta.json()["direccion_nodo"]
print("Dirección del nodo (minero):", dir_nodo)
print("Dirección de Ana:", dir_ana)

# --- 1. Transacción VÁLIDA: el nodo (que ya tiene 50 de una minería previa) le envía a Ana ---
# Nota: para esta prueba simple, Ana firma un envío hacia sí misma desde su propia wallet
datos_tx = f"{dir_ana}->{dir_nodo}:5"
firma = sign_transaction(priv_ana, datos_tx)

payload = {
    "de": dir_ana,
    "para": dir_nodo,
    "monto": 5,
    "firma": firma.hex(),
    "llave_publica_hex": pub_ana.to_string().hex()
}

r = requests.post(f"{NODO}/transacciones/nueva", json=payload)
print("\n--- Transacción válida ---")
print(r.status_code, r.json())

# --- 2. Minar el bloque ---
r = requests.get(f"{NODO}/minar")
print("\n--- Minado ---")
print(r.status_code, r.json())

# --- 3. Consultar balances ---
r = requests.get(f"{NODO}/balance/{dir_nodo}")
print("\n--- Balance del nodo ---")
print(r.status_code, r.json())

r = requests.get(f"{NODO}/balance/{dir_ana}")
print("\n--- Balance de Ana ---")
print(r.status_code, r.json())

# --- 4. Prueba de seguridad (a): firma inválida ---
print("\n=== Prueba de seguridad: firma inválida ===")
priv_falsa, pub_falsa = create_wallet()  # otra wallet, no la de Ana
datos_falsos = f"{dir_ana}->{dir_nodo}:1000"
firma_falsa = sign_transaction(priv_falsa, datos_falsos)  # firmado con llave equivocada

payload_falso = {
    "de": dir_ana,
    "para": dir_nodo,
    "monto": 1000,
    "firma": firma_falsa.hex(),
    "llave_publica_hex": pub_ana.to_string().hex()  # dice ser de Ana, pero la firma no es de ella
}

r = requests.post(f"{NODO}/transacciones/nueva", json=payload_falso)
print(r.status_code, r.json())