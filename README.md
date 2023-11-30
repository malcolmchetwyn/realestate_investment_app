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

