# Justificación conceptual - Semana 1

## ¿Por qué el efecto avalancha del hash es indispensable para detectar manipulación?

[Escribe aquí tu explicación: cómo un solo cambio en cualquier campo de un bloque
produce un hash completamente distinto, y por qué eso permite que is_chain_valid()
detecte cualquier alteración comparando el hash guardado contra el recalculado.]

## ¿Qué pasaría si se usara una función hash sin esa propiedad?

[Escribe aquí: si cambios pequeños produjeran cambios pequeños y predecibles en el
hash, alguien podría alterar una transacción y ajustar el hash "a mano" o por fuerza
bruta más fácil, haciendo que la manipulación pase desapercibida.]