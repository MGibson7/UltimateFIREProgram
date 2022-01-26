#FIRE VARIABLES
#Starting Years and Age
from tokenize import PlainToken

import matplotlib
from matplotlib import pyplot as plt


year = 2022
age = 30

#ANNUAL INFO
original_annual_post_tax_income = 80179
original_annual_expenses = 49538
vacation_funds = 1000

#Retirement Savings Info
retirement_savings = 63650
current_debt = 0
compound_yield = 0.07
#^ S&P Adjusted for inflation 7% returns
margin_percent_saved_annual = 0.8
estimated_withdrawal_rate = 0.04
retirement_age = 65

#Introduce New Expense Variables
annual_kid_cost = 10513
college_fund = "yes"
college_fund_annual_529 = 6000
roth_fund_for_kid_annual = 6000
roth_fund_for_kid = "no"
number_of_kids = 1
kid_year = 2024
kid2_year = 0
kid3_year = 0
new_home_cost_annual = 18000
#Assuming 400K home is 24000 500K is 30000 300K is 18000 ^
new_home_year = 2024
new_car_cost_annual = 6000
new_car_year = 0

#Introduce New Income Variables
updated_annual_post_tax_income = 58079
updated_income_year = 0
rental_income = 8800
rental_income_year = 0

#Lists for plotting purposes
retirement_list = []
age_list = []
year_list = []
margin_list = []
annual_expenses_list = []
annual_post_tax_income_list = []

#Output is starting year age so at 31 if retirement savings is X that's what you'd start at

withdrawal_amt = retirement_savings*estimated_withdrawal_rate

while age != 65:
    annual_expenses = original_annual_expenses
    annual_post_tax_income = original_annual_post_tax_income

    if year >= updated_income_year and updated_income_year != 0:
        annual_post_tax_income = updated_annual_post_tax_income
    if year >= kid_year and year < (kid_year + 18):
        annual_expenses = annual_expenses + annual_kid_cost
        if college_fund == "yes":
            annual_expenses = annual_expenses + college_fund_annual_529
        if roth_fund_for_kid == "yes":
            annual_expenses = annual_expenses + roth_fund_for_kid_annual
    if year >= new_home_year and year < (new_home_year + 30):
        annual_expenses = annual_expenses + new_home_cost_annual
    if year >= new_home_year and new_home_year != 0:
        annual_post_tax_income = annual_post_tax_income + rental_income
    margin = annual_post_tax_income - annual_expenses
    retirement_savings = (retirement_savings*compound_yield) + retirement_savings + (margin*margin_percent_saved_annual)
    withdrawal_amt = retirement_savings*estimated_withdrawal_rate
    #CONVERT TO $ FORMAT
    retirement_savings_a = "${:,.2f}".format(retirement_savings)
    withdrawal_amt_a = "${:,.2f}".format(withdrawal_amt)
    annual_post_tax_income_a = "${:,.2f}".format(annual_post_tax_income)
    annual_expenses_a = "${:,.2f}".format(annual_expenses)
    margin_a = "${:,.2f}".format(margin)

    year = year + 1
    age = age + 1

    if withdrawal_amt > annual_expenses:
        print(f"{year} age {age} can retire. Retirement Savings = {retirement_savings_a} Withdrawal = {withdrawal_amt_a} Income = {annual_post_tax_income_a} Expenses = {annual_expenses_a} Margin = {margin_a}")
    else: 
        print(f"{year} age {age} cant retire. Retirement Savings = {retirement_savings_a} Withdrawal = {withdrawal_amt_a} Income = {annual_post_tax_income_a} Expenses = {annual_expenses_a} Margin = {margin_a}")
    
    retirement_list.append((retirement_savings))
    age_list.append(int(age))
    year_list.append(int(year))
    annual_post_tax_income_list.append(int(annual_post_tax_income))
    annual_expenses_list.append(int(annual_expenses))
    margin_list.append(int(margin))


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.plot(age_list, retirement_list)
plt.show()




    

