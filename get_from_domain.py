from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import random
from selenium_stealth import stealth

# List of user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",  # Google Chrome on Windows 10
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",  # Mozilla Firefox on Windows 10
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",  # Apple Safari on macOS
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.36"  # Microsoft Edge on Windows 10
]

# Choose a random user agent
random_user_agent = random.choice(user_agents)


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--incognito")  # Use incognito mode
    #chrome_options.add_argument("--window-size=1920x1080")  # Window size
    #chrome_options.add_argument(f"user-agent={random_user_agent}")
    # s = Service('path/to/chromedriver')  # Replace with the path to your chromedriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver
'''
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_argument(f"user-agent={random_user_agent}")
    #chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    #chrome_options.add_argument("--incognito")  # Use incognito mode
    #chrome_options.add_argument("--window-size=1920x1080")  # Window size
    
    driver = webdriver.Chrome(options=chrome_options)

    # Stealth settings
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    return driver
'''
def parse_price(price_str):
    # Find all numbers in the string
    numbers = re.findall(r'\d+(?:,\d+)*(?:\.\d+)?', price_str)
    
    # Convert found numbers to integers, handling commas and decimals
    prices = sorted([int(num.replace(',', '').split('.')[0]) for num in numbers], reverse=True)

    # Return the highest number if available, otherwise return None
    return prices[0] if prices else None



def is_valid_price(price_str, max_price):
    # Check if the price string contains a valid numerical price
    if 'EOI' in price_str or 'Offers' in price_str or 'Auction' in price_str or 'Enquire' in price_str or 'Contact' in price_str:
        return False

    price = parse_price(price_str)
    #print(f"######: {price}")
    return price is not None and price <= max_price



def strip_url_query(url):
    return url.split('?')[0]

def scrape_property_address(driver, property_url):
    stripped_url = strip_url_query(property_url)
    driver.get(stripped_url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    address_wrapper = soup.select_one('div[data-testid="listing-details__button-copy-wrapper"] h1')
    #print(f"address: {address_wrapper}")  # For debugging

    return address_wrapper.text.strip() if address_wrapper else "Address Not Found"

import sys

def scrape_page(driver, url, max_price):
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = []

    # Select all listings
    listings = soup.select('div.css-qrqvvg')

    for listing in listings:
        # Extract price
        #print(listing.prettify())
       # sys.exit("asd")
        price_tag = listing.select_one('p[data-testid="listing-card-price"]')
        if price_tag:
            price_text = price_tag.text.strip()

            if is_valid_price(price_text, max_price):
                # Extract URL
                
                link_element = listing.select_one('a[href]')
                
                if link_element and 'href' in link_element.attrs:
                    link = link_element['href']
                    full_link = f"https://www.domain.com.au{link}" if not link.startswith('http') else link

                    # Extract address if needed
                    address_wrapper = listing.select_one('h2[data-testid="address-wrapper"]')
                    if address_wrapper:
                            address_text = address_wrapper.text.replace('\xa0', ' ').replace(',', '').strip().lower()
                    else:
                        address_text = "Address Not Found"        


                    # Extract suburb name for each individual listing
                    suburb_container = listing.select_one('span[data-testid="address-line2"]')
                    if suburb_container:
                        first_span = suburb_container.find('span')
                        suburb_name = first_span.get_text(strip=True) if first_span else "Suburb Not Found"
                    else:
                        suburb_name = "Suburb Not Found"


                    print(suburb_name)

                    # Extract number of bedrooms and bathrooms
                    beds = listing.select_one('span[data-testid="property-features-text-container"]:contains("Bed")')
                    baths = listing.select_one('span[data-testid="property-features-text-container"]:contains("Bath")')
                    num_beds = beds.text.split(' ')[0] if beds else "N/A"
                    num_baths = baths.text.split(' ')[0] if baths else "N/A"

                    # Extract property type
                    property_type_div = listing.select_one('div.css-11n8uyu span.css-693528')
                    # Assuming property_type_div contains the text as extracted earlier
                    if property_type_div:
                        property_type_text = property_type_div.get_text().strip()
                        # Check if the extracted text is "House"
                        if property_type_text == "House":
                            property_type = "House"
                        else:
                            property_type = "Unit"
                    else:
                        property_type = "N/A"




                    results.append((parse_price(price_text), full_link, address_text, num_beds, num_baths, property_type, suburb_name))

                    
    return results



def main():
    driver = setup_driver()
    base_url = "https://www.domain.com.au/sale/"

    # Base query parameters
    base_params = {
        'ptype': 'apartment-unit-flat,block-of-units,duplex,free-standing,new-apartments,new-home-designs,new-house-land,pent-house,semi-detached,studio,terrace,town-house,villa',
        'price': '200000-555000',
        'establishedtype': 'established'
    }

    max_price = 555000  # Adjust maximum price threshold as needed
    page = 1

    try:
        while True:
            print(f"Scraping page {page}...")

            # Add page number to the parameters
            params = base_params.copy()
            if page > 1:
                params['page'] = page

            full_url = f"{base_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
            scraped_data = scrape_page(driver, full_url, max_price)

            if not scraped_data:
                print("No more data found, stopping...")
                break

            # Write data to file
            with open('properties_data.txt', 'a') as file:
                for price, link, address, num_beds, num_baths, property_type, suburb_name in scraped_data:
                    #file.write(f"{price}|{address}|{link}\n")
                    file.write(f"{price}|{address}|{link}|{num_beds}|{num_baths}|{property_type}|{suburb_name}\n")

            page += 1

    finally:
        driver.quit()

if __name__ == "__main__":
    main()