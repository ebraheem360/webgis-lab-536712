import sys
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsVectorFileWriter,
    QgsCoordinateReferenceSystem,
    QgsProject
)

qgs = QgsApplication([], False)
qgs.initQgis()

sys.path.append(r"C:\Program Files\QGIS 3.38.3\apps\qgis\python\plugins")
import processing
from processing.core.Processing import Processing
Processing.initialize()

layer_path = r"C:\webgis-lab\Versions\districts_A.geojson"
layer = QgsVectorLayer(layer_path, "districts_A", "ogr")
print("Layer features:", layer.featureCount())

# Version B: Precision 5
opts_b = QgsVectorFileWriter.SaveVectorOptions()
opts_b.driverName = "GeoJSON"
opts_b.layerOptions = ["COORDINATE_PRECISION=5"]
err = QgsVectorFileWriter.writeAsVectorFormatV3(layer, r"C:\webgis-lab\Versions\districts_B.geojson", QgsProject.instance().transformContext(), opts_b)
print("Version B write result:", err[0])

# Version C: Simplify 0.001, precision 5
params_c = {
    'INPUT': layer,
    'METHOD': 0, # Distance (Douglas-Peucker)
    'TOLERANCE': 0.001,
    'OUTPUT': 'TEMPORARY_OUTPUT'
}
res_c = processing.run("native:simplifygeometries", params_c)
layer_c = res_c['OUTPUT']
opts_c = QgsVectorFileWriter.SaveVectorOptions()
opts_c.driverName = "GeoJSON"
opts_c.layerOptions = ["COORDINATE_PRECISION=5"]
err_c = QgsVectorFileWriter.writeAsVectorFormatV3(layer_c, r"C:\webgis-lab\Versions\districts_C.geojson", QgsProject.instance().transformContext(), opts_c)
print("Version C write result:", err_c[0])

# Version D: Simplify 0.01, precision 5
params_d = {
    'INPUT': layer,
    'METHOD': 0,
    'TOLERANCE': 0.01,
    'OUTPUT': 'TEMPORARY_OUTPUT'
}
res_d = processing.run("native:simplifygeometries", params_d)
layer_d = res_d['OUTPUT']
opts_d = QgsVectorFileWriter.SaveVectorOptions()
opts_d.driverName = "GeoJSON"
opts_d.layerOptions = ["COORDINATE_PRECISION=5"]
err_d = QgsVectorFileWriter.writeAsVectorFormatV3(layer_d, r"C:\webgis-lab\Versions\districts_D.geojson", QgsProject.instance().transformContext(), opts_d)
print("Version D write result:", err_d[0])

# Part 10: Reproject to EPSG:3857 and EPSG:32643
# 10.1 Produce two projected copies
# d_3857 (EPSG:3857)
params_3857 = {
    'INPUT': layer,
    'TARGET_CRS': 'EPSG:3857',
    'OUTPUT': r"C:\webgis-lab\Versions\d_3857.geojson"
}
res_3857 = processing.run("native:reprojectlayer", params_3857)
print("d_3857 reprojected")

# d_32643 (EPSG:32643)
params_32643 = {
    'INPUT': layer,
    'TARGET_CRS': 'EPSG:32643',
    'OUTPUT': r"C:\webgis-lab\Versions\d_32643.geojson"
}
res_32643 = processing.run("native:reprojectlayer", params_32643)
print("d_32643 reprojected")

qgs.exitQgis()
