from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://github.com/collections/machine-learning")
driver.maximize_window()

links = driver.find_elements("xpath", "//h1[@class='h3 lh-condensed']")

# Extract information for each project
project_list = {}
for link in links:
 link_name = link.text # Project name
 link_url = link.find_elements("xpath", "a")[0].get_attribute('href')
 project_list[link_name] = link_url

print(project_list)

driver.quit()

# Extracting data
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)

# Export project dataframe to CSV
project_df.to_csv('project_list.csv')