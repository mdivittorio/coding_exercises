import requests
from bs4 import BeautifulSoup


def main():
    url = 'http://nytimes.com'
    print('Article titles\n-----\n')
    get_list_articles(url)


def get_list_articles(url: str):
    soup = BeautifulSoup(get_page_text(url), 'html.parser')
    for title in soup.find_all('h2'):   # TODO add CSS selector
        print(title.text)


def get_page_text(url: str):
    response = requests.get(url)
    return response.text


main()
