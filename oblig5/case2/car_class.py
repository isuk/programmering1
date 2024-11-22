    # Import date to use in Class-methods
from datetime import date

class car:
        # Class to store car information
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km
        '''Takes information about the car and stores it in the class to be used by the class-methods below.'''

        # Class-method to print car information
    def print_car_information(self):
        pass
        '''This method prints the information of the car object. For user readability.
           Using a class-method i could easily import this code into other programms. This allows me to easily change the format
           of how the information would be printed out if i wanted to in all programms that uses this class-method. This makes 
           the code reusable and easy to change.
        '''

        # Class-method to calculate monthly price
    def rent_car_monthly_price(self):
        pass
        '''This method calculates monthly price based off of it's age, condition and price.
           Putting this function inside a class makes it easy to change the formula to calculate the monthly price.
           That way, if i wanted to change how much the customer has to pay every month, i can do it in one place.
        '''

        # Class-method to calculate total price
    def calculate_total_price(self):
        pass
        '''This method calculates total price based off of it's age, condition and price.
           Similar to the method to calculate the monthly price for renting a car, this method put in a class gives the same advantages.
           It makes the code reusable and easy to edit the formula that calculates the total price.
        '''

    # Create a car object from the car class
car1 = car("Volvo", "V90", 850_000, 2021, 12, True, 0)
car2 = car("Porsche", "911", 1_500_000, 2022, 4, True, 0)
car3 = car("Audi", "RS3", 1_500_000, 2022, 4, True, 0)

    # Example of how class-methods are easier to understand because it is used directly on the instanced object. 
car1.print_car_information()
car1.rent_car_monthly_price()
car1.calculate_total_price()
''' Here we can see exactly which object and what method is being used on it. This makles the code much easier to read and understand.
    In this case, car1's information is printed out, the monthly price is calculated and the total price is calculated.
'''

car2.print_car_information()
''' Here we see the second car object having it's information printed out. Easy to see what object is being used, and what method is being used on it. '''

car3.calculate_total_price()
''' Here we see the third car object having it's total price calculated.'''
