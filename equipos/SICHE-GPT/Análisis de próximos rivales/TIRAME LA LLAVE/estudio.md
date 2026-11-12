# TIRAME LA LLAVE: hipótesis de avance intermitente

Se midieron posiciones individuales en las aproximaciones de las rondas 1 y 2, usando medianas de ventanas de 0,6 segundos del seguimiento existente. Coordenadas normalizadas por la elipse del ring, no metros ni poses reales. El ruido de placa y perspectiva impide interpretar movimientos pequeños como órdenes de motor.

Contra Nocco (8–24 s), su placa roja permanece alrededor de x=-0,275. TIRAME pasa de x=0,299 a 0,047, con una caída marcada entre 13 y 14 s (0,245 a 0,139), mientras en otras ventanas apenas cambia o retrocede ligeramente. Contra Armon (25–28 s), Armon pasa de x=-0,193 a -0,005 y TIRAME de 0,302 a 0,201. Por tanto, el cierre rápido del segundo episodio no exige que TIRAME use un programa diferente: Armon también se acerca.

Se añade una alternativa ejecutable de aproximación por impulsos: cuatro ciclos de avance y giro de búsqueda durante el resto de un período de 120 ciclos. A 32 ms, son 128 ms y 3,84 s. Ambos números son hipótesis de ensayo, no parámetros identificados. Al detectar distancia menor de 10 se mantiene el ataque cercano; borde y recuperación tienen prioridad y no hay esperas bloqueantes. Se ofrecen H0 y H1 para la incertidumbre de bumpers.

No se reemplaza el modelo lento: el giro entre impulsos puede perder detección y reiniciar el contador, produciendo más avances de los previstos. Es una consecuencia que debe medirse, no ocultarse. El período se cuenta en ciclos con detección lejana, no es un reloj absoluto desde el inicio de la pelea.

La irregularidad también puede surgir de detección intermitente sin temporizador. Esta alternativa no permite afirmar que el programa auténtico tenga un contador. Debe compararse con el modelo lento en ambos colores, evaluando desplazamiento individual, pausa entre avances y contacto con Armon. Coincidir con el ganador no es criterio suficiente.

Estado: nueva hipótesis implementada y comprobada en lógica. No simulada, no seleccionada como réplica más fiel. SICHE y el paquete anterior permanecen sin cambios. Los otros seis modelos siguen pendientes de refinamiento equivalente.
