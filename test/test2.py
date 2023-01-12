from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

movie_name = "Inception"
url = f"https://www.imdb.com/find?q={movie_name}&s=tt"

# start the browser
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get(url)

# wait for the search result to load
wait = WebDriverWait(driver, 10)

try:
    result = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='result_text']/a")))
    # extract the movie url
    movie_url = result.get_attribute("href")
    # go to the movie page
    driver.get(movie_url)
    # wait for the plot to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='sc-16ede8a-1 jVOMyL']")))
# extract the plot
    plot = driver.find_element_by_xpath("//span[@class='sc-16ede8a-1 jVOMyL']").text
# print the plot

    print(plot)

except TimeoutException:
    print("Movie not found or website structure has changed.")