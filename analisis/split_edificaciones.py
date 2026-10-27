"""Split the Galapagos-wide buildings layer into solar-potential, existing-solar and hard-exclusion layers."""
from pathlib import Path

import geopandas as gpd

IN_DIR = Path(r"C:\Users\mahone5n\Research\HyGalapagos\idoneidad_hygalapagos\inputs\05_cobertura\edificaciones")
src = IN_DIR / "Construcciones_Galapagos_IERSE_Pasantias_2023.shp"

POTENTIAL = ["Escuela Galo Plaza", "Escuela San Francisco", "ElecGalapagosLL"]
EXISTING = ["Panel solar", "Fotovoltarico puerto ayora"]

g = gpd.read_file(src)
is_potential = g["Tipo"].isna() | g["Tipo"].isin(POTENTIAL)
is_existing = g["Tipo"].isin(EXISTING)

outputs = {
    "edificaciones_potencial_solar.shp": g[is_potential],
    "edificaciones_paneles_solares_existentes.shp": g[is_existing],
    "edificaciones_exclusion_dura.shp": g[~(is_potential | is_existing)],
}
for name, layer in outputs.items():
    layer.to_file(IN_DIR / name)
    print(f"{name}: {len(layer)} features")
