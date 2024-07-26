# Lab 2
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
# function is defined to caluculate education details 
def education_details(major, graduation_year):
    print(f' {major}, {graduation_year} ')
    
# invoke function example: uncomment below line after completing above function

# calling function
education_details("Computer Science", "2025")


# ----------------- Question 2 -----------------
# Create global variable named "usd_to_gbp" with value as 1.25
# WRITE CODE HERE

usd_to_gbp = 1.25

def yearly_allowance(hourly_wage, weekly_hours, weeks_per_year):
    annual_salary = hourly_wage * weekly_hours * weeks_per_year
    return int(annual_salary)


def conversion_to_british_pound(usd_amount):
     british_pound = usd_amount / usd_to_gbp
     return round(british_pound,1)


# uncomment below lines after completing above functions
hourly_wage = 15
weekly_hours = 40
weeks_per_year = 52

# uncomment below and invoke the function with relevant args
usd_amount = yearly_allowance(hourly_wage,weekly_hours,weeks_per_year)
gbp_amount = conversion_to_british_pound(usd_amount)

print(gbp_amount)

# ----------------- Question 3 -----------------
def yearly_profit(daily_profit, days_per_year):
    annual_profit = daily_profit * days_per_year
    return annual_profit

def percentage_change(current_profit, previous_profit):
    change =((current_profit - previous_profit)/ previous_profit) *100
    if change > 0:
        return f"{round(change,2)}% profit"
    else:
        return f"{round(abs(change),2)}% loss"
    

# uncomment below lines after completing above functions
daily_profit = 250
days_per_year = 365
previous_profit = 100000

# uncomment below and invoke the function with relevant args
current_profit = yearly_profit(daily_profit,days_per_year)
percent_change = percentage_change(current_profit,previous_profit)
print(percent_change)

