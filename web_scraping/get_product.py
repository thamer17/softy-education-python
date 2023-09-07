from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


def get_product(driver, url):
    driver.get(url)
    # get data
    product = {}
    title_element = driver.find_element(By.CLASS_NAME, "h1")
    title = title_element.text
    product["title"] = title

    reference_element = driver.find_element(By.CLASS_NAME, "product-reference")
    reference = reference_element.text
    product["reference"] = reference
    try:
        description_element = driver.find_element(By.ID, "product-description-short-66704")
    except NoSuchElementException:
        description_element = driver.find_element(By.CLASS_NAME, "prodes")
    description = description_element.text
    product["description"] = description

    price_element = driver.find_element(By.CLASS_NAME, "current-price")
    price = price_element.text
    product["price"] = price

    available_element = driver.find_element(By.ID, "stock_availability")
    available = available_element.text
    product["available"] = available

    all_images = driver.find_elements(By.TAG_NAME, "img")
    print(all_images)
    image = all_images[1].get_attribute("src")
    product["image"] = image

    brand_image_element = driver.find_element(By.CLASS_NAME,  "manufacturer-logo")
    brand_image = brand_image_element.get_attribute("src")
    product["brand image"] = brand_image

    return product