# 1. ✅ Demonstrate First Class Functions
    # Create functions to be used as callbacks 
    # Create a higher-order function that will take a callback as an argument


# 2. ✅ Create a higher-order function that returns a function


# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'

    # Without pie syntax 


    # With pie syntax

def coupon_calculator(callbackfunc):

    def report_price():
        print('Initial price = $28.00') #print the initial price 
        final_price = callbackfunc 

        print(f'Newly Discounted price = ${final_price}')
    
    return report_price

#9
#without decorator aka pie syntax
def calculate_price(price):
    return '{:.2f}'.format(round(price/2, 2)) #with 2 decimal points

calculate = coupon_calculator(calculate_price)
calculate() #invoke the coupon calculator


#with pie/decorator syntax
@coupon_calculator
def calculate_price(price):
    return '{:.2f}'.format