def calculate_simple_interest():
    principal = validate_input("principal(₦)")
    rate = validate_input("rate(%)")
    time = validate_input("time")

    simple_interest = principal * rate * time / 100.00
    return simple_interest

def calculate_compound_interest():
    principal = validate_input("principal(₦)")
    rate = validate_input("rate(%)")
    time = validate_input("time")

    amount = principal * ((1 + (rate / 100.00)) ** time)
    compound_interest = amount - principal
    return compound_interest

def calculate_pva():
    pmt = validate_input("periodic payment amount (pmt)")
    rate = validate_input("rate(%)") / 100 #Convert the rate to a percentage
    no_of_years = validate_input("no_of_years")

    pva = pmt * ((1 - (1 / ((1 + rate) ** no_of_years))) / rate)
    return pva


def validate_input(msg):
    #Ask the user to enter the expected parameter
    print(f"Enter the {msg}: ")
    num = None

    #Force the user to give a valid positive input
    while True:
        try:
            num = int(input())
            if num < 1:
                print("You have entered an invalid input. Please try again.")
            else:
                break
        except:
            #If the type cast was unsuccessful, the input is invalid
            print("You have entered an invalid input. Please try again.")

    return num

print("""
Welcome to my formula calculator program. Please select your formula:
1. Simple Interest (Press 1)
2. Compound Interest (Press 2)
3. Present Value of Annuity (Press 3) 
""")
formula_chosen = None

#Force the user to put in a valid input
valid_inputs = ['1', '2', '3']

while True:
    formula_chosen = input()
    if formula_chosen in valid_inputs:
        break
    else:
        print("You have not entered a valid input. Please try again.")

result = None
formula = None

if formula_chosen == "1":
    formula = "simple interest"
    result = "{:.2f}".format(calculate_simple_interest()) #converts this into 2 dp
elif formula_chosen == "2":
    formula = "compound interest"
    result = "{:.2f}".format(calculate_compound_interest())
else: #We can safely use the else here since we have already done error handling in the past
    formula = "pva"
    result = "{:.2f}".format(calculate_pva())

print(f"The results of the {formula} calculation is ₦{result}")
print("Thank you so much for using this program.")