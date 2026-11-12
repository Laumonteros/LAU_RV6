# Los destructores: cierre a distancia reducida

## Revisión de evidencia
Se inspeccionó el panel de fotogramas de zona 3, ronda 2 y los gráficos de trayectoria de rondas 1 y 3. No se reprodujeron nuevamente las tres peleas completas.

Frente a UPPER 6, tras el movimiento inicial, ambos permanecen separados durante casi toda la pelea. Frente a TAF, entre aproximadamente 73 y 80 s, hay aproximación y desenlace rápido. Frente a LOS INTOCABLES, 181–205 s, hay períodos largos de permanencia en una región pequeña, una excursión intermedia y movimiento final conjunto al borde.

El modelo actual persigue cualquier lectura válida menor de 100. Una alternativa que puede explicar la permanencia mientras el rival circula es iniciar el cierre solo a menor distancia. Se implementa límite 30 conservando búsqueda, ataque, correcciones, bumpers y borde. No se copia el límite 12 de Parachoquesitos: son hipótesis independientes.

**30 no se obtuvo como lectura real del video.** Es un valor inicial de ensayo. La distancia entre placas no equivale a la del sonar. La falta de encuentro también puede deberse al campo de visión, orientación, hardware o cambios de programa entre rondas. No se considera validada esta explicación.

## Comprobación necesaria
Comparar modelo anterior y alternativa en ambos colores. La alternativa debe conservar períodos sin aproximación, pero también poder realizar el cierre contra TAF y el encuentro final contra INTOCABLES. Si vuelve al robot pasivo durante esos encuentros, rechazarla. No basta reproducir el empate frente a UPPER 6.

Las alternativas H0/H1 preservan la incertidumbre de bumpers. Se verificaron límite exacto, lectura cercana, ambos sentidos, lectura inválida y prioridad de borde: 12 casos. No se ejecutaron batallas. SICHE y las versiones anteriores permanecen intactos.
