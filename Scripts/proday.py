from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
#driver = webdriver.Firefox(executable_path=r'C:/Users/ryhil/Downloads/geckodriver-v0.30.0-win64/geckodriver.exe')]
driver = webdriver.Chrome(executable_path=r'C:/Users/ryhil/Downloads/chromedriver_win32/chromedriver.exe')
#wd = webdriver.Firefox()

driver.implicitly_wait(0.5)
driver.maximize_window()
driver.get("https://datawrapper.dwcdn.net/gIsE0/1/")
#selenium.webdriver.support.wait.WebDriverWait()
#l = driver.find_element(By.CLASS_NAME, value = "next svelte-1ya2siw");
#driver.execute_script("arguments[0].click();", l);
name = "next svelte-1ya2siw"
Osoup = BeautifulSoup(driver.page_source, 'lxml')
tables = Osoup.find_all('table')
dflist = pd.read_html(str(tables))
print(dflist[1])
df = dflist[1]
print(type(df))
for x in range (35):
    l = driver.find_element(By.XPATH, '//button[@class ="next svelte-1ya2siw"]')
    driver.execute_script("arguments[0].click();", l);

    soup = BeautifulSoup(driver.page_source, 'lxml')
    tables = soup.find_all('table')
    dfstemp = pd.read_html(str(tables))
    print(x)
    #print(type(dfstemp[0]), type(df[0]))
    df = pd.concat([df, dfstemp[1]],ignore_index=True)

    
#print(df.to_json(r'ProDay.json'))\
df.to_csv(r'out.csv', index=False)
