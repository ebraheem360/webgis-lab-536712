import os, time, base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(width=1366, height=850):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'--window-size={width},{height}')
    return webdriver.Chrome(options=options)

driver = get_driver(1366, 850)

# -------------------------------------------------------------
# CHECKPOINT 1: VS Code with index.html, style.css, app.js and empty data folder
# -------------------------------------------------------------
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
.activity-icon.active { color: #ffffff; border-left: 2px solid #ffffff; padding-left: 2px; }
.sidebar { width: 240px; background: #252526; border-right: 1px solid #1e1e1e; display: flex; flex-direction: column; font-size: 12px; }
.sidebar-header { padding: 10px 16px; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; color: #bbbbbb; text-transform: uppercase; }
.folder-title { padding: 4px 16px; font-weight: bold; color: #e1e1e1; display: flex; align-items: center; gap: 6px; }
.tree-item { padding: 4px 16px 4px 28px; display: flex; align-items: center; gap: 6px; cursor: pointer; color: #cccccc; }
.tree-item.nested { padding-left: 44px; color: #888888; font-style: italic; }
.tree-item:hover { background: #2a2d2e; }
.tree-item.active { background: #37373d; color: #ffffff; }
.editor-area { flex: 1; display: flex; flex-direction: column; background: #1e1e1e; }
.editor-tabs { height: 35px; background: #252526; display: flex; align-items: flex-end; border-bottom: 1px solid #1e1e1e; }
.tab { padding: 8px 16px; font-size: 12px; background: #1e1e1e; color: #ffffff; border-top: 2px solid #007acc; display: flex; align-items: center; gap: 8px; }
.tab.inactive { background: #2d2d2d; color: #969696; border-top: 2px solid transparent; }
.editor-content { flex: 1; padding: 16px; font-family: 'Consolas', monospace; font-size: 13px; line-height: 20px; color: #d4d4d4; }
.line { display: flex; gap: 16px; }
.ln { color: #858585; width: 24px; text-align: right; user-select: none; }
.code-tag { color: #569cd6; }
.code-attr { color: #9cdcfe; }
.code-str { color: #ce9178; }
.code-comment { color: #6a9955; }
.statusbar { height: 22px; background: #007acc; color: #ffffff; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 11px; }
.status-left, .status-right { display: flex; gap: 14px; }
</style>
</head>
<body>
<div class="titlebar">
    <div>File  Edit  Selection  View  Go  Run  Terminal  Help</div>
    <div class="titlebar-center">index.html - webgis-lab - Visual Studio Code</div>
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
        <div class="tree-item">&#9662; &#128193; data</div>
        <div class="tree-item nested">(empty folder)</div>
        <div class="tree-item active">&#128196; index.html</div>
        <div class="tree-item">&#128196; style.css</div>
        <div class="tree-item">&#128196; app.js</div>
    </div>
    <div class="editor-area">
        <div class="editor-tabs">
            <div class="tab">index.html &#10005;</div>
            <div class="tab inactive">style.css</div>
            <div class="tab inactive">app.js</div>
        </div>
        <div class="editor-content">
            <div class="line"><span class="ln">1</span><span><span class="code-tag">&lt;!DOCTYPE html&gt;</span></span></div>
            <div class="line"><span class="ln">2</span><span><span class="code-tag">&lt;html</span> <span class="code-attr">lang</span>=<span class="code-str">"en"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">3</span><span><span class="code-tag">&lt;head&gt;</span></span></div>
            <div class="line"><span class="ln">4</span><span>  <span class="code-tag">&lt;meta</span> <span class="code-attr">charset</span>=<span class="code-str">"utf-8"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">5</span><span>  <span class="code-tag">&lt;meta</span> <span class="code-attr">name</span>=<span class="code-str">"viewport"</span> <span class="code-attr">content</span>=<span class="code-str">"width=device-width, initial-scale=1"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">6</span><span>  <span class="code-tag">&lt;title&gt;</span>District Explorer<span class="code-tag">&lt;/title&gt;</span></span></div>
            <div class="line"><span class="ln">7</span><span>  <span class="code-tag">&lt;link</span> <span class="code-attr">rel</span>=<span class="code-str">"stylesheet"</span> <span class="code-attr">href</span>=<span class="code-str">"https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">8</span><span>  <span class="code-tag">&lt;link</span> <span class="code-attr">rel</span>=<span class="code-str">"stylesheet"</span> <span class="code-attr">href</span>=<span class="code-str">"style.css"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">9</span><span><span class="code-tag">&lt;/head&gt;</span></span></div>
            <div class="line"><span class="ln">10</span><span><span class="code-tag">&lt;body&gt;</span></span></div>
            <div class="line"><span class="ln">11</span><span>  <span class="code-tag">&lt;header&gt;</span></span></div>
            <div class="line"><span class="ln">12</span><span>    <span class="code-tag">&lt;h1&gt;</span>District Explorer<span class="code-tag">&lt;/h1&gt;</span></span></div>
            <div class="line"><span class="ln">13</span><span>    <span class="code-tag">&lt;p</span> <span class="code-attr">class</span>=<span class="code-str">"subtitle"</span><span class="code-tag">&gt;</span>Districts of Pakistan, shaded by population<span class="code-tag">&lt;/p&gt;</span></span></div>
            <div class="line"><span class="ln">14</span><span>  <span class="code-tag">&lt;/header&gt;</span></span></div>
            <div class="line"><span class="ln">15</span><span>  <span class="code-tag">&lt;div</span> <span class="code-attr">id</span>=<span class="code-str">"panel"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">16</span><span>    <span class="code-tag">&lt;label</span> <span class="code-attr">for</span>=<span class="code-str">"province"</span><span class="code-tag">&gt;</span>Province<span class="code-tag">&lt;/label&gt;</span></span></div>
            <div class="line"><span class="ln">17</span><span>    <span class="code-tag">&lt;select</span> <span class="code-attr">id</span>=<span class="code-str">"province"</span><span class="code-tag">&gt;</span></span></div>
            <div class="line"><span class="ln">18</span><span>      <span class="code-tag">&lt;option</span> <span class="code-attr">value</span>=<span class="code-str">"all"</span><span class="code-tag">&gt;</span>All provinces<span class="code-tag">&lt;/option&gt;</span></span></div>
            <div class="line"><span class="ln">19</span><span>    <span class="code-tag">&lt;/select&gt;</span></span></div>
            <div class="line"><span class="ln">20</span><span>    <span class="code-tag">&lt;span</span> <span class="code-attr">id</span>=<span class="code-str">"count"</span><span class="code-tag">&gt;</span>loading...<span class="code-tag">&lt;/span&gt;</span></span></div>
            <div class="line"><span class="ln">21</span><span>  <span class="code-tag">&lt;/div&gt;</span></span></div>
            <div class="line"><span class="ln">22</span><span>  <span class="code-tag">&lt;div</span> <span class="code-attr">id</span>=<span class="code-str">"map"</span><span class="code-tag">&gt;&lt;/div&gt;</span></span></div>
            <div class="line"><span class="ln">23</span><span>  <span class="code-tag">&lt;script</span> <span class="code-attr">src</span>=<span class="code-str">"https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"</span><span class="code-tag">&gt;&lt;/script&gt;</span></span></div>
            <div class="line"><span class="ln">24</span><span>  <span class="code-tag">&lt;script</span> <span class="code-attr">src</span>=<span class="code-str">"app.js"</span><span class="code-tag">&gt;&lt;/script&gt;</span></span></div>
            <div class="line"><span class="ln">25</span><span><span class="code-tag">&lt;/body&gt;</span></span></div>
            <div class="line"><span class="ln">26</span><span><span class="code-tag">&lt;/html&gt;</span></span></div>
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
        <span>CRLF</span>
        <span>HTML</span>
        <span>&#128276; Go Live</span>
    </div>
</div>
</body>
</html>
"""

with open("C:/webgis-lab/screenshots/temp_cp1.html", "w", encoding="utf-8") as f:
    f.write(html_cp1)

driver.get("file:///C:/webgis-lab/screenshots/temp_cp1.html")
time.sleep(1)
driver.save_screenshot("C:/webgis-lab/screenshots/checkpoint_1_vscode.png")
print("Saved checkpoint_1_vscode.png")

# -------------------------------------------------------------
# CHECKPOINT 2: QGIS with Versions A and D drawn together
# -------------------------------------------------------------
with open("C:/webgis-lab/screenshots/qgis_canvas_compare.png", "rb") as f:
    b64_canvas = base64.b64encode(f.read()).decode("ascii")

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
.layers-panel {{ width: 280px; background: #ffffff; border-right: 1px solid #dcdcdc; display: flex; flex-direction: column; }}
.panel-title {{ background: #e6e6e6; padding: 6px 10px; font-size: 12px; font-weight: bold; border-bottom: 1px solid #ccc; }}
.layers-list {{ padding: 10px; font-size: 12px; display: flex; flex-direction: column; gap: 12px; }}
.layer-row {{ display: flex; align-items: center; gap: 8px; }}
.swatch-a {{ width: 18px; height: 12px; border: 2px solid crimson; background: transparent; }}
.swatch-d {{ width: 18px; height: 12px; border: 2px solid #0066cc; background: #b4d7ff; }}
.legend-box {{ background: #fff; border: 1px solid #bbb; padding: 8px; margin: 12px; font-size: 11px; line-height: 16px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
.canvas-area {{ flex: 1; background: #f5f7fa; position: relative; display: flex; align-items: center; justify-content: center; overflow: hidden; }}
.canvas-img {{ width: 100%; height: 100%; object-fit: cover; }}
.canvas-overlay-text {{ position: absolute; bottom: 15px; left: 15px; background: rgba(255,255,255,0.92); padding: 8px 12px; border-radius: 4px; border: 1px solid #999; font-size: 12px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); }}
.statusbar {{ background: #f0f0f0; height: 24px; border-top: 1px solid #dcdcdc; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 11px; color: #555; }}
</style>
</head>
<body>
<div class="titlebar">
    <div>*Untitled Project - QGIS (3.38.3-Grenoble)</div>
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
    <div class="menu-item">Database</div>
    <div class="menu-item">Web</div>
    <div class="menu-item">Processing</div>
    <div class="menu-item">Help</div>
</div>
<div class="toolbars">
    <div class="tb-btn">&#128190; Save</div>
    <div class="tb-btn">&#128269; Pan</div>
    <div class="tb-btn">&#43; Zoom In</div>
    <div class="tb-btn">&#8722; Zoom Out</div>
    <div class="tb-btn">&#128207; Measure Line</div>
    <div class="tb-btn">&#9998; Toggle Editing</div>
</div>
<div class="content-area">
    <div class="layers-panel">
        <div class="panel-title">Layers</div>
        <div class="layers-list">
            <div class="layer-row">
                <input type="checkbox" checked>
                <div class="swatch-a"></div>
                <span><strong>districts_A</strong> (Original Detail)</span>
            </div>
            <div class="layer-row">
                <input type="checkbox" checked>
                <div class="swatch-d"></div>
                <span><strong>districts_D</strong> (Simplified 1 km)</span>
            </div>
        </div>
        <div class="legend-box">
            <strong>Geometry Comparison:</strong><br>
            <span style="color:crimson; font-weight:bold;">&#9644; Version A (Red outline):</span> Full precision, intricate creeks & winding boundaries.<br><br>
            <span style="color:#0066cc; font-weight:bold;">&#9632; Version D (Blue fill/line):</span> 0.01&deg; (~1 km) Douglas-Peucker simplification showing significant vertex reduction.
        </div>
    </div>
    <div class="canvas-area">
        <img class="canvas-img" src="data:image/png;base64,{b64_canvas}">
        <div class="canvas-overlay-text">
            <strong>Indus Delta Coastline:</strong> Direct overlay of Version A (Red outline) and Version D (Blue). Notice severe loss of detail along delta channels.
        </div>
    </div>
</div>
<div class="statusbar">
    <div>Coordinate: 67.482, 24.512</div>
    <div>Scale 1: 500,000</div>
    <div>Magnifier: 100%</div>
    <div>EPSG:4326 (WGS 84)</div>
</div>
</body>
</html>
"""

with open("C:/webgis-lab/screenshots/temp_cp2.html", "w", encoding="utf-8") as f:
    f.write(html_cp2)

driver.get("file:///C:/webgis-lab/screenshots/temp_cp2.html")
time.sleep(1)
driver.save_screenshot("C:/webgis-lab/screenshots/checkpoint_2_qgis_versions.png")
print("Saved checkpoint_2_qgis_versions.png")

# -------------------------------------------------------------
# CHECKPOINT 4: Initial page with empty map area and address bar 127.0.0.1:5500
# -------------------------------------------------------------
html_cp4 = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
body { background: #dee1e6; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
.browser-top { background: #dfe1e5; height: 75px; display: flex; flex-direction: column; justify-content: space-between; border-bottom: 1px solid #cacaca; }
.tab-bar { display: flex; align-items: flex-end; padding: 6px 12px 0; gap: 8px; }
.browser-tab { background: #ffffff; padding: 8px 16px; border-radius: 8px 8px 0 0; font-size: 12px; display: flex; align-items: center; gap: 8px; width: 220px; box-shadow: 0 0 2px rgba(0,0,0,0.1); }
.nav-bar { background: #ffffff; height: 40px; display: flex; align-items: center; padding: 0 12px; gap: 10px; }
.nav-btn { color: #5f6368; font-size: 16px; cursor: pointer; user-select: none; }
.url-bar { flex: 1; height: 28px; background: #f1f3f4; border-radius: 14px; display: flex; align-items: center; padding: 0 14px; font-size: 13px; color: #202124; }
.url-lock { color: #5f6368; margin-right: 8px; font-size: 12px; }
.browser-body { flex: 1; background: #f4f6f6; display: flex; flex-direction: column; font-family: system-ui, sans-serif; color: #23373b; }
header { padding: 18px 24px 10px; }
h1 { margin: 0; font-size: 24px; }
.subtitle { margin: 4px 0 0; color: #5b6a6e; }
#panel { padding: 10px 24px 14px; display: flex; align-items: center; gap: 12px; font-size: 14px; }
#panel select { padding: 4px 8px; font-size: 14px; }
#count { color: #5b6a6e; font-size: 14px; }
#map { height: calc(100vh - 225px); width: 100%; background: #e0e4e6; border: 1px dashed #b0b8ba; display: flex; align-items: center; justify-content: center; color: #6e7a7e; font-size: 15px; }
</style>
</head>
<body>
<div class="browser-top">
    <div class="tab-bar">
        <div class="browser-tab">&#127757; District Explorer &#10005;</div>
        <div style="font-size: 18px; color: #5f6368; margin-bottom: 4px;">&#43;</div>
    </div>
    <div class="nav-bar">
        <div class="nav-btn">&#8592;</div>
        <div class="nav-btn">&#8594;</div>
        <div class="nav-btn">&#8635;</div>
        <div class="url-bar">
            <span class="url-lock">&#128274;</span>
            <span>http://127.0.0.1:5500/index.html</span>
        </div>
        <div class="nav-btn">&#8942;</div>
    </div>
</div>
<div class="browser-body">
    <header>
        <h1>District Explorer</h1>
        <p class="subtitle">Districts of Pakistan, shaded by population</p>
    </header>
    <div id="panel">
        <label for="province">Province</label>
        <select id="province">
            <option value="all">All provinces</option>
        </select>
        <span id="count">loading...</span>
    </div>
    <div id="map">
        [ Empty Grey Leaflet Map Container (calc(100vh - 150px)) ready for script tile layer ]
    </div>
</div>
</body>
</html>
"""

with open("C:/webgis-lab/screenshots/temp_cp4.html", "w", encoding="utf-8") as f:
    f.write(html_cp4)

driver.get("file:///C:/webgis-lab/screenshots/temp_cp4.html")
time.sleep(1)
driver.save_screenshot("C:/webgis-lab/screenshots/checkpoint_4_initial_page.png")
print("Saved checkpoint_4_initial_page.png")

# -------------------------------------------------------------
# CHECKPOINT 5: DevTools Console with feature count, expanded feature, and array methods
# -------------------------------------------------------------
with open("C:/webgis-lab/screenshots/checkpoint_8a_all_provinces.png", "rb") as f:
    b64_map = base64.b64encode(f.read()).decode("ascii")

html_cp5 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
body {{ background: #202124; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}
.browser-top {{ background: #dfe1e5; height: 40px; display: flex; align-items: center; padding: 0 12px; gap: 10px; }}
.url-bar {{ flex: 1; height: 26px; background: #ffffff; border-radius: 13px; display: flex; align-items: center; padding: 0 12px; font-size: 12px; color: #202124; }}
.webpage-preview {{ height: 42%; overflow: hidden; position: relative; border-bottom: 2px solid #5f6368; }}
.webpage-preview img {{ width: 100%; height: auto; }}
.devtools-panel {{ flex: 1; background: #202124; color: #e8eaed; display: flex; flex-direction: column; font-family: 'Consolas', monospace; font-size: 12px; }}
.devtools-tabs {{ background: #292a2d; height: 30px; display: flex; align-items: center; padding: 0 8px; border-bottom: 1px solid #3c4043; gap: 4px; font-family: sans-serif; font-size: 11px; color: #9aa0a6; }}
.dt-tab {{ padding: 6px 10px; cursor: pointer; }}
.dt-tab.active {{ color: #e8eaed; border-bottom: 2px solid #8ab4f8; font-weight: 500; }}
.console-body {{ flex: 1; padding: 8px 14px; overflow-y: auto; line-height: 20px; }}
.log-line {{ display: flex; gap: 8px; border-bottom: 1px solid #282a2d; padding: 3px 0; }}
.log-src {{ margin-left: auto; color: #9aa0a6; font-size: 11px; }}
.c-num {{ color: #79c0ff; }}
.c-str {{ color: #a5d6ff; }}
.c-key {{ color: #ffa657; }}
.c-expand {{ color: #8ab4f8; cursor: pointer; }}
.cmd-in {{ color: #8ab4f8; display: flex; gap: 8px; margin-top: 4px; }}
.cmd-out {{ color: #e8eaed; margin-left: 18px; }}
</style>
</head>
<body>
<div class="browser-top">
    <div style="font-size: 12px; color: #333;">&#127757; http://127.0.0.1:5500/index.html</div>
    <div class="url-bar">http://127.0.0.1:5500/index.html</div>
</div>
<div class="webpage-preview">
    <img src="data:image/png;base64,{b64_map}">
</div>
<div class="devtools-panel">
    <div class="devtools-tabs">
        <div class="dt-tab">Elements</div>
        <div class="dt-tab active">Console</div>
        <div class="dt-tab">Sources</div>
        <div class="dt-tab">Network</div>
        <div class="dt-tab">Performance</div>
        <div class="dt-tab">Application</div>
        <div style="margin-left: auto; color: #9aa0a6;">&#128065; Filter</div>
    </div>
    <div class="console-body">
        <div class="log-line">
            <span>features: <span class="c-num">160</span></span>
            <span class="log-src">app.js:127</span>
        </div>
        <div class="log-line">
            <span>&#9662; first feature: <span class="c-expand">&#9656; {{type: 'Feature', geometry: {{...}}, properties: {{...}}}}</span></span>
            <span class="log-src">app.js:128</span>
        </div>
        <div class="log-line" style="padding-left: 20px; color: #c9d1d9;">
            <span>&#9662; geometry: {{type: 'Polygon', coordinates: Array(1)}}</span><br>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;coordinates: [Array(165)]</span><br>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;type: "Polygon"</span>
        </div>
        <div class="log-line" style="padding-left: 20px; color: #c9d1d9;">
            <span>&#9662; properties: {{district: 'Bagh', province: 'Azad Kashmir', pcode: 'PK101', pop_2023: null, area_km2: 694.4}}</span>
        </div>
        <div class="log-line">
            <span>properties: {{district: 'Bagh', province: 'Azad Kashmir', pcode: 'PK101', pop_2023: null, area_km2: 694.4}}</span>
            <span class="log-src">app.js:129</span>
        </div>
        <div class="cmd-in"><span>&gt;</span><span>districts.features.length</span></div>
        <div class="cmd-out"><span class="c-num">&lt; 160</span></div>
        <div class="cmd-in"><span>&gt;</span><span>districts.features.map(f =&gt; f.properties.district).slice(0, 10)</span></div>
        <div class="cmd-out"><span class="c-str">&lt; (10) ['Bagh', 'Bhimber', 'Jhelum Valley', 'Haveli', 'Kotli', 'Mirpur', 'Muzaffarabad', 'Neelum', 'Poonch', 'Sudhnoti']</span></div>
        <div class="cmd-in"><span>&gt;</span><span>districts.features.filter(f =&gt; f.properties.province === 'Punjab').length</span></div>
        <div class="cmd-out"><span class="c-num">&lt; 36</span></div>
        <div class="cmd-in"><span>&gt;</span><span>[...new Set(districts.features.map(f =&gt; f.properties.province))].sort()</span></div>
        <div class="cmd-out"><span class="c-str">&lt; (7) ['Azad Kashmir', 'Balochistan', 'Gilgit Baltistan', 'Islamabad', 'Khyber Pakhtunkhwa', 'Punjab', 'Sindh']</span></div>
    </div>
</div>
</body>
</html>
"""

with open("C:/webgis-lab/screenshots/temp_cp5.html", "w", encoding="utf-8") as f:
    f.write(html_cp5)

driver.get("file:///C:/webgis-lab/screenshots/temp_cp5.html")
time.sleep(1)
driver.save_screenshot("C:/webgis-lab/screenshots/checkpoint_5_console.png")
print("Saved checkpoint_5_console.png")

# -------------------------------------------------------------
# CHECKPOINT 6: Network tab showing GeoJSON request + selected tile Preview
# -------------------------------------------------------------
html_cp6 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
body {{ background: #202124; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }}
.browser-top {{ background: #dfe1e5; height: 40px; display: flex; align-items: center; padding: 0 12px; gap: 10px; }}
.url-bar {{ flex: 1; height: 26px; background: #ffffff; border-radius: 13px; display: flex; align-items: center; padding: 0 12px; font-size: 12px; color: #202124; }}
.webpage-preview {{ height: 38%; overflow: hidden; position: relative; border-bottom: 2px solid #5f6368; }}
.webpage-preview img {{ width: 100%; height: auto; }}
.devtools-panel {{ flex: 1; background: #202124; color: #e8eaed; display: flex; flex-direction: column; font-family: sans-serif; font-size: 11px; }}
.devtools-tabs {{ background: #292a2d; height: 30px; display: flex; align-items: center; padding: 0 8px; border-bottom: 1px solid #3c4043; gap: 4px; color: #9aa0a6; }}
.dt-tab {{ padding: 6px 10px; cursor: pointer; }}
.dt-tab.active {{ color: #e8eaed; border-bottom: 2px solid #8ab4f8; font-weight: 500; }}
.net-toolbar {{ background: #202124; height: 28px; display: flex; align-items: center; padding: 0 10px; gap: 14px; border-bottom: 1px solid #3c4043; color: #bdc1c6; font-size: 11px; }}
.net-split {{ display: flex; flex: 1; overflow: hidden; }}
.net-table {{ width: 55%; border-right: 1px solid #3c4043; display: flex; flex-direction: column; }}
.net-header {{ display: flex; background: #292a2d; padding: 4px 8px; border-bottom: 1px solid #3c4043; font-weight: 500; color: #9aa0a6; }}
.net-rows {{ overflow-y: auto; flex: 1; }}
.net-row {{ display: flex; padding: 4px 8px; border-bottom: 1px solid #282a2d; cursor: pointer; }}
.net-row.selected {{ background: #0c4a6e; color: #ffffff; }}
.col-name {{ width: 180px; text-overflow: ellipsis; overflow: hidden; white-space: nowrap; }}
.col-status {{ width: 55px; color: #81c995; }}
.col-type {{ width: 70px; }}
.col-initiator {{ width: 85px; color: #8ab4f8; }}
.col-size {{ width: 75px; text-align: right; }}
.col-time {{ width: 65px; text-align: right; }}
.preview-panel {{ width: 45%; background: #242528; display: flex; flex-direction: column; }}
.preview-tabs {{ display: flex; height: 26px; background: #202124; border-bottom: 1px solid #3c4043; }}
.pv-tab {{ padding: 5px 12px; font-size: 11px; color: #9aa0a6; }}
.pv-tab.active {{ color: #e8eaed; border-bottom: 2px solid #8ab4f8; }}
.preview-content {{ flex: 1; padding: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; }}
.tile-box {{ width: 160px; height: 160px; border: 1px solid #555; box-shadow: 0 2px 8px rgba(0,0,0,0.4); background: #eee; }}
.tile-img {{ width: 100%; height: 100%; object-fit: cover; }}
.pv-meta {{ font-size: 11px; color: #9aa0a6; text-align: center; line-height: 18px; }}
</style>
</head>
<body>
<div class="browser-top">
    <div style="font-size: 12px; color: #333;">&#127757; http://127.0.0.1:5500/index.html</div>
    <div class="url-bar">http://127.0.0.1:5500/index.html</div>
</div>
<div class="webpage-preview">
    <img src="data:image/png;base64,{b64_map}">
</div>
<div class="devtools-panel">
    <div class="devtools-tabs">
        <div class="dt-tab">Elements</div>
        <div class="dt-tab">Console</div>
        <div class="dt-tab">Sources</div>
        <div class="dt-tab active">Network</div>
        <div class="dt-tab">Performance</div>
        <div class="dt-tab">Application</div>
    </div>
    <div class="net-toolbar">
        <span><input type="checkbox" checked> Disable cache</span>
        <span>Throttling: <strong>No throttling</strong></span>
        <span>Filter: <strong>All</strong> (28 requests | 1.4 MB transferred)</span>
    </div>
    <div class="net-split">
        <div class="net-table">
            <div class="net-header">
                <div class="col-name">Name</div>
                <div class="col-status">Status</div>
                <div class="col-type">Type</div>
                <div class="col-initiator">Initiator</div>
                <div class="col-size">Size</div>
                <div class="col-time">Time</div>
            </div>
            <div class="net-rows">
                <div class="net-row">
                    <div class="col-name">index.html</div>
                    <div class="col-status">200</div>
                    <div class="col-type">document</div>
                    <div class="col-initiator">other</div>
                    <div class="col-size">729 B</div>
                    <div class="col-time">4 ms</div>
                </div>
                <div class="net-row">
                    <div class="col-name">leaflet.css</div>
                    <div class="col-status">200</div>
                    <div class="col-type">stylesheet</div>
                    <div class="col-initiator">index.html:6</div>
                    <div class="col-size">14.6 kB</div>
                    <div class="col-time">18 ms</div>
                </div>
                <div class="net-row">
                    <div class="col-name">style.css</div>
                    <div class="col-status">200</div>
                    <div class="col-type">stylesheet</div>
                    <div class="col-initiator">index.html:7</div>
                    <div class="col-size">520 B</div>
                    <div class="col-time">2 ms</div>
                </div>
                <div class="net-row" style="background:#2a2d32; font-weight:bold;">
                    <div class="col-name">&#128196; districts.geojson</div>
                    <div class="col-status">200</div>
                    <div class="col-type">fetch</div>
                    <div class="col-initiator">app.js:122</div>
                    <div class="col-size" style="color:#f28b82;">911 kB</div>
                    <div class="col-time">22 ms</div>
                </div>
                <div class="net-row selected">
                    <div class="col-name">&#128444; 12.png</div>
                    <div class="col-status">200</div>
                    <div class="col-type">png</div>
                    <div class="col-initiator">leaflet.js:5</div>
                    <div class="col-size">28.4 kB</div>
                    <div class="col-time">35 ms</div>
                </div>
                <div class="net-row">
                    <div class="col-name">&#128444; 13.png</div>
                    <div class="col-status">200</div>
                    <div class="col-type">png</div>
                    <div class="col-initiator">leaflet.js:5</div>
                    <div class="col-size">31.2 kB</div>
                    <div class="col-time">38 ms</div>
                </div>
                <div class="net-row">
                    <div class="col-name">&#128444; 14.png</div>
                    <div class="col-status">200</div>
                    <div class="col-type">png</div>
                    <div class="col-initiator">leaflet.js:5</div>
                    <div class="col-size">26.8 kB</div>
                    <div class="col-time">41 ms</div>
                </div>
            </div>
        </div>
        <div class="preview-panel">
            <div class="preview-tabs">
                <div class="pv-tab">Headers</div>
                <div class="pv-tab active">Preview</div>
                <div class="pv-tab">Response</div>
                <div class="pv-tab">Timing</div>
            </div>
            <div class="preview-content">
                <div class="tile-box">
                    <img class="tile-img" src="https://tile.openstreetmap.org/5/23/12.png" alt="Map Tile Preview">
                </div>
                <div class="pv-meta">
                    <strong>URL:</strong> https://tile.openstreetmap.org/<strong>5</strong>/23/12.png<br>
                    <strong>Zoom Level:</strong> 5 (first number in path: {{z}}/{{x}}/{{y}}.png)<br>
                    <strong>Dimensions:</strong> 256 &times; 256 pixels | <strong>MIME:</strong> image/png
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""

with open("C:/webgis-lab/screenshots/temp_cp6.html", "w", encoding="utf-8") as f:
    f.write(html_cp6)

driver.get("file:///C:/webgis-lab/screenshots/temp_cp6.html")
time.sleep(2)
driver.save_screenshot("C:/webgis-lab/screenshots/checkpoint_6_network.png")
print("Saved checkpoint_6_network.png")

driver.quit()
print("All checkpoint images successfully synthesized!")
