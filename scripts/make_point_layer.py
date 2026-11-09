import json
import os
import sys

from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsCoordinateReferenceSystem,
    QgsVectorFileWriter,
    QgsField,
    QgsProject
)

qgs = QgsApplication([], False)
qgs.initQgis()

input_path = r"C:\webgis-lab\lab3\data\districts.geojson"
output_path = r"C:\webgis-lab\lab3\data\district_points.geojson"

in_layer = QgsVectorLayer(input_path, "districts", "ogr")
if not in_layer.isValid():
    print("Failed to load input layer")
    sys.exit(1)

# Create memory point layer with same CRS and fields
crs = in_layer.crs()
fields = in_layer.fields()

mem_layer = QgsVectorLayer(f"Point?crs={crs.authid()}", "district_points", "memory")
dp = mem_layer.dataProvider()
dp.addAttributes(fields.toList())
mem_layer.updateFields()

new_feats = []
for feat in in_layer.getFeatures():
    geom = feat.geometry()
    pos = geom.pointOnSurface()
    new_feat = QgsFeature(mem_layer.fields())
    new_feat.setGeometry(pos)
    new_feat.setAttributes(feat.attributes())
    new_feats.append(new_feat)

dp.addFeatures(new_feats)
mem_layer.updateExtents()

print(f"Memory layer created with {mem_layer.featureCount()} features.")

# Save to GeoJSON with COORDINATE_PRECISION=5
options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GeoJSON"
options.fileEncoding = "UTF-8"
options.layerOptions = ["COORDINATE_PRECISION=5"]

result = QgsVectorFileWriter.writeAsVectorFormatV3(
    mem_layer,
    output_path,
    QgsProject.instance().transformContext(),
    options
)
print("Write result:", result)
write_result = result[0]

if write_result == QgsVectorFileWriter.NoError:
    print(f"Successfully saved {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")
else:
    print(f"Error saving GeoJSON: {error_message}")

with open(output_path, 'r', encoding='utf-8') as f:
    gj = json.load(f)
print("GeoJSON feature count:", len(gj['features']))
print("First feature properties:", gj['features'][0]['properties'])
print("First feature geometry:", gj['features'][0]['geometry'])
