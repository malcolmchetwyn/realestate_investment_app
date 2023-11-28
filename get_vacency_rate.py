from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def extract_last_tooltip_value(url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        # Wait for the Highcharts graph to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".highcharts-tooltip"))
        )

        # Find the Highcharts graph element to hover over
        graph_element = driver.find_element(By.CSS_SELECTOR, ".highcharts-container")

        # Hover over the graph element to trigger the tooltip
        ActionChains(driver).move_to_element(graph_element).perform()

        # Wait for the tooltip to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".highcharts-tooltip"))
        )

        # Find the last tooltip element
        tooltips = driver.find_elements(By.CSS_SELECTOR, ".highcharts-tooltip")
        if tooltips:
            last_tooltip = tooltips[-1]
            tooltip_text = last_tooltip.text
            print("Last Tooltip Text:", tooltip_text)
        else:
            print("No tooltip elements found.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()

# Example usage
url = "https://sqmresearch.com.au/graph_vacancy.php?postcode=4000"
extract_last_tooltip_value(url)
