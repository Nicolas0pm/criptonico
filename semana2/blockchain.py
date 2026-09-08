from block import Block

DIFICULTAD = 4  # ceros iniciales requeridos (ajustable, ver Sección 5.2 de la guía)
RECOMPENSA_MINERIA = 50


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.mempool = []  # Actividad 2.5: transacciones pendientes

    def create_genesis_block(self):
        return Block(0, ["Genesis Block - Criptonico"], "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction_to_mempool(self, transaction):
        # Actividad 2.5/2.8: solo entra al mempool si pasó la verificación de firma
        self.mempool.append(transaction)

    def mine_pending_transactions(self, miner_address):
        # Actividad 2.6: toma las transacciones del mempool y mina un nuevo bloque
        transactions = list(self.mempool)

        # Transacción de recompensa para quien mina (no requiere firma: la crea la red)
        reward_tx = {
            "de": "RED",
            "para": miner_address,
            "monto": RECOMPENSA_MINERIA
        }
        transactions.append(reward_tx)

        new_block = Block(
            index=self.get_last_block().index + 1,
            transactions=transactions,
            previous_hash=self.get_last_block().hash
        )
        new_block.mine_block(DIFICULTAD)

        self.chain.append(new_block)
        self.mempool = []  # se vacía el mempool tras confirmar
        return new_block

    def get_balance(self, address):
        # Actividad 2.7: recorre TODA la cadena confirmada (nunca el mempool)
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if isinstance(tx, dict):
                    if tx.get("para") == address:
                        balance += tx["monto"]
                    if tx.get("de") == address:
                        balance -= tx["monto"]
        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                print(f"Bloque {current.index} inválido: el hash no coincide.")
                return False
            if current.previous_hash != previous.hash:
                print(f"Bloque {current.index} inválido: no está bien encadenado.")
                return False
        return True