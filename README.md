## process_properties.py

`process_properties.py` is a Python script designed for analyzing and evaluating real estate investment opportunities. It integrates various functionalities to calculate investment metrics, such as ROI and IRR, and assesses the potential of real estate properties as profitable investments.

### Features

- **Data Extraction and Analysis:** Extracts rental data, calculates appreciation rates, and evaluates investment potential based on various financial metrics.
- **Investment Decision Making:** Determines the break-even year and calculates return on investment (ROI) and internal rate of return (IRR).
- **Output Management:** Prints detailed property analysis to the console and writes promising investment details to a file.

### How to Use

1. **Set Up:** Ensure all dependencies are installed, including `numpy`, `numpy_financial`, and other required modules.
2. **Data Input:** Prepare a text file (`properties_data.txt`) with property details in the specified format.
3. **Running the Script:** Execute the script using Python. The script will read the data file, process each property, and output investment analysis results.
4. **Output Review:** Review the console output for immediate insights and check `good_investments.txt` for properties with an investment score greater than or equal to 3.

### Example Output

The script outputs various investment metrics, including appreciation rate, purchase price, rental value, break-even year, ROI, and IRR. Example console output for a property might look like:


## get_from_domain.py

`get_from_domain.py` is a web scraping script specifically tailored to extract real estate listings from the Domain website. It leverages tools like Selenium and BeautifulSoup to navigate the website, parse data, and extract detailed information about properties listed for sale.

### Features

- **Dynamic Web Scraping:** Utilizes Selenium to interact with the Domain website dynamically, accommodating for JavaScript-rendered content.
- **Data Parsing:** Employs BeautifulSoup for extracting and parsing relevant data from the web pages.
- **Customizable Search Parameters:** Supports defining custom search parameters like price range, property type, and others.
- **User-Agent Randomization:** Randomizes user-agent strings to mimic different browsers, helping to reduce the risk of being detected as a bot.
- **Data Extraction:** Gathers comprehensive details about each property, including price, address, URL, number of bedrooms and bathrooms, property type, and suburb.

### How to Use

1. **Setup:** Ensure Python environment is set up with Selenium, BeautifulSoup, and other required dependencies.
2. **Driver Configuration:** Set up the Selenium WebDriver to match your system and browser configuration.
3. **Running the Script:** Execute the script. It will start scraping data from Domain based on the specified search parameters.
4. **Data Output:** The script writes the extracted property data into `properties_data.txt`, appending new listings to the file.



## investment_finder.py

The `investment_finder.py` script is a comprehensive tool designed for analyzing real estate investments. It includes functions for calculating various financial metrics essential for assessing the profitability and viability of real estate investments.

### Features

- **Stamp Duty Calculation:** Calculates stamp duty for properties, currently configured for NSW jurisdiction. 
- **Real Estate Investment Analysis:** Conducts a detailed investment analysis considering factors like purchase price, renovation cost, loan amount, and others.
- **Additional Metrics Calculation:** Calculates additional investment metrics such as Debt Service Coverage Ratio (DSCR), Gross Rent Multiplier (GRM), and Break-Even Point (BEP).
- **Advanced Investment Analysis:** Further refines the investment analysis by incorporating risk factors, exit strategy score, and local market score.

### Usage

1. **Setup:** Ensure Python environment is set up with necessary libraries including `pandas`, `numpy`, and `matplotlib`.
2. **Data Input:** Input required parameters like purchase price, loan amount, rental income, etc., for investment analysis.
3. **Executing Functions:** Use the script’s functions to calculate stamp duty, conduct basic and advanced investment analysis, and calculate additional investment metrics.
4. **Output Review:** Review the output for each function to gain insights into the investment's potential, including ROI, cash-on-cash return, and investment score.

### Example Usage

```python
# Example of basic investment analysis
basic_investment_results = real_estate_investment_analysis(
    purchase_price=500000,        # Purchase price of the property
    renovation_cost=20000,        # Cost of renovations
    loan_amount=400000,           # Loan amount
    interest_rate=4.5,            # Interest rate of the loan
    loan_term=25,                 # Term of the loan in years
    rental_income=2500,           # Monthly rental income
    sale_year=15,                 # Year of property sale
    vacancy_rate=5,               # Vacancy rate percentage
    operating_expenses=500,       # Monthly operating expenses
    appreciation_rate=2,          # Annual property appreciation rate
    location_score=2,             # Location desirability score
    market_growth_rate=3          # Annual market growth rate
)

# Print investment results
print("Investment Metrics and Score:", basic_investment_results)