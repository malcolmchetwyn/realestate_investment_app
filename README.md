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


## properties_data.txt

### File Format

Each line in the file represents a single property listing with the following pipe-separated (`|`) values:

1. **Price:** The price of the property in AUD.
2. **Address:** The full address of the property.
3. **URL:** A link to the property listing.
4. **Room Count:** The number of rooms in the property.
5. **Bathroom Count:** The number of bathrooms in the property.
6. **Property Type:** The type of property (e.g., House, Unit).
7. **Suburb:** The suburb where the property is located.

### Example Entry

365000|28 flemming crescent tamworth nsw 2340|https://www.domain.com.au/28-flemming-crescent-tamworth-nsw-2340-2018879427?topspot=1|3|2|House|TAMWORTH


In this example:
- The property price is 365,000 AUD.
- Located at 28 Flemming Crescent, Tamworth, NSW 2340.
- Contains 3 rooms and 2 bathrooms.
- It’s a house located in the suburb of Tamworth.

### Usage

1. **Data Input for Scripts:** This file is read by `process_properties.py` and `investment_finder.py` scripts. Ensure it is in the same directory as these scripts or update the script to point to its location.
2. **Updating Data:** To add new properties, append new lines following the same format. Ensure accuracy in the details for precise investment analysis.

### Note

- The URL provided in each listing is essential for further data scraping or detailed analysis by the scripts.
- Ensure the data format consistency for the scripts to process the information correctly.
