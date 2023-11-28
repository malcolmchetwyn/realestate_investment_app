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
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException



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
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-images")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument(f"user-agent={random_user_agent}")


def get_average_appreciation_rate():
    # Historical average annual appreciation rate in Australia
    return 2  # You can adjust this based on the most recent data or specific market trends

def click_view_more_results(driver):
    try:
        view_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.css-e4xbky'))
        )
        if view_more_button.is_displayed() and view_more_button.is_enabled():
            view_more_button.click()
            time.sleep(2)
    except TimeoutException:
        print("Timeout waiting for 'View more results' button.")
    except NoSuchElementException:
        print("'View more results' button not found.")
    except ElementClickInterceptedException:
        print("Unable to click 'View more results' button.")
    except Exception as e:
        print(f"Error clicking 'View more results': {e}")



def convert_price(price_text):
    price_text = price_text.replace('$', '').strip().upper()
    if 'M' in price_text:
        return float(price_text.replace('M', '')) * 1000000
    elif 'K' in price_text:
        return float(price_text.replace('K', '')) * 1000
    else:
        return float(price_text)


def calculate_yearly_appreciation_rate(closest_sale_price, current_mid_price, years_difference):
    if closest_sale_price is not None and years_difference > 0:
        return (((current_mid_price - closest_sale_price) / closest_sale_price) / years_difference) * 100
    return None

def get_appreciate_rate(address):
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) as driver:
        driver.get("https://www.domain.com.au/property-profile")

        # Wait for the popup banner to appear
        popup_banner = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section[data-testid="popupbanner-wrapper"]'))
        )

        # Find the close button and click it
        close_button = popup_banner.find_element(By.CSS_SELECTOR, 'button[data-testid="popupbanner-wrapper__close-cta"]')
        close_button.click()

        # Wait for the input field to be clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="search"]'))
        )

        # Find the input field and send the address
        input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
        input_field.send_keys(address)
        
        # Press the space bar to trigger the list
        input_field.send_keys(Keys.SPACE)
        
        # Wait for the results to load (you might need to adjust the waiting condition here)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'downshift-0-item-0'))
        )
        
        # Click on the first record to make it work
        first_record = driver.find_element(By.ID, 'downshift-0-item-0')
        first_record.click()

        # Extracting property entries
        try:


            mid_value_text = None

            try:
                # Locating all containers that might contain the 'Mid' value
                mid_containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'css-8nlvsz')][div[text()='Mid']]")

                # Iterate through each container found
                for container in mid_containers:
                    currency_element = container.find_element(By.XPATH, ".//div[@data-testid='currency']")
                    mid_value_text = currency_element.text
                    break

                if mid_value_text is not None:
                    print(f"Mid Value Text: {mid_value_text}")
                else:
                    print("Mid value text not found.")

            except Exception as e:
                print(f"An error occurred: {e}")


            if mid_value_text is not None:
                #mid_price_text = mid_price_element.text
                mid_price = convert_price(mid_value_text)

            # print(f"Mid price: ${mid_value_text}")

                # Current year and the target year (5 years ago)
                current_year = datetime.now().year
                target_year = current_year - 5
                
                click_view_more_results(driver)



                # Waiting for property entries to load
                property_entries = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.css-16ezjtx'))
                )

                # Initialize variables
                closest_sale_year = None
                closest_sale_price = None
                smallest_year_difference = float('inf')

                # Iterate through each property entry to extract the information
                for entry in property_entries:
                    category_elements = entry.find_elements(By.CSS_SELECTOR, 'div[data-testid="fe-co-property-timeline-card-category"]')

                    # Skip entry if category element is not found
                    if not category_elements:
                        continue

                    category_text = category_elements[0].text

                    # Processing if category is 'SOLD'
                    if category_text == 'SOLD':
                        year = int(entry.find_element(By.CSS_SELECTOR, 'div.css-1qi20sy').text)
                        price_text = entry.find_element(By.CSS_SELECTOR, 'span.css-b27lqk').text
                        price = convert_price(price_text)

                        year_difference = abs(year - target_year)
                        if year_difference < smallest_year_difference:
                            smallest_year_difference = year_difference
                            closest_sale_year = year
                            closest_sale_price = price


                if closest_sale_price is not None:
                    print(f"Selected Sale: Year - {closest_sale_year}, Price - ${closest_sale_price}")
                    years_difference = current_year - closest_sale_year
                    if years_difference > 0:
                        appreciation_rate = calculate_yearly_appreciation_rate(closest_sale_price, mid_price, years_difference)
                        formatted_rate = round(appreciation_rate, 2)
                        return {"appreciation_rate": formatted_rate, "property_mid_price": mid_price}
                    else:
                        print("No appreciation calculation due to same year sale.")
                        return {"appreciation_rate": get_average_appreciation_rate(), "property_mid_price": mid_price}
                else:
                    print("No suitable sale found within 5 years.")
             
                    return {"appreciation_rate": get_average_appreciation_rate(), "property_mid_price": mid_price}
            
        except Exception as e:
            print("An error occurred:", e)
        mid_price = None
        return {"appreciation_rate": get_average_appreciation_rate(), "property_mid_price": mid_price}

# Example usage#
#rate = get_appreciate_rate("14 blaxland drive illawong nsw 2234")
#print(  f"Appreciate Rate: {rate['appreciation_rate']}")

#rate = get_appreciate_rate("25/11 oryx road cable beach wa 6726")
#print(f"Appreciation rate: {rate}%")