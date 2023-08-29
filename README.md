# juego_de_la_vida.py

Esta es una implementación del famoso **Juego de la Vida de Conway** en Python. El Juego de la Vida es un autómata celular creado por el matemático británico John Conway en 1970. Es un ejemplo clásico de cómo reglas simples pueden dar lugar a comportamientos complejos.

El juego se desarrolla en una cuadrícula bidimensional donde cada celda puede estar viva o muerta. Las células evolucionan de acuerdo con reglas simples:

1. Una célula viva con menos de 2 vecinos vivos muere (por soledad).
2. Una célula viva con 2 o 3 vecinos vivos permanece viva.
3. Una célula viva con más de 3 vecinos vivos muere (por sobrepoblación).
4. Una célula muerta con exactamente 3 vecinos vivos se convierte en una célula viva (por reproducción).

## Requisitos

- Python 3.x

## Como jugar
1. Sigue las instrucciones en la consola para establecer la configuración inicial de la cuadrícula.
2. Observa cómo evolucionan las células con cada generación.

## Recursos

- [Wikipedia: Juego de la Vida](https://es.wikipedia.org/wiki/Juego_de_la_vida)
- [Artículo original por John Conway](https://web.stanford.edu/class/sts145/Library/life.pdf)

## Notas
- No se ha usado ninguna libreria adicional
- El código está comentado
- Este es un archivo antiguo, de cuando estaba aprendiendo Python. El código es funcional, pero ni mucho menos óptimo (de antes de ChatGPT :P)
