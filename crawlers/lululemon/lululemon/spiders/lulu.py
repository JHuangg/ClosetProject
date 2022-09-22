import scrapy
import json
from bs4 import BeautifulSoup
import time
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Lululemon(scrapy.Spider):
    name = 'lulu'
    allowed_domains = ['lululemon.com']
    start_urls = ['https://api.bazaarvoice.com/data/reviews.json?passkey=e82lq5pbxy7tur5plumvaqqyz&ApiVersion=5.4&filter=productId%3APace_Breaker_Short_Linerless_7&filter=submissionTime%3Agt%3A1514782800&filter=ContentLocale%3Aen*&FilteredStats=Reviews&Include=Products&Offset=0&Limit=16&Sort=SubmissionTime%3Adesc&search=']

    def parse(self, response):
        review_json = json.loads(response.body)

        review_list = []
        for i in range(0, len(review_json["Results"])):
            review_list.append(review_json["Results"][i]["ReviewText"])

        # with open('data.json', 'w') as f:
        #     json.dump(review_json, f)
        
        with open('reviews.txt', 'w') as f:
            for line in review_list:
                f.write(f"{line}\n")
        # print(response.body)
        pass

'''
OLD CRAWLER WEBSITE HAS BEEN UPDATED!
soup = BeautifulSoup(response.body, 'html.parser')
top = soup.find('div', class_ = 'pdp-container OneLinkTx')
test = top.find_all('div', class_ = 'wrapper container-fluid')

wrapper_inner = test[2].find('div', class_ = 'col-xs-12 product-reviews-wrapper product-reviews-wrapper--with-rv')
review_root = wrapper_inner.find('div', class_ = 'reviews-container_reviewsContainerRoot__l67XG')
review_container = review_root.find('div', class_ = 'reviews-container_reviews__g9FIx')
review_text = review_container.find('div', class_ = 'lll-text-xsmall lll-font-weight-regular review-content_reviewText__l2duN')
'''