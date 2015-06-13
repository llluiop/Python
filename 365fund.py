import urllib2
from HTMLParser import HTMLParser



def Run():
    url = "http://fund.eastmoney.com"
    html = load_html(url)

    parser(html)


def load_html(url):
    html = urllib2.urlopen(url).read()
    return html

def parser(html):
    print html

if __name__ == "__main__":
    Run()
