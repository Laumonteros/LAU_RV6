# Parachoquesitos: revisión individual

Fecha: 9 de noviembre de 2026. Estado: hipótesis implementada; semejanza física pendiente de comprobar. No es el programa auténtico ni una mejora de SICHE.

## Evidencia de sus tres peleas

Los tiempos siguientes son segundos del archivo de video, no del reloj de batalla. Se revisaron los registros conservados, las trayectorias extraídas y los paneles visuales. El seguimiento de placas a 10 Hz no proporciona orientación, lecturas de sensores, fuerza ni contacto físico confirmado. Las oclusiones no se rellenan como si fueran posiciones conocidas.

| Video local | Color | Episodios relevantes | Resultado y alcance |
|---|---|---|---|
| Zona 1, ronda 1, 26/09/2026 | Rojo contra CHELSY | Aproximación y pequeñas separaciones aproximadamente 143–161 s; proximidad prolongada en una región interior hasta aproximadamente 295 s. | Empate. La persistencia del contacto no demuestra que esté intentando escapar ni que tenga más fuerza. |
| Zona 1, ronda 2, 10/10/2026 | Verde contra BOSCO BOTS Marquez | Aproximadamente 57–129 s: Parachoquesitos permanece en una región pequeña; Marquez repite recorridos que llegan progresivamente al borde. | Victoria con separación final. No hay evidencia de un empuje continuo hasta expulsar al rival. |
| Zona 1, ronda 3, 31/10/2026 | Rojo contra Merida | Merida hace recorridos amplios; encuentros aproximadamente 35–51 y 81–103 s. La placa roja queda oculta durante parte del segundo. Separación y salida de Merida al final. | Victoria. La inclinación impide deducir qué bumper o lectura causó cada reacción. |

Fuentes: videos originales en `work/drive_sumo_readonly/videos`; paneles y CSV `work/quarters_20261109/video/z1_r*_bout*.jpg` y `z1_r*_tracks.csv`; episodios conservados en `outputs/Cuartos_2026-11-09/Episodios_clasificados.json`. Los tres videos pertenecen a fechas distintas: no consta que mantuvieran el mismo programa.

## Desajuste detectado

El modelo v0.1 persigue con cualquier lectura válida inferior a 100. En el diagnóstico anterior, con un objetivo inmóvil delante a 0,35 m entre centros, alcanzó una separación inferior a 0,15 m en 0,928 s. Esa disposición a perseguir desde lejos no explica bien la permanencia de Parachoquesitos frente a Marquez. No es una comparación de situaciones idénticas: el rival del video se mueve y desconocemos el hardware original.

La separación entre placas y la distancia del sonar son medidas diferentes. No convertimos una en la otra para afirmar que recuperamos su umbral. También podrían explicar la permanencia un campo de visión estrecho, otra orientación del sensor, una condición adicional de ataque o un programa distinto entre rondas.

## Cambio acotado: v0.2 experimental

Se crea una variante con `LIMITE_RIVAL = 12`, frente al límite anterior de 100. Solo las lecturas menores de 12 activan la persecución; fuera de ese intervalo conserva el giro sobre su lugar. Se mantienen el ataque cercano, las correcciones de dirección y la protección de borde anteriores.

**12 es un punto inicial de ensayo, no una medición obtenida del video.** El cambio representa la hipótesis «se compromete a perseguir solo cuando el rival está cerca». Puede exagerar la pasividad o perder encuentros reales: todavía no se elige como réplica más fiel.

Se conservan dos posibilidades de bumper porque no podemos identificar esa rama: H1 avanza al activarse un bumper; H0 no usa esa condición. Ambas reciben exactamente el mismo cambio de distancia. Las velocidades y tiempos heredados también siguen siendo supuestos, no parámetros recuperados.

## Comprobación y siguiente diagnóstico

El registro `verificacion.json` comprueba límites del umbral, detección por ambos lados, prioridad del piso y conservación de las decisiones anteriores en secuencias de contacto y recuperación. Esto verifica programación, no similitud con el rival. No se ejecutaron batallas nuevas en esta revisión.

Cuando retomemos el diagnóstico, comparar v0.1 y v0.2 en rojo y verde: permanencia frente a pasadas separadas, inicio de aproximación, continuidad del contacto y reacción a la separación. Usar también distancias próximas al nuevo límite para detectar oscilaciones. Evaluar los encuentros completos, no seleccionar solo fotogramas favorables. Si falla la aproximación observada contra CHELSY o Merida, rechazar o revisar esta hipótesis; no compensar cambiando varios parámetros a la vez.

SICHE_estudio y los siete modelos anteriores se conservan sin cambios. Este estudio no aporta una nueva estadística de victorias ni justifica sustituir la recomendación de competición.
