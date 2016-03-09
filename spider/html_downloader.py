import urllib2


class HtmlDownloader(object):
    def download(self, url):
        #print("[INFO]downloading")
        if url is None:
            print("[WARN]url none")
            return None
        try:
            response = urllib2.urlopen(url, timeout=3)
        except:
            print("[ERRO]download failed")
            return None
        return response.read()
