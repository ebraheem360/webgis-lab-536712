import json, math
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsDistanceArea,
    QgsCoordinateReferenceSystem
)

qgs = QgsApplication([], False)
qgs.initQgis()

layer_3857 = QgsVectorLayer(r"C:\webgis-lab\Versions\d_3857.geojson", "d_3857", "ogr")
layer_32643 = QgsVectorLayer(r"C:\webgis-lab\Versions\d_32643.geojson", "d_32643", "ogr")
layer_A = QgsVectorLayer(r"C:\webgis-lab\Versions\districts_A.geojson", "districts_A", "ogr")

# Let's map districts by name to get lat (centroid in 4326), area in 3857, area in 32643
dist_data = {}

for f in layer_A.getFeatures():
    geom = f.geometry()
    centroid = geom.centroid().asPoint()
    name = f["district"]
    dist_data[name] = {
        "lat": centroid.y(),
        "lon": centroid.x(),
        "province": f["province"]
    }

for f in layer_3857.getFeatures():
    name = f["district"]
    # in QGIS, $area in planar coordinates of the layer (EPSG:3857) is geom.area()
    area_3857_km2 = f.geometry().area() / 1e6
    if name in dist_data:
        dist_data[name]["area_3857"] = area_3857_km2

for f in layer_32643.getFeatures():
    name = f["district"]
    # in QGIS, $area in planar coordinates of the layer (EPSG:32643) is geom.area()
    area_32643_km2 = f.geometry().area() / 1e6
    if name in dist_data:
        dist_data[name]["area_32643"] = area_32643_km2

# Sort districts by latitude from south to north
sorted_dists = sorted(dist_data.items(), key=lambda x: x[1]["lat"])

print("--- South to North Sample Districts ---")
# Pick 5 districts spread from south to north:
# 1. Very South (lat ~24-25)
# 2. Lower-Mid (lat ~27-28)
# 3. Middle (lat ~30)
# 4. Upper-Mid (lat ~33-34)
# 5. Far North (lat ~35-36)

indices = [5, 45, 80, 120, 155]
selected = [sorted_dists[i] for i in indices]

for name, d in selected:
    lat = d["lat"]
    a3857 = d["area_3857"]
    aUTM = d["area_32643"]
    pct_diff = ((a3857 - aUTM) / aUTM) * 100
    pred_factor = 1.0 / (math.cos(math.radians(lat)) ** 2)
    pred_diff = (pred_factor - 1.0) * 100
    print(f"District: {name:20} Province: {d['province']:15} Lat: {lat:6.2f} | 3857: {a3857:10.2f} km2 | UTM: {aUTM:10.2f} km2 | % diff: {pct_diff:6.2f}% | predicted: {pred_diff:6.2f}%")

qgs.exitQgis()
