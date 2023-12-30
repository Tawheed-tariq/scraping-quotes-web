"""
    Scraping quotes.toscrape and storing to mongodb
    to run spider use command : `scrapy crawl <spider_name>` (scrapy crawl quotes) in my case
    we can also store to any other databse like sql, sqlLite3(check pipelines.py to see database)
    to create containers use items.py
    we can also store data into a file using `scrapy crawl -o <filename>.<extension>`
    e.g; `scrapy crawl -o quotes.json`
"""

import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import Project1Item
class QuoteSpider(scrapy.Spider):
    name = "quotes" 
    pageNumber = 2 #page 1 get scraped automatically
    start_urls = [ 
        'https://quotes.toscrape.com/login'
    ]
    def parse(self, response):
        """logging in to the quotes.toscrape website
        """

        token = response.css('form input::attr(value)').extract_first()#csrf token
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username' : 'exceptme',
            'password' : 'exceptme123'
        }, callback=self.startScraping)
    
    def startScraping(self, response):
        '''open_in_browser(response)''' # this opens up every webpage i brwoser which is getting crawled(uncoment it to use)
        
        
        items = Project1Item() # here we create an instance of items class that 
                               # is created in items.py which creates containers 
                                #for every wuote here and now we can store them to 
                                #database or to a json, xml or csv file
        
        # title = response.css('title::text').extract() #=> returns  title of the web page
        allDivQuotes = response.css('div.quote')
        for item in allDivQuotes:
            quote = item.css('span.text::text').extract()
            author = item.css('.author::text').extract()
            tags = item.css('div.tags').css('a.tag::text').extract()
            
            items['quote'] = quote
            items['author'] = author
            items['tags'] = tags
            yield items
        # to store items in a json file we just pass angrgument with command
            #scrapy crawl quotes -o quotes.json
            #this tells the spider that we want the output in a json file

            #scraping by taking url of next button
        '''nextPage = response.css('li.next a::attr(href)').get()
        if nextPage is not None:
            yield response.follow(nextPage, callback=self.parse)'''

        #using pagination to scrape every page
        nextPage = f'https://quotes.toscrape.com/page/' + str(QuoteSpider.pageNumber) + '/'
        if QuoteSpider.pageNumber < 11:
            QuoteSpider.pageNumber += 1
            yield response.follow(nextPage, callback=self.startScraping)



"""
Use scrapy shell

write `scrapy shell "<url>"`

# using css selectors to get data

then shell will open 
now for test write 
`response.css('title::text').extract()`

`response.css(<selector>).extract()`


# using xpath to get data
response.xpath("//title/text()").extract() => returns the title of page

response.xpath("//span[@class='text']/text()").extract() => returns the text of span tags with class 'text'


# using both css selectors and xpath
response.css("li.next a").xpath("@href").extract()  => returns href of an <a> tag which is inside of an <li> tag with class of 'next'


response.css("a").xpath("@href").extract() => returns all the href of <a> tags
"""