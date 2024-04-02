from requests_html import HTMLSession
from bs4 import BeautifulSoup

import sys

def html_request_error( returncode,url ):
    sys.exit("Error: Returncode %1 accessing url %2",returncode,url)

def get_soiltemp():
    # using the Nebraska Mesonet data to download table and extract object that contains the data

    url = "https://mesonet.unl.edu/conditions"

    session = HTMLSession()

    resp = session.get(url)
 
    resp.html.render()

    # now look at rendered html for table
    soup = BeautifulSoup(resp.html.html, 'html.parser')

    table = soup.find('table', class_ = 'debug-table')
    print(table)


if __name__ == '__main__':
    get_soiltemp()