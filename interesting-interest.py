#started on 26/2
def convert_to_annual_rate(interest_rate, compound_period):
    return (1 + interest_rate / compound_period) ** compound_period - 1

def get_data():

    print("Simple Interest Account:")
    Sstarting_amount, Sinterest_rate, Sinterest_rate_time,  = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): ")
    print("\n\nCompound Interest Account:")
    Cstarting_amount, Cinterest_rate, Cinterest_rate_time, Compound_period = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): "), input("\nEnter the compounding period time unit (year, quarter, month, week, day, custom): ")
    if Compound_period == 'custom':
        Compound_period = float(input("\nEnter the number of compounding periods per interest rate time unit: "))
    print("\n\nFuture projection timeframe for both accounts:")
    time_into_future, unit_into_future = int(input("Enter the amount of time to project into the future:")), input("Enter the projection time unit (year, quarter, month, week, day): ")

    compounding = {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period}
    simple = {'starting_amount' : Sstarting_amount, 'interest_rate' : Sinterest_rate, 'interest_rate_time' : Sinterest_rate_time}

    print(f"SI Account: P = {simple['starting_amount']}, r = {simple['interest_rate']} per {simple['interest_rate_time']}")
    print(f"CI Account: P = {compounding['starting_amount']}, r = {compounding['interest_rate']} per {compounding['interest_rate_time']}, Compounding Frequenc")
    print(f"Projection timeframe: {time_into_future} {unit_into_future}")

    return compounding, simple, time_into_future, unit_into_future

def calculate_compounding(account, time_into_future, unit_into_future, time_units):
    if account['Compound_period'] in time_units:
        account.update({'Compound_period' : time_units[account['Compound_period']]})

    print((1+((account['interest_rate'] / 100) / account['Compound_period'])))

    print(((time_into_future / time_units[unit_into_future]) * account['Compound_period']))

    return account['starting_amount'] * (1+((account['interest_rate'] / 100) / account['Compound_period'])) ** ((time_into_future / time_units[unit_into_future]) * account['Compound_period'])

def calculate_simple(account, time_into_future, unit_into_future, time_units):
    return account['starting_amount'] * ()

time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}

accounts = get_data()
compounding_account, simple_account, time_into_future, unit_into_future = accounts[0], accounts[1], accounts[2], accounts[3]

print(compounding_account, '\n',simple_account)

compounding_account_calculated = calculate_compounding(compounding_account, time_into_future, unit_into_future, time_units)

print(compounding_account_calculated)