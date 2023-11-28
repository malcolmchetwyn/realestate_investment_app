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
# Python Process Properties Script

This section details the functionalities of the `process_properties.py` script.

### Functions

#### `calculate_stamp_duty(property_value)`
- Calculates stamp duty for a specified property value.

#### `real_estate_investment_analysis(...)`
- Conducts a comprehensive analysis of a real estate investment.

#### `calculate_additional_metrics_and_score(results)`
- Computes additional metrics and an investment score based on analysis results.

#### `advanced_investment_analysis(results, risk_factor, exit_strategy_score, local_market_score)`
- Enhances the investment analysis by incorporating additional factors like risk and market scores.

### Using the real_estate_investment_analysis function
To use the `real_estate_investment_analysis` function, follow this example:

```python
results = real_estate_investment_analysis(purchase_price=300000, renovation_cost=20000, ...)
print(results)
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

