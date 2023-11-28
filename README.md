# Real Estate Investment Analysis App

This application is designed to provide a comprehensive analysis of real estate investments. It includes functionality for calculating stamp duty, analyzing real estate investments, and determining investment scores. The app is initially configured for New South Wales (NSW) stamp duty calculations but can be adapted for other jurisdictions.

## Features

- **Stamp Duty Calculation**: Uses `calculate_stamp_duty` to compute the stamp duty based on property value, specifically for NSW.
- **Real Estate Investment Analysis**: `real_estate_investment_analysis` function performs a detailed analysis using inputs like purchase price, renovation cost, loan details, and others.
- **Additional Metrics and Scoring**: `calculate_additional_metrics_and_score` derives additional financial metrics and an overall investment score from the analysis.
- **Advanced Investment Analysis**: The `advanced_investment_analysis` function refines the investment analysis by factoring in risk and market considerations.
- **Diverse Investment Scenarios**: Includes predefined investment scenarios like "Top Investment", "Average Investment", etc., for varied analysis.

## Usage

### Main Functions

## process_properties.py

The `process_properties.py` file serves as the primary script for running the real estate investment analysis application. It integrates various components and functionalities to process real estate property data, analyze investment opportunities, and output results.

### investment_finder.py
## Key Functionalities

- **Integration with Other Modules**: Imports functions from `investment_finder` and other modules for comprehensive analysis.
- **Data Extraction and Parsing**: Processes property data, including median asking rent extraction using regular expressions.
- **Investment Detail Recording**: Writes investment details to a file based on the calculated investment score.
- **Financial Calculations**: Includes functions to calculate break-even points, ROI (Return on Investment), and IRR (Internal Rate of Return).
- **Property Data Processing**: Reads property data from a file and conducts a detailed analysis on each property.

### Workflow

1. **Reading Property Data**: The script reads property data from a file, typically containing details like price, address, room count, and more.
2. **Data Extraction and Validation**: Extracts rental values and appreciation rates for each property, handling any data inconsistencies or format issues.
3. **Investment Analysis**: Utilizes the `real_estate_investment_analysis` function to analyze each property based on purchase price, renovation costs, loan amount, and other parameters.
4. **Additional Metrics Calculation**: Calculates additional metrics such as break-even year and investment score using `calculate_additional_metrics_and_score`.
5. **Financial Metrics Computation**: Computes ROI and IRR for each property.
6. **Output and Logging**: Prints detailed analysis results for each property and logs good investment opportunities based on a predefined score threshold.
7. **Randomized Time Delays**: Introduces randomized delays between processing individual properties to mimic human-like interaction when fetching data.

### Running the Script

To execute the script, simply run:

```bash
python process_properties.py


#### `calculate_stamp_duty(property_value)`
- Calculates stamp duty for a specified property value.

#### `real_estate_investment_analysis(...)`
- Conducts a comprehensive analysis of a real estate investment.

#### `calculate_additional_metrics_and_score(results)`
- Computes additional metrics and an investment score based on analysis results.

#### `advanced_investment_analysis(results, risk_factor, exit_strategy_score, local_market_score)`
- Enhances the investment analysis by incorporating additional factors like risk and market scores.

# Using the real_estate_investment_analysis function
results = real_estate_investment_analysis(purchase_price=300000, renovation_cost=20000, ...)
print(results)

# Calculating additional metrics and investment score
additional_metrics = calculate_additional_metrics_and_score(results)
print(additional_metrics)

## get_from_domain.py

The `get_from_domain.py` script automates the process of fetching real estate property data from the Domain website. It uses web scraping techniques to extract detailed information about properties within a specified price range. The script is designed for educational and research purposes. Ensure compliance with Domains terms of service and scraping policies when using or modifying this script.

### Key Functionalities

- **Web Scraping**: Utilizes Selenium and BeautifulSoup for scraping data from web pages.
- **Random User-Agent Selection**: Chooses a random user agent from a predefined list to simulate different browsers.
- **Stealth Mode**: Employs `selenium_stealth` for a more undetectable scraping process.
- **Data Extraction**: Parses and extracts relevant data such as price, address, number of bedrooms and bathrooms, and property type.
- **Price Filtering**: Filters properties based on a maximum price threshold.
- **Data Normalization**: Processes and normalizes extracted data for consistency.
- **Pagination Handling**: Navigates through multiple pages of listings.

### Workflow

1. **Driver Setup**: Initializes a headless Chrome WebDriver with optional stealth settings for inconspicuous scraping.
2. **Scraping Functionality**: 
   - Visits the Domain website and navigates through the listing pages.
   - Extracts key details of each property listing, including price, address, and other features.
3. **Data Parsing**: Employs regular expressions and BeautifulSoup to parse and clean the scraped data.
4. **Data Storage**: Writes the extracted property data to a file, typically for further analysis.

### Running the Script

To run the script, execute the following command:

```bash
python get_from_domain.py
```  

## Data Files Outputs

### properties_data.txt

The `properties_data.txt` file serves as a storage medium for raw property data extracted by the `get_from_domain.py` script. It contains detailed information about various real estate properties, which are potential investment opportunities.

#### Format
Each line in this file represents a single property listing with key details separated by a pipe (`|`) character. The typical format of each line is: [Price]|[Address]|[URL]|[Number of Bedrooms]|[Number of Bathrooms]|[Property Type]|[Suburb Name]



- **Price**: The listing price of the property.
- **Address**: The physical address of the property.
- **URL**: The URL link to the property listing on the Domain website.
- **Number of Bedrooms**: The number of bedrooms in the property.
- **Number of Bathrooms**: The number of bathrooms in the property.
- **Property Type**: The type of property (e.g., House, Unit).
- **Suburb Name**: The name of the suburb where the property is located.

### good_investments.txt

The `good_investments.txt` file is used to record properties that are identified as good investment opportunities based on the analysis performed by the application. This file is generated and updated by the `process_properties.py` script.

#### Format
Each entry in this file represents a property that has met or exceeded a certain investment score threshold. The format of each entry is: Address: [Address], URL: [URL], Investment Score: [Investment Score]


- **Address**: The physical address of the property.
- **URL**: The URL link to the property listing.
- **Investment Score**: The calculated investment score for the property.

#### Usage
This file helps in quickly identifying properties that are worth considering for investment based on the predefined investment score criteria set in the analysis process.

### Notes

- The format of these files is crucial for the proper functioning of the scripts. Any changes to the structure of these files might require corresponding adjustments in the scripts.
- These files are intended for educational and research purposes. Users should ensure they comply with any legal requirements and terms of service related to data usage and scraping.

