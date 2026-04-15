# AI Log — Tlahtoa Data
## Hack ODS UNAM 2026

---

## Herramientas utilizadas

| Herramienta | Integrante(s) | Uso principal |
|---|---|---|
| Claude (Anthropic) | Rafael, Zabdiel | Arquitectura de datos, estructura de código, auditoría de repositorio, integración OJS/Quarto |
| GitHub Copilot | Rafael, Zabdiel | Autocompletado de código en Python y JavaScript, boilerplate de scripts del pipeline |
| ChatGPT (OpenAI) | Ilse | Verificación de conceptos metodológicos, exploración de fuentes oficiales |

---

## Filosofía explícita de uso

En nuestro equipo decidimos utilizar la IA como lo que es: una herramienta veloz para las tareas mecánicas, no como un oráculo para nuestras decisiones de fondo.

Hay una línea que trazamos desde el inicio y que no se cruzó en ningún momento del hackathon: todo lo que requiere entender México, es decir, conocer el contexto de la desigualdad, decidir qué historia vale la pena contar, elegir las variables que miden lo que queremos medir y cuáles descartamos, eso es del equipo. Todo lo que es implementación técnica repetitiva, exploración de estructuras de código, validación de formato o generación de boilerplate, eso decidimos que podíamos acelerarlo con la IA.

Esto significa, en resumen, que dejamos que la IA nos ayudara a escribir un script de normalización min-max, pero no permitimos que esta decidiera si la formalidad laboral es la única variable que se invierte, ya que para esa decisión necesitamos saber qué estamos midiendo y por qué, así que eso no se delega.

---

## Registro de uso

### 2026-03-04 | Claude | Definición del marco analítico
**Prompt:** "Quiero construir un índice que mida desigualdad estructural por etapas de vida a nivel estatal en México. ¿Qué enfoques metodológicos existen para índices compuestos de desarrollo humano a nivel subnacional? Necesito que el índice sea transparente, replicable y construido solo con variables elementales verificables."

**Resultado:** Claude presentó varios enfoques: desagregación subnacional del IDH (PNUD), el Índice de Marginación de CONAPO, la medición multidimensional de pobreza de CONEVAL, y la opción de construir un índice propio con normalización min-max y ponderación por dimensiones.

**Decisión del equipo:** Rafael rechazó usar el IDH y el Índice de Marginación. Meter un índice compuesto de otra institución dentro del nuestro mezclaría dos construcciones analíticas y oscurecería qué estamos midiendo exactamente. Por esa razón decidió construir el IRTE desde cero con variables elementales verificables (con URL, fuente oficial y cobertura para los 32 estados). Esa decisión es la diferencia principal del proyecto contra la réplica de índices existentes y es completamente de Rafael.

---

### 2026-03-06 | ChatGPT | Investigación de fuentes oficiales
**Prompt:** "Ya identifiqué estas fuentes oficiales para datos estatales en México: CONEVAL para pobreza, INEGI Censo 2020 para servicios, SSA para mortalidad infantil, SEP para abandono escolar, CONAPO para fecundidad adolescente, IMSS para empleo formal. ¿Hay alguna fuente oficial que me falte para medir condiciones de vida por estado? También: ¿cuál es la diferencia exacta entre tasa de fecundidad adolescente y tasa de embarazo adolescente?"

**Resultado:** ChatGPT sugirió ENSANUT para salud y ENDIREH para violencia de género como fuentes adicionales. Explicó que la tasa de fecundidad adolescente mide nacimientos por 1,000 mujeres de 15-19 años, mientras que la tasa de embarazo incluye abortos y pérdidas — son conceptos distintos con denominadores diferentes. También citó algunas URLs que resultaron estar desactualizadas.

**Decisión del equipo:** Ilse confirmó lo que ya sospechaba: la investigación manual en los portales oficiales es mucho más confiable que depender de la IA para descubrir nuevas fuentes. ChatGPT confundió URLs y citó páginas que ya no existían. Por lo tanto, decidió quedarse con las fuentes que ella había verificado personalmente y usó la IA solo para aclarar la distinción fecundidad vs. embarazo, una distinción que el proyecto necesitaba documentar ya que se utilizó fecundidad_adolescente (CONAPO), no embarazo.

---

### 2026-03-12 | GitHub Copilot | Pipeline de procesamiento
**Prompt:** (Autocompletado en VS Code) Rafael escribió los docstrings y la estructura de cada script del pipeline — `01_build_base_indicators.py`, `02_compute_irte.py`, `03_generate_scenarios.py` — y dejó que Copilot generara el boilerplate de lectura de archivos, loops de normalización y escritura de CSVs.

**Resultado:** Copilot generó código funcional para la normalización min-max y la exportación a CSV. El código corría sin errores y producía outputs con el formato esperado.

**Decisión del equipo:** Rafael detectó un error sutil que Copilot no señaló: la normalización min-max se aplicó uniformemente a todas las variables, sin respetar la direccionalidad. `formalidad_laboral` es la única variable donde mayor valor = mejor condición (dirección positiva). Copilot la normalizó igual que las demás, produciendo scores invertidos para esa variable, es decir, un estado con alta formalidad recibía score de alto riesgo. El código no fallaba; los números eran incorrectos. Rafael lo detectó comparando los scores contra los datos crudos y corrigió la lógica de inversión manualmente: `score_riesgo = 1 - valor_normalizado` para formalidad laboral.

---

### 2026-03-18 | Claude | Narrativa del proyecto
**Prompt:** "Queremos usar la Lotería mexicana como metáfora para un proyecto de datos sobre desigualdad estructural en México. La idea es que el destino en la Lotería se decide por azar, igual que el estado donde naces. Necesito opciones de párrafo de apertura para el README que conecten el símbolo cultural con el argumento estadístico. Tono directo, sin dramatismo de ONG."

**Resultado:** Claude generó 4 versiones de párrafo de apertura. Todas conectaban la Lotería con la desigualdad pero con diferentes registros: una más poética, una más periodística, una más académica, una más provocadora.

**Decisión del equipo:** Ilse rechazó las 4 versiones tal como estaban. Las que sonaban poéticas caían en clichés sobre México. Las periodísticas sonaban a nota de prensa sensacionalista. Ilse tomó dos elementos que le parecieron honestos: la descripción de la Lotería como azar puro y la conversión del símbolo a estadística verificable, luego reescribió el párrafo con su propia voz. La frase final del README "en México, el estado donde naces no es sólo una cuestión de suerte, es estadística." es de Ilse, no de Claude. La metáfora de la Lotería como hilo conductor del proyecto surgió de una conversación del equipo semanas antes de abrir cualquier herramienta de IA, pues nos inspiramos en el juego "Dumb ways to die", una campaña australiana de prevención de riesgos y la gamificación como herramienta para generar engagement.

---

### 2026-03-25 | Claude | Arquitectura del frontend
**Prompt:** "Necesito diseñar un sistema de etapas para un juego interactivo en JavaScript donde cada etapa (nacimiento, infancia, adolescencia, adultez) pueda activarse o desactivarse independientemente. El juego debe poder crecer — agregar etapas cuando lleguen más datos — sin romper lo que ya funciona. ¿Qué patrón de diseño me conviene?"

**Resultado:** Claude propuso el patrón pipeline con un array de objetos de etapa, cada uno con su propia función `ejecutar()` y una bandera `activa`. Sugirió un layout de dashboard con paneles laterales y métricas en tarjetas.

**Decisión del equipo:** Zabdiel aceptó el patrón de arquitectura (array de etapas con ejecución independiente) pero rechazó completamente la propuesta visual. Claude sugería un dashboard corporativo con paneles y KPIs. Zabdiel decidió que el producto debía sentirse como un videojuego con atmósfera mexicana sutil, con guiños hacia la lotería mexicana, no una imitación demasiado folclórica con sombreros y cactus, sino detalles que evocaran familiaridad: la paleta con acentos dorados cálidos, la revelación de cartas como mecánica central, la sensación de que el destino se "lanza" y no se "calcula". Esa dirección visual es completamente del equipo y define la identidad del producto.

---

### 2026-03-29 | Claude | Decisiones de descarte del IRTE
**Prompt:** "Tengo 4 variables candidatas que cumplen cobertura y verificabilidad pero quiero descartar del IRTE: acceso_electricidad (correlación >0.80 con agua y drenaje), abandono_preparatoria (correlación 0.87 con secundaria), tasa_homicidios (mezcla violencia con desarrollo), PIB per cápita (mide producción no condiciones de vida). ¿Qué argumentos metodológicos formales existen para descartar variables de un índice compuesto por estas razones?"

**Resultado:** Claude explicó los argumentos estándar: inflación dimensional por colinealidad (VIF >5), redundancia en la varianza capturada (correlación de Pearson), confusión conceptual al mezclar constructos de diferentes dominios, y el principio de parsimonia en índices compuestos.

**Decisión del equipo:** Rafael ya había tomado las 4 decisiones de descarte por criterio propio. Usó a Claude para obtener el vocabulario técnico formal y documentar las decisiones en `docs/analytical_decisions.md`. La IA no tomó ninguna de esas decisiones, solo las articuló con lenguaje metodológico una vez que Rafael ya sabía qué quería descartar y por qué. La distinción es importante, pues pedir argumentos para una decisión tomada es diferente de pedir que la IA tome la decisión por ti.

---

### 2026-04-03 | Claude | Integración OJS en Quarto
**Prompt:** "Necesito cargar un archivo JSON externo en OJS dentro de un documento .qmd de Quarto. El JSON tiene datos de 32 estados mexicanos con scores, trayectorias y escenarios. Quiero alimentar selectores reactivos y gráficas de Plotly desde ese JSON. El tablero debe funcionar como sitio estático en GitHub Pages — sin servidor, sin Shiny, sin dependencias de runtime."

**Resultado:** Claude generó un ejemplo funcional usando `FileAttachment` para cargar el JSON y reactive statements de OJS para conectar selectores con visualizaciones de Plotly.

**Decisión del equipo:** Zabdiel aceptó la estructura base de carga y reactividad pero rediseñó el manejo de estado del jugador. Claude modeló el estado como variables sueltas (`estadoSeleccionado`, `etapaActual`, `sexo`). Zabdiel lo centralizó en un objeto único `jugador` que atraviesa todas las etapas del juego y mantiene el historial de decisiones. Esa decisión arquitectónica es la que hace posible agregar etapas futuras sin reescribir la lógica existente y es la razón por la que el tablero puede crecer cuando lleguen los datos de violencia, ingreso y planificación familiar que aún no tenemos.

---

### 2026-04-07 | Claude Code | Auditoría de datos y brechas
**Prompt:** Prompt de auditoría completa diseñado por el equipo para que Claude Code recorriera todos los archivos del repositorio Tlahtoa_Data_Team y produjera un reporte estructurado con: mapa del repositorio, contrato de datos, mapeo de variables al juego, estado del pipeline, archivos listos para el frontend, brechas y recomendación de estructura.

**Resultado:** Claude Code analizó 112 archivos de datos (56 CSV + 56 JSON), 18 scripts de Python, y toda la configuración y documentación. Produjo un reporte de 7 secciones con tablas de cobertura por variable y diagnóstico por etapa del juego. Identificó que 9 de 18 variables requeridas estaban completas, 1 parcial y 8 ausentes.

**Decisión del equipo:** El equipo usó el reporte como insumo, no como veredicto. Rafael decidió que mostrar las brechas honestamente era más valioso que simular datos que no existían. Las etapas de violencia y empleo quedan marcadas como "próximamente" en el tablero porque el equipo estuvo de acuerdo en que la honestidad sobre los límites del modelo es más defendible que la completitud artificial. La sección de brechas del README y del metadata.md es producto de esa decisión.

---

## Lo que deliberadamente NO delegamos a IA

Esta sección documenta las decisiones que el equipo tomó sin consultar, pedir sugerencias ni delegar a ninguna herramienta de IA. Esto es el núcleo de nuestro proyecto.

**1. La pregunta de investigación:** Medir la desigualdad como una trayectoria de vida acumulada desde el nacimiento, infancia, adolescencia, adultez, y no como un índice de momento puntual. Esta perspectiva es la contribución intelectual de nuestro equipo. No le preguntamos a ninguna IA cómo enmarcar el problema.

**2. La metáfora de la Lotería mexicana:** Usar la Lotería como hilo conductor, el azar del destino, la carta que te tocó, el "te tocó nacer aquí", todo esto surgió de una conversación del equipo. Si bien la IA ayudó a articular parte de la prosa, la metáfora es completamente nuestra.

**3. Qué variables entran al IRTE y cuáles se descartan:** La IA nos ofreció argumentos técnicos estándar cuando se los pedimos. Pero la decisión de excluir homicidios (mezcla narrativas), PIB per cápita (concepto incorrecto), electricidad (redundancia con agua y drenaje) y preparatoria (correlación 0.87 con secundaria) fue de Rafael. Cada descarte tiene una razón concreta documentada en el README, y no fue producto de una recomendación algorítmica.

**4. La investigación manual de fuentes oficiales:** Ilse recorrió personalmente los portales de CONEVAL, INEGI, SSA, SEP, CONAPO e IMSS antes de usar ninguna herramienta de IA. Verificó cada URL, cada año de referencia, cada licencia. La IA confundió URLs cuando se le preguntó, pero la investigación manual fue la más confiable.

**5. La dirección visual del tablero:** Videojuego con atmósfera mexicana sutil, no dashboard corporativo ni imitación folclórica. Paleta con acentos dorados, mecánica de cartas, sensación de que el destino se lanza. Esa dirección fue idea de Zabdiel y define la identidad del producto.

**6. La narrativa final del tablero:** Los textos que contextualizan cada etapa de "la lotería de vida", que conectan las variables con la historia de una persona, que convierten un número en una pregunta sobre justicia, todos los textos son resultado de conversaciones e ideas del equipo. En este punto nos empeñamos a permanecer completamente humanos, por lo que no se le pidió inspiración ni ayuda a la IA.

**7. La decisión de mostrar las brechas:** Cuando la auditoría nos reveló que 8 de 18 variables estaban ausentes, el equipo decidió documentarlas abiertamente en lugar de ocultarlas. Eso no lo sugirió la IA, fue una decisión sobre qué tipo de proyecto quisimos hacer, y nuestra decisión de no disimular los faltantes, sino señalarlos y buscar nuevas herramientas para hacerlo posible.
