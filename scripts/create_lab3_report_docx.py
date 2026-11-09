import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

doc = Document()

# Set standard 1 inch margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(1)
    s.bottom_margin = Inches(1)
    s.left_margin = Inches(1)
    s.right_margin = Inches(1)

# Document Title
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(4)
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = title_p.add_run("Web GIS Laboratory 3: District Dashboard")
run_title.font.name = "Calibri"
run_title.font.size = Pt(26)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(31, 78, 121)

sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_after = Pt(16)
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_sub = sub_p.add_run("Layers, Controls, Proportional Symbols, Panes, and Event Interaction\nComplete Technical & Analytical Report")
run_sub.font.name = "Calibri"
run_sub.font.size = Pt(13)
run_sub.font.color.rgb = RGBColor(89, 89, 89)

# Meta Box Table
meta_table = doc.add_table(rows=5, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_table.autofit = False

metadata = [
    ("Course & Department", "MS Remote Sensing and GIS | Institute of Geographical Information Systems (IGIS)"),
    ("Institution", "National University of Sciences and Technology (NUST), Islamabad"),
    ("Instructor", "Dr. Shahid Nawaz Khan"),
    ("Student Author", "Muhammad Ibrahim"),
    ("Repository & Live Dashboard", "https://github.com/ebraheem360/webgis-lab-536712\nLive: https://ebraheem360.github.io/webgis-lab-536712/lab3/")
]

for i, (k, v) in enumerate(metadata):
    cell_k = meta_table.cell(i, 0)
    cell_v = meta_table.cell(i, 1)
    cell_k.width = Inches(2.2)
    cell_v.width = Inches(4.3)
    set_cell_background(cell_k, "F2F2F2")
    set_cell_background(cell_v, "FAFAFA")
    set_cell_margins(cell_k, 80, 80, 120, 120)
    set_cell_margins(cell_v, 80, 80, 120, 120)
    
    pk = cell_k.paragraphs[0]
    rk = pk.add_run(k)
    rk.font.name = "Calibri"
    rk.font.size = Pt(10)
    rk.font.bold = True
    rk.font.color.rgb = RGBColor(31, 78, 121)
    
    pv = cell_v.paragraphs[0]
    rv = pv.add_run(v)
    rv.font.name = "Calibri"
    rv.font.size = Pt(10)
    rv.font.color.rgb = RGBColor(50, 50, 50)

doc.add_paragraph().paragraph_format.space_after = Pt(12)

def add_heading_1(text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(18)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = RGBColor(31, 78, 121)
    return h

def add_heading_2(text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = RGBColor(46, 117, 182)
    return h

def add_body(text, bold_prefix=None, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.font.name = "Calibri"
        rb.font.size = Pt(11)
        rb.font.bold = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(50, 50, 50)
    return p

def add_image_box(img_path, caption):
    if os.path.exists(img_path):
        doc.add_paragraph().paragraph_format.space_before = Pt(6)
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = "Calibri"
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(89, 89, 89)

# ----------------- SECTION 1 -----------------
add_heading_1("1. Project Architecture & Setup (Checkpoint 1)")
add_body("Web GIS Laboratory 3 builds upon the foundational spatial data structures established in Lab 2, upgrading a single choropleth display into an interactive, multi-layered dashboard. The application is decoupled cleanly across index.html, style.css, and app.js inside a dedicated /lab3/ directory to ensure Lab 2 remains accessible and operational on GitHub Pages.")
add_body("Relative data paths load directly from lab3/data/districts.geojson and lab3/data/district_points.geojson, utilizing Promise.all() for concurrent network requests.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_1_vscode.png", "Figure 1 (Checkpoint 1): VS Code showing lab3 project structure, data files, and script implementation.")

# ----------------- SECTION 2 -----------------
add_heading_1("2. Point Layer in QGIS: Centroid vs. Point on Surface (Checkpoint 2)")
add_body("A fundamental principle of thematic cartography is that symbols representing an administrative region must fall unambiguously inside that region's visual boundary. Geometric centroids calculate the center of mass based strictly on vertex coordinates. For concave, crescent, or irregular shapes, this center of mass frequently falls outside the polygon boundary entirely.")
add_body("By testing both Centroids and Point on Surface across all 160 districts in QGIS, Sibi District in Balochistan was identified as having its centroid outside its administrative boundary:")
add_body("• District: Sibi, Balochistan\n• Calculated Centroid: (67.94472°E, 29.76149°N) — Falls outside Sibi inside neighboring Harnai District!\n• Point on Surface: (68.25013°E, 29.72711°N) — Guaranteed by topology to remain strictly inside Sibi.\n• Exported File: lab3/data/district_points.geojson | 160 features | 35,737 bytes (34.9 KB) | EPSG:4326 | 5 decimals.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_2_qgis_sibi.png", "Figure 2 (Checkpoint 2): QGIS visualization of Sibi District demonstrating the centroid (red) displaced into Harnai, contrasted with Point on Surface (green) secured inside Sibi.")

# ----------------- SECTION 3 -----------------
add_heading_1("3. Basemaps, Constraints, and Tile Architecture (Checkpoint 3)")
add_body("The Leaflet map is instantiated with strict boundary envelopes (maxBounds: [[21.5, 58.5], [39.0, 80.5]], maxBoundsViscosity: 1.0) and zoom limits (minZoom: 5, maxZoom: 14) tailored to Pakistan's geographic extent.")
add_body("Three basemaps are offered through L.control.layers: Carto Positron (default), OpenStreetMap, and Esri World Imagery (Satellite).")
add_heading_2("Esri Tile URL Analysis (Section 3.4)")
add_body("Inspection of network traffic for Esri World Imagery reveals tile request URLs formatted as:")
add_body("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/5/13/23", bold_prefix="Sample URL: ")
add_body("• Zoom Level ({z}): 5\n• Row ({y}): 13 (the first coordinate number in the URL path)\n• Column ({x}): 23 (the second coordinate number in the URL path)")
add_body("Architectural Note: Standard Slippy Maps (OSM and Carto) follow the {z}/{x}/{y} pattern (Column before Row). Esri ArcGIS Server MapServer services invert this standard, requiring {z}/{y}/{x} (Row before Column). Leaflet substitutes placeholders by token name, necessitating exact template specification.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_3_esri_tile_network.png", "Figure 3 (Checkpoint 3): DevTools Network panel recording Esri World Imagery tile requests, identifying row 13 and column 23 at zoom 5.")

# ----------------- SECTION 4 -----------------
add_heading_1("4. Thematic Layer: Population Density Choropleth (Checkpoint 4)")
add_body("Cartographic Rule: Choropleth maps must depict rates, ratios, percentages, or densities—never raw counts or absolute totals. Shading large districts (e.g. Chagai, 45,912 km²) by raw population gives a false impression of massive human concentration simply because the polygon is large. Dividing 2023 census population by area_km2 yields true density.")
add_body("Classification: The 135 reporting districts are classed into 5 sequential blue steps: under 50 (22), 50 to 150 (41), 150 to 400 (34), 400 to 1000 (18), and over 1000 (20). An explicit neutral grey (#c9cfd1) styles the 25 districts without census data.")
add_body("Layer Persistence: A permanent L.featureGroup() (districtGroup) is added to the layer switcher, ensuring that when draw() rebuilds the GeoJSON layer during province filtering, the layer control retains a stable handle.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_4_density_map.png", "Figure 4 (Checkpoint 4): Population density choropleth map with the layer control expanded and density legend.")

# ----------------- SECTION 5 -----------------
add_heading_1("5. Interaction: Highlighting and Dynamic Info Panel (Checkpoint 5)")
add_body("To avoid popup clutter, a custom Leaflet control (L.control({ position: 'topright' })) serves as a lightweight, non-intrusive information panel that updates dynamically on hover. Click and scroll propagation are suppressed via L.DomEvent.")
add_body("Hovering a district triggers highlight(), which elevates the polygon outline (weight: 3, #1a202c), brings it to front, and updates the info panel. Unhovering calls districts.resetStyle(e.target) to seamlessly restore the original classification styling.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_5_hover_highlight.png", "Figure 5 (Checkpoint 5): Hover highlight on Lahore showing dark outline, tooltip, and info panel reporting population (13,004,135) and density (7,339 per km²).")

# ----------------- SECTION 6 -----------------
add_heading_1("6. Proportional Symbols and Custom Panes (Checkpoint 6)")
add_body("Proportional symbols represent counts (pop_2023). To prevent polygon hover bringToFront() from occluding circle symbols, a custom Leaflet map pane ('symbols', z-index 450) was established above overlayPane (400) and below markers/tooltips (600+).")
add_body("Perceptual Sizing: Radius is computed using the square root transformation (radius = sqrt(pop_2023) / 160) so that symbol visual area—not radius—scales linearly with population.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_6a_proportional_symbols.png", "Figure 6A (Checkpoint 6): Complete dashboard displaying proportional population circles floating in their dedicated pane above density shading, with dual legend.")
add_heading_2("Metres vs. Pixels Demonstration (NUST Overlay)")
add_body("The NUST overlay directly contrasts L.circle (radius: 25000 in ground metres) against L.circleMarker (radius: 6 in screen pixels). At Zoom 6 (national scale), the 25 km circle appears compact; at Zoom 10 (metropolitan scale), it spans the screen while precisely matching 25 km on the scale bar. In contrast, L.circleMarker maintains a constant 6-pixel visual footprint.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_6b_nust_overlay.png", "Figure 6B (Checkpoint 6): NUST overlay at Zoom 6 (scale bar 100 km) vs Zoom 10 (scale bar 5 km) illustrating ground distance vs screen pixel rendering.")

# ----------------- SECTION 7 -----------------
add_heading_1("7. Map Events: Dynamic Registration and Removal (Checkpoint 7)")
add_body("An interactive checkbox (#coords) toggles a coordinate click handler (map.on / map.off).")
add_heading_2("Laboratory Observations:")
add_body("1. Sea Click & District Click: Clicking the Arabian Sea opens a coordinate popup (24.2185°N, 66.8421°E). Clicking a district executes both handlers: the district click event zooms to the district bounds, while the map click event opens the coordinate popup.\n2. Click Propagation: Clicking inside the legend produces no popup because L.DomEvent.disableClickPropagation(div) halts bubbling. When removed, clicks on the legend bleed through to the map canvas beneath.\n3. Unticking: Unchecking #coords invokes map.off('click', showCoordinates), cleanly deregistering the listener.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_7_coordinates_sea.png", "Figure 7 (Checkpoint 7): Active coordinate popup in the Arabian Sea south of Karachi.")

# ----------------- SECTION 8 -----------------
add_heading_1("8. Filter by Province Extension (Checkpoint 8)")
add_body("A dynamic dropdown populated from district feature attributes filters the map by province. When Gilgit Baltistan is selected, 14 districts are reported, shaded grey, and 0 circles appear. This occurs because 2023 census counts are null for this region; the hasPopulation filter safely drops null features to prevent NaN runtime exceptions.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_8_filter_province.png", "Figure 8 (Checkpoint 8): Filter active for Punjab (41 districts) with layer overlays switchable on the rebuilt layers.")

# ----------------- SECTION 9 -----------------
add_heading_1("9. SVG vs Canvas Rendering Benchmark (Checkpoint 9)")
add_body("The rendering engine was benchmarked across 5 reloads using performance.now() via the URL parameter index.html?canvas.")

# Benchmark Table
b_table = doc.add_table(rows=6, cols=3)
b_table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Metric / Architectural Feature", "SVG Mode (Default)", "Canvas Mode (?canvas)"]
for j, h in enumerate(headers):
    c = b_table.cell(0, j)
    set_cell_background(c, "1F4E79")
    set_cell_margins(c, 80, 80, 100, 100)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

table_data = [
    ("draw('all'), Median of 5 runs", "48.1 ms (77.6, 46.9, 69.0, 48.1, 47.0)", "46.5 ms (35.2, 47.6, 48.1, 46.5, 28.8)"),
    ("Elements inside leaflet-overlay-pane", "162 elements (1 <svg> + 1 <g> + 160 <path>)", "1 element (1 <canvas>)"),
    ("Elements inside leaflet-symbols-pane", "137 elements (1 <svg> + 1 <g> + 135 <path>)", "1 element (1 <canvas>)"),
    ("Hover highlight still works?", "Yes (Native SVG event listeners)", "Yes (Leaflet internal hit detection)"),
    ("Can you inspect one district in Elements?", "Yes (Discrete DOM path nodes)", "No (Flat bitmap; only <canvas> tag)")
]

for i, row_data in enumerate(table_data):
    for j, val in enumerate(row_data):
        c = b_table.cell(i+1, j)
        set_cell_background(c, "F2F2F2" if (i % 2 == 1) else "FFFFFF")
        set_cell_margins(c, 70, 70, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        if j == 0:
            r.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(6)
add_body("Architectural Analysis: For 160 districts and 135 circles, the performance difference is negligible (~48 ms vs ~46 ms). However, for the tehsil layer (administrative level 3, ~600 units with >100,000 vertices), SVG suffers from severe DOM bloat, memory footprint growth (>150 MB), and reflow stutter during panning. Canvas excels at scale because it renders directly to an immediate-mode 2D pixel buffer, bypassing the DOM entirely and maintaining smooth 60 FPS interactions.")
add_image_box(r"C:\webgis-lab\screenshots\Lab3\checkpoint_9_elements_comparison.png", "Figure 9 (Checkpoint 9): Elements tab comparison showing 162 discrete SVG path nodes in default mode vs. a single <canvas> element in Canvas mode.")

# ----------------- SECTION 10 -----------------
add_heading_1("10. Answers to Laboratory Questions (Section 10.3)")

add_heading_2("Question 1: Large vs. Small Districts on a Count Choropleth")
add_body("Q: Lab 2 shaded districts by population. Name one large, thinly populated district and one small, crowded one, and explain how each would mislead on the Lab 2 map.", bold_prefix="")
add_body("Answer: Chagai in Balochistan (45,912 km², pop ~269,000, density ~5.8/km²) is large and thinly populated. Lahore in Punjab (1,772 km², pop ~13,004,000, density ~7,339/km²) or Karachi Central in Sindh (69 km², pop ~3,822,000, density ~55,391/km²) are small and crowded.\nOn the Lab 2 map, Chagai occupied a massive portion of the canvas and appeared visually prominent simply because of its geographic area, falsely suggesting immense population concentration. In contrast, Lahore and Karachi Central appeared as tiny, barely noticeable specks despite housing millions. Choropleths shade areas, so the displayed metric must be normalized by area (density) to prevent area from biasing the reader's perception.")

add_heading_2("Question 2: Perceptual Sizing with Square Roots")
add_body("Q: radiusFor takes a square root. What would the map suggest about Lahore against a district of 3 million if it did not?", bold_prefix="")
add_body("Answer: The human eye assesses circular symbols by area (A = πr²), not radius. If radius scaled linearly with population, the radius ratio between Lahore (13M) and a 3M district would be 13/3 ≈ 4.33. The resulting visual area ratio would be (4.33)² ≈ 18.78. The map would visually suggest that Lahore is nearly 19 times larger than a 3-million district rather than 4.3 times, severely misleading the reader and occluding neighboring districts. Taking the square root ensures perceived symbol area scales 1:1 with population.")

add_heading_2("Question 3: Persistent Layer Groups in Layer Controls")
add_body("Q: Why does the layer control hold districtGroup rather than the L.geoJSON layer itself?", bold_prefix="")
add_body("Answer: During province filtering, the district GeoJSON layer is destroyed and re-instantiated. If the layer control held a direct reference to the initial L.geoJSON layer, its switcher checkbox would become orphaned, pointing to an object no longer present on the map. By holding a permanent L.featureGroup() (districtGroup), the layer control maintains an unbroken reference while draw() clears and updates its internal layers.")

add_heading_2("Question 4: Dedicated Panes vs OverlayPane Draw Order")
add_body("Q: What would go wrong if the circles were drawn in overlayPane instead of the symbols pane? Describe what the user would see when hovering.", bold_prefix="")
add_body("Answer: Both polygons and circle markers are vector SVG paths. Within a shared overlayPane (z-index 400), invoking e.target.bringToFront() during district hover moves the hovered polygon's SVG <path> to the bottom of the container, drawing it in front of all other paths. If circles were in overlayPane, hovering over a district would lift the large colored polygon above the proportional circles, hiding the circles beneath the polygon fill. The symbols pane (z-index 450) ensures circles remain permanently on top.")

add_heading_2("Question 5: Named Functions and map.off")
add_body("Q: Why can map.off remove showCoordinates, when it could not remove an anonymous function passed to map.on?", bold_prefix="")
add_body("Answer: In JavaScript, functions are compared by object reference (===). Leaflet stores listeners in an internal array. map.off looks up the exact function reference to remove it. When a named function (showCoordinates) is used, the exact memory reference is provided. If an anonymous function is used (function(e) { ... }), there is no persistent reference handle. Calling map.off with another inline function creates a different object that fails the equality check, leaving the listener permanently bound.")

add_heading_2("Question 6: Ground Metres vs. Screen Pixels on the NUST Overlay")
add_body("Q: On the NUST overlay, which circle would you use to show a 25 km evacuation zone, and which to mark the campus on a national map? Why?", bold_prefix="")
add_body("Answer: For a 25 km evacuation zone, use L.circle (radius: 25000 in ground metres). An evacuation zone is a physical real-world spatial boundary; as the user zooms in or out, L.circle expands or contracts on screen to constantly represent 25 kilometers of ground terrain, aligning with the scale bar.\nTo mark the campus on a national map, use L.circleMarker (radius: 6 in screen pixels). A map marker identifies a location point and must remain legible across all zoom levels without expanding into an oversized blob at high zoom or vanishing into sub-pixel obscurity at national zoom.")

output_docx = r"C:\webgis-lab\lab3\report.docx"
doc.save(output_docx)
print(f"Report docx successfully generated at: {output_docx}")
