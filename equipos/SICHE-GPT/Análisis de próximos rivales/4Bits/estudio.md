# 4Bits: contacto sostenido y oscilación central

Se revisaron los gráficos de trayectoria contra LOMAS y Troya, y se incorporó el episodio previamente revisado contra LOS UNICOS. Esto no constituye una reproducción nueva y continua de las tres grabaciones.

## Resultado concreto
En la pelea contra Troya, 4Bits permanece próximo durante aproximadamente 150 segundos y describe un movimiento repetitivo en una región interior pequeña. La autocorrelación del radio de su placa entre los segundos 185 y 325 del video presenta un máximo cerca de 6,5 segundos, buscando retardos entre 2 y 11,9 s. Se repite la medición en dos subventanas para comprobar estabilidad; los valores exactos quedan en el JSON adjunto.

Es una periodicidad de posición observada, no una prueba de temporizador, lectura de sonar ni velocidad de rueda. Puede proceder del contacto de ambos cuerpos, correcciones del controlador, movimiento de Troya o geometría del seguimiento visual. No se convierte en una maniobra programada cada 6,5 segundos.

Frente a LOMAS, desde aproximadamente 46 s hay proximidad sostenida y desplazamiento hacia el borde, con LOMAS más afuera. Frente a LOS UNICOS hay un encuentro breve y salida después de separación. Un mismo modelo debe poder producir contacto estable y desplazamiento conjunto según el encuentro; no debe forzarse un resultado distinto identificando el rival.

## Decisión sobre el código
Se conserva el programa anterior y sus alternativas H0/H1. No hay todavía una discrepancia simulada que permita elegir una nueva asimetría de motores o un temporizador. Agregar cualquiera de ellos solo para tener una versión nueva no demostraría mayor fidelidad.

Se comprobaron 5000 ciclos consecutivos con ambas lecturas cercanas por alternativa: conserva ataque sin un rescate periódico. Después, una lectura de borde interrumpe inmediatamente el ataque. Son pruebas de lógica, no peleas; no reproducen la oscilación física.

## Comparación pendiente en Webots
Con hardware base común, ejecutar ambos colores y las mismas condiciones para modelo anterior y cualquier candidata posterior. Registrar aproximación, separación, tamaño de la región recorrida y periodicidad durante contacto; aplicar la misma proyección o una medida geométrica comparable antes de enfrentar curvas de simulador y video. No basta coincidir con 6,5 s o con el ganador. La oscilación depende también del modelo de Troya, que no está reconstruido; por tanto una prueba frente a SICHE no puede validar por sí sola este episodio.

Estado: revisión y objetivo cuantitativo de fidelidad completados; código conservado; validación física pendiente. SICHE permanece intacto.
