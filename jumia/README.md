This project is a simple tuto for using scrapy for web scraping. 
As example we use [Jumia Senegal](https://www.jumia.sn) and the laptop category website.

This project is organized as:

```bash
project_name
├── spiders
    ├──jumia_products.py 
├── items.py
├── middlewares.py
├── pipelines.py
├── settings.py
```
The items.py script define the items we want to scrape (title, description, price,...), the middlewares.py is important for proxy settings, settings.py for defining the rules and the pipelines.py is for processing items just after being scrapped.

In the spiders folder we define the spiders for the main project.

For launching the crawler you have to run this command:  scrapy crawl spider_name -o output_data
