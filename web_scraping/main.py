from selenium import webdriver
from get_product import get_product
from save_product import save_product
import time
from get_products import get_products_urls

driver = webdriver.Edge()

urls = get_products_urls(driver)
for url in urls:
    product = get_product(driver, url)
    save_product(product)
time.sleep(1)
driver.close()


