# Proof of Work vs Proof of Stake

En Proof of Work (PoW), el mecanismo que implementamos en Criptonico, el derecho a
proponer el siguiente bloque se gana resolviendo un problema computacional: encontrar
un nonce tal que el hash del bloque cumpla una condición de dificultad (empezar con
cierta cantidad de ceros). Esto significa que atacar la red requiere poder de cómputo
real (hardware y energía), lo cual es su principal fortaleza en términos de seguridad,
pero también su mayor desventaja: consume una cantidad de energía muy alta, como se ve
en redes reales como Bitcoin.

En Proof of Stake (PoS), en cambio, el derecho a proponer un bloque no se gana
compitiendo por cómputo, sino que se asigna de forma probabilística según cuánta
moneda tiene "apostada" (staked) cada participante en la red. Su ventaja principal es
que el consumo energético es significativamente menor, como ocurre en Ethereum desde
su migración a PoS (The Merge, 2022). Su desventaja es que el costo de atacar la red
ya no depende de infraestructura física, sino de capital económico bloqueado, lo que
puede favorecer a quienes ya tienen más moneda acumulada.

En resumen: PoW prioriza seguridad probada por consumo real de recursos físicos, a
costa de energía; PoS prioriza eficiencia energética, a costa de depender de
incentivos económicos en vez de un costo físico verificable.