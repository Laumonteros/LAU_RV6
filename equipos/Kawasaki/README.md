# Entrega del programa Kawasaki

**Nombre del equipo:** no informado. Kawasaki es el nombre declarado por el programa.  
**Nombre y versión del código:** Kawasaki, archivo recibido más reciente kawasaki.py.  
**Fecha de esta entrega:** 25 de octubre de 2026.

El Python de esta carpeta es una copia idéntica del archivo recibido. La copia anterior Kawasaki (1).py tiene la misma huella SHA-256, por lo que no se incluye como una versión distinta.

## Archivos y dependencias

| Archivo | Función |
|---|---|
| kawasaki.py | Código fuente completo. |
| FICHA_TECNICA.md | Esta descripción. |

No se recibió un archivo original de bloques ni una configuración JSON de Kawasaki. El programa importa RobotRL, suministrado por la instalación de RoboLiga/Webots, y utiliza el modelo base disponible cuando no se carga una configuración propia. No se agregaron bloques o hardware supuestos.

## Estrategia

Kawasaki busca al rival girando, se orienta con los dos sensores frontales de distancia y avanza a máxima velocidad cuando ambos detectan. La variable interna variable cambia a 1 tras la primera detección.

- Si el brillo del piso supera 90, ordena retroceder con ambas ruedas a −70 durante dos segundos y luego girar con motor izquierdo −60 y derecho +60 durante un segundo.
- Con ambas distancias menores o iguales a 80, ordena +100/+100.
- Si solo el sensor derecho ve una distancia inferior a 80 mientras el izquierdo supera 80, gira con derecho −60 e izquierdo +60.
- Si solo el izquierdo ve una distancia inferior a 80 mientras el derecho supera 80, gira en el sentido contrario.
- Antes de la primera detección, busca con derecho +50 e izquierdo −50. Tras esa primera detección, si ninguna condición vuelve a ordenar motores, permanece la última orden.

El programa imprime las dos distancias en cada ciclo de búsqueda o seguimiento. Hay una función adicional llamada girar_d que ordena +60/+60, pero no aparece en el flujo de ejecución.

## Sensores y motores

| Dispositivo | Método de RobotRL | Respuesta |
|---|---|---|
| Distancia izquierda y derecha | getDI(), getDD() | Búsqueda, giro y ataque. |
| Sensor de piso | getColorPiso() | Retroceso y giro al superar 90. |
| Motor izquierdo y derecho | setVI(), setVD() | Órdenes de −70 a +100 en las ramas usadas. |

El programa no consulta los bumpers. Los valores de distancia y velocidad son lecturas y órdenes del simulador; no miden fuerza ni desplazamiento real.

## Funcionamiento y límites conocidos

Su lógica de ataque es simple y directa: cuando ambos sensores detectan al rival, empuja a +100/+100. El giro sobre el eje con un solo sensor puede orientar el frente rápidamente. La respuesta al borde usa esperas de dos y un segundo; durante esos intervalos el bucle principal no vuelve a decidir con lecturas nuevas. Después de la primera detección, perderla no inicia necesariamente una búsqueda nueva: la última orden puede continuar. Los umbrales usan comparaciones estrictas y no todas las combinaciones con una lectura exactamente igual a 80 producen una orden nueva. Estas son observaciones del código; no se modificó para corregirlas.

No se conoce el JSON empleado por Kawasaki fuera de los ensayos locales. Por eso esta ficha no atribuye posiciones de sensores ni resultados de competición a una configuración que no fue entregada.

## Ejecución en Webots / RoboLiga

Cargá kawasaki.py como programa del color elegido en la aplicación. RoboLiga lo coloca en robot0Controller si juega como rojo y en robot1Controller si juega como verde. La biblioteca RobotRL y el modelo base proceden de la instalación. La aplicación permite cargar una configuración de robot por separado, pero este paquete no contiene una configuración propia recibida.

**SHA-256 del Python original y de esta copia:** 83164ebe266efe50538d91f7594359f7949c9834fda3877f75638d2f168fd8e7.

---

**Líder del proyecto:** Laureano Monteros  
**Sitio web personal:** pendiente de agregar  
**Contacto:** pendiente de agregar
