from blockchain import Blockchain

# Crear la cadena (con su bloque génesis automático)
criptonico = Blockchain()

# Actividad 1.2/1.3: agregar al menos 5 bloques encadenados
criptonico.add_block(["Nico envía 10 CRN a Ana"])
criptonico.add_block(["Ana envía 5 CRN a Luis"])
criptonico.add_block(["Luis envía 2 CRN a Nico"])
criptonico.add_block(["Nico envía 1 CRN a Ana"])
criptonico.add_block(["Ana envía 3 CRN a Luis"])

print("=== Estado de la cadena ===")
for block in criptonico.chain:
    print(f"Bloque {block.index} | hash: {block.hash[:16]}... | prev: {block.previous_hash[:16]}...")

print("\n=== Validación ANTES de manipular ===")
print("¿Cadena válida?", criptonico.is_chain_valid())

# Actividad 1.5: prueba de manipulación
print("\n>>> Manipulando el bloque 2 (cambiando la transacción)...")
criptonico.chain[2].transactions = ["Ana envía 5000 CRN a Luis (FRAUDE)"]

print("\n=== Validación DESPUÉS de manipular ===")
print("¿Cadena válida?", criptonico.is_chain_valid())