import time
import html_outputer, html_downloader, html_parser

class SpiderMain(object):
    def __init__(self):
        self.downloder = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count_all = 1
        count_downloaded = 1
        root_cont = self.downloder.download(root_url)
        urls = self.parser.get_all_urls(root_cont)
        for url in urls:
            try:
                now = str(time.strftime("%X", time.localtime()))
                print('[INFO][%s]craw (%d/%d) : %s' % (now, count_downloaded,
                                                       count_all, url))
                count_all += 1
                html_cont = self.downloder.download(url)
                print("[INFO]downloaded!")
                data = self.parser.parse(url, html_cont)
                print("[INFO]parsed!")
                self.outputer.output_data(data)
                print("[INFO]output successed!")
                count_downloaded += 1
            except:
                print("[WARN]craw failed")
        self.outputer.output_metadata(count_all, count_downloaded)
        print("[INFO]Done!:)")


if __name__ == "__main__":
    root_url = "https://zh.moegirl.org/%E8%90%8C%E5%B1%9E%E6%80%A7"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
