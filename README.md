# Real Estate Investment Analysis App

This application is designed to provide a comprehensive analysis of real estate investments. It includes functionality for calculating stamp duty, analyzing real estate investments, and determining investment scores. The app is initially configured for New South Wales (NSW) stamp duty calculations but can be adapted for other jurisdictions.

## Features

- **Stamp Duty Calculation**: Uses `calculate_stamp_duty` to compute the stamp duty based on property value, specifically for NSW.
- **Real Estate Investment Analysis**: The `real_estate_investment_analysis` function performs a detailed analysis using inputs like purchase price, renovation cost, loan details, and others.
- **Additional Metrics and Scoring**: The `calculate_additional_metrics_and_score` function derives additional financial metrics and an overall investment score from the analysis.
- **Advanced Investment Analysis**: The `advanced_investment_analysis` function refines the investment analysis by factoring in risk and market considerations.
- **Diverse Investment Scenarios**: Includes predefined investment scenarios like "Top Investment", "Average Investment", etc., for varied analysis.

## Usage

### Main Functions

This section details the functionalities of the `process_properties.py` script.

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
