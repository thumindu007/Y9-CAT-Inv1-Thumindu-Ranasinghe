#started on 26/2
from tabulate import tabulate
def get_compounding_account(module):    #gathers all the inputs for the accounts
    Cstarting_amount, Cinterest_rate, Cinterest_rate_time, Compound_period = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): "), input("\nEnter the compounding period time unit (year, quarter, month, week, day, custom): ")
    if Compound_period == 'custom':  Compound_period = float(input("\nEnter the number of compounding periods per interest rate time unit: "))
    time_into_future, unit_into_future = False, False
    if module == 4:    #gathers all the inputs for module 4
        deposit_amount, target_amount  = float(input("\nEnter the regular deposit amount per compounding period: ")), float(input("\nEnter the dollar amount to project to (if you enter 0, you will be asked for the amount of time to project for): "))
        if target_amount == 0:  time_into_future, unit_into_future = int(input("\nIn that case, enter the amount of time to project for: ")), input("\nEnter the projection time unit (year, quarter, month, week, day, custom): ")
        return {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period, 'time_into_future' : time_into_future, 'unit_into_future' : unit_into_future, 'target_amount' : target_amount, 'deposit_amount' : deposit_amount}
    if module == 3:    #gathers all the inputs for module 3
        time_into_future, unit_into_future = int(input("\nEnter the amount of time to project into the future: ")), input("\nEnter the projection time unit (year, quarter, month, week, day): ")
        return {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period, 'time_into_future' : time_into_future, 'unit_into_future' : unit_into_future}
    else:   return {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate, 'interest_rate_time' : Cinterest_rate_time, 'Compound_period' : Compound_period}
    
def calculate_minimum_compounds(account, time_units, projections, periods, module):    #function that calculates all the data for all parts
    deposit, interest_amount, compounding_per_year, current_amount, pinciples, interests, deposits = 0, 0, account['Compound_period'], account['starting_amount'], [], [], []
    if module == 4: deposit = account['deposit_amount']   #Sets all the list and variables for each part
    if compounding_per_year in time_units:
        compounding_per_year = time_units[compounding_per_year]   #sets the compoundings per year to the users input if its a set amount
        compound_unit = time_units[account['Compound_period']]
    else: compound_unit = float(compounding_per_year)    #sets the compoundings per year to the users custom ammount

    interest_rate_per_compound = (account['interest_rate'] / (compound_unit / time_units[account['interest_rate_time']])) / 100   #sets the interest rate per compounding period
    if module == 3 or (module == 4 and account['target_amount'] == 0) or module == 5 or module == 1:   # the loop used for calculating for a set amount of time
        for _ in range(int(compound_unit) * account['time_into_future']):
            pinciples.append(current_amount)
            current_amount = current_amount + deposit
            interest_amount = current_amount * interest_rate_per_compound
            current_amount += interest_amount
            projections.append(round(current_amount, 2))
            interests.append(interest_amount)
            deposits.append(deposit)
    else:
        while current_amount < account['target_amount']:    # the loop used for calculating for a target
            pinciples.append(current_amount)   # adds the current amount to a list
            interest_amount = (current_amount) * (interest_rate_per_compound)  # calculates the interest amount
            current_amount += interest_amount + deposit  # calculates the current amount for the compound period
            projections.append(round(current_amount, 2))  # adds the projection after the calculation to a list
            interests.append(round(interest_amount, 2))  # adds the interest amount to a list
            deposits.append(deposit)  # adds the deposit amount to a list
            periods += 1

    data = [pinciples, interests, deposits, projections]  # creates a big list for all the lists to be printed
    data = list(map(list, zip(*data)))   # format
    header = ["Princible", "Interest", "Deposit", "Final"] # creates header for the table
    if module != 5:   # only prints table if the part is not 5
        print(tabulate(data, tablefmt="grid", headers=header))  # prints the big table
    # Calculate the minimum number of compounding periods needed
    min_periods = periods / compounding_per_year  # calculates the minimum amount of time to reach the target
    return projections, min_periods

def get_data():  # function the gets the data for part 1
    print("Simple Interest Account:")  # gets data for simple account
    Sstarting_amount, Sinterest_rate, Sinterest_rate_time,  = float(input("\nEnter the principal amount in $: ")), float(input("\nEnter the interest rate (enter 7%' as 7): ")), input("\nEnter the interest rate time unit (year, quarter, month, week, day): ")
    print("\n\nCompound Interest Account:")  # gets data for compound account
    compounding = get_compounding_account(1)
    print("\n\nFuture projection timeframe for both accounts:")
    time_into_future, unit_into_future = int(input("\nEnter the amount of time to project into the future: ")), input("\nEnter the projection time unit (year, quarter, month, week, day): ")
    simple = {'starting_amount' : Sstarting_amount, 'interest_rate' : Sinterest_rate, 'interest_rate_time' : Sinterest_rate_time}
    print(f"\n\nSI Account: P = {simple['starting_amount']}, r = {simple['interest_rate']} per {simple['interest_rate_time']}\nCI Account: P = {compounding['starting_amount']}, r = {compounding['interest_rate']} per {compounding['interest_rate_time']}, Compounding Frequency: {compounding['Compound_period']}\nProjection timeframe: {time_into_future} {unit_into_future}\n")

    return compounding, simple, time_into_future, unit_into_future

def interface(): # function for the user interface                      # asks what module the user wants to run
    module = int(input("\n\n==================================================================\nThis program has five modules. Choose a module by typing its number\n\n(1) Compare simple and compound interest savings acccounts\n(2) Calculate the time for a CI savings account to reach a target amount\n(3) Compare two Compound Interest savings accounts\n(4) Model a CI savings account with regular deposits\n(5) Model increases in compounding frequency\n\nEnter 1 to 5, or 6 to quit:  "))
    if module == 6:   return False   # if the module is 6, then the program quits
    else:  # otherwise it looks at which part the user wants to run
        if module == 1:  # code for part 1
            print("\n***MODULE 1: SIMPLE AND COMPOUND INTEREST COMPARISON***")
            accounts = get_data()  # collects data
            compounding_account, simple_account, time_into_future, unit_into_future = accounts[0], accounts[1], accounts[2], accounts[3]
            compounding_account["time_into_future"], compounding_account["unit_into_future"] = time_into_future, unit_into_future
            compounding_account_calculated = calculate_minimum_compounds(compounding_account, time_units, [], 0, module)
            simple_account_calculated = round(simple_account['starting_amount'] + simple_account['starting_amount'] * ((simple_account['interest_rate'] * time_units[simple_account['interest_rate_time']]) / 100) * (time_into_future / time_units[unit_into_future]), 2)
            # prints all the information for part 1
            print(f"\n\n\nSI Account projected amount: ${simple_account_calculated}, Interest earned: ${simple_account_calculated - simple_account['starting_amount']}\nCI Account projected amount: ${compounding_account_calculated[0][-1]}, Interest earned: ${compounding_account_calculated[0][-1] - compounding_account['starting_amount']}")
        
        elif module == 2: # code for part 2
            print("\n***MODULE 2: TIME FOR A CI ACCOUNT TO REACH A TARGET AMOUNT***")
            compounding_account_target = get_compounding_account(2)  # collects data
            compounding_account_target["target_amount"] = float(input("\nEnter the target amount: "))
            print(f"\n\nCI Account: P = {compounding_account_target['starting_amount']}, r = {compounding_account_target['interest_rate']} per {compounding_account_target['interest_rate_time']}, Compounding Frequency: {compounding_account_target['Compound_period']}\nTarget amount: {compounding_account_target['target_amount']}")
            mask_off = calculate_minimum_compounds(compounding_account_target, time_units, [], 0, module)
            print(f"\n\nForward projection: {mask_off[0]}\nTime taken: {mask_off[1] * time_units[compounding_account_target['Compound_period']]} {compounding_account_target['Compound_period']}")

        elif module == 3: # code for part 3
            print("\n***MODULE 3: COMPARE TWO CI ACCOUNTS***")   # collects data for 2 accounts
            compounding_account1, compounding_account2 = get_compounding_account(module), get_compounding_account(module)
            compounding_account1_calculated, compounding_account2_calculated = calculate_minimum_compounds(compounding_account1, time_units, [], 0, module), calculate_minimum_compounds(compounding_account2, time_units, [], 0, module)
            print(f"\n\nFinal amount account 1: {compounding_account1_calculated[0][-1]}\nFinal amount account 2: {compounding_account2_calculated[0][-1]}")

        elif module == 4: # code for part 4
            print("\n***MODULE 4: MODEL REGULAR DEPOSITS***")
            deposit_account = get_compounding_account(module)   # collects data
            deposit_account_calculated = calculate_minimum_compounds(deposit_account, time_units, [], 0, module)
            if deposit_account_calculated[1] != 0:  # if the user wanted to have a target amount this will print
                print(f"\nTime taken: {deposit_account_calculated[1] * time_units[deposit_account['Compound_period']]} {deposit_account['Compound_period']}")

        elif module == 5: # code for part 5
            print("\n***MODULE 5: SIMULATE INCREASES IN COMPOUNDINGFREQUENCY***")    # creates all the accounts with different compounding periods
            quarterly, weekly, daily, hourly, tenminutely = calculate_minimum_compounds({'starting_amount' : 1000, 'interest_rate' : 100, 'interest_rate_time' : 'year', 'Compound_period' : 'quarter', 'time_into_future' : 1, 'unit_into_future' : 'year'}, time_units, [], 0, module), calculate_minimum_compounds({'starting_amount' : 1000, 'interest_rate' : 100, 'interest_rate_time' : 'year', 'Compound_period' : 'week', 'time_into_future' : 1, 'unit_into_future' : 'year'}, time_units, [], 0, module), calculate_minimum_compounds({'starting_amount' : 1000, 'interest_rate' : 100, 'interest_rate_time' : 'year', 'Compound_period' : 'day', 'time_into_future' : 1, 'unit_into_future' : 'year'}, time_units, [], 0, module), calculate_minimum_compounds({'starting_amount' : 1000, 'interest_rate' : 100, 'interest_rate_time' : 'year', 'Compound_period' : (365*24), 'time_into_future' : 1, 'unit_into_future' : 'year'}, time_units, [], 0, module), calculate_minimum_compounds({'starting_amount' : 1000, 'interest_rate' : 100, 'interest_rate_time' : 'year', 'Compound_period' : 52704, 'time_into_future' : 1, 'unit_into_future' : 'year'}, time_units, [], 0, module)
            print(f"\n\nFinal amount account quarterly: {quarterly[0][-1]}\n\nFinal amount account weekly: {weekly[0][-1]}\n\nFinal amount account daily: {daily[0][-1]}\n\nFinal amount account hourly: {hourly[0][-1]}\n\nFinal amount account tenminutely: {tenminutely[0][-1]}")

        else:
            print("""
                                  µçççççççµ
                         µ▄æ╧╜╩ññ.  ▄▄▄æ##æ▄▓▀▄,
                    ▄#╜²         ¿ççç▄▄▄▄▄▄▄▄▄,;▀gµ
                 ▄▀²                               ▀▄
               ▄▀         ,▄æ▀╨▀▀▀æ▄,               ²▀
             ,▀         ▄▀          _▀▄          ▄▀╜ñ²▀
            ▄▀         █              "▌        █      █
           █`         ▄ææM▀╩ñññññ╙▀%▄,                 ╘▌
         ¿▀      ,▄██▌                ²▀▄,µ,    ▄#▀╨╨╨╨╨▀█æwçµ
        ▐Ö      █▓╜ ▐¿                  ▐.  a/╙▓         Ñ▄   ²%,
       ▐Ö     ▄▓▀    ▓  ▐╨▀▒▄▄çñ▀%▄    ▓▐   ²▀▓⌂,▄▄gæææµ Ñ     ▓▓█
       ▌    ▄▓▀      "█,▓▄▓▓▓▓▓▄æ#▀╙   ▌╨"       ²█▓▓▓  ▓  █    ▓▓"
      █    █▀          _²²╙╩╙╨▀▀════#█▒▄æ▀▀       ▓  ¡²²└  ╙▄  ▐▓
      ▓  J▀                         ▌    ,¿▄µ      ²▀▄²ñ╙╩╩█▌╙╙▓_
     ]M #"                          ▓   █▓▓▓▀   ▄▓██ _█     ²▌▌
     ]▄▀                            ▀ç,╘▀▀░_     ▀▀å¿▀        █
     ]&                                ²²        ╨╨▀;          ▌
     ]«                                                        Ñ
     ]«                                   µççççççµ              █
     ]«                              ▄#▀▓« ▌  ▐  ▐M▀▄           ÑΩ
     ]«                           ¿▌²Ñ, ▄██▓▓▓▓██▓▄▌╙▌           ▓
     ]«                          ▀╙▐▄█▓▓▓▓▓▓▓▓▓▓▓▓═▓g▓           ]Ω
     ]M    ,█              ▄    ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▀#█▒▓           ▐
    ,█▌  ñ▒M,▄M           █    ▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌           ▌
   ²░]▄▓██▓▌_ ¿          ▐╜    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓M  ▌       █
     ▐▌█▓ñ▒▌█╩          ▐`    ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓M  ▓     *▓█*
   æ▀ç▓▀▒▒▄▀▄█          ▌    ,█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   Ñ     ▐▓▄²
 ²ñ²_▓▓▓▓▓▀ç▄#╛       █     ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   Ñ    ▓▓▓▌
     ,▄▓▓ ,╬&          ÑΩ    ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌   ▓    ▓▓█╙
    ,,,▄▓▌▀█▓══         ▌     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   █    █▓▓▀*
     _µ▄▓▓▄▄▄                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓M  ]&   █▓▒_
     ¿▄█▓▓▓▓▀                  ▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▌       ]▓▀▀
      "▀▀▓█▀▄▄▓▀               ▐▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ]▓█▌
         ▐▄▓▒▄▀▄    $█M#┘       ▐▓╓▓▓▓▓▓▓▓▓▓▓▓▒▓▓_       ▐▒▓▓
       æ▀▓▓▀▓▄▄Ö╙╩▀▓▓▓▓ç▄▄æ      ╙▓█ÖÅ▓▀▓▀█▀▌▄█▀        ▐▓▓▓▀
     ¿▄Ö² ]M.▓▌▐█▄▄▓æææ▓▓`          ²▀▀▀██▓▀▀╙     g█▄ ▐▓▓██▌
  ¿#Ö    µ█#Öµ▓█▓▓ πçç█▄▒▓▓Ö`                    ▐g▓▌ j▓▐▓█▄æ
¿#▀_    ╙╩` #▀▓▓▀▓▓▓▓▓▓█▄]▀▒▄▄▌∩                ▀▄▓▓²▀▄▓▓▀▀▀²╙%▄
▄▀▀_          ╓█▓▀▀▀▀░█▓▓å▄▓²ñ)▓▓▌ ¡▄       ¿    ██Ñ▓▒▀]▓▄▓▓█µ▄   :▀▀æç
             *æææ▀▀╢▓█▓▄▄»▄▓═▀▀▓▓▄▄▓]▄µ▌▓▓▄█▌▄▓▓⌂█ ¢▓╙▀æ∞           :ñ╩╨¼æ▄µ
                ▐█▀▓▓▓▓▓██▓M▄²░²²▓▀Q▓▄MÑM  ▓  ²▓▒▓▓▌æ
                  ² ╘╙Ñ▀▓▓%∩ ▌▌┌Ö▀▀▀╨▀.        ∞░▓▓▓▓▓▀╨
                     ═▀░█,▒██▓▓▀ ╥ ▌,  ¡,,▌█▓▓▓▒▒▒ç
                    ]æ#Ö  └▀▓▓▓▄▄▓██▄▓▄▄▓▓▓▓▓▄
                           ²▄▄▓▓▀▀█▓▒▓▀▀█▄ç Ñ
                                   ╙*    ╛
    """)

        input("\n\nClick enter when you are done looking:  ")  # lets the user look at the output before the program starts again
        return True  # returns true since the user wants to continue

#====================================================================================================================================================================================================
global time_units   # sets a global dictionary that will be referd to but not changed
time_units = {'year' : 1, 'quarter' : 4, 'month' : 12, 'week' : 52, 'day' : 365}
module = True

while module:  # continuously runs until the user wants to stop where interface() will reutrn false and stops the program
    module = interface()

