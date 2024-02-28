#started on 26/2
def get_data():

    print("Simple Interest Account:")
    Sstarting_amount, Sinterest_rate, Sinterest_rate_time,  = int(input("Enter the principal amount in $: ")), int(input("Enter the interest rate (enter 7%' as 7): ")), input("Enter the interest rate time unit (year, quarter, month, week, day): ")
    print("Compound Interest Account:")
    Cstarting_amount, Cinterest_rate, Cinterest_rate_time, Compound_period = int(input("Enter the principal amount in $: ")), int(input("Enter the interest rate (enter 7%' as 7): ")), input("Enter the interest rate time unit (year, quarter, month, week, day): "), input("Enter the compounding period time unit (year, quarter, month, week, day, custom): ")

    compounding_account = {'starting_amount' : Cstarting_amount, 'interest_rate' : Cinterest_rate}


get_data()