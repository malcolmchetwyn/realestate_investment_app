from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",  # Google Chrome on Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",  # Mozilla Firefox on Windows 10
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",  # Apple Safari on macOS
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",  # Google Chrome on Android
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",  # Apple Safari on iOS (iPhone)
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.36"  # Microsoft Edge on Windows 10
]

# Choose a random user agent
random_user_agent = random.choice(user_agents)

# Chrome options for optimal web scraping
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration in headless mode
chrome_options.add_argument("--disable-images")  # Disable images
chrome_options.add_argument("--incognito")  # Use incognito mode
chrome_options.add_argument("--window-size=1920x1080")  # Window size
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
chrome_options.add_argument(f"user-agent={random_user_agent}")

# Initialize the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://www.domain.com.au/property-profile")


def calculate_average_growth(growth_values):
    """Calculates the average growth from the given growth values."""
    total_growth = 0
    count = 0

    for growth in growth_values.values():
        try:
            growth_rate = float(growth.strip('%'))
            total_growth += growth_rate
            count += 1
        except ValueError:
            pass  # Skip invalid or missing values

    if count > 0:
        return total_growth / count
    else:
        return None

def extract_growth_values(property_type, room_count):
    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.domain.com.au/suburb-profile/rose-bay-nsw-2029")

    try:
        # Wait for the market trends table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'table.css-15dn4s8'))
        )

        # Find all rows in the table
        rows = driver.find_elements(By.CSS_SELECTOR, 'tbody[data-test="insight"] > tr')

        growth_values = {}
        for row in rows:
            try:
                bedrooms = row.find_element(By.CSS_SELECTOR, 'td.css-15k02nu').text.strip()
                type_ = row.find_element(By.CSS_SELECTOR, 'td.css-mz9cyk').text.strip()

                # Check if the row matches the property type and room count
                if type_ == property_type and bedrooms == str(room_count):
                    # Click to expand the row for more details
                    expand_button = row.find_element(By.CSS_SELECTOR, 'button[title="Open"]')
                    expand_button.click()

                    # Wait for the expanded section to load and extract growth values
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.suburb-insights'))
                    )
                    growth_data = driver.find_elements(By.CSS_SELECTOR, 'table#suburb-insights__table tbody > tr')
                    for data in growth_data:
                        year = data.find_element(By.CSS_SELECTOR, 'td:first-child').text.strip()
                        growth = data.find_element(By.CSS_SELECTOR, 'td[data-testid="suburb-insights__annual-growth-value"]').text.strip()
                        growth_values[year] = growth

                    break
            except NoSuchElementException:
                print("Required element not found in a row.")

        return calculate_average_growth(growth_values)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()


def get_growth(property_type, room_count):
    try:
        average_growth_rate = extract_growth_values(property_type, room_count)
        if average_growth_rate is not None:
            formatted_rate = round(average_growth_rate, 2)
            print(f"Average Growth Rate: {formatted_rate}%")
            return formatted_rate
        else:
            print("Average Growth Rate could not be calculated.")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
print ( get_growth("House", "3") )
