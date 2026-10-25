# AU_RV6 — RoboLiga Virtual de Sumo

Repositorio privado para organizar y documentar los programas de los equipos que participan en RoboLiga Virtual de Sumo. Los controladores están desarrollados en Python para ejecutarse con Webots y la biblioteca `RobotRL` provista por la aplicación.

## Estado actual

La entrega del 25 de octubre de 2026 reúne tres programas: **SICHE-GPT**, **Kawasaki** y **Alexino**. Cada uno se conserva en su propia carpeta para facilitar su revisión y comparación. Los archivos fuente se copiaron sin modificar su contenido; los nombres de Kawasaki y Alexino se normalizaron para que sean más claros. Las fichas técnicas adjuntas describen cómo funciona cada programa y sus límites conocidos.

La documentación de esta entrega identifica a **SICHE_estudio** como la versión recomendada actualmente para SICHE-GPT, porque es la que tiene respaldo de comparación en los materiales recibidos. Esa recomendación describe el estado documentado del proyecto, no garantiza resultados futuros.

## Estructura

```text
AU_RV6/
├── README.md
├── equipos/
│   ├── SICHE-GPT/
│   │   ├── README.md
│   │   ├── GUIA_SICHE.md
│   │   ├── SICHE_estudio.py
│   │   ├── SICHE_estudio.blocks
│   │   └── SICHE_estudio.json
│   ├── Kawasaki/
│   │   ├── README.md
│   │   └── kawasaki.py
│   └── Alexino/
│       ├── README.md
│       └── alexino_v4.py
└── docs/
    └── competencia/
        └── README.md
```

## Cómo estamos trabajando

1. Cada equipo mantiene su código separado y envía la versión completa que quiere conservar.
2. Junto con el código se incluyen, cuando existan, el archivo de bloques, la configuración del robot y los recursos necesarios para ejecutarlo.
3. La descripción de cada programa se registra en el `README.md` de su carpeta: estrategia, sensores, decisiones, motores, ejecución y límites conocidos.
4. Se conserva el código recibido sin cambios al archivarlo. Las correcciones o nuevas estrategias deben identificarse como una versión nueva y compararse con una referencia clara.
5. Para comparar programas, se anotan las condiciones de prueba —color, orientación, lado y rival— y se separan los resultados de protocolos distintos. Una observación de una simulación no se presenta como una garantía general.
6. Los documentos comunes de reglas y competencia se guardan en `docs/competencia/`. Las guías propias de un robot permanecen junto a ese equipo.
7. No se suben contraseñas, claves ni tokens.

## Programas incluidos

| Equipo | Programa | Archivos adicionales | Descripción breve |
|---|---|---|---|
| SICHE-GPT | `SICHE_estudio.py` | Bloques originales y configuración JSON | Vigila el borde, busca y sigue al rival con sensores de distancia, y usa los bumpers traseros. |
| Kawasaki | `kawasaki.py` | Ninguno recibido | Busca girando, ataca con detecciones frontales y reacciona al brillo del piso. |
| Alexino | `alexino_v4.py` | Ninguno recibido | Combina reacción al piso, bumpers traseros y sensores frontales de distancia. |

Las descripciones detalladas y las instrucciones de carga están en el README de cada equipo. SICHE también incluye una guía de estudio y comparación.

## Cargar los programas

Los controladores se cargan desde la aplicación de RoboLiga/Webots para el color elegido. En los materiales recibidos, el controlador rojo corresponde a `robot0Controller` y el verde a `robot1Controller`. La configuración del robot se carga por separado del programa: para SICHE-GPT, cargar `SICHE_estudio.json` en el robot base del mismo color que el programa. Kawasaki y Alexino no incluyen una configuración propia en esta entrega.

## Documentación de competencia

En esta entrega no se recibió el reglamento oficial ni una guía general de la competencia. La carpeta `docs/competencia/` indica dónde agregarlos cuando estén disponibles. La guía de SICHE es específica de ese programa y está en `equipos/SICHE-GPT/GUIA_SICHE.md`.

---

**Líder del proyecto:** Laureano Monteros  
**Sitio web personal:** pendiente de agregar  
**Contacto:** pendiente de agregar
