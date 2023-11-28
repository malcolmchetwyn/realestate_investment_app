from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

def calculate_annual_appreciation_rate(current_price, price_5_years_ago):
    try:
        annual_rate = ((current_price / price_5_years_ago) ** (1 / 5)) - 1
        return annual_rate
    except ZeroDivisionError:
        return None


def address_needs_normalization(address):
    # Regular expression pattern to check 'number/number-number'
    pattern = r'\d+/\d+-\d+'

    # Use re.match or re.search to check if the pattern exists in the address
    return re.search(pattern, address) is not None

def normalize_address(address):
    # Regular expression pattern to find 'number/number-number'
    pattern = r'(\d+)/(\d+)-\d+'

    # Replacement pattern to change 'number/number-number' to 'number/number'
    replacement = r'\1/\2'

    # Replace using regex
    normalized_address = re.sub(pattern, replacement, address)

    return normalized_address

def submit_address_and_get_data(url, address):
    data = {}
    normalized_address = normalize_address(address) if address_needs_normalization(address) else address

    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        driver.get(url)
        # Handle cookie consent or any pop-ups
        try:
            cookie_consent_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class*='accept-cookies'],button[id*='cookie'],div[id*='cookie']"))
            )
            cookie_consent_button.click()
        except Exception:
            pass  # No cookie consent or pop-up found

        address_field = driver.find_element(By.ID, "da_optional_address_text")
        address_field.send_keys(normalized_address)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "da_optional_address_suggest"))
        )

        suggestion_box = driver.find_element(By.ID, "da_optional_address_suggest")

        if "Address/Suburb not found" in suggestion_box.text:
            data["Error"] = "Address not found. Please check the address and try again."
            return data

        suggestions = suggestion_box.find_elements(By.CLASS_NAME, "da_optional_address_item")

        if suggestions:
            driver.execute_script("arguments[0].click();", suggestions[0])

        submit_button = driver.find_element(By.ID, "da_optional_address_button")
        submit_button.click()

        # Wait for the new page to load
        time.sleep(5)

        cards = driver.find_elements(By.CLASS_NAME, "da-card")
        for card in cards:
            title_parts = card.find_elements(By.CLASS_NAME, "da-card-title")
            card_title = " ".join([part.text.strip() for part in title_parts])

            card_value = card.find_element(By.CLASS_NAME, "da-card-value").text.strip() if card.find_elements(By.CLASS_NAME, "da-card-value") else "N/A"
            card_footer = card.find_element(By.CLASS_NAME, "da-card-footer").text.strip() if card.find_elements(By.CLASS_NAME, "da-card-footer") else "N/A"

            formatted_title = ' '.join(card_title.split())
            data[formatted_title] = {"Value": card_value, "Footer": card_footer}


    return data

# Example usage
#url = "https://www.pulseproperty.com.au"
#address = "6/13-15 lambert street richmond vic 3121"
#data = submit_address_and_get_data(url, address)
#print(data)


