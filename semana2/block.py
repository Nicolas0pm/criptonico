import hashlib
import json
import time


class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        contenido = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(contenido).hexdigest()

    def mine_block(self, difficulty):
        # Busca un nonce tal que el hash empiece con 'difficulty' ceros (Sección 2.3.1)
        objetivo = "0" * difficulty
        while self.hash[:difficulty] != objetivo:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Bloque {self.index} minado. Nonce: {self.nonce} | Hash: {self.hash}")