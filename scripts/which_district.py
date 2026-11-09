from qgis.core import QgsApplication, QgsVectorLayer, QgsPointXY, QgsGeometry
qgs = QgsApplication([], False)
qgs.initQgis()

layer = QgsVectorLayer(r"C:\webgis-lab\data\districts.geojson", "districts", "ogr")
c = QgsGeometry.fromPointXY(QgsPointXY(67.94472, 29.76149))

for f in layer.getFeatures():
    if f.geometry().contains(c):
        print(f"The centroid of Sibi falls inside district: '{f['district']}', province: '{f['province']}'")

