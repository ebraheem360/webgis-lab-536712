import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1280,850')

driver = webdriver.Chrome(options=options)

# 1. Checkpoint 8A: All provinces
driver.get('http://127.0.0.1:5500/index.html')
time.sleep(3)
driver.save_screenshot('screenshots/checkpoint_8a_all_provinces.png')
print("Saved checkpoint_8a_all_provinces.png")

# 2. Checkpoint 8B: Filtered province (Punjab)
prov_select = Select(driver.find_element(By.ID, 'province'))
prov_select.select_by_value('Punjab')
time.sleep(2)
print("Count for Punjab:", driver.find_element(By.ID, 'count').text)
driver.save_screenshot('screenshots/checkpoint_8b_filtered_province.png')
print("Saved checkpoint_8b_filtered_province.png")

# 3. Checkpoint 7: Shaded map with legend and popup open
driver.get('http://127.0.0.1:5500/index.html')
time.sleep(3)
driver.execute_script('''
layer.eachLayer(function(l) {
    if (l.feature.properties.district === 'Lahore') {
        l.openPopup();
    }
});
''')
time.sleep(1)
driver.save_screenshot('screenshots/checkpoint_7_choropleth_popup.png')
print("Saved checkpoint_7_choropleth_popup.png")

driver.quit()
