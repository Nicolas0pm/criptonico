# Diagrama de arquitectura - Criptonico

```mermaid
flowchart TD
    Cliente[Cliente / cliente_prueba.py] -->|POST /transacciones/nueva| API[API REST - Flask]
    Cliente -->|GET /minar| API
    Cliente -->|GET /balance/direccion| API
    Cliente -->|GET /cadena| API

    API --> Wallet[wallet.py<br/>firma y verificación ECDSA]
    API --> Mempool[(Mempool<br/>transacciones pendientes)]
    API --> Blockchain[blockchain.py<br/>Blockchain]

    Blockchain --> Block1[block.py<br/>Block: hash, nonce, PoW]
    Blockchain --> Validacion[is_chain_valid]
    Mempool -->|al minar| Block1
    Block1 -->|se agrega a| Chain[(Cadena de bloques)]
```

## Componentes

- **wallet.py**: genera pares de llaves (ECDSA/secp256k1), deriva direcciones,
  firma y verifica transacciones.
- **block.py**: define la estructura de un bloque y el algoritmo de minería
  (Proof of Work).
- **blockchain.py**: mantiene la cadena, el mempool, calcula balances y valida
  la integridad de toda la cadena.
- **nodo.py**: expone todo lo anterior como una API REST con Flask.
- **cliente_prueba.py**: simula un usuario externo que crea una wallet, firma
  una transacción y la envía al nodo.