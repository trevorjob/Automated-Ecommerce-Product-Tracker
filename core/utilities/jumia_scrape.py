from time import sleep

# # windows
from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# linux
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scrape_jumia(
    search_query: str, price_limit: str = None, discount_filter: str = None
) -> list:
    # # windows
    # driver = Chrome()

    # linux
    print('starting scrape...........')
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    print('driver installed .......')
    all_products = []
    url = f"https://www.jumia.com.ng/catalog/?q={search_query}"
    if price_limit is not None:
        url += f"&price=0-{price_limit}"
    if discount_filter is not None:
        url += f"&price_discount={discount_filter}-100"

    driver.get(url)
    print('successfully scraped data')
    sleep(5)

    products = driver.find_elements(by=By.CLASS_NAME, value="core")
    for product in products:
        try:
            page_link = product.get_attribute("href")
            product_img = (
                product.find_element(by=By.CLASS_NAME, value="img-c")
                .find_element(by=By.TAG_NAME, value="img")
                .get_attribute("data-src")
            )
            product_info = product.find_element(by=By.CLASS_NAME, value="info")
            name = product_info.find_element(by=By.CLASS_NAME, value="name").text

            current_price = product_info.find_element(
                by=By.CLASS_NAME, value="prc"
            ).text
            try:
                rvs = product_info.find_element(by=By.CLASS_NAME, value="rev")
                rev = rvs.text
                reviews = rev.split()[0]
                stars_element = rvs.find_element(by=By.CLASS_NAME, value="stars")
                stars = stars_element.text

            except NoSuchElementException:
                reviews = "0"
                stars = "no stars yet"
            discount_info = product_info.find_element(by=By.CLASS_NAME, value="s-prc-w")
            original_price = discount_info.find_element(
                by=By.CLASS_NAME, value="old"
            ).text
            discount = discount_info.find_element(by=By.CLASS_NAME, value="_dsct").text
            prods = {
                "name": name,
                "current_price": current_price,
                "original_price": original_price,
                "discount": discount,
                "reviews": reviews,
                "product_img": product_img,
                "page_link": page_link,
                "stars": stars,
            }
            all_products.append(prods)
        except Exception as e:
            raise e

    driver.close()

    return all_products


# products = scrape_jumia("boots", discount_filter="50", price_limit="12000")
# print(products)
