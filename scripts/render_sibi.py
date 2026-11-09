import sys
import os
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsProject,
    QgsMapSettings,
    QgsMapRendererParallelJob,
    QgsRectangle,
    QgsSingleSymbolRenderer,
    QgsFillSymbol,
    QgsMarkerSymbol,
    QgsPalLayerSettings,
    QgsVectorLayerSimpleLabeling,
    QgsTextFormat,
    QgsTextBufferSettings,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsCoordinateReferenceSystem,
    QgsRuleBasedRenderer,
    QgsLineSymbol
)
from PyQt5.QtGui import QColor, QImage, QPainter, QFont
from PyQt5.QtCore import QSize

qgs = QgsApplication([], False)
qgs.initQgis()

districts_path = r"C:\webgis-lab\data\districts.geojson"
dist_layer = QgsVectorLayer(districts_path, "Districts", "ogr")

# Find Sibi
sibi_feat = None
for f in dist_layer.getFeatures():
    if f['district'] == 'Sibi':
        sibi_feat = f
        break

sibi_geom = sibi_feat.geometry()
centroid_pt = sibi_geom.centroid().asPoint()
surface_pt = sibi_geom.pointOnSurface().asPoint()
bbox = sibi_geom.boundingBox()

print(f"Sibi BoundingBox: xMin={bbox.xMinimum():.4f}, yMin={bbox.yMinimum():.4f}, xMax={bbox.xMaximum():.4f}, yMax={bbox.yMaximum():.4f}")
print(f"Centroid: {centroid_pt.toString(5)}")
print(f"Point on Surface: {surface_pt.toString(5)}")

# Create memory layer for Centroid
cent_layer = QgsVectorLayer("Point?crs=EPSG:4326", "Centroid (Outside)", "memory")
dp_cent = cent_layer.dataProvider()
f_c = QgsFeature()
f_c.setGeometry(sibi_geom.centroid())
dp_cent.addFeatures([f_c])
cent_layer.updateExtents()

# Style Centroid: Red filled circle with dark red border
cent_sym = QgsMarkerSymbol.createSimple({
    'name': 'circle',
    'color': '230,50,50,255',
    'outline_color': '150,0,0,255',
    'outline_width': '1.2',
    'size': '4.5'
})
cent_layer.setRenderer(QgsSingleSymbolRenderer(cent_sym))

# Create memory layer for Point on Surface
pos_layer = QgsVectorLayer("Point?crs=EPSG:4326", "Point on Surface (Inside)", "memory")
dp_pos = pos_layer.dataProvider()
f_p = QgsFeature()
f_p.setGeometry(sibi_geom.pointOnSurface())
dp_pos.addFeatures([f_p])
pos_layer.updateExtents()

# Style Point on Surface: Bright Green/Blue circle
pos_sym = QgsMarkerSymbol.createSimple({
    'name': 'circle',
    'color': '34,197,94,255',
    'outline_color': '20,83,45,255',
    'outline_width': '1.2',
    'size': '4.5'
})
pos_layer.setRenderer(QgsSingleSymbolRenderer(pos_sym))

# Style districts: Sibi highlighted with soft amber fill, others light grey with border
root_rule = QgsRuleBasedRenderer.Rule(None)

# Rule for Sibi
sibi_symbol = QgsFillSymbol.createSimple({
    'color': '254,240,138,200',
    'outline_color': '180,83,9,255',
    'outline_width': '1.5'
})
sibi_rule = QgsRuleBasedRenderer.Rule(sibi_symbol)
sibi_rule.setFilterExpression('"district" = \'Sibi\'')
sibi_rule.setLabel("Sibi District")
root_rule.appendChild(sibi_rule)

# Rule for Other Districts
other_symbol = QgsFillSymbol.createSimple({
    'color': '241,245,249,180',
    'outline_color': '148,163,184,255',
    'outline_width': '0.8'
})
other_rule = QgsRuleBasedRenderer.Rule(other_symbol)
other_rule.setFilterExpression('"district" != \'Sibi\'')
other_rule.setLabel("Surrounding Districts")
root_rule.appendChild(other_rule)

dist_layer.setRenderer(QgsRuleBasedRenderer(root_rule))

# Setup labeling for district names
pal = QgsPalLayerSettings()
pal.fieldName = "district"
pal.enabled = True
text_format = QgsTextFormat()
text_format.setFont(QFont("Arial", 9, QFont.Bold))
text_format.setColor(QColor(51, 65, 85))
buffer = QgsTextBufferSettings()
buffer.setEnabled(True)
buffer.setSize(1.0)
buffer.setColor(QColor(255, 255, 255))
text_format.setBuffer(buffer)
pal.setFormat(text_format)
dist_layer.setLabeling(QgsVectorLayerSimpleLabeling(pal))
dist_layer.setLabelsEnabled(True)

# Map Settings
settings = QgsMapSettings()
settings.setLayers([cent_layer, pos_layer, dist_layer])
settings.setBackgroundColor(QColor(238, 242, 246))
settings.setOutputSize(QSize(1200, 800))

# Extend extent slightly around Sibi to show the crescent shape and neighboring districts
pad = 0.35
extent = QgsRectangle(
    bbox.xMinimum() - pad,
    bbox.yMinimum() - pad * 0.7,
    bbox.xMaximum() + pad,
    bbox.yMaximum() + pad * 0.7
)
settings.setExtent(extent)

os.makedirs(r"C:\webgis-lab\screenshots\Lab3", exist_ok=True)
output_img = r"C:\webgis-lab\screenshots\Lab3\sibi_centroid_canvas.png"

job = QgsMapRendererParallelJob(settings)
job.start()
job.waitForFinished()

img = job.renderedImage()
img.save(output_img)
print(f"Saved rendered canvas to {output_img}")

