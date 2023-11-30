## Real Estate Investment Analysis Tool

This tool is designed to analyze real estate investments by calculating key financial metrics and assessing property details. It consists of several functions, each serving a specific purpose in the investment analysis process.

### Disclaimer for Web Scraping

This tool includes functionality for web scraping from real estate websites. It is important to note that this feature is intended strictly for **educational purposes only**. Users are responsible for adhering to the terms of service of the websites they scrape, and this tool should not be used in a way that violates those terms or any applicable laws. Always obtain permission from website owners before scraping their sites.


### Overview

- **Imported Modules:** The tool imports various modules like `re` for regular expressions, `numpy` and `numpy_financial` for numerical calculations, and custom modules for specific functionalities like `real_estate_investment_analysis`.
- **Global Variable:** `investment_amount_ability` is set, indicating the maximum investment ability (e.g., $50,000).

### Key Functions

#### `extract_median_asking_rent(data)`
Extracts the median asking rent from a given data dictionary. It searches for a key containing "MEDIAN ASKING RENT" and extracts the numerical value.

#### `write_investment_details_to_file(address, url, investment_score, file_path="good_investments.txt")`
Writes the details of an investment property to a file. It records the address, URL, and investment score of the property.

#### `calculate_break_even(cash_flows)`
Calculates the break-even year based on yearly cash flows. It uses cumulative cash flow calculations to find the first year where the investment breaks even.

#### `calculate_roi_and_irr(total_investment, cash_flows, sale_proceeds)`
Calculates the Return on Investment (ROI) and Internal Rate of Return (IRR) for an investment. It uses total investment, yearly cash flows, and sale proceeds for these calculations.

#### `read_and_print_properties(filename)`
Reads property data from a file, processes each property, and prints detailed analysis. This includes fetching rental values, appreciation rates, and performing a comprehensive investment analysis.

#### `calculate_stamp_duty(property_value)`
Calculates the stamp duty based on property value, specifically for NSW jurisdiction. This function uses a tier-based calculation method.

#### `real_estate_investment_analysis(...)`
Performs an in-depth investment analysis. It takes into account various factors like purchase price, loan amount, rental income, etc., and calculates essential investment metrics.

#### `calculate_additional_metrics_and_score(results)`
Processes the results from the basic analysis and calculates additional investment metrics like Debt Service Coverage Ratio (DSCR), Gross Rent Multiplier (GRM), and Break-Even Point (BEP).

#### `advanced_investment_analysis(results, risk_factor, exit_strategy_score, local_market_score)`
Enhances the basic investment score by considering additional factors such as risk and local market conditions.

### Usage

1. **Populate the real estat data:** run the get_domain script first
2. **Analysis Execution:** Run the process_properties.py
3. **Output:** The results, including ROI, IRR, and investment scores, are printed out for each property. Properties with a high investment score are written to a separate file.

### Note

- The tool is currently configured for NSW stamp duty calculations and needs adjustments for other jurisdictions.
- The investment amount ability is a configurable global variable that can be adjusted based on user preference.


## Installation and Setup

Follow these steps to set up your Python environment for running the scripts included in this repository. These instructions assume that Python 3 is already installed on your system.

### Creating a Virtual Environment

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Creating a virtual environment allows you to manage dependencies for different projects separately.

1. **Create the Virtual Environment:**
python3 -m venv .venv

This command creates a new directory named `.venv` in your current directory, which will contain the Python interpreter and libraries.

2. **Activate the Virtual Environment:**
- On macOS and Linux:
  ```
  . .venv/bin/activate
  ```
- On Windows:
  ```
  .venv\Scripts\activate
  ```
Activating the virtual environment will change your shell’s prompt to show the name of the environment and modify the environment so that running `python` will get you that particular version and installation of Python.

### Installing Dependencies

Once the virtual environment is activated, you can install the required dependencies.

1. **Install Required Packages:**
  ```
pip install -r requirements.txt
  ```

This command will install all the Python packages listed in the `requirements.txt` file. These packages are necessary for the scripts to run properly.

### Deactivating the Virtual Environment

After you finish working in the virtual environment, you can deactivate it by running:
deactivate

This command will revert your Python environment back to normal.

### Note

- Ensure you have the `requirements.txt` file in the same directory where you are running these commands.
- If you encounter any issues during installation, make sure your Python and `pip` are up-to-date.







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