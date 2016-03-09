import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print("[WARN]content none")
            return None
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding='utf-8')
        new_data = self._get_new_data(page_url, soup)
        return new_data

    def get_all_urls(self, root_cont):
        root_soup = BeautifulSoup(root_cont, "html.parser", from_encoding ='utf-8')
        urls = set()
        page_url = "https://zh.moegirl.org/"
        # https://zh.moegirl.org/%E8%90%8C%E5%B1%9E%E6%80%A7
        links = root_soup.find('div', class_='MOEAttribute').\
                find_all('a', href=re.compile(r'/.+'))
        for link in links:
            new_url = link["href"]
            new_full_url = urlparse.urljoin(page_url, new_url)
            urls.add(new_full_url)
        return urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        # <div id="siteNotice"><h1 id="firstHeading"></h1></div>
        title_node = soup.find('h1', id="firstHeading")
        data['title'] = title_node.get_text()
        # <div id="bodyContent"></div>
        body_cont_node = soup.find('div', id="bodyContent")
        data['content'] = str(body_cont_node)
        return data
