from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
startUrl = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('chromedriver')
browser.get(startUrl)