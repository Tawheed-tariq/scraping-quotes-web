 # Scraping quotes.toscrape and storing to mongodb

To create project use command `scrapy startproject <project_name>`


To create spider use command : `scrapy genspider <spider_name> <url_to_crawl>`



  to run spider use command : `scrapy crawl <spider_name>` (scrapy crawl quotes) in my case <br>
  we can also store to any other databse like sql, sqlLite3(check pipelines.py to see database) <br>
  to create containers use items.py <br>
  we can also store data into a file using `scrapy crawl -o <filename>.<extension>` <br>
  e.g; `scrapy crawl -o quotes.json`
