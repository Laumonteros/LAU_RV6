# Entrega del programa Alexino

**Nombre del equipo:** no informado. Alexino es el nombre declarado por el programa.  
**Nombre y versión del código:** Alexino v4, archivo recibido más reciente alexino_v4.py.  
**Fecha de esta entrega:** 25 de octubre de 2026.

El Python de esta carpeta es una copia idéntica del archivo recibido. Alexino v4.py y alexino_v4.py tienen la misma huella SHA-256, por lo que se conserva una sola copia.

## Archivos y dependencias

| Archivo | Función |
|---|---|
| alexino_v4.py | Código fuente completo. |
| FICHA_TECNICA.md | Esta descripción. |

No se recibió un archivo original de bloques ni una configuración JSON de Alexino. El programa usa la biblioteca RobotRL suministrada por RoboLiga/Webots. En las pruebas locales se empleó el modelo base disponible; no se conoce su posible configuración de competición.

## Estrategia

Alexino empieza ordenando −100/−100 durante medio segundo. Después, en cada ciclo, consulta primero el piso, luego los bumpers y por último las distancias frontales:

1. Si el brillo del piso supera 85, gira con izquierdo −100 y derecho +100 durante 300 ms y avanza a +100/+100 durante 700 ms.
2. Si se presionan ambos bumpers, ordena retroceso a −100/−100. Si se presiona solo uno, primero ordena un giro y después retrocede. Sin bumpers presionados, mantiene un giro sobre el eje.
3. Si ambas distancias frontales son inferiores a 3, retrocede a −100/−100 durante 200 ms.
4. Si una distancia es inferior a 4 y la otra no detecta (100 o más), gira sobre el eje durante 450 ms hacia el lado programado.

Las órdenes posteriores de bumpers o distancias pueden reemplazar la última orden de una maniobra de piso después de que terminan sus esperas. Cuando no se cumple una condición nueva de distancias, queda vigente la orden tomada por la lógica de bumpers. El programa imprime mensajes y algunas lecturas para diagnóstico.

## Sensores y motores

| Dispositivo | Método de RobotRL | Respuesta |
|---|---|---|
| Distancia izquierda y derecha | getDI(), getDD() | Retroceso muy cercano o giro lateral. |
| Sensor de piso | getColorPiso() | Giro y avance al superar 85. |
| Bumpers izquierdo y derecho | getBI(), getBD() | Retroceso cuando hay contacto. |
| Motor izquierdo y derecho | setVI(), setVD() | Avance, retroceso y giro con órdenes de −100 a +100. |

Los sensores y motores pertenecen al modelo y a RobotRL. La velocidad ordenada no es una medida de fuerza ni demuestra por sí sola desplazamiento real.

## Funcionamiento y límites conocidos

La reacción a los bumpers traseros es una característica destacada: puede cambiar de inmediato la dirección de empuje durante el contacto. Los umbrales de distancia muy cortos activan maniobras diferentes de las de búsqueda. En los ensayos locales frente a SICHE, esos contactos fueron difíciles para SICHE; ello no establece una tasa general de victorias de Alexino.

Las llamadas a esperar detienen la nueva evaluación del bucle durante 200, 300, 450, 500 o 700 ms, según la rama, y la secuencia de piso puede sumar un segundo. La reacción posterior a bumpers y distancias puede sobrescribir una orden previa. Existen funciones definidas que no son llamadas por el bucle principal, como GIRO_LOCO, culo_atras, parar y Avanzar. Se describen estas limitaciones sin alterar el archivo recibido.

## Ejecución en Webots / RoboLiga

Cargá alexino_v4.py como programa del color elegido en la aplicación. RoboLiga lo coloca en robot0Controller si juega como rojo y en robot1Controller si juega como verde. La biblioteca RobotRL y el modelo base proceden de la instalación. Una configuración propia del robot se carga por separado si su autor la proporciona; este paquete no incluye una no recibida.

**SHA-256 del Python original y de esta copia:** 6a12e987139c2550eae92f2af476d23230b3061f8c3c8214f1798aa23ded73b9.

---

**Líder del proyecto:** Laureano Monteros  
**Sitio web personal:** pendiente de agregar  
**Contacto:** pendiente de agregar
