# ============================================================
# @project      Tlahtoa Data 2026
# @author       Jesús Rafael Loggen Gonzalez <loggibooy@gmail.com>
# @coauthor     Zabdiel Taboada Vera (dashboard/visualización)
# @architecture Loggen Architecture™
# @copyright    © 2026 Tlahtoa Data Team · CC BY-NC-SA 4.0
# @hackods      HackODS UNAM 2026 · ODS 1, 4, 5, 6, 10
# ============================================================
"""
generar_mapa.py
Tlahtoa Data — Hack ODS UNAM 2026

Genera el mapa coroplético de México con Plotly
usando los datos del IRTE por estado.

Uso:
    python scripts/generar_mapa.py

Output:
    dashboard/mapa_irte.html
"""

import json
import unicodedata
import pandas as pd
import plotly.express as px
from pathlib import Path


def normalizar(s):
    s = unicodedata.normalize("NFD", str(s))
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower().strip()


ALIASES = {
    "estado de mexico": "mexico",
}


def main():
    with open("datos/raw/state_panel.json", encoding="utf-8") as f:
        panel = json.load(f)

    with open("dashboard/mexico.geojson", encoding="utf-8") as f:
        geojson = json.load(f)

    rows = []
    for estado in panel["estados"]:
        rows.append({
            "nombre": estado["nombre"],
            "irte_score": round(estado["irte_score"], 3),
            "irte_rank": estado["irte_rank"],
            "irte_nivel": estado["irte_nivel"],
            "tasa_pobreza": estado["trayectoria"]["infancia"]["indicadores"]["tasa_pobreza"],
            "mortalidad_infantil": estado["trayectoria"]["nacimiento"]["indicadores"]["mortalidad_infantil"],
            "abandono_secundaria": estado["trayectoria"]["adolescencia"]["indicadores"]["abandono_secundaria"],
            "formalidad_laboral": estado["trayectoria"]["adultez"]["indicadores"]["formalidad_laboral"],
        })

    df = pd.DataFrame(rows)

    for feature in geojson["features"]:
        nombre_geo = feature["properties"].get("name", "")
        feature["properties"]["_loc"] = normalizar(nombre_geo)

    df["_loc"] = df["nombre"].apply(lambda s: ALIASES.get(normalizar(s), normalizar(s)))

    fig = px.choropleth(
        df,
        geojson=geojson,
        locations="_loc",
        featureidkey="properties._loc",
        color="irte_score",
        color_continuous_scale=[
            [0.0, "#367A4F"],
            [0.5, "#E8C547"],
            [1.0, "#B8432A"]
        ],
        range_color=[0, 1],
        hover_name="nombre",
        hover_data={
            "irte_score": ":.3f",
            "irte_rank": True,
            "irte_nivel": True,
            "tasa_pobreza": ":.1f",
            "_loc": False
        },
        labels={
            "irte_score": "IRTE",
            "irte_rank": "Ranking (1=mayor riesgo)",
            "irte_nivel": "Nivel de riesgo",
            "tasa_pobreza": "Tasa de pobreza %"
        }
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=480,
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Work Sans, sans-serif"),
        coloraxis_colorbar=dict(title="IRTE", thickness=15)
    )

    output = Path("dashboard/mapa_irte.html")
    fig.write_html(output, include_plotlyjs="cdn", full_html=False)
    print(f"Mapa generado: {output}")
    print(f"Estados matcheados: {df['_loc'].isin([f['properties']['_loc'] for f in geojson['features']]).sum()}/32")


if __name__ == "__main__":
    main()
