import requests
import json
from bs4 import BeautifulSoup


def extract_docs_for_menu(menu_soup, docs):
    content_box = menu_soup.find_all(class_="content-box")[0]
    [x.extract() for x in content_box.find_all(class_=['BC-Textnote', 'next-pg', 'leadgen'])]
    [x.extract() for x in content_box('script')]
    text = content_box.text
    docs.append({'id' : 'Investopedia_CFA_{}'.format(len(docs)), 'text': text})


def get_soup(relative_url):
    res = requests.get('https://www.investopedia.com{}'.format(relative_url))
    return BeautifulSoup(res.text, 'html.parser')


def write_result(docs):
    result = {'docs': docs}
    json_result = json.dumps(result)
    with open('investopedia_cfa.json', 'w') as f:
        f.write(json_result)


def extract_docs(soup):
    docs = []
    nav_tab = soup.find_all(class_='tab-nav')
    for nav in nav_tab:
        menus = nav.select('.tab-menu.menuright > ol > li > a')
        for menu in menus:
            href = menu.attrs['href']
            print("Extracting {}".format(href))
            menu_soup = get_soup(href)
            extract_docs_for_menu(menu_soup, docs)
    return docs


if __name__ == '__main__':
    soup = get_soup('/exam-guide/cfa-level-1/')
    docs = extract_docs(soup)
    write_result(docs)
