from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

keyword= "car side -clipart -steering  -Applebee -flame -door -rims -vector -lights -youtube -appstore -icons -shade -classycara -splitter -drawing -mirror"

google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': 'vehicle'})

google_crawler.crawl(keyword=keyword, offset=0, max_num=500, date_min=None, date_max=None, min_size=(500,500), max_size=None)


# bing_crawler = BingImageCrawler(downloader_threads=4,
#                                 storage={'root_dir': 'your_image_dir'})
# bing_crawler.crawl(keyword=keyword, offset=0, max_num=1000,
#                    min_size=None, max_size=None)

# baidu_crawler = BaiduImageCrawler(storage={'root_dir': 'your_image_dir'})
# baidu_crawler.crawl(keyword=keyword, offset=0, max_num=1000,
#                     min_size=None, max_size=None)
