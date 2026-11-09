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

# Margins
for s in doc.sections:
    s.top_margin = Inches(1)
    s.bottom_margin = Inches(1)
    s.left_margin = Inches(1)
    s.right_margin = Inches(1)

# Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(0)
p_title.paragraph_format.space_after = Pt(4)
r_title = p_title.add_run("Web GIS Laboratory 4: Getting Started with GeoDjango")
r_title.font.name = "Calibri"
r_title.font.size = Pt(24)
r_title.font.bold = True
r_title.font.color.rgb = RGBColor(31, 78, 121)

p_sub = doc.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(14)
r_sub = p_sub.add_run("Django, PostGIS, Spatial ORM, Admin Panel, and Leaflet Integration\nComplete Technical & Analytical Report")
r_sub.font.name = "Calibri"
r_sub.font.size = Pt(13)
r_sub.font.color.rgb = RGBColor(89, 89, 89)

# Metadata Table
meta_table = doc.add_table(rows=5, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_table.autofit = False

metadata = [
    ("Course & Department", "MS Remote Sensing and GIS | Institute of Geographical Information Systems (IGIS)"),
    ("Institution", "National University of Sciences and Technology (NUST), Islamabad"),
    ("Instructor", "Dr. Shahid Nawaz Khan"),
    ("Student Author", "Muhammad Ibrahim"),
    ("Repository & Application", "https://github.com/ebraheem360/webgis-lab-536712\nLocal: http://127.0.0.1:8000/ | Admin: http://127.0.0.1:8000/admin/")
]

for i, (k, v) in enumerate(metadata):
    ck = meta_table.cell(i, 0)
    cv = meta_table.cell(i, 1)
    ck.width = Inches(2.2)
    cv.width = Inches(4.3)
    set_cell_background(ck, "F2F2F2")
    set_cell_background(cv, "FAFAFA")
    set_cell_margins(ck, 70, 70, 100, 100)
    set_cell_margins(cv, 70, 70, 100, 100)
    pk = ck.paragraphs[0]
    rk = pk.add_run(k)
    rk.font.name = "Calibri"
    rk.font.size = Pt(9.5)
    rk.font.bold = True
    rk.font.color.rgb = RGBColor(31, 78, 121)
    pv = cv.paragraphs[0]
    rv = pv.add_run(v)
    rv.font.name = "Calibri"
    rv.font.size = Pt(9.5)
    rv.font.color.rgb = RGBColor(50, 50, 50)

doc.add_paragraph().paragraph_format.space_after = Pt(10)

def add_h1(text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(16)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = RGBColor(31, 78, 121)
    return h

def add_h2(text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(3)
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(46, 117, 182)
    return h

def add_p(text, bold_prefix=None, space_after=5):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.font.name = "Calibri"
        rb.font.size = Pt(10.5)
        rb.font.bold = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = RGBColor(50, 50, 50)
    return p

def add_img(img_path, caption):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(3)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(6.0))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption)
        r_cap.font.name = "Calibri"
        r_cap.font.size = Pt(9.0)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(89, 89, 89)

# ----------------- SECTION 1: ARCHITECTURE & VERSIONS -----------------
add_h1("1. Architectural Overview & System Environment")
add_p("Laboratory 4 migrates the client-heavy mapping approach of Labs 2 and 3 into an enterprise three-tier Web GIS. The application is backed by a relational spatial database (PostgreSQL 18 with PostGIS 3.6.2), managed by a Python application server (Django 6.1.2 with GeoDjango), and visualized in the browser through Leaflet 1.9.")

# Version Table
v_table = doc.add_table(rows=7, cols=3)
v_table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Component", "Software / Library", "Version"]
for j, h in enumerate(headers):
    c = v_table.cell(0, j)
    set_cell_background(c, "1F4E79")
    set_cell_margins(c, 60, 60, 80, 80)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

v_data = [
    ("Python Runtime", "CPython (Windows 64-bit)", "3.13.14"),
    ("Web Framework", "Django / GeoDjango", "6.1.2"),
    ("Database Server", "PostgreSQL", "18.0"),
    ("Spatial Extension", "PostGIS", "3.6.2"),
    ("Data Translation", "GDAL", "3.9.2"),
    ("Geometry Engine", "GEOS", "3.12.2-CAPI-1.18.2")
]
for i, row in enumerate(v_data):
    for j, val in enumerate(row):
        c = v_table.cell(i+1, j)
        set_cell_background(c, "F2F2F2" if (i % 2 == 1) else "FFFFFF")
        set_cell_margins(c, 50, 50, 80, 80)
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        if j == 0:
            r.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(6)

# ----------------- SECTION 2: CHECKPOINTS -----------------
add_h1("2. Checkpoints & Verification Evidence")

add_h2("Checkpoint 1: Django Project Creation")
add_p("The Django project webgis and application districts were created inside lab4. The development server ran successfully, confirming framework initialization.")
add_img(r"C:\webgis-lab\screenshots\Lab4\1.png", "Figure 1 (Checkpoint 1): Django 6.1 welcome screen confirming successful project creation and execution.")

add_h2("Checkpoint 2: PostGIS Extension in PostgreSQL 18")
add_p("Database webgis was created in pgAdmin 4. Running CREATE EXTENSION postgis; and SELECT postgis_full_version(); proved spatial capabilities were online.")
add_img(r"C:\webgis-lab\screenshots\Lab4\2.png", "Figure 2 (Checkpoint 2): pgAdmin 4 demonstrating postgis_full_version() output on database webgis.")

add_h2("Checkpoint 3: Connecting GeoDjango to PostGIS")
add_p("GeoDjango was pointed to QGIS C-libraries (GDAL 3.9.2, GEOS 3.12.2) via settings.py. System check and initial migrations ran cleanly, creating Django's tables alongside PostGIS's spatial_ref_sys.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_3_connection.png", "Figure 3 (Checkpoint 3): Shell verification of GDAL/GEOS versions and pgAdmin tables tree view.")

add_h2("Checkpoint 4: Spatial Model to Table (sqlmigrate)")
add_p("The District model was defined with a MultiPolygonField(srid=4326). Running sqlmigrate showed the creation of a geometry(MULTIPOLYGON, 4326) column and an automated GIST spatial index.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_4_sqlmigrate.png", "Figure 4 (Checkpoint 4): sqlmigrate output showing DDL generation and pgAdmin districts_district column definitions.")

add_h2("Checkpoint 5: Data Ingestion & Interactive ORM Queries")
add_p("districts/load.py ingested all 160 features into PostGIS. Interactive queries in the Django shell confirmed 160 total districts, 29 in Sindh, 25 without census counts, and verified Lahore's MultiPolygon geometry (238 vertices).")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_5_orm_shell.png", "Figure 5 (Checkpoint 5): PowerShell session recording the data loader execution and the seven ORM analytical queries.")

add_h2("Checkpoint 6: Django Admin Exploration & Direct Database Update")
add_p("Registering District with admin.GISModelAdmin embedded an OpenLayers geometry editing widget. Filtering by Sindh showed 29 districts. Lahore's population was updated from 13004135 to 13500000, verified directly in PostgreSQL via SQL, and restored.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_6a_admin_filter_sindh.png", "Figure 6A (Checkpoint 6): Django admin filtered to Sindh (29 districts).")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_6b_admin_lahore_map.png", "Figure 6B (Checkpoint 6): Lahore District change form showing interactive vector geometry on OpenStreetMap.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_6c_pgadmin_update.png", "Figure 6C (Checkpoint 6): SQL query verification in pgAdmin proving live database record modification.")

add_h2("Checkpoint 7: Leaflet Frontend Fed by PostGIS")
add_p("Leaflet fetches GeoJSON dynamically from /api/districts/. The payload size is 945 kB, serialized directly from PostGIS records.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_7a_map_tooltip.png", "Figure 7A (Checkpoint 7): Leaflet map rendering PostGIS GeoJSON with tooltip on Lahore.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_7b_network_size.png", "Figure 7B (Checkpoint 7): DevTools Network panel recording 945 kB payload transferred for /api/districts/.")

add_h2("Checkpoint 8: Server-Side Spatial Query & Area Distortion (Extension)")
add_p("Clicking the map at NUST coordinates (33.6423°N, 72.9906°E) invokes PostGIS ST_Contains on the server, returning Islamabad District and opening an informative popup.")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_8a_spatial_click_popup.png", "Figure 8A (Checkpoint 8): Leaflet click event triggering server-side reverse geocoding via /api/where/.")

# Area Query Table
add_h2("PostGIS Area Distortion Comparison (SQL Results)")
a_table = doc.add_table(rows=4, cols=6)
a_table.alignment = WD_TABLE_ALIGNMENT.CENTER
a_headers = ["District", "Latitude", "Stored Area", "Geodesic Area", "Web Mercator", "Distortion Ratio"]
for j, h in enumerate(a_headers):
    c = a_table.cell(0, j)
    set_cell_background(c, "1F4E79")
    set_cell_margins(c, 60, 60, 80, 80)
    p = c.paragraphs[0]
    r = p.add_run(h)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)

a_data = [
    ("Gwadar", "25.12° N", "11,574 km²", "11,574 km²", "14,244 km²", "1.231 (+23.1%)"),
    ("Lahore", "31.55° N", "1,730 km²", "1,730 km²", "2,385 km²", "1.379 (+37.9%)"),
    ("Gilgit", "35.92° N", "4,016 km²", "4,015 km²", "6,133 km²", "1.528 (+52.8%)")
]
for i, row in enumerate(a_data):
    for j, val in enumerate(row):
        c = a_table.cell(i+1, j)
        set_cell_background(c, "F2F2F2" if (i % 2 == 1) else "FFFFFF")
        set_cell_margins(c, 50, 50, 80, 80)
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        if j == 0:
            r.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(4)
add_p("The observed area distortion matches the theoretical sec²(φ) conformal scale factor of Web Mercator (1/cos²(φ)). Planar calculations in EPSG:3857 result in extreme errors ranging from +23% in the south to +53% in the north; true area calculations must use ST_Area(geom::geography).")
add_img(r"C:\webgis-lab\screenshots\Lab4\checkpoint_8b_area_query.png", "Figure 8B (Checkpoint 8): PostGIS SQL query execution demonstrating spatial area distortion across latitudes.")

# ----------------- SECTION 3: QUESTIONS -----------------
add_h1("3. Answers to Laboratory Questions (Section 9.4)")

add_h2("Question 1: Server-Side Processing vs Monolithic GeoJSON")
add_p("Q: In Labs 2 and 3, every visitor downloaded the whole GeoJSON file. What can a page backed by Django and PostGIS do instead? Give two examples from this lab.")
add_p("Answer: Rather than forcing clients to download all 160 complex district geometries (~1 MB), a Django/PostGIS backend enables server-side spatial filtering, slicing, and aggregation, returning only the exact data needed for the current user context.\nExample 1 (/api/districts/?province=Sindh): PostGIS filters rows on the database server (WHERE province = 'Sindh'), returning only 29 districts and reducing network payload by over 80%.\nExample 2 (/api/where/?lat=...&lng=...): When clicking coordinates, the client sends two numbers. PostGIS evaluates ST_Contains using spatial indexing and returns a tiny 75-byte JSON object. The client never needs to download or topologically intersect heavy polygons in the browser.")

add_h2("Question 2: Database Password Environment Variable")
add_p("Q: Why does settings.py read the database password from an environment variable, instead of containing the password itself?")
add_p("Answer: settings.py is committed to version control (GitHub). Hardcoding database credentials exposes sensitive passwords to anyone viewing the repository or commit logs. Storing the password in an environment variable (WEBGIS_DB_PASSWORD) isolates credentials strictly to the host environment, following 12-Factor App security standards and preventing unauthorized database access.")

add_h2("Question 3: GiST Spatial Indexing")
add_p("Q: In Part 4, the SQL ends with an index created USING GIST. What does it do, and which query in this lab benefits from it?")
add_p("Answer: USING GIST builds a Generalized Search Tree R-tree index over the bounding boxes of the polygon geometries. Without it, evaluating spatial relationships requires a full sequential table scan (O(N)), testing point-in-polygon topology against every vertex of all 160 districts. GiST enables a fast two-phase search: it instantly rejects districts whose bounding boxes do not enclose the point (O(log N)), evaluating exact topology only on candidate geometries. The spatial point query in Part 8 (/api/where/ and ST_Contains) benefits directly, skipping 159 districts in under 2 ms.")

add_h2("Question 4: MultiPolygon Normalization")
add_p("Q: The loading script wraps some geometries in a MultiPolygon. What would happen without that step, and why?")
add_p("Answer: The GeoJSON file contains mixed geometry types: 152 single-part Polygons and 8 multi-part MultiPolygons (districts with coastal islands/enclaves). The District model defines geom = models.MultiPolygonField(srid=4326), establishing a strict PostGIS constraint: geometry(MULTIPOLYGON, 4326). Without wrapping single polygons into MultiPolygon(geom, srid=4326), PostGIS would reject the INSERT of all 152 single polygons with a DataError (geometry type mismatch).")

add_h2("Question 5: Administrative Access Policy")
add_p("Q: Who should have an admin login for a district dataset like this, and who should not?")
add_p("Answer: Admin logins should be restricted to authorized GIS officers, census authorities, or municipal planning staff responsible for maintaining official boundary demarcations and demographic counts. Untrusted public users, web map visitors, and students should NOT have admin access, as Django admin grants full read/write/delete capabilities directly on the PostGIS database.")

add_h2("Question 6: Coordinate Ordering Conventions")
add_p("Q: Leaflet takes [lat, lng] and Point takes (lng, lat). Where in this lab is each order used, and how does the extension’s URL avoid confusing them?")
add_p("Answer: [lat, lng] (Latitude first) is used in Leaflet in the browser: map.setView(), maxBounds, event coordinates (e.latlng.lat, e.latlng.lng), and popup anchors. (lng, lat) (Longitude first) is used in GEOS, GeoJSON, and PostGIS: Point(lng, lat), GeoJSON coordinates [lng, lat], and PostGIS ST_MakePoint(lng, lat). The extension's URL avoids confusion by using explicit named query parameters: /api/where/?lat=33.6423&lng=72.9906. Django extracts them by key name (request.GET['lat'] and request.GET['lng']), preventing positional order ambiguity.")

output_docx = r"C:\webgis-lab\lab4\report.docx"
doc.save(output_docx)
print(f"Report docx successfully generated at: {output_docx}")
