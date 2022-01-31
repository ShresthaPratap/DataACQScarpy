import scrapy
from ..items import ScrapperItem

class DataScrap (scrapy.Spider):
    name = 'scrape'
    start_urls = ['https://pasalnepal.com/laptops-at-best-price-in-nepal']
   
    def parse(self, response):  

        brand_url = response.css('.product-info a::attr(href)').extract()
        
        for i in brand_url:
            yield response.follow(i, callback=self.parse_brand_items)
            
            
       
    def parse_brand_items(self, response):
        
        items_url = response.css('.name a::attr(href)').extract()

        for i in items_url:
            yield response.follow(i, callback=self.parse_product_detail)

    def parse_product_detail(self, response):
        items = ScrapperItem()

        name = response.css("h1.name::text").extract()       
        #description = response.css("h3::text")[0].extract()
        price = response.css("span#mainprice::text").extract()
        old_price = response.css("span.price-strike::text").extract()
        manufacturer_temp = response.css(".stock-box span h3 a::text")[0].extract()
        manufacturer = manufacturer_temp.split(" ")[1]
        #weight_temp = response.css(".stock-box span h3 a::text")[1].extract()
        #weight = weight_temp.split(" ")[1]
        availability = response.css(".value h3::text").extract()
        
        items['items_name'] = name
        #items['items_description'] = description
        items['items_price'] = price
        items['items_old_price'] = old_price
        items['items_manufacturer'] = manufacturer
        #items['items_weight'] = weight
        items['items_availability'] = availability
        yield items
    

    
        
        
        


 