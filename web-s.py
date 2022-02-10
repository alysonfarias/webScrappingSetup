from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#insert your url here
driver.get("YOUR_URL")

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser', from_encoding='UTF-8')

# out.html is a file to check the html code returned of the page
html = BeautifulSoup.prettify(soup) 
with open("out.html","w") as out:
    for i in range(0, len(html)):
        try:
            out.write(html[i])
        except Exception:
            1+1

