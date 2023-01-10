import requests
from bs4 import BeautifulSoup
import re


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # returns list with all the citations
    citations = soup.find_all(class_="Template-Fact")
    print(citations)
    return len(citations)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # returns list of all paragraphs
    paragraphs = soup.find_all("p")

    report = ''

    pattern = '(<sup class="noprint Inline-Template)'

    # From list of paragraphs, grab the ones needing citations
    for par in paragraphs:
        if re.search(pattern, str(par)):
            report += par.get_text() + '\n'

    return report


if __name__ == "__main__":
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
