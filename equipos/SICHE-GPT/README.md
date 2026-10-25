# Entrega del equipo SICHE-GPT

**Nombre del equipo:** SICHE-GPT  
**Nombre del robot en el programa:** SICHE  
**Nombre y versión del código:** SICHE_estudio, versión recomendada  
**Fecha de entrega:** 25 de octubre de 2026

El código y la configuración de esta entrega son copias idénticas de la versión recomendada. SICHE-GPT identifica al equipo; no se cambió el nombre interno SICHE ni ninguna instrucción del programa.

## Archivos

| Archivo | Función |
|---|---|
| SICHE_estudio.py | Código fuente completo del controlador. |
| SICHE_estudio.blocks | Archivo original del editor de bloques, correspondiente al Python. |
| SICHE_estudio.json | Posiciones de los tres sensores existentes. |
| FICHA_TECNICA.md | Esta documentación. |

RoboLiga/Webots proporciona la biblioteca RobotRL y el modelo base del robot. No hay imágenes, claves ni otros archivos propios necesarios.

## Estrategia y sensores

SICHE lee dos sensores frontales de distancia, el brillo del piso y dos bumpers traseros. Decide en cada ciclo sin esperas que bloqueen la vigilancia del borde. No conoce la identidad ni la posición del rival.

1. **Borde:** una lectura del piso superior a 85 dispara retroceso inmediato a −90/−90. También confirma el borde con dos lecturas consecutivas superiores a 70. Después del retroceso usa un giro a 60/−60. Los contadores limitan la secuencia; una nueva lectura de borde puede reiniciarla.
2. **Bumpers:** si un bumper trasero se presiona y ambos sensores frontales están ciegos, avanza a 100/100.
3. **Búsqueda:** sin rival detectado, gira a ±35 según el último lado donde lo vio.
4. **Seguimiento:** con un solo sensor frontal activo, avanza en curva a 40/100 o 100/40. Con ambos activos, corrige diferencias de más de 8 unidades mediante 75/100 o 100/75. Si está alineado o ambas distancias son menores de 12, empuja recto a 100/100.

| Sensor o motor | Método de RobotRL | Respuesta |
|---|---|---|
| Distancia izquierda y derecha | getDI(), getDD() | Búsqueda, alineación y empuje. |
| Piso | getColorPiso() | Retroceso y giro prioritarios ante borde. |
| Bumpers traseros | getBI(), getBD() | Avance si el frente no ve al rival. |
| Motores izquierdo y derecho | setVI(), setVD() | Órdenes de velocidad entre −100 y 100. |

Una distancia de 100 se interpreta como ausencia de detección. La orden de velocidad 100 no mide fuerza ni desplazamiento real. El JSON sitúa los sensores de distancia en (−22, +4, −40) mm y (+22, +4, −40) mm; el sensor de piso está en (0, −10, −40) mm. Los sensores frontales tienen 4 mm de altura local.

## Funcionamiento observado y límites

Esta versión ganó **62 de 108** peleas en el protocolo histórico: 25/36 contra rara, 11/36 contra Alexino y 26/36 contra Kawasaki. En otra muestra, bajo una réplica de las reglas de la aplicación y con SICHE en ambos colores, ganó 41/72. Son protocolos distintos y ninguna cifra garantiza resultados futuros.

El programa rindió mejor frente a rara y Kawasaki que frente a Alexino. Alexino puede levantar el frente de SICHE y empujarlo hacia afuera mientras los sensores frontales pierden información útil. El sensor de piso delantero no siempre detecta a tiempo una salida por atrás o por un costado. Las configuraciones de competición de los rivales no se conocen; se usaron sus modelos base disponibles. Se probaron cambios posteriores, pero ninguno demostró una mejora equilibrada que justifique reemplazar SICHE_estudio.

## Ejecución en Webots / RoboLiga

1. Mantené SICHE_estudio.py y SICHE_estudio.blocks juntos en la misma carpeta. El archivo de bloques permite abrir el programa en el editor visual.
2. En la aplicación, cargá SICHE_estudio.py como programa del color elegido para SICHE.
3. Cargá SICHE_estudio.json en **Robot base del mismo color**. Programa y hardware se seleccionan por separado.
4. Después de reiniciar la simulación, verificá ambos archivos seleccionados.

Para el robot rojo, RoboLiga carga el programa en el controlador Webots **robot0Controller**. Para el verde usa **robot1Controller**. No hace falta renombrar el Python para cambiar de color.

## Integridad

Los tres archivos del programa enviados conservan sus huellas SHA-256 originales:

| Archivo | SHA-256 |
|---|---|
| SICHE_estudio.py | 99327c51103bf61d0139c92d4ca3bacf53046e0f3d57b879d981c36760620b00 |
| SICHE_estudio.blocks | 56a4ceaa3d0a4dfda2308da2681b1ae8b4c96230b6e8f05c88a9ff14996956cf |
| SICHE_estudio.json | 363a4ebe2260192217ebef591499bf8e5ab1f984fc0066a4a4ba54647a062ca6 |

---

**Líder del proyecto:** Laureano Monteros  
**Sitio web personal:** pendiente de agregar  
**Contacto:** pendiente de agregar
