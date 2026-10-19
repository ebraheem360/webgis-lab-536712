import sys
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsProject,
    QgsMapSettings,
    QgsMapRendererParallelJob,
    QgsRectangle,
    QgsSingleSymbolRenderer,
    QgsFillSymbol,
    QgsSimpleFillSymbolLayer,
    QgsLineSymbol
)
from PyQt5.QtGui import QColor, QImage, QPainter
from PyQt5.QtCore import QSize

qgs = QgsApplication([], False)
qgs.initQgis()

# Load layer A and layer D
layer_A = QgsVectorLayer(r"C:\webgis-lab\Versions\districts_A.geojson", "districts_A (Original Detail)", "ogr")
layer_D = QgsVectorLayer(r"C:\webgis-lab\Versions\districts_D.geojson", "districts_D (Simplified 1km)", "ogr")

# Style Layer D: semi-transparent blue fill with blue border
sym_D = QgsFillSymbol.createSimple({
    'color': '180,215,255,140',
    'outline_color': '0,102,204,255',
    'outline_width': '0.8',
    'outline_style': 'solid'
})
layer_D.setRenderer(QgsSingleSymbolRenderer(sym_D))

# Style Layer A: hollow with strong red outline showing original intricate vertices
sym_A = QgsFillSymbol.createSimple({
    'color': '0,0,0,0',
    'outline_color': '220,20,60,255',
    'outline_width': '0.6',
    'outline_style': 'solid'
})
layer_A.setRenderer(QgsSingleSymbolRenderer(sym_A))

# Set up map settings
settings = QgsMapSettings()
settings.setLayers([layer_A, layer_D]) # layer_A on top of layer_D
settings.setBackgroundColor(QColor(245, 247, 250))
settings.setOutputSize(QSize(1100, 750))

# Zoom into coastal / southern Pakistan (Sindh & Balochistan coast) where coastline detail differences are extreme
# Lat: 23.8 to 26.5, Lon: 66.5 to 69.5
extent = QgsRectangle(66.2, 23.8, 69.8, 26.2)
settings.setExtent(extent)

job = QgsMapRendererParallelJob(settings)
job.start()
job.waitForFinished()

img = job.renderedImage()
img.save(r"C:\webgis-lab\screenshots\qgis_canvas_compare.png")
print("Saved qgis_canvas_compare.png successfully!")

qgs.exitQgis()
