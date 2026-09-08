# Cómo se extendería Criptonico a una red de nodos

Aunque en esta entrega Criptonico corre como un solo nodo, el sistema está diseñado
para poder extenderse a una red distribuida sin cambiar su lógica central. Así se
haría:

1. **Registro de nodos** (`POST /nodos/registrar`): cada nodo mantendría una lista
   de direcciones (IP:puerto) de otros nodos conocidos. Al levantar un nuevo nodo,
   este se registraría con al menos un nodo existente, y ese nodo le compartiría su
   lista de pares conocidos.

2. **Propagación de transacciones**: cuando un nodo recibe una transacción nueva en
   su mempool, la reenviaría (broadcast) a todos los nodos que conoce, para que
   todos tengan el mismo conjunto de transacciones pendientes.

3. **Resolución de conflictos** (`GET /nodos/resolver`): cuando dos nodos minan
   bloques distintos casi al mismo tiempo (una bifurcación o "fork"), cada nodo
   consultaría la cadena de sus pares y aplicaría la regla de la cadena más larga
   (Sección 2.6.1 de la guía): la cadena con más trabajo computacional acumulado
   gana, y los nodos con la cadena más corta la reemplazan por la más larga
   (siempre que sea válida según is_chain_valid()).

4. **Consenso eventual**: con este mecanismo, aunque los nodos no confíen entre sí
   ni se conozcan de antemano, eventualmente todos convergen hacia el mismo
   historial de transacciones, sin necesidad de una autoridad central — resolviendo
   así el Problema de los Generales Bizantinos mencionado en la Sección 1.2 de la
   guía.

Esta arquitectura es la razón por la que diseñamos is_chain_valid() para poder
validar cualquier cadena recibida de un tercero, no solo la propia: esa misma
función sería la que usaría cada nodo para decidir si acepta la cadena de otro nodo
como la nueva verdad compartida.