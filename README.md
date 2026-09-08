# Criptonico

Criptomoneda educativa construida desde cero para el taller de Blockchain de
Ingeniería de Software - Universidad Manuela Beltrán (UMB).

Elaborado por: Nicolás — usuario GitHub `Nicolas0pm`

## Estructura del proyecto

- `semana1/` — Fundamentos: clase `Block`, clase `Blockchain`, validación de
  integridad (`is_chain_valid`).
- `semana2/` — Wallets (ECDSA), firma/verificación de transacciones, Proof of
  Work, mempool, balances y recompensa de minería.
- `semana3/` — API REST (Flask), pruebas de seguridad (pytest), documentación
  y arquitectura del sistema.

## Cómo ejecutar (Semana 3 - versión final)

### 1. Instalar dependencias

```bash
cd semana3
py -m pip install flask ecdsa requests pytest
```

### 2. Levantar el nodo

```bash
py nodo.py
```

El servidor queda escuchando en `http://127.0.0.1:5000`.

### 3. Probar con el cliente de ejemplo (en otra terminal)

```bash
py cliente_prueba.py
```

Esto crea una wallet, firma una transacción, la envía al nodo, mina un bloque
y consulta balances.

### 4. Endpoints disponibles

| Método | Endpoint                  | Descripción                                  |
|--------|----------------------------|-----------------------------------------------|
| POST   | `/transacciones/nueva`    | Registra una transacción firmada en el mempool |
| GET    | `/cadena`                 | Devuelve la blockchain completa                |
| GET    | `/minar`                  | Mina un nuevo bloque con las transacciones pendientes |
| GET    | `/balance/<direccion>`    | Consulta el balance de una dirección           |
| GET    | `/mi-direccion`           | Devuelve la dirección del nodo (minero)        |

### 5. Correr las pruebas de seguridad

```bash
py -m pytest test_seguridad.py -v
```

## Documentación adicional

- [`semana3/explicacion_red_nodos.md`](semana3/explicacion_red_nodos.md) —
  cómo se extendería el sistema a una red de nodos.
- [`semana3/diagrama_arquitectura.md`](semana3/diagrama_arquitectura.md) —
  diagrama de arquitectura del sistema.
- [`semana2/comparativo_pow_pos.md`](semana2/comparativo_pow_pos.md) —
  comparación Proof of Work vs Proof of Stake.