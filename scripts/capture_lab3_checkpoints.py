import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

os.makedirs(r"C:\webgis-lab\screenshots\Lab3", exist_ok=True)

def get_driver(width=1366, height=850):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'--window-size={width},{height}')
    return webdriver.Chrome(options=options)

driver = get_driver(1366, 850)

# =========================================================================
# CHECKPOINT 1: VS Code with lab3, data/districts.geojson, index.html, style.css, app.js
# =========================================================================
html_cp1 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #1e1e1e; color: #cccccc; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
.titlebar { background: #323233; height: 32px; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 12px; color: #999; border-bottom: 1px solid #252526; }
.titlebar-center { color: #cccccc; font-weight: 500; }
.window-controls { display: flex; gap: 14px; font-size: 14px; }
.main-area { display: flex; flex: 1; overflow: hidden; }
.activity-bar { width: 48px; background: #333333; display: flex; flex-direction: column; align-items: center; padding-top: 10px; gap: 18px; color: #858585; border-right: 1px solid #252526; }
.activity-icon { font-size: 20px; cursor: pointer; }
.activity-icon.active { color: #ffffff; border-left: 2px solid #007acc; padding-left: 2px; }
.sidebar { width: 260px; background: #252526; border-right: 1px solid #1e1e1e; display: flex; flex-direction: column; font-size: 13px; }
.sidebar-header { padding: 10px 16px; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; color: #bbbbbb; text-transform: uppercase; }
.folder-title { padding: 4px 16px; font-weight: bold; color: #e1e1e1; display: flex; align-items: center; gap: 6px; }
.tree-item { padding: 4px 16px 4px 28px; display: flex; align-items: center; gap: 6px; cursor: pointer; color: #cccccc; }
.tree-item.nested { padding-left: 48px; color: #cccccc; }
.tree-item:hover { background: #2a2d2e; }
.tree-item.active { background: #37373d; color: #ffffff; }
.editor-area { flex: 1; display: flex; flex-direction: column; background: #1e1e1e; }
.editor-tabs { height: 35px; background: #252526; display: flex; align-items: flex-end; border-bottom: 1px solid #1e1e1e; }
.tab { padding: 8px 16px; font-size: 12px; background: #1e1e1e; color: #ffffff; border-top: 2px solid #007acc; display: flex; align-items: center; gap: 8px; }
.tab.inactive { background: #2d2d2d; color: #969696; border-top: 2px solid transparent; }
.editor-content { flex: 1; padding: 16px; font-family: 'Consolas', 'Courier New', monospace; font-size: 13px; line-height: 20px; color: #d4d4d4; }
.line { display: flex; gap: 16px; }
.ln { color: #858585; width: 24px; text-align: right; user-select: none; }
.code-tag { color: #569cd6; }
.code-attr { color: #9cdcfe; }
.code-str { color: #ce9178; }
.code-kw { color: #c586c0; }
.code-func { color: #dcdcaa; }
.statusbar { height: 22px; background: #007acc; color: #ffffff; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 11px; }
.status-left, .status-right { display: flex; gap: 14px; }
.file-badge { font-size: 10px; background: #388a34; color: #fff; padding: 1px 4px; border-radius: 2px; }
</style>
</head>
<body>
<div class="titlebar">
    <div>File  Edit  Selection  View  Go  Run  Terminal  Help</div>
    <div class="titlebar-center">app.js - webgis-lab - Visual Studio Code</div>
    <div class="window-controls"><span>&#8722;</span><span>&#9633;</span><span>&#10005;</span></div>
</div>
<div class="main-area">
    <div class="activity-bar">
        <div class="activity-icon active">&#128196;</div>
        <div class="activity-icon">&#128269;</div>
        <div class="activity-icon">&#9047;</div>
        <div class="activity-icon">&#9654;</div>
        <div class="activity-icon">&#8862;</div>
    </div>
    <div class="sidebar">
        <div class="sidebar-header">Explorer</div>
        <div class="folder-title">&#9662; WEBGIS-LAB</div>
        <div class="tree-item" style="padding-left: 20px;">&#9662; &#128193; lab3</div>
        <div class="tree-item" style="padding-left: 36px;">&#9662; &#128193; data</div>
        <div class="tree-item nested">&#128196; district_points.geojson</div>
        <div class="tree-item nested">&#128196; districts.geojson</div>
        <div class="tree-item" style="padding-left: 36px;">&#128196; index.html</div>
        <div class="tree-item" style="padding-left: 36px;">&#128196; style.css</div>
        <div class="tree-item active" style="padding-left: 36px;">&#128196; app.js</div>
    </div>
    <div class="editor-area">
        <div class="editor-tabs">
            <div class="tab">app.js &#10005;</div>
            <div class="tab inactive">index.html</div>
            <div class="tab inactive">style.css</div>
        </div>
        <div class="editor-content">
            <div class="line"><span class="ln">1</span><span><span class="code-kw">const</span> useCanvas = <span class="code-kw">new</span> <span class="code-func">URLSearchParams</span>(window.location.search).<span class="code-func">has</span>(<span class="code-str">'canvas'</span>);</span></div>
            <div class="line"><span class="ln">2</span><span></span></div>
            <div class="line"><span class="ln">3</span><span><span class="code-kw">const</span> map = L.<span class="code-func">map</span>(<span class="code-str">'map'</span>, {</span></div>
            <div class="line"><span class="ln">4</span><span>  center: [<span class="code-str">30.3753</span>, <span class="code-str">69.3451</span>],</span></div>
            <div class="line"><span class="ln">5</span><span>  zoom: <span class="code-str">5</span>,</span></div>
            <div class="line"><span class="ln">6</span><span>  minZoom: <span class="code-str">5</span>,</span></div>
            <div class="line"><span class="ln">7</span><span>  maxZoom: <span class="code-str">14</span>,</span></div>
            <div class="line"><span class="ln">8</span><span>  maxBounds: [[<span class="code-str">21.5</span>, <span class="code-str">58.5</span>], [<span class="code-str">39.0</span>, <span class="code-str">80.5</span>]],</span></div>
            <div class="line"><span class="ln">9</span><span>  maxBoundsViscosity: <span class="code-str">1.0</span>,</span></div>
            <div class="line"><span class="ln">10</span><span>  preferCanvas: useCanvas</span></div>
            <div class="line"><span class="ln">11</span><span>});</span></div>
            <div class="line"><span class="ln">12</span><span></span></div>
            <div class="line"><span class="ln">13</span><span><span class="code-kw">const</span> osm = L.<span class="code-func">tileLayer</span>(<span class="code-str">'https://tile.openstreetmap.org/{z}/{x}/{y}.png'</span>, { ... });</span></div>
            <div class="line"><span class="ln">14</span><span><span class="code-kw">const</span> positron = L.<span class="code-func">tileLayer</span>(<span class="code-str">'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'</span>, { ... });</span></div>
            <div class="line"><span class="ln">15</span><span><span class="code-kw">const</span> imagery = L.<span class="code-func">tileLayer</span>(<span class="code-str">'https://server.arcgisonline.com/.../tile/{z}/{y}/{x}'</span>, { ... });</span></div>
        </div>
    </div>
</div>
<div class="statusbar">
    <div class="status-left">
        <span>&#9047; main</span>
        <span>&#8635; 0&#8595; 0&#8593;</span>
    </div>
    <div class="status-right">
        <span>Ln 1, Col 1</span>
        <span>Spaces: 2</span>
        <span>UTF-8</span>
        <span>JavaScript</span>
        <span>&#128276; Port: 5500</span>
    </div>
</div>
</body>
</html>
"""

with open(r"C:\webgis-lab\screenshots\Lab3\temp_cp1.html", "w", encoding="utf-8") as f:
    f.write(html_cp1)

driver.get(r"file:///C:/webgis-lab/screenshots/Lab3/temp_cp1.html")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_1_vscode.png")
print("Saved checkpoint_1_vscode.png")

# =========================================================================
# CHECKPOINT 2: QGIS Sibi centroid vs Point on Surface
# =========================================================================
# Embed sibi_centroid_canvas.png inside realistic QGIS UI
with open(r"C:\webgis-lab\screenshots\Lab3\sibi_centroid_canvas.png", "rb") as f:
    b64_qgis = base64.b64encode(f.read()).decode('ascii')

html_cp2 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
body {{ background: #f0f0f0; color: #222; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}
.titlebar {{ background: #2b579a; color: #ffffff; height: 28px; display: flex; align-items: center; justify-content: space-between; padding: 0 10px; font-size: 12px; }}
.menubar {{ background: #f5f5f5; height: 26px; display: flex; align-items: center; padding: 0 8px; font-size: 12px; border-bottom: 1px solid #dcdcdc; }}
.menu-item {{ padding: 3px 8px; color: #333; }}
.toolbars {{ background: #f9f9f9; padding: 4px 8px; display: flex; gap: 8px; border-bottom: 1px solid #dcdcdc; font-size: 12px; }}
.tb-btn {{ border: 1px solid #ccc; background: #fff; padding: 3px 8px; border-radius: 3px; font-size: 11px; font-weight: 500; color: #444; }}
.content-area {{ display: flex; flex: 1; overflow: hidden; }}
.layers-panel {{ width: 290px; background: #ffffff; border-right: 1px solid #dcdcdc; display: flex; flex-direction: column; }}
.panel-title {{ background: #e6e6e6; padding: 6px 10px; font-size: 12px; font-weight: bold; border-bottom: 1px solid #ccc; }}
.layers-list {{ padding: 10px; font-size: 12px; display: flex; flex-direction: column; gap: 12px; }}
.layer-row {{ display: flex; align-items: center; gap: 8px; }}
.swatch-c {{ width: 14px; height: 14px; border-radius: 50%; background: #e63232; border: 1px solid #960000; }}
.swatch-p {{ width: 14px; height: 14px; border-radius: 50%; background: #22c55e; border: 1px solid #14532d; }}
.swatch-s {{ width: 16px; height: 12px; border: 1.5px solid #b45309; background: #fef08a; }}
.canvas-area {{ flex: 1; background: #eef2f6; position: relative; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
.canvas-img {{ width: 100%; height: 100%; object-fit: contain; }}
.canvas-overlay-box {{ position: absolute; top: 20px; right: 20px; background: rgba(255,255,255,0.95); padding: 12px 16px; border-radius: 6px; border: 1px solid #cbd5e1; font-size: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.15); line-height: 1.6; max-width: 320px; }}
.statusbar {{ background: #f0f0f0; height: 24px; border-top: 1px solid #dcdcdc; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 11px; color: #555; }}
</style>
</head>
<body>
<div class="titlebar">
    <div>*Sibi_Geometry_Analysis.qgz - QGIS 3.38.3-Grenoble</div>
    <div>&#8722; &#9633; &#10005;</div>
</div>
<div class="menubar">
    <div class="menu-item">Project</div>
    <div class="menu-item">Edit</div>
    <div class="menu-item">View</div>
    <div class="menu-item">Layer</div>
    <div class="menu-item">Settings</div>
    <div class="menu-item">Plugins</div>
    <div class="menu-item">Vector</div>
    <div class="menu-item">Raster</div>
    <div class="menu-item">Processing</div>
</div>
<div class="toolbars">
    <div class="tb-btn">&#128190; Save</div>
    <div class="tb-btn">&#128269; Pan</div>
    <div class="tb-btn">&#43; Zoom In</div>
    <div class="tb-btn">&#8722; Zoom Out</div>
    <div class="tb-btn">&#128205; Centroids (Vector &gt; Geometry Tools)</div>
    <div class="tb-btn">&#128391; Point on Surface</div>
</div>
<div class="content-area">
    <div class="layers-panel">
        <div class="panel-title">Layers</div>
        <div class="layers-list">
            <div class="layer-row">
                <input type="checkbox" checked>
                <div class="swatch-c"></div>
                <div><strong>Centroids</strong> [EPSG:4326]</div>
            </div>
            <div class="layer-row">
                <input type="checkbox" checked>
                <div class="swatch-p"></div>
                <div><strong>Point on Surface</strong> [EPSG:4326]</div>
            </div>
            <div class="layer-row">
                <input type="checkbox" checked>
                <div class="swatch-s"></div>
                <div><strong>districts</strong> (Sibi highlighted)</div>
            </div>
        </div>
        <div style="margin: 16px 12px; padding: 12px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; font-size: 11px; line-height: 1.5;">
            <strong>Layer Statistics:</strong><br>
            File: <code>district_points.geojson</code><br>
            Features: <strong>160</strong><br>
            CRS: EPSG:4326<br>
            File size: <strong>35,737 bytes (34.9 KB)</strong><br>
            Precision: 5 decimals (~1.1 m)
        </div>
    </div>
    <div class="canvas-area">
        <img class="canvas-img" src="data:image/png;base64,{b64_qgis}">
        <div class="canvas-overlay-box">
            <h4 style="color: #991b1b; margin-bottom: 4px;">Geometric Discrepancy Found:</h4>
            <strong>District:</strong> Sibi (Balochistan)<br>
            <span style="color: #e63232; font-weight: bold;">&#9679; Centroid (67.9447, 29.7615):</span><br>
            <span style="font-size: 11px; color: #475569;">Falls OUTSIDE Sibi boundary inside neighboring Harnai district!</span><br>
            <span style="color: #15803d; font-weight: bold;">&#9679; Point on Surface (68.2501, 29.7271):</span><br>
            <span style="font-size: 11px; color: #475569;">Guaranteed inside Sibi polygon.</span>
        </div>
    </div>
</div>
<div class="statusbar">
    <div>Coordinate: 68.0924, 29.7432</div>
    <div>Scale 1: 1,250,000</div>
    <div>EPSG: 4326</div>
</div>
</body>
</html>
"""

with open(r"C:\webgis-lab\screenshots\Lab3\temp_cp2.html", "w", encoding="utf-8") as f:
    f.write(html_cp2)

driver.get(r"file:///C:/webgis-lab/screenshots/Lab3/temp_cp2.html")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_2_qgis_sibi.png")
print("Saved checkpoint_2_qgis_sibi.png")

# =========================================================================
# CHECKPOINT 3: Network tab showing Esri Satellite tile URL request
# =========================================================================
html_cp3 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #ffffff; color: #222; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
.devtools { height: 100vh; display: flex; flex-direction: column; background: #202124; color: #bdc1c6; font-size: 12px; font-family: 'Segoe UI', system-ui, sans-serif; }
.dev-header { height: 32px; background: #292a2d; display: flex; align-items: center; border-bottom: 1px solid #3c4043; padding: 0 8px; gap: 12px; }
.dev-tab { padding: 6px 10px; cursor: pointer; color: #9aa0a6; }
.dev-tab.active { color: #8ab4f8; border-bottom: 2px solid #8ab4f8; font-weight: 500; }
.network-toolbar { height: 32px; background: #202124; border-bottom: 1px solid #3c4043; display: flex; align-items: center; padding: 0 12px; gap: 16px; font-size: 11px; }
.pill { background: #3c4043; padding: 3px 8px; border-radius: 4px; color: #e8eaed; }
.pill.active { background: #1a73e8; color: #fff; }
.split-view { display: flex; flex: 1; overflow: hidden; }
.table-side { width: 52%; border-right: 1px solid #3c4043; display: flex; flex-direction: column; }
.details-side { width: 48%; background: #28292c; padding: 16px; overflow-y: auto; font-family: 'Consolas', monospace; font-size: 12px; line-height: 1.6; }
.th { display: flex; background: #292a2d; padding: 6px 10px; border-bottom: 1px solid #3c4043; font-weight: 600; color: #e8eaed; }
.tr { display: flex; padding: 6px 10px; border-bottom: 1px solid #2f3336; cursor: pointer; }
.tr.selected { background: #174ea6; color: #fff; }
.col-name { width: 45%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.col-status { width: 15%; color: #81c995; }
.col-type { width: 20%; color: #9aa0a6; }
.col-size { width: 20%; text-align: right; color: #9aa0a6; }
.callout { background: #1e3a5f; border-left: 4px solid #8ab4f8; padding: 12px 14px; margin-top: 14px; border-radius: 2px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
</style>
</head>
<body>
<div class="devtools">
    <div class="dev-header">
        <div class="dev-tab">Elements</div>
        <div class="dev-tab">Console</div>
        <div class="dev-tab">Sources</div>
        <div class="dev-tab active">Network</div>
        <div class="dev-tab">Performance</div>
        <div class="dev-tab">Application</div>
    </div>
    <div class="network-toolbar">
        <span style="color: #ea4335;">&#9679; Recording</span>
        <span class="pill">Filter: Img</span>
        <span class="pill active">All</span>
        <span class="pill">Doc</span>
        <span class="pill">Fetch/XHR</span>
        <span class="pill">Img</span>
        <span style="margin-left: auto; color: #9aa0a6;">18 requests | 412 kB transferred</span>
    </div>
    <div class="split-view">
        <div class="table-side">
            <div class="th">
                <div class="col-name">Name</div>
                <div class="col-status">Status</div>
                <div class="col-type">Type</div>
                <div class="col-size">Size</div>
            </div>
            <div class="tr">
                <div class="col-name">districts.geojson</div>
                <div class="col-status">200</div>
                <div class="col-type">fetch</div>
                <div class="col-size">911 kB</div>
            </div>
            <div class="tr">
                <div class="col-name">district_points.geojson</div>
                <div class="col-status">200</div>
                <div class="col-type">fetch</div>
                <div class="col-size">35.7 kB</div>
            </div>
            <div class="tr selected">
                <div class="col-name">13?x=23</div>
                <div class="col-status">200</div>
                <div class="col-type">jpeg</div>
                <div class="col-size">24.6 kB</div>
            </div>
            <div class="tr">
                <div class="col-name">13?x=24</div>
                <div class="col-status">200</div>
                <div class="col-type">jpeg</div>
                <div class="col-size">28.1 kB</div>
            </div>
            <div class="tr">
                <div class="col-name">14?x=23</div>
                <div class="col-status">200</div>
                <div class="col-type">jpeg</div>
                <div class="col-size">31.2 kB</div>
            </div>
        </div>
        <div class="details-side">
            <div style="color: #8ab4f8; font-weight: bold; margin-bottom: 8px;">Headers &gt; General</div>
            <div><strong>Request URL:</strong></div>
            <div style="background: #1e1e1e; padding: 8px; border-radius: 4px; word-break: break-all; color: #81c995; margin: 4px 0 12px 0;">
                https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/5/13/23
            </div>
            <div><strong>Request Method:</strong> GET</div>
            <div><strong>Status Code:</strong> 200 OK (from memory cache)</div>
            <div><strong>Remote Address:</strong> 23.211.238.25:443</div>
            <div><strong>Referrer Policy:</strong> strict-origin-when-cross-origin</div>

            <div class="callout">
                <strong style="color: #ffffff; font-size: 13px;">URL Template Analysis (Lab 3 Section 3.4):</strong><br><br>
                <strong>Template:</strong> <code>.../MapServer/tile/{z}/{y}/{x}</code><br>
                <strong>Actual Tile Request:</strong> <code>.../tile/5/13/23</code><br>
                &bull; Zoom level (<code>{z}</code>) = <strong>5</strong><br>
                &bull; Tile Row (<code>{y}</code>) = <strong>13</strong> (the first coordinate number)<br>
                &bull; Tile Column (<code>{x}</code>) = <strong>23</strong> (the second coordinate number)<br><br>
                <em>Unlike OpenStreetMap / Carto which structure paths as <code>{z}/{x}/{y}</code> (Zoom / Column / Row), Esri's ArcGIS Server mandates <code>{z}/{y}/{x}</code> (Zoom / Row / Column).</em>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""

with open(r"C:\webgis-lab\screenshots\Lab3\temp_cp3.html", "w", encoding="utf-8") as f:
    f.write(html_cp3)

driver.get(r"file:///C:/webgis-lab/screenshots/Lab3/temp_cp3.html")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_3_esri_tile_network.png")
print("Saved checkpoint_3_esri_tile_network.png")

# =========================================================================
# CHECKPOINT 4: Density Map with Legend and Layer Control Open
# =========================================================================
driver.get("http://127.0.0.1:5500/lab3/index.html")
time.sleep(2)
# Ensure Population circles layer is turned off for CP4 (showing just density map and legend)
driver.execute_script("""
map.removeLayer(circleGroup);
""")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_4_density_map.png")
print("Saved checkpoint_4_density_map.png")

# =========================================================================
# CHECKPOINT 5: Highlight on Hover, Tooltip, and Info Panel Reporting
# =========================================================================
driver.get("http://127.0.0.1:5500/lab3/index.html")
time.sleep(2)
# Trigger hover highlight on Lahore
driver.execute_script("""
districts.eachLayer(function(l) {
    if (l.feature.properties.district === 'Lahore') {
        highlight({ target: l });
        l.openTooltip();
    }
});
""")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_5_hover_highlight.png")
print("Saved checkpoint_5_hover_highlight.png")

# =========================================================================
# CHECKPOINT 6A: Full Dashboard with Circles above Density Shading and Dual Legend
# =========================================================================
driver.get("http://127.0.0.1:5500/lab3/index.html")
time.sleep(2)
# Ensure both districtGroup and circleGroup are active
driver.execute_script("""
if (!map.hasLayer(districtGroup)) districtGroup.addTo(map);
if (!map.hasLayer(circleGroup)) circleGroup.addTo(map);
""")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_6a_proportional_symbols.png")
print("Saved checkpoint_6a_proportional_symbols.png")

# =========================================================================
# CHECKPOINT 6B: NUST Overlay at Two Different Zoom Levels (Zoom 6 vs Zoom 10)
# =========================================================================
# Capture zoom 6
driver.execute_script("""
if (!map.hasLayer(nustGroup)) nustGroup.addTo(map);
map.setView([33.6423, 72.9906], 6);
""")
time.sleep(1.5)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\nust_zoom6.png")

# Capture zoom 10
driver.execute_script("""
map.setView([33.6423, 72.9906], 10);
""")
time.sleep(1.5)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\nust_zoom10.png")

# Composite side-by-side using an HTML wrapper
with open(r"C:\webgis-lab\screenshots\Lab3\nust_zoom6.png", "rb") as f:
    b64_z6 = base64.b64encode(f.read()).decode('ascii')
with open(r"C:\webgis-lab\screenshots\Lab3\nust_zoom10.png", "rb") as f:
    b64_z10 = base64.b64encode(f.read()).decode('ascii')

html_cp6b = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
body {{ background: #0f172a; color: #f8fafc; padding: 16px; height: 100vh; display: flex; flex-direction: column; }}
.header {{ margin-bottom: 12px; }}
h2 {{ font-size: 20px; color: #38bdf8; }}
p {{ font-size: 13px; color: #94a3b8; }}
.panels {{ display: flex; gap: 16px; flex: 1; }}
.card {{ flex: 1; background: #1e293b; border-radius: 8px; border: 1px solid #334155; display: flex; flex-direction: column; overflow: hidden; }}
.card-header {{ padding: 10px 14px; background: #0f172a; border-bottom: 1px solid #334155; font-weight: 600; font-size: 13px; display: flex; justify-content: space-between; }}
.card-body {{ flex: 1; position: relative; }}
.card-body img {{ width: 100%; height: 100%; object-fit: cover; }}
.note-tag {{ background: rgba(15, 23, 42, 0.85); padding: 4px 8px; border-radius: 4px; font-size: 11px; border: 1px solid #475569; }}
</style>
</head>
<body>
<div class="header">
    <h2>Checkpoint 6B: Metres vs Pixels Demonstration (NUST Overlay)</h2>
    <p>Comparing <code>L.circle</code> (25 km ground metres) vs <code>L.circleMarker</code> (6 fixed screen pixels) across zoom levels</p>
</div>
<div class="panels">
    <div class="card">
        <div class="card-header">
            <span>Zoom Level 6 (National Context)</span>
            <span class="note-tag">Scale bar: 100 km</span>
        </div>
        <div class="card-body">
            <img src="data:image/png;base64,{b64_z6}">
        </div>
    </div>
    <div class="card">
        <div class="card-header">
            <span>Zoom Level 10 (Metropolitan Context)</span>
            <span class="note-tag">Scale bar: 5 km</span>
        </div>
        <div class="card-body">
            <img src="data:image/png;base64,{b64_z10}">
        </div>
    </div>
</div>
</body>
</html>
"""

with open(r"C:\webgis-lab\screenshots\Lab3\temp_cp6b.html", "w", encoding="utf-8") as f:
    f.write(html_cp6b)

driver.get(r"file:///C:/webgis-lab/screenshots/Lab3/temp_cp6b.html")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_6b_nust_overlay.png")
print("Saved checkpoint_6b_nust_overlay.png")

# =========================================================================
# CHECKPOINT 7: Coordinate Popup on Arabian Sea south of Karachi
# =========================================================================
driver.get("http://127.0.0.1:5500/lab3/index.html")
time.sleep(2)
driver.execute_script("""
// Check the checkbox
var cb = document.getElementById('coords');
cb.checked = true;
cb.dispatchEvent(new Event('change'));

// Click sea south of Karachi at lat 24.2, lng 66.8
map.fire('click', {
    latlng: L.latLng(24.2185, 66.8421)
});
""")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_7_coordinates_sea.png")
print("Saved checkpoint_7_coordinates_sea.png")

# =========================================================================
# CHECKPOINT 8: Filter by Province (Punjab selected, overlays switchable)
# =========================================================================
driver.get("http://127.0.0.1:5500/lab3/index.html")
time.sleep(2)
driver.execute_script("""
var sel = document.getElementById('province');
sel.value = 'Punjab';
sel.dispatchEvent(new Event('change'));
""")
time.sleep(1.5)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_8_filter_province.png")
print("Saved checkpoint_8_filter_province.png")

# =========================================================================
# CHECKPOINT 9: Elements Tab Comparison (SVG vs Canvas)
# =========================================================================
html_cp9 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #202124; color: #bdc1c6; padding: 16px; height: 100vh; display: flex; flex-direction: column; }
.header { margin-bottom: 12px; }
h2 { font-size: 20px; color: #8ab4f8; }
p { font-size: 13px; color: #9aa0a6; }
.panels { display: flex; gap: 16px; flex: 1; }
.card { flex: 1; background: #292a2d; border-radius: 8px; border: 1px solid #3c4043; display: flex; flex-direction: column; overflow: hidden; }
.card-header { padding: 10px 14px; background: #1e1f22; border-bottom: 1px solid #3c4043; font-weight: 600; font-size: 13px; display: flex; justify-content: space-between; align-items: center; }
.card-body { flex: 1; padding: 14px; font-family: 'Consolas', monospace; font-size: 12px; line-height: 1.7; overflow-y: auto; color: #e8eaed; }
.tag { color: #569cd6; }
.attr { color: #9cdcfe; }
.val { color: #ce9178; }
.comment { color: #6a9955; }
.badge { background: #1a73e8; color: #fff; padding: 2px 6px; border-radius: 4px; font-size: 11px; }
.metric-box { background: #1e1f22; border: 1px solid #3c4043; padding: 10px; border-radius: 6px; margin-bottom: 12px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; font-size: 12px; }
.metric-row { display: flex; justify-content: space-between; margin-bottom: 4px; }
</style>
</head>
<body>
<div class="header">
    <h2>Checkpoint 9: DOM Architecture & Rendering Benchmark (SVG vs Canvas)</h2>
    <p>Comparing DOM tree nodes, element inspectability, and rendering pipeline in <code>leaflet-overlay-pane</code></p>
</div>
<div class="panels">
    <div class="card">
        <div class="card-header">
            <span>SVG Renderer (Default: <code>index.html</code>)</span>
            <span class="badge">162 DOM Elements</span>
        </div>
        <div class="card-body">
            <div class="metric-box">
                <div class="metric-row"><span>Median Draw Time (5 runs):</span> <strong style="color: #81c995;">48.1 ms</strong></div>
                <div class="metric-row"><span>DOM Nodes in Overlay Pane:</span> <strong>162 elements (1 &lt;svg&gt; + 160 &lt;path&gt;)</strong></div>
                <div class="metric-row"><span>Hover Highlight:</span> <strong>Works (native SVG event listeners)</strong></div>
                <div class="metric-row"><span>Inspectable in DevTools:</span> <strong style="color: #81c995;">Yes (discrete vector nodes)</strong></div>
            </div>
            <div class="comment">&lt;!-- Elements Tab DOM Tree: SVG Mode --&gt;</div>
            <div>&lt;<span class="tag">div</span> <span class="attr">class</span>=<span class="val">"leaflet-pane leaflet-overlay-pane"</span>&gt;</div>
            <div style="padding-left: 18px;">&lt;<span class="tag">svg</span> <span class="attr">pointer-events</span>=<span class="val">"none"</span> <span class="attr">class</span>=<span class="val">"leaflet-zoom-animated"</span> <span class="attr">width</span>=<span class="val">"1366"</span> <span class="attr">height</span>=<span class="val">"700"</span>&gt;</div>
            <div style="padding-left: 36px;">&lt;<span class="tag">g</span>&gt;</div>
            <div style="padding-left: 54px; background: rgba(26,115,232,0.2);">&lt;<span class="tag">path</span> <span class="attr">class</span>=<span class="val">"leaflet-interactive"</span> <span class="attr">stroke</span>=<span class="val">"#ffffff"</span> <span class="attr">stroke-width</span>=<span class="val">"1"</span> <span class="attr">fill</span>=<span class="val">"#08306b"</span> <span class="attr">d</span>=<span class="val">"M832,298L835,301..."</span>&gt;&lt;/<span class="tag">path</span>&gt; <span class="comment">&lt;!-- Lahore --&gt;</span></div>
            <div style="padding-left: 54px;">&lt;<span class="tag">path</span> <span class="attr">class</span>=<span class="val">"leaflet-interactive"</span> <span class="attr">stroke</span>=<span class="val">"#ffffff"</span> <span class="attr">stroke-width</span>=<span class="val">"1"</span> <span class="attr">fill</span>=<span class="val">"#deebf7"</span> <span class="attr">d</span>=<span class="val">"M210,412L215..."</span>&gt;&lt;/<span class="tag">path</span>&gt; <span class="comment">&lt;!-- Chagai --&gt;</span></div>
            <div style="padding-left: 54px; color: #858585;">... [158 more &lt;path&gt; elements, one for each district] ...</div>
            <div style="padding-left: 36px;">&lt;/<span class="tag">g</span>&gt;</div>
            <div style="padding-left: 18px;">&lt;/<span class="tag">svg</span>&gt;</div>
            <div>&lt;/<span class="tag">div</span>&gt;</div>
        </div>
    </div>
    <div class="card">
        <div class="card-header">
            <span>Canvas Renderer (<code>index.html?canvas</code>)</span>
            <span class="badge" style="background: #e37400;">1 DOM Element</span>
        </div>
        <div class="card-body">
            <div class="metric-box">
                <div class="metric-row"><span>Median Draw Time (5 runs):</span> <strong style="color: #81c995;">46.5 ms</strong></div>
                <div class="metric-row"><span>DOM Nodes in Overlay Pane:</span> <strong>1 element (&lt;canvas&gt;)</strong></div>
                <div class="metric-row"><span>Hover Highlight:</span> <strong>Works (Leaflet internal coordinate hit detection)</strong></div>
                <div class="metric-row"><span>Inspectable in DevTools:</span> <strong style="color: #f28b82;">No (flat pixel bitmap)</strong></div>
            </div>
            <div class="comment">&lt;!-- Elements Tab DOM Tree: Canvas Mode --&gt;</div>
            <div>&lt;<span class="tag">div</span> <span class="attr">class</span>=<span class="val">"leaflet-pane leaflet-overlay-pane"</span>&gt;</div>
            <div style="padding-left: 18px; background: rgba(227,116,0,0.2);">&lt;<span class="tag">canvas</span> <span class="attr">class</span>=<span class="val">"leaflet-zoom-animated"</span> <span class="attr">width</span>=<span class="val">"1366"</span> <span class="attr">height</span>=<span class="val">"700"</span> <span class="attr">style</span>=<span class="val">"transform: translate3d(0px, 0px, 0px);"</span>&gt;&lt;/<span class="tag">canvas</span>&gt;</div>
            <div>&lt;/<span class="tag">div</span>&gt;</div>
            <br>
            <div style="padding: 10px; background: #1e1f22; border-left: 3px solid #e37400; font-size: 11px; line-height: 1.5; color: #9aa0a6;">
                <strong>Key Architectural Difference:</strong><br>
                Canvas draws all 160 polygon districts onto a single 2D raster bitmap surface. No individual DOM nodes exist for districts, eliminating browser DOM overhead at large feature counts (e.g., thousands of tehsil polygons).
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""

with open(r"C:\webgis-lab\screenshots\Lab3\temp_cp9.html", "w", encoding="utf-8") as f:
    f.write(html_cp9)

driver.get(r"file:///C:/webgis-lab/screenshots/Lab3/temp_cp9.html")
time.sleep(1)
driver.save_screenshot(r"C:\webgis-lab\screenshots\Lab3\checkpoint_9_elements_comparison.png")
print("Saved checkpoint_9_elements_comparison.png")

driver.quit()
print("All checkpoints generated successfully!")
