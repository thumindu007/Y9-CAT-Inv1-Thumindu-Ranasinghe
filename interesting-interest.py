#started on 26/2

def get_data():
    print("Simple Interest Account:")
    Sstarting_amount, Sinterest_rate, Sinterest_rate_time,  = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): ")
    print("\n\nCompound Interest Account:")
    Cstarting_amount, Cinterest_rate, Cinterest_rate_time, Compound_period = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): "), input("\nEnter the compounding period time unit (year, quarter, month, week, day, custom): ")
    if Compound_period == 'custom':
        Compound_period = float(input("\nEnter the number of compounding periods per interest rate time unit: "))
    print("\n\nFuture projection timeframe for both accounts:")
    time_into_future, unit_into_future = int(input("\nEnter the amount of time to project into the future: ")), input("\nEnter the projection time unit (year, quarter, month, week, day): ")

    compounding = {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period}
    simple = {'starting_amount' : Sstarting_amount, 'interest_rate' : Sinterest_rate, 'interest_rate_time' : Sinterest_rate_time}

    print(f"\n\nSI Account: P = {simple['starting_amount']}, r = {simple['interest_rate']} per {simple['interest_rate_time']}")
    print(f"\nCI Account: P = {compounding['starting_amount']}, r = {compounding['interest_rate']} per {compounding['interest_rate_time']}, Compounding Frequency: {compounding['Compound_period']}")
    print(f"\nProjection timeframe: {time_into_future} {unit_into_future}\n")

    return compounding, simple, time_into_future, unit_into_future

def calculate_compounding(account, time_into_future, unit_into_future, time_units):
    compounding_per_year = account['Compound_period']
    interest_rate_yearly = account['interest_rate'] * time_units[account['interest_rate_time']]
    time_in_years = time_into_future * time_units[unit_into_future]
    if compounding_per_year in time_units:
        compounding_per_year = time_units[compounding_per_year]

    return round(account['starting_amount'] * (1+((interest_rate_yearly / 100) / compounding_per_year)) ** (time_in_years * compounding_per_year), 2)

def calculate_simple(account, time_into_future, unit_into_future, time_units):
    return round(account['starting_amount'] + account['starting_amount'] * ((account['interest_rate'] * time_units[account['interest_rate_time']]) / 100) * (time_into_future * time_units[unit_into_future]), 2)

def interface():
    module = int(input("\n\n==================================================================\nThis program has five modules. Choose a module by typing its number\n\n(1) Compare simple and compound interest savings acccounts\n(2) Calculate the time for a CI savings account to reach a target amount\n(3) Compare two Compound Interest savings accounts\n(4) Model a CI savings account with regular deposits\n(5) Model increases in compounding frequency\n\nEnter 1 to 5, or 6 to quit:  "))
    if module == 6:
        return False
    else:
        if module == 1:
            accounts = get_data()
            compounding_account, simple_account, time_into_future, unit_into_future = accounts[0], accounts[1], accounts[2], accounts[3]

            compounding_account_calculated = calculate_compounding(compounding_account, time_into_future, unit_into_future, time_units)
            simple_account_calculated = calculate_simple(simple_account, time_into_future, unit_into_future, time_units)

            print(f"\n\n\nSI Account projected amount: ${simple_account_calculated}, Interest earned: ${simple_account_calculated - simple_account['starting_amount']}")
            print(f"\nCI Account projected amount: ${compounding_account_calculated}, Interest earned: ${compounding_account_calculated - compounding_account['starting_amount']}")
        
        input("\n\nClick enter when you are done looking:  ")
        return True


#====================================================================================================================================================================================================
global time_units
time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}
module = True

while module:
    module = interface()