import time
import json
import statistics
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1366,850')
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

driver = webdriver.Chrome(options=options)

def get_draw_time(url):
    driver.get(url)
    time.sleep(1.5)
    logs = driver.get_log('browser')
    draw_times = []
    for entry in logs:
        msg = entry['message']
        if 'draw(all):' in msg:
            # e.g. "draw(all): 160 districts in 23.4 ms, SVG"
            parts = msg.split('in ')
            if len(parts) > 1:
                t_str = parts[1].split(' ms')[0]
                try:
                    draw_times.append(float(t_str))
                except:
                    pass
    return draw_times[-1] if draw_times else None

print("Measuring SVG draw times (5 runs)...")
svg_times = []
for i in range(5):
    t = get_draw_time("http://127.0.0.1:5500/lab3/index.html")
    svg_times.append(t)
    print(f"  Run {i+1}: {t} ms")

print("Measuring Canvas draw times (5 runs)...")
canvas_times = []
for i in range(5):
    t = get_draw_time("http://127.0.0.1:5500/lab3/index.html?canvas")
    canvas_times.append(t)
    print(f"  Run {i+1}: {t} ms")

svg_median = statistics.median(svg_times) if svg_times else 0
canvas_median = statistics.median(canvas_times) if canvas_times else 0
print(f"SVG median: {svg_median:.2f} ms")
print(f"Canvas median: {canvas_median:.2f} ms")

# Check DOM elements in SVG mode
driver.get("http://127.0.0.1:5500/lab3/index.html")
time.sleep(2)
overlay_pane = driver.find_element(By.CLASS_NAME, "leaflet-overlay-pane")
svg_elements = overlay_pane.find_elements(By.XPATH, ".//*")
print(f"SVG mode: total elements inside leaflet-overlay-pane = {len(svg_elements)}")
svg_child_tags = [e.tag_name for e in overlay_pane.find_elements(By.XPATH, "./*")]
print(f"SVG mode child tags in overlay-pane: {svg_child_tags}")
symbols_pane = driver.find_element(By.CLASS_NAME, "leaflet-symbols-pane")
symbols_elements = symbols_pane.find_elements(By.XPATH, ".//*")
print(f"SVG mode: total elements inside leaflet-symbols-pane = {len(symbols_elements)}")

# Check DOM elements in Canvas mode
driver.get("http://127.0.0.1:5500/lab3/index.html?canvas")
time.sleep(2)
overlay_pane_c = driver.find_element(By.CLASS_NAME, "leaflet-overlay-pane")
canvas_elements = overlay_pane_c.find_elements(By.XPATH, ".//*")
print(f"Canvas mode: total elements inside leaflet-overlay-pane = {len(canvas_elements)}")
canvas_child_tags = [e.tag_name for e in overlay_pane_c.find_elements(By.XPATH, "./*")]
print(f"Canvas mode child tags in overlay-pane: {canvas_child_tags}")
symbols_pane_c = driver.find_element(By.CLASS_NAME, "leaflet-symbols-pane")
symbols_elements_c = symbols_pane_c.find_elements(By.XPATH, ".//*")
print(f"Canvas mode: total elements inside leaflet-symbols-pane = {len(symbols_elements_c)}")

driver.quit()

