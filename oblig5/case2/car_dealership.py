from datetime import date

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },

    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },

    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
    },
}

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000


def print_car_information(car):
    # Oppgave 3.1
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price:{car['price']},-")
    print(f"Manufactured: 2012-8")
    if car['new']:
        print(f"Condition: New")
    else:
        print(f"Condition: Used")

def create_car(car_register, brand, model, price, year, month, new, km):
    # Oppgave 3.2
    new_car = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km
    }
    car_register[f"{brand} {model}"] = new_car
    return new_car

def get_car_age(car):
    # Oppgave 3.3
    current_year = date.today().year
    car_year = car['year']
    car_age = current_year - car_year
    return car_age

def next_eu_control(car):
    # Oppgave 3.4
    current_month = date.today().month
    current_year = date.today().year
    car_month = car['month']
    car_age = get_car_age(car)
    if car_age % 2 == 0:
        if current_month > car_month:
            return date(current_year + 2, car_month, 1)
        else:
            return date(current_year, car_month, 1)
    else:
        return date(current_year + 1, car_month, 1)
            

def rent_car_monthly_price(car):
    # Oppgave 3.5
    year_price = car['price'] * RENT_CAR_PERCENTAGE
    month_price = year_price / 12
    car_condition_new = car['new']
    if car_condition_new:
        return round(month_price + RENT_NEW_CAR__FEE, 2)
    else:
        return round(month_price, 2)

def calculate_total_price(car):
    # Oppgave 3.6
    car_age = get_car_age(car)
    car_price = car['price']
    if car['new']:
        return car_price + 10783
    else:
        if car_age <= 3:
            return car_price + 6681
        elif car_age <= 11:
            return car_price <= 29
        else:
            return car_price

def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)

    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)

    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")

    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")

    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")

    audi = car_register['audiRS3']
    print_car_information(audi)

    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")

    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")

    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")
