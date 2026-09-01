from block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # El bloque génesis no tiene bloque anterior real (Sección 2.2.1)
        return Block(0, ["Genesis Block - Criptonico"], "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        # Actividad 1.3: enlaza el nuevo bloque al último existente
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            transactions=transactions,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        # Actividad 1.4: recorre toda la cadena verificando integridad
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # ¿El hash guardado coincide con el hash recalculado?
            if current.hash != current.calculate_hash():
                print(f"Bloque {current.index} inválido: el hash no coincide.")
                return False

            # ¿El previous_hash coincide con el hash real del bloque anterior?
            if current.previous_hash != previous.hash:
                print(f"Bloque {current.index} inválido: no está bien encadenado.")
                return False

        return True