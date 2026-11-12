# Merida: revisión individual final de esta ronda

Estado: modelo v0.2 conservado; fidelidad física pendiente. Se revisaron los gráficos de CHELSY y Parachoquesitos y los registros conservados de las tres apariciones. No se afirma haber reproducido nuevamente las tres grabaciones completas.

## Evidencia y decisión
Contra CHELSY, Merida recorre repetidamente el perímetro con cambios de rumbo. Frente a Parachoquesitos alterna recorridos largos con encuentros; parte del contacto presenta placas ocultas. Contra Marquez, el registro incluye contacto prolongado y una posible relocalización. No se interpretan saltos de posición ni oclusiones como maniobras propias.

Se conserva la búsqueda con avance y la recuperación de borde. El umbral 40 del modelo actual proviene del diagnóstico previo con hardware base; NO es una lectura recuperada del programa auténtico. Cambiar otra vez ese valor, el tiempo de giro o la posición de cámara sin comparar trayectorias no demuestra mayor fidelidad. El modelo necesita reproducir recorridos amplios y retornos, además de poder perder tras una separación.

Se generaron medidas de las tres apariciones: cobertura de seguimiento, radio mediano y proporción de muestras válidas con radio superior a 0,85. Son indicadores de posición en imagen normalizada, no activaciones del sensor de piso. Los huecos no se cuentan como interior ni se interpolan. Una fracción no es una duración de contacto ni una probabilidad de salida.

## Pruebas y próximo contraste
Las dos alternativas H0/H1 conservan sus archivos exactos. Se comprobó búsqueda, contacto sostenido, umbral exacto del piso, prioridad del borde y finalización de seis ciclos de retroceso y ocho de giro después de dejar de detectar borde. Mientras el brillo sigue alto, el contador se recarga: no confundir duración después de abandonar blanco con duración total del escape.

En Webots hay que comparar frecuencia de retornos, profundidad del retorno hacia el interior y contacto con inclinación, en rojo y verde. Una mejor recuperación estática no basta si el umbral provoca falsos escapes en contacto. Se mantiene el mismo hardware base del rival, sin inventar su JSON auténtico. No se ejecutaron nuevas batallas en esta revisión.
