import io
import re
import requests
import http.cookiejar
from bs4 import BeautifulSoup
import html
import csv
import time
import multiprocessing

cookiejar = http.cookiejar.MozillaCookieJar('cookies.txt')
cookiejar.load()

retry_strategy = requests.packages.urllib3.util.retry.Retry(total=3)
http_adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
http_session = requests.Session()
http_session.mount("https://", http_adapter)
http_session.mount("http://", http_adapter)
http_session.cookies = cookiejar


def read_url(url):
    r = http_session.get(url)
    return r.text

def