from celery import shared_task
from .models import Product
from project.celery import app
from utilities.jumia_scrape import scrape_jumia


@app.task
def test_task():
    print("running tasks...new")
    data = scrape_jumia("laptops", "80000", "40")
    product = Product()
    return data
