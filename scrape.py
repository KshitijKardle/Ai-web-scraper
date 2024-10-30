import selenium.webdriver as webdriver
from selenium.webdriver.edge.service  import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    
    edge_driver_path = '.\msedgedriver.exe'
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=Service(edge_driver_path), options=options)

    try:
        driver.get(website)
        html = driver.page_source
        return html
    
    finally:
        driver.quit()

def get_body(html):
    soup = BeautifulSoup(html, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    clean_content = soup.get_text(separator='\n')
    clean_content = '\n'.join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )

    return clean_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0, len(dom_content),max_length)
    ]


