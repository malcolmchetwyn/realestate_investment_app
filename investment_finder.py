import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This is only NSW Stamp duty. You'll need to update the script to handle different states or for your jurisdiction.
def calculate_stamp_duty(property_value):
    # Function to calculate stamp duty based on property value
    if property_value <= 16000:
        return max(1.25 * property_value / 100, 10)
    elif property_value <= 35000:
        return 200 + 1.50 * (property_value - 16000) / 100
    elif property_value <= 93000:
        return 485 + 1.75 * (property_value - 35000) / 100
    elif property_value <= 351000:
        return 1500 + 3.50 * (property_value - 93000) / 100
    elif property_value <= 1168000:
        return 10530 + 4.50 * (property_value - 351000) / 100
    else:
        return 47295 + 5.50 * (property_value - 1168000) / 100


def real_estate_investment_analysis(purchase_price, renovation_cost, loan_amount,
                                    interest_rate, loan_term, rental_income,
                                    operating_expenses, vacancy_rate, appreciation_rate,
                                    sale_year, location_score, market_growth_rate):
    # Validating input data
    if purchase_price <= 0 or loan_amount <= 0 or rental_income <= 0:
        return "Invalid input data"

    monthly_interest_rate = interest_rate / 12 / 100
    number_of_payments = loan_term * 12

    # Monthly mortgage payment calculation
    monthly_mortgage = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)

    yearly_cash_flows, property_values, remaining_loan_balances = [], [], []
    current_loan_balance = loan_amount
    property_value = purchase_price + renovation_cost

    # Stamp duty and total initial investment calculation
    stamp_duty = calculate_stamp_duty(purchase_price)
    total_investment = purchase_price + renovation_cost + stamp_duty
    capital_investment_required = total_investment - loan_amount

    for year in range(1, sale_year + 1):
        property_value *= (1 + (appreciation_rate + market_growth_rate) / 100)
        adjusted_rental_income = rental_income * 12 * (1 - vacancy_rate / 100)
        net_operating_income = adjusted_rental_income - (operating_expenses * 12)
        annual_mortgage_payment = monthly_mortgage * 12
        cash_flow = net_operating_income - annual_mortgage_payment
        yearly_cash_flows.append(cash_flow)
        property_values.append(property_value)
        interest_for_year = current_loan_balance * interest_rate / 100
        principal_paid_for_year = annual_mortgage_payment - interest_for_year
        current_loan_balance -= principal_paid_for_year
        remaining_loan_balances.append(max(current_loan_balance, 0))

    total_cash_flow = sum(yearly_cash_flows)
    sale_proceeds = property_values[-1] - remaining_loan_balances[-1]
    roi = ((sale_proceeds + total_cash_flow - total_investment) / total_investment) * 100 * location_score
    cash_on_cash_return = (yearly_cash_flows[0] / capital_investment_required) * 100

    # Corrected DSCR, GRM, BEP calculations
    annual_rental_income = rental_income * 12
    dscr = net_operating_income / annual_mortgage_payment if annual_mortgage_payment > 0 else float('-inf')
    grm = purchase_price / annual_rental_income if annual_rental_income > 0 else float('inf')
    bep = (operating_expenses * 12) / adjusted_rental_income if adjusted_rental_income > 0 else float('inf')

    # Valid investment check
    valid_investment = dscr > 1 and grm > 0 and bep >= 0 and bep <= 1

    # Investment score based on normalized metrics
    normalized_dscr = (dscr - 1) if dscr > 1 else 0
    normalized_grm = 1 / grm if grm > 0 else 0
    normalized_bep = 1 - bep if bep >= 0 and bep <= 1 else 0
    investment_score = (normalized_dscr + normalized_grm + normalized_bep) / 3 * 10 if valid_investment else 0

    return {
        "Yearly Cash Flows": yearly_cash_flows,
        "Property Values": property_values,
        "Remaining Loan Balances": remaining_loan_balances,
        "Sale Proceeds": sale_proceeds,
        "ROI (%)": roi,
        "Cash on Cash Return (%)": cash_on_cash_return,
        "Stamp Duty": stamp_duty,
        "Total Investment": total_investment,
        "Capital Investment Required": capital_investment_required,
        "Interest Rate": interest_rate,
        "Renovation Cost": renovation_cost,
        "Operating Expenses": operating_expenses,
        "DSCR": dscr,
        "GRM": grm,
        "BEP": bep,
        "Investment Score": investment_score,
        "Valid Investment": valid_investment
    }

def calculate_additional_metrics_and_score(results):
    # Extract necessary values from the results dictionary
    renovation_cost = results["Renovation Cost"]
    purchase_price = results["Total Investment"] - results["Stamp Duty"] - renovation_cost
    loan_amount = results["Remaining Loan Balances"][0]
    interest_rate = results["Interest Rate"]
    operating_expenses = results["Operating Expenses"]
    annual_rental_income = results["Yearly Cash Flows"][0] + (loan_amount * (interest_rate / 12 / 100) * 12)

    dscr = results["DSCR"]
    grm = results["GRM"]
    bep = results["BEP"]

   # Adjusting weights for DSCR, GRM, and BEP
    weight_dscr = 0.5  # Assuming DSCR is most critical
    weight_grm = 0.3
    weight_bep = 0.2

    # Assuming valid investment criteria are met
    valid_investment = dscr > 1 and grm > 0 and bep >= 0 and bep <= 1

    # Updated normalization and scoring
    normalized_dscr = min((results["DSCR"] - 1) / (5 - 1), 1) if results["DSCR"] > 1 else 0
    normalized_grm = min((12 - results["GRM"]) / (12 - 1), 1) if results["GRM"] >= 1 and results["GRM"] <= 12 else 0
    normalized_bep = 1 - results["BEP"] if results["BEP"] >= 0 and results["BEP"] <= 1 else 0

    # Weighted score calculation
    investment_score = (normalized_dscr * weight_dscr + normalized_grm * weight_grm + normalized_bep * weight_bep) * 10
    investment_score = min(investment_score, 10)

    return {
        "DSCR": dscr,
        "GRM": grm,
        "BEP": bep,
        "Investment Score": investment_score,
        "Valid Investment": valid_investment
    }

def advanced_investment_analysis(results, risk_factor, exit_strategy_score, local_market_score):
    # Extract the basic investment score
    basic_investment_score = results["Investment Score"]

    # Adjust the basic score based on additional factors
    adjusted_score = basic_investment_score * (1 - risk_factor) * exit_strategy_score * local_market_score

    return adjusted_score

'''
good_investment_results = real_estate_investment_analysis(
    purchase_price=250000,        # Lower purchase price
    renovation_cost=15000,        # Modest renovation cost
    loan_amount=200000,           # Lower loan amount (80% of purchase price)
    interest_rate=3.0,            # More favorable interest rate
    loan_term=30,                 # Standard loan term
    rental_income=3500,           # Higher rental income
    sale_year=10,                 # Selling after 10 years
    vacancy_rate=3,               # Lower vacancy rate
    operating_expenses=400,       # Lower operating expenses
    appreciation_rate=3,          # Annual property appreciation rate
    location_score=1.5,           # Good location score
    market_growth_rate=2          # Market growth rate
)


################################################################################################
#
#
#   TEST DATA - YOU CAN USE THIS TO TEST THE MODEL
#
#
#
# Calculate additional metrics and score
good_additional_metrics_and_score = calculate_additional_metrics_and_score(good_investment_results)
print("Investment Metrics and Score:", good_additional_metrics_and_score)
print("Total Investment Required (Including Loan):", good_investment_results["Total Investment"])
print("Capital Investment Required (Out-of-Pocket):", good_investment_results["Capital Investment Required"])


# Define your real_estate_investment_analysis and calculate_additional_metrics_and_score functions here

def print_investment_results(name, results):
    metrics_and_score = calculate_additional_metrics_and_score(results)
    print(f"{name} Metrics and Score:", metrics_and_score)
    print("Total Investment Required (Including Loan):", results["Total Investment"])
    print("Capital Investment Required (Out-of-Pocket):", results["Capital Investment Required"])
    print()



    
# Investment scenarios with their respective parameters
investment_scenarios = {
    "Terrible Investment": {
        "purchase_price": 500000,
        "renovation_cost": 50000,
        "loan_amount": 450000,
        "interest_rate": 6.0,
        "loan_term": 15,
        "rental_income": 1500,
        "sale_year": 5,
        "vacancy_rate": 10,
        "operating_expenses": 1000,
        "appreciation_rate": 1,
        "location_score": 0.8,
        "market_growth_rate": 1
    },
        "Below Average Investment": {
        "purchase_price": 350000,
        "renovation_cost": 25000,
        "loan_amount": 280000,
        "interest_rate": 4.5,
        "loan_term": 30,
        "rental_income": 2200,
        "sale_year": 10,
        "vacancy_rate": 7,
        "operating_expenses": 600,
        "appreciation_rate": 1.5,
        "location_score": 0.9,
        "market_growth_rate": 1.5
    },
    "Average Investment": {
        "purchase_price": 300000,
        "renovation_cost": 20000,
        "loan_amount": 240000,
        "interest_rate": 4.0,
        "loan_term": 30,
        "rental_income": 2500,
        "sale_year": 10,
        "vacancy_rate": 5,
        "operating_expenses": 500,
        "appreciation_rate": 2,
        "location_score": 1.0,
        "market_growth_rate": 2
    },
    "Above-Average Investment": {
        "purchase_price": 250000,
        "renovation_cost": 15000,
        "loan_amount": 200000,
        "interest_rate": 3.5,
        "loan_term": 30,
        "rental_income": 3200,
        "sale_year": 10,
        "vacancy_rate": 4,
        "operating_expenses": 400,
        "appreciation_rate": 3,
        "location_score": 1.2,
        "market_growth_rate": 2.5
    },
    "Top Investment": {
        "purchase_price": 200000,
        "renovation_cost": 10000,
        "loan_amount": 160000,
        "interest_rate": 2.5,
        "loan_term": 30,
        "rental_income": 3500,
        "sale_year": 10,
        "vacancy_rate": 2,
        "operating_expenses": 300,
        "appreciation_rate": 4,
        "location_score": 1.5,
        "market_growth_rate": 3
    },
     "Terrible Investment": {
        "purchase_price": 500000,
        "renovation_cost": 50000,
        "loan_amount": 450000,
        "interest_rate": 6.0,
        "loan_term": 15,
        "rental_income": 1500,
        "sale_year": 5,
        "vacancy_rate": 10,
        "operating_expenses": 1000,
        "appreciation_rate": 1,
        "location_score": 0.8,
        "market_growth_rate": 1
    },
    "Below Average Investment": {
        "purchase_price": 350000,
        "renovation_cost": 25000,
        "loan_amount": 280000,
        "interest_rate": 4.5,
        "loan_term": 30,
        "rental_income": 2200,
        "sale_year": 10,
        "vacancy_rate": 7,
        "operating_expenses": 600,
        "appreciation_rate": 1.5,
        "location_score": 0.9,
        "market_growth_rate": 1.5
    },
    "Average Investment": {
        "purchase_price": 300000,
        "renovation_cost": 20000,
        "loan_amount": 240000,
        "interest_rate": 4.0,
        "loan_term": 30,
        "rental_income": 2500,
        "sale_year": 10,
        "vacancy_rate": 5,
        "operating_expenses": 500,
        "appreciation_rate": 2,
        "location_score": 1.0,
        "market_growth_rate": 2
    },
    "Above-Average Investment": {
        "purchase_price": 250000,
        "renovation_cost": 15000,
        "loan_amount": 200000,
        "interest_rate": 3.5,
        "loan_term": 30,
        "rental_income": 3200,
        "sale_year": 10,
        "vacancy_rate": 4,
        "operating_expenses": 400,
        "appreciation_rate": 3,
        "location_score": 1.2,
        "market_growth_rate": 2.5
    },
    "Top Investment": {
        "purchase_price": 200000,
        "renovation_cost": 10000,
        "loan_amount": 160000,
        "interest_rate": 2.5,
        "loan_term": 30,
        "rental_income": 3500,
        "sale_year": 10,
        "vacancy_rate": 2,
        "operating_expenses": 300,
        "appreciation_rate": 4,
        "location_score": 1.5,
        "market_growth_rate": 3
    },
        # Example 6: Moderate Investment
    "Moderate Investment": {
        "purchase_price": 320000,
        "renovation_cost": 25000,
        "loan_amount": 260000,
        "interest_rate": 5.8,
        "loan_term": 20,
        "rental_income": 2600,
        "sale_year": 12,
        "vacancy_rate": 6,
        "operating_expenses": 550,
        "appreciation_rate": 2.5,
        "location_score": 1.1,
        "market_growth_rate": 10
    },

    # Example 7: Steady Growth Investment
    "Steady Growth Investment": {
        "purchase_price": 280000,
        "renovation_cost": 20000,
        "loan_amount": 225000,
        "interest_rate": 5.8,
        "loan_term": 25,
        "rental_income": 2400,
        "sale_year": 15,
        "vacancy_rate": 5,
        "operating_expenses": 450,
        "appreciation_rate": 3,
        "location_score": 1.2,
        "market_growth_rate": 10
    },

    # Example 8: High Yield Investment
    "High Yield Investment": {
        "purchase_price": 400000,
        "renovation_cost": 30000,
        "loan_amount": 350000,
        "interest_rate": 5.8,
        "loan_term": 15,
        "rental_income": 3200,
        "sale_year": 10,
        "vacancy_rate": 4,
        "operating_expenses": 600,
        "appreciation_rate": 4,
        "location_score": 1.3,
        "market_growth_rate": 10
    },

    # Example 9: Low Cost Investment
    "Low Cost Investment": {
        "purchase_price": 180000,
        "renovation_cost": 10000,
        "loan_amount": 150000,
        "interest_rate": 5.8,
        "loan_term": 30,
        "rental_income": 1800,
        "sale_year": 8,
        "vacancy_rate": 7,
        "operating_expenses": 350,
        "appreciation_rate": 2,
        "location_score": 0.9,
        "market_growth_rate": 10
    },

    # Example 10: Expansive Investment
    "Expansive Investment": {
        "purchase_price": 450000,
        "renovation_cost": 40000,
        "loan_amount": 400000,
        "interest_rate": 5.8,
        "loan_term": 20,
        "rental_income": 3000,
        "sale_year": 12,
        "vacancy_rate": 3,
        "operating_expenses": 700,
        "appreciation_rate": 3.5,
        "location_score": 1.4,
        "market_growth_rate": 10
    },
      # Example 11: Balanced Growth Investment
    "Balanced Growth Investment": {
        "purchase_price": 310000,
        "renovation_cost": 18000,
        "loan_amount": 248000,
        "interest_rate": 5.8,
        "loan_term": 25,
        "rental_income": 2900,
        "sale_year": 10,
        "vacancy_rate": 5,
        "operating_expenses": 480,
        "appreciation_rate": 3.2,
        "location_score": 1.1,
        "market_growth_rate": 10
    },

    # Example 12: High-Potential Investment
    "High-Potential Investment": {
        "purchase_price": 360000,
        "renovation_cost": 22000,
        "loan_amount": 290000,
        "interest_rate": 5.8,
        "loan_term": 30,
        "rental_income": 3100,
        "sale_year": 12,
        "vacancy_rate": 4,
        "operating_expenses": 520,
        "appreciation_rate": 4.5,
        "location_score": 1.3,
        "market_growth_rate": 10
    },

    # Example 13: Long-Term Stable Investment
    "Long-Term Stable Investment": {
        "purchase_price": 270000,
        "renovation_cost": 15000,
        "loan_amount": 216000,
        "interest_rate": 5.8,
        "loan_term": 20,
        "rental_income": 2500,
        "sale_year": 15,
        "vacancy_rate": 6,
        "operating_expenses": 420,
        "appreciation_rate": 2.8,
        "location_score": 1.0,
        "market_growth_rate": 10
    },

    # Example 14: Urban Core Investment
    "Urban Core Investment": {
        "purchase_price": 420000,
        "renovation_cost": 35000,
        "loan_amount": 378000,
        "interest_rate": 5.8,
        "loan_term": 25,
        "rental_income": 3400,
        "sale_year": 8,
        "vacancy_rate": 3,
        "operating_expenses": 600,
        "appreciation_rate": 4,
        "location_score": 1.4,
        "market_growth_rate": 10
    },

    # Example 15: Niche Market Investment
    "Niche Market Investment": {
        "purchase_price": 200000,
        "renovation_cost": 12000,
        "loan_amount": 180000,
        "interest_rate": 5.8,
        "loan_term": 30,
        "rental_income": 1900,
        "sale_year": 7,
        "vacancy_rate": 8,
        "operating_expenses": 320,
        "appreciation_rate": 2.2,
        "location_score": 0.9,
        "market_growth_rate": 10
    },

    # Example 16: Speculative Investment
    "Speculative Investment": {
        "purchase_price": 500000,
        "renovation_cost": 60000,
        "loan_amount": 450000,
        "interest_rate": 5.8,
        "loan_term": 15,
        "rental_income": 2800,
        "sale_year": 5,
        "vacancy_rate": 10,
        "operating_expenses": 800,
        "appreciation_rate": 5,
        "location_score": 1.5,
        "market_growth_rate": 10
    },

    # Example 17: Suburban Family Investment
    "Suburban Family Investment": {
        "purchase_price": 330000,
        "renovation_cost": 20000,
        "loan_amount": 264000,
        "interest_rate": 5.8,
        "loan_term": 20,
        "rental_income": 2700,
        "sale_year": 12,
        "vacancy_rate": 5,
        "operating_expenses": 500,
        "appreciation_rate": 3.5,
        "location_score": 1.2,
        "market_growth_rate": 10
    },

    # Example 18: Retirement Investment
    "Retirement Investment": {
        "purchase_price": 240000,
        "renovation_cost": 18000,
        "loan_amount": 192000,
        "interest_rate": 5.8,
        "loan_term": 30,
        "rental_income": 2000,
        "sale_year": 15,
        "vacancy_rate": 7,
        "operating_expenses": 400,
        "appreciation_rate": 2.5,
        "location_score": 1.0,
        "market_growth_rate": 10
    },

    # Example 19: Growth Focused Investment
    "Growth Focused Investment": {
        "purchase_price": 400000,
        "renovation_cost": 30000,
        "loan_amount": 360000,
        "interest_rate": 5.8,
        "loan_term": 25,
        "rental_income": 3300,
        "sale_year": 10,
        "vacancy_rate": 4,
        "operating_expenses": 550,
        "appreciation_rate": 4.2,
        "location_score": 1.3,
        "market_growth_rate": 10
    },

    # Example 20: Small Town Stable Investment
    "Small Town Stable Investment": {
        "purchase_price": 180000,
        "renovation_cost": 10000,
        "loan_amount": 162000,
        "interest_rate": 5.8,
        "loan_term": 30,
        "rental_income": 1600,
        "sale_year": 10,
        "vacancy_rate": 6,
        "operating_expenses": 300,
        "appreciation_rate": 2,
        "location_score": 0.8,
        "market_growth_rate": 10
    },
      "Score 7 Investment": {
        "purchase_price": 230000,
        "renovation_cost": 20000,
        "loan_amount": 184000,  # 80% of purchase price
        "interest_rate": 4.0,
        "loan_term": 30,
        "rental_income": 3200,  # High rental income for lower GRM
        "sale_year": 10,
        "vacancy_rate": 3,
        "operating_expenses": 350,  # Lower operating expenses for higher DSCR
        "appreciation_rate": 3.5,
        "location_score": 1.2,
        "market_growth_rate": 3
    },

    # Investment for Score ~8
    "Score 8 Investment": {
        "purchase_price": 220000,
        "renovation_cost": 15000,
        "loan_amount": 176000,  # 80% of purchase price
        "interest_rate": 3.5,
        "loan_term": 30,
        "rental_income": 3300,  # Higher rental income
        "sale_year": 10,
        "vacancy_rate": 2,
        "operating_expenses": 300,  # Lower operating expenses
        "appreciation_rate": 4,
        "location_score": 1.3,
        "market_growth_rate": 3.5
    },

    # Investment for Score ~9
    "Score 9 Investment": {
        "purchase_price": 210000,
        "renovation_cost": 10000,
        "loan_amount": 168000,  # 80% of purchase price
        "interest_rate": 3.0,
        "loan_term": 30,
        "rental_income": 3400,  # Very high rental income
        "sale_year": 10,
        "vacancy_rate": 1,
        "operating_expenses": 250,  # Very low operating expenses
        "appreciation_rate": 4.5,
        "location_score": 1.4,
        "market_growth_rate": 4
    },

    # Investment for Score ~10
    "Score 10 Investment": {
        "purchase_price": 200000,
        "renovation_cost": 5000,
        "loan_amount": 160000,  # 80% of purchase price
        "interest_rate": 2.5,
        "loan_term": 30,
        "rental_income": 3500,  # Exceptionally high rental income
        "sale_year": 10,
        "vacancy_rate": 0,
        "operating_expenses": 200,  # Minimal operating expenses
        "appreciation_rate": 5,
        "location_score": 1.5,
        "market_growth_rate": 4.5
    }
}

# Processing each investment scenario
for name, params in investment_scenarios.items():
    results = real_estate_investment_analysis(**params)
    print_investment_results(name, results)

'''



