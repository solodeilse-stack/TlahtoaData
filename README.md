<!--
  @project      Tlahtoa Data 2026
  @author       Jesús Rafael Loggen Gonzalez <loggibooy@gmail.com>
  @architecture Loggen Architecture™
  @copyright    © 2026 Tlahtoa Data Team · CC BY-NC-SA 4.0
-->

# Tlahtoa Data — Lotería de la Vida

> *¿Cuánto pesa el código postal de tu nacimiento sobre el techo de tu vida?*

**HackODS UNAM 2026 · ODS 1 · 4 · 5 · 6 · 10**

🌐 **Demo en vivo:** https://tlahtoa-data.github.io/Oficial/

---

## Equipo

| Nombre | Rol |
|---|---|
| **Jesús Rafael Loggen Gonzalez** | Arquitectura de datos · Motor IRTE · Pipeline ETL |
| **Ilse Cristina Gonzalez Diaz** | Análisis narrativo · Marco conceptual |
| **Zabdiel Taboada Vera** | Dashboard · Visualizaciones · Frontend |

---

## El proyecto

**Tlahtoa** (del náhuatl: *narrar, hablar*) convierte las desventajas territoriales
estructurales de México en una experiencia interactiva comprensible para jóvenes.

Pregunta central:
> *¿Qué tanto determina el estado mexicano en el que naces tu trayectoria de vida?*

El **IRTE (Índice de Riesgo de Trayectoria Estructural)** integra **9 variables**
de **6 fuentes oficiales** en **4 dimensiones** con peso igual (25%):

| Dimensión | Variables | Fuente |
|---|---|---|
| Salud | Mortalidad infantil, acceso agua, acceso drenaje | INEGI Censo 2020 |
| Pobreza | Tasa de pobreza, pobreza extrema | CONEVAL 2022 |
| Educación | Rezago educativo, abandono escolar | SEP/INEA 2022 |
| Género / Empleo | Fecundidad adolescente, formalidad laboral | CONAPO 2021 / INEGI |

---

## Herramientas utilizadas

| Herramienta | Uso |
|---|---|
| [Quarto](https://quarto.org/) | Generación del tablero (formato HTML) |
| [Python 3.12](https://www.python.org/) | Pipeline ETL + visualizaciones |
| [Plotly](https://plotly.com/python/) | Mapa coroplético interactivo |
| [Observable JS](https://observablehq.com/) | Simulador interactivo (nativo de Quarto) |
| [uv](https://docs.astral.sh/uv/) | Gestión de dependencias |
| [pandas](https://pandas.pydata.org/) | Procesamiento de datos |

---

## Fuentes de datos

| Dataset | Organismo | Año | Licencia |
|---|---|---|---|
| Pobreza multidimensional estatal | CONEVAL | 2022 | Datos abiertos |
| Censo de Población y Vivienda | INEGI | 2020 | Datos abiertos |
| Rezago educativo por entidad | SEP/INEA | 2022 | Datos abiertos |
| Proyecciones demográficas | CONAPO | 2021 | Datos abiertos |
| Validación externa ODS | ONU/PNUD | 2022 | Datos abiertos |

Todos los datos son de **acceso público, gratuito y fuentes verificables institucionales**.

---

## Estructura del repositorio

```
dashboard/
  index.qmd          ← Tablero principal (Lotería de la Vida)
  comparativa.qmd    ← Comparativa territorial entre estados
  trayectorias.qmd   ← Trayectorias de vida por etapa
  metodologia.qmd    ← Método IRTE, fuentes y evidencia

data/
  processed/         ← 8 outputs del pipeline IRTE
  static_api/        ← API estática (480 escenarios pre-calculados)
  metadata/          ← Manifests de provenance y fuentes

scripts/
  generar_mapa.py    ← Genera el mapa coroplético con Plotly
```

---

## Ejecutar localmente

```bash
# Instalar dependencias con uv
uv sync

# Preview del tablero
quarto preview dashboard/index.qmd
```

---

## Licencia

**CC BY-NC-SA 4.0** · © 2026 Tlahtoa Data Team

Jesús Rafael Loggen Gonzalez · Ilse Cristina Gonzalez Diaz · Zabdiel Taboada Vera
