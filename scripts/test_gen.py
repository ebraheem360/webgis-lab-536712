import os, time, base64
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(width=1366, height=850):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(f'--window-size={width},{height}')
    return webdriver.Chrome(options=options)

print("Selenium ready for checkpoint synthesis")
