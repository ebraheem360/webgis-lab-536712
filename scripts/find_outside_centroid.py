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
    QgsProject,
    QgsMapSettings,
    QgsMapRendererParallelJob,
    QgsRectangle,
    QgsSingleSymbolRenderer,
    QgsFillSymbol,
    QgsMarkerSymbol
)
from PyQt5.QtGui import QColor, QImage, QPainter
from PyQt5.QtCore import QSize

qgs = QgsApplication([], False)
qgs.initQgis()

layer_path = r"C:\webgis-lab\data\districts.geojson"
layer = QgsVectorLayer(layer_path, "districts", "ogr")

if not layer.isValid():
    print("Layer failed to load!")
    sys.exit(1)

print(f"Loaded {layer.featureCount()} features.")

outside_districts = []

for feat in layer.getFeatures():
    geom = feat.geometry()
    c = geom.centroid()
    pos = geom.pointOnSurface()
    
    # Check if centroid is within polygon
    # Note: contains returns true if the point is strictly inside
    # intersects returns true if point is inside or on boundary
    is_inside = geom.intersects(c)
    if not is_inside:
        dist_name = feat['district']
        prov_name = feat['province']
        outside_districts.append((feat.id(), dist_name, prov_name, c.asPoint(), pos.asPoint(), geom.boundingBox()))
        print(f"FOUND: District '{dist_name}', Province '{prov_name}' has centroid OUTSIDE boundary!")
        print(f"  Centroid: ({c.asPoint().x():.5f}, {c.asPoint().y():.5f})")
        print(f"  PointOnSurface: ({pos.asPoint().x():.5f}, {pos.asPoint().y():.5f})")

print(f"Total outside: {len(outside_districts)}")

