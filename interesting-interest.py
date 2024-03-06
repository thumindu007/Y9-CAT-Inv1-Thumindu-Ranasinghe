#started on 26/2

def get_compounding_account(module):
    Cstarting_amount, Cinterest_rate, Cinterest_rate_time, Compound_period = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): "), input("\nEnter the compounding period time unit (year, quarter, month, week, day, custom): ")
    if Compound_period == 'custom':
        Compound_period = float(input("\nEnter the number of compounding periods per interest rate time unit: "))
    time_into_future, unit_into_future = False, False
    if module == 4:
        deposit_amount, target_amount = float(input("\nEnter the regular deposit amount per compounding period: ")), float(input("\nEnter the dollar amount to project to (if you enter 0, you will be asked for the amount of time to project for): "))
        if target_amount == 0:
            time_into_future, unit_into_future = int(input("\nIn that case, enter the amount of time to project for: ")), input("\nEnter the projection time unit (year, quarter, month, week, day, custom): ")
        return {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period, 'time_into_future' : time_into_future, 'unit_into_future' : unit_into_future, 'target_amount' : target_amount, 'deposit_amount' : deposit_amount}
    if module == 3:
        time_into_future, unit_into_future = int(input("\nEnter the amount of time to project into the future: ")), input("\nEnter the projection time unit (year, quarter, month, week, day): ")
        return {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period, 'time_into_future' : time_into_future, 'unit_into_future' : unit_into_future}
    else:
        return {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period}

def calculate_minimum_compounds(account, time_units, projections, periods, module):
    deposit = 0
    
    compounding_per_year = account['Compound_period']
    current_amount = account['starting_amount']
    interest_rate_per_compound = (account['interest_rate']/100) / time_units[account['interest_rate_time']]
    if module == 4:
        deposit = account['deposit_amount']
    if compounding_per_year in time_units:
        compounding_per_year = time_units[compounding_per_year]

    if module == 3 or (module == 4 and account['target_amount'] == 0):
        for _ in range(time_units[account['Compound_period']] * account['time_into_future']):
            interest_amount = current_amount * (interest_rate_per_compound/time_units[account['Compound_period']])
            current_amount += interest_amount + deposit
            projections.append(round(current_amount, 2))
    
    else:
        while current_amount < account['target_amount']:
            interest_amount = (current_amount) * (interest_rate_per_compound)
            current_amount += interest_amount + deposit
            projections.append(round(current_amount, 2))
            periods += 1

    # Calculate the minimum number of compounding periods needed
    min_periods = periods / compounding_per_year

    return projections, min_periods

def get_data():
    print("Simple Interest Account:")
    Sstarting_amount, Sinterest_rate, Sinterest_rate_time,  = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): ")
    print("\n\nCompound Interest Account:")
    compounding = get_compounding_account(1)
    print("\n\nFuture projection timeframe for both accounts:")
    time_into_future, unit_into_future = int(input("\nEnter the amount of time to project into the future: ")), input("\nEnter the projection time unit (year, quarter, month, week, day): ")
    simple = {'starting_amount' : Sstarting_amount, 'interest_rate' : Sinterest_rate, 'interest_rate_time' : Sinterest_rate_time}

    print(f"\n\nSI Account: P = {simple['starting_amount']}, r = {simple['interest_rate']} per {simple['interest_rate_time']}")
    print(f"\nCI Account: P = {compounding['starting_amount']}, r = {compounding['interest_rate']} per {compounding['interest_rate_time']}, Compounding Frequency: {compounding['Compound_period']}")
    print(f"\nProjection timeframe: {time_into_future} {unit_into_future}\n")

    return compounding, simple, time_into_future, unit_into_future

def calculate_compounding(account, time_into_future, unit_into_future, time_units):
    compounding_per_year = account['Compound_period']
    interest_rate_yearly = account['interest_rate'] * time_units[account['interest_rate_time']]
    time_in_years = time_into_future / time_units[unit_into_future]
    if compounding_per_year in time_units:
        compounding_per_year = time_units[compounding_per_year]
    
    return round(account['starting_amount'] * (1+((interest_rate_yearly / 100) / compounding_per_year)) ** (time_in_years * compounding_per_year), 2)

def calculate_simple(account, time_into_future, unit_into_future, time_units):
    return round(account['starting_amount'] + account['starting_amount'] * ((account['interest_rate'] * time_units[account['interest_rate_time']]) / 100) * (time_into_future / time_units[unit_into_future]), 2)

def interface():
    module = int(input("\n\n==================================================================\nThis program has five modules. Choose a module by typing its number\n\n(1) Compare simple and compound interest savings acccounts\n(2) Calculate the time for a CI savings account to reach a target amount\n(3) Compare two Compound Interest savings accounts\n(4) Model a CI savings account with regular deposits\n(5) Model increases in compounding frequency\n\nEnter 1 to 5, or 6 to quit:  "))
    if module == 6:
        return False
    else:
        if module == 1:
            print("\n***MODULE 1: SIMPLE AND COMPOUND INTEREST COMPARISON***")
            accounts = get_data()
            compounding_account, simple_account, time_into_future, unit_into_future = accounts[0], accounts[1], accounts[2], accounts[3]
            compounding_account_calculated = calculate_compounding(compounding_account, time_into_future, unit_into_future, time_units)
            simple_account_calculated = calculate_simple(simple_account, time_into_future, unit_into_future, time_units)

            print(f"\n\n\nSI Account projected amount: ${simple_account_calculated}, Interest earned: ${simple_account_calculated - simple_account['starting_amount']}")
            print(f"\nCI Account projected amount: ${compounding_account_calculated}, Interest earned: ${compounding_account_calculated - compounding_account['starting_amount']}")
        
        elif module == 2:
            print("\n***MODULE 2: TIME FOR A CI ACCOUNT TO REACH A TARGET AMOUNT***")
            compounding_account_target = get_compounding_account(2)
            compounding_account_target["target_amount"] = float(input("\nEnter the target amount: "))
            print(f"\n\nCI Account: P = {compounding_account_target['starting_amount']}, r = {compounding_account_target['interest_rate']} per {compounding_account_target['interest_rate_time']}, Compounding Frequency: {compounding_account_target['Compound_period']}\nTarget amount: {compounding_account_target['target_amount']}")
            mask_off = calculate_minimum_compounds(compounding_account_target, time_units, [], 0, module)
            print(f"\n\nForward projection: {mask_off[0]}\nTime taken: {mask_off[1] * time_units[compounding_account_target['Compound_period']]} {compounding_account_target['interest_rate_time']}")

        elif module == 3:
            print("\n***MODULE 3: COMPARE TWO CI ACCOUNTS***")
            compounding_account1, compounding_account2 = get_compounding_account(module), get_compounding_account(module)
            compounding_account1_calculated, compounding_account2_calculated = calculate_minimum_compounds(compounding_account1, time_units, [], 0, module), calculate_minimum_compounds(compounding_account2, time_units, [], 0, module)
            print(compounding_account1_calculated[0],'\n', compounding_account2_calculated[0])
            print(f"\n\nFinal amount account 1: {compounding_account1_calculated[0][-1]}\nFinal amount account 2: {compounding_account2_calculated[0][-1]}")

        elif module == 4:
            print("\n***MODULE 4: MODEL REGULAR DEPOSITS***")
            deposit_account = get_compounding_account(module)
            deposit_account_calculated = calculate_minimum_compounds(deposit_account, new_units, [], 0, module)
            print('\n',deposit_account_calculated[0])
            if deposit_account_calculated[1] != 0:
                print(f"\nTime taken: {deposit_account_calculated[1] * time_units[deposit_account['Compound_period']]} {deposit_account['interest_rate_time']}")
        input("\n\nClick enter when you are done looking:  ")
        return True


#====================================================================================================================================================================================================
global time_units
time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}
new_units = {'year' : {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}, 'quarter' : {'year' : 0.25, 'quarter' : 1, 'month' : 3, 'week' : 13, 'day' : 91}, 'month' : {'year' : (1/12), 'quarter' : (1/3), 'month' : 1, 'week' : (30/7), 'day' : 30}, 'week' : {'year' : (1/52), 'quarter' : (1/13), 'month' : (1/7.5), 'week' : 1, 'day' : 7}, 'day' : {'year' : (1/365), 'quarter' : (1/91), 'month' : (1/30), 'week' : (1/7), 'day' : 1}}
module = True

while module:
    module = interface()