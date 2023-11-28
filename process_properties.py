import re
from investment_finder import real_estate_investment_analysis, calculate_additional_metrics_and_score
from get_rental_value import submit_address_and_get_data
from get_sale_history_2 import get_appreciate_rate
import time
import random
import sys
import numpy as np
import numpy_financial as npf

investment_amount_ability = 50000

def extract_median_asking_rent(data):
    for key, value in data.items():
        if "MEDIAN ASKING RENT" in key:
            rent_value = value.get("Value", "")
            rent_numbers = re.findall(r'\d+', rent_value)
            return ''.join(rent_numbers) if rent_numbers else "Data not available"
    return "Data not available"

def write_investment_details_to_file(address, url, investment_score, file_path="good_investments.txt"):
    with open(file_path, "a") as file:
        file.write(f"Address: {address}, URL: {url}, Investment Score: {investment_score}\n")

def calculate_break_even(cash_flows):
    cumulative_cash_flow = np.cumsum(cash_flows)
    break_even_year = np.where(cumulative_cash_flow >= 0)[0]
    return break_even_year[0] + 1 if break_even_year.size > 0 else None

def calculate_roi_and_irr(total_investment, cash_flows, sale_proceeds):
    total_cash_flow = sum(cash_flows) + sale_proceeds
    roi = ((total_cash_flow - total_investment) / total_investment) * 100

    # Adding a zero initial cash flow for IRR calculation
    irr_cash_flows = [-total_investment] + cash_flows + [sale_proceeds]
    irr = npf.irr(irr_cash_flows) * 100

    return roi, irr if not np.isnan(irr) else None



def read_and_print_properties(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) >= 6:
                    price, address, url, room_count, bathroom_count, suburb = parts[:6]
                    numeric_price = int(price.replace(",", ""))

                    try:
                        data = submit_address_and_get_data("https://www.pulseproperty.com.au", address)
                        rental_value = extract_median_asking_rent(data)

                        if rental_value.isdigit():
                            rental_value = int(rental_value)
                        else:
                            print("Invalid rental value format. Setting default value to 450.")
                            rental_value = 450
                        
                        rental_value = int(rental_value) * 4

                        apprec_rate = get_appreciate_rate(address)

                        # Print the values
                        print("Rppreciation Rate:", apprec_rate["appreciation_rate"])
                        print("Mid Price",  apprec_rate["property_mid_price"])



                        est_purchase_price = price
    
                        if apprec_rate["property_mid_price"] is not None:
                            est_purchase_price = apprec_rate["property_mid_price"]
                        
                        #reduced_price = int(est_purchase_price) - int(investment_amount_ability)
                        reduced_price = int(est_purchase_price) * 0.8
                        '''
                        print(  f"Purchase Price: {est_purchase_price}, Address: {address}, URL: {url}, Rooms: {room_count}, "
                                f"Baths: {bathroom_count}, Suburb: {suburb}, Loan Amount: {reduced_price}, "
                                f"Appreciate Rate: {apprec_rate['appreciation_rate']}, Rental Value: {rental_value}")
                        '''
                        
                        analysis_result = real_estate_investment_analysis(
                                            purchase_price=int(est_purchase_price),
                                            renovation_cost=5000,
                                            loan_amount=int(reduced_price),
                                            interest_rate=5.6,
                                            loan_term=20,
                                            rental_income=rental_value,
                                            sale_year=15,
                                            vacancy_rate=1,
                                            operating_expenses=300,
                                            appreciation_rate=apprec_rate['appreciation_rate'],
                                            location_score=1.5,
                                            market_growth_rate=10
                                        )
                        

                            # After analysis_result = real_estate_investment_analysis(...)
                        additional_metrics_and_score = calculate_additional_metrics_and_score(analysis_result)
                        break_even_year = calculate_break_even(analysis_result["Yearly Cash Flows"])
                        roi, irr = calculate_roi_and_irr(analysis_result["Total Investment"], analysis_result["Yearly Cash Flows"], analysis_result["Sale Proceeds"])


                        print(f"Purchase Price: {est_purchase_price}, Address: {address}, URL: {url}, Rooms: {room_count}, "
                              f"Baths: {bathroom_count}, Suburb: {suburb}, Loan Amount: {reduced_price}, "
                              f"Appreciate Rate: {apprec_rate['appreciation_rate']}, Rental Value: {rental_value}")
                        print("Investment Metrics and Score:", additional_metrics_and_score)
                        print(f"Break-even Year: Year {break_even_year if break_even_year else 'N/A'}, ROI: {roi:.2f}%, IRR: {'{:.2f}%'.format(irr) if irr is not None else 'N/A'}")
                        print("Total Investment Required (Including Loan):", analysis_result["Total Investment"])
                        print("Capital Investment Required (Out-of-Pocket):", analysis_result["Capital Investment Required"])
                        print("\n\n")

                        # Check if investment score is greater than or equal to 3 and write to file
                        if additional_metrics_and_score["Investment Score"] >= 3:
                            write_investment_details_to_file(address, url, additional_metrics_and_score["Investment Score"])


                    except Exception as inner_e:
                        print(f"Error processing property {address}: {inner_e}")

                    # Generate a random integer between 4 and 10
                    random_sleep_time = random.randint(5, 10)                    
                    time.sleep(random_sleep_time)

                else:
                    print("Invalid line format:", line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    read_and_print_properties("properties_data.txt")

if __name__ == "__main__":
    main()
