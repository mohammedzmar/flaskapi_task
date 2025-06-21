from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_books():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    books = []
    url = "https://books.toscrape.com/catalogue/page-{}.html"
    #site = "https://books.toscrape.com/catalogue/"

    for page in range(1, 3):
        driver.get(url.format(page))
        time.sleep(1)

        items = driver.find_elements(By.CLASS_NAME, "product_pod")
        for item in items:
            a_tag = item.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
            title = a_tag.get_attribute("title")
            price = item.find_element(By.CLASS_NAME, "price_color").text
            rating_p = item.find_element(By.CSS_SELECTOR, "p.star-rating")
            rating_class = rating_p.get_attribute("class").replace("star-rating", "").strip()
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = rating_map.get(rating_class, 0)
            relative_url = a_tag.get_attribute("href")
            driver.get(relative_url)
            time.sleep(0.5)
            category = driver.find_element(By.CSS_SELECTOR, "ul.breadcrumb li:nth-child(3) a").text
            driver.back()
            time.sleep(0.5)

            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "category": category
            })

    driver.quit()
    return books
