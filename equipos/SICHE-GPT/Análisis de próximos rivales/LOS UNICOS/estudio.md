# LOS UNICOS: continuidad después de perder detección

## Evidencia revisada
Se inspeccionaron los paneles de fotogramas de las rondas 2 y 3 y el gráfico de trayectoria de la ronda 1 de zona 4. No es una revisión continua de todos los fotogramas. Se extrajeron medianas por segundo de sus posiciones en las tres apariciones; las coordenadas son normalizadas por la elipse del ring, no mediciones del simulador.

- Troya, ronda 1, verde, 8–21 s: recorridos interiores, acercamiento y separación; Troya termina fuera mientras LOS UNICOS queda dentro.
- LOMAS, ronda 2, rojo, 8–160 s: cambios de posición interiores y varios encuentros separados por recorridos. No se mantiene sobre un único punto.
- 4Bits, ronda 3, verde, 8–18 s: encuentro inicial, separación y desplazamiento hacia arriba hasta la salida. El desplazamiento tras la separación es relevante; no demuestra que estuviera sin detección.

## Alternativa implementada
El modelo anterior vuelve inmediatamente al giro de búsqueda cuando ambos sensores dejan de detectar. La alternativa conserva la última orden de seguimiento hasta 16 ciclos sin detección (512 ms si el ciclo es 32 ms), y luego vuelve al giro. Una detección nueva actualiza la orden y el contador. El piso y la recuperación de borde cancelan la memoria y tienen prioridad; los bumpers también la cancelan. No se conserva una orden de escape de borde como si fuera ataque.

Se generan H0 y H1, manteniendo la incertidumbre de respuesta a bumpers. El cambio no utiliza posición global, datos del contrario ni información del video durante la ejecución. No hay esperas bloqueantes.

## Límites y criterio de comparación
512 ms es un parámetro inicial supuesto, no una duración recuperada del video. Persistir puede explicar desplazamiento tras pérdida breve de lectura, pero también puede aumentar salidas propias. Las trayectorias observadas podrían explicarse por lecturas que siguen siendo válidas, inercia, contacto, orientación del hardware o cambios de programa entre fechas.

Comparar la alternativa y el modelo anterior en rojo y verde: continuidad tras separación, extensión de recorridos interiores contra LOMAS y salida contra 4Bits. La réplica debe reproducir también limitaciones, pero no se debe forzar una derrota desactivando el borde. Rechazar esta alternativa si agrega excursiones que no aparecen en los videos o si solo coincide con el resultado final.

Estado: dos programas creados, pruebas de lógica de duración, ambos sentidos, reactivación y prioridad de borde superadas. Falta simulación de fidelidad. No se afirma que sean más fieles hasta compararlos. SICHE y las versiones anteriores permanecen intactos.
