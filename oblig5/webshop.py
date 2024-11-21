def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    for item in ware:
        print(f"{item}: {ware[item]}")

def calculate_average_ware_rating(ware):
    '''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    for rating in ware["ratings"]:
        average_rating = sum(ware["ratings"]) / len(ware["ratings"])
        round(average_rating, 1)
        return average_rating

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    for ware in all_wares:
        if ware["number_in_stock"] >= 0:
            

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av
    en gitt vare finnes på lager.'''
    if ware["number_in_stock"] <= 0:
        return False

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,
number_of_ware):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert
    handlevogn.'''
    shopping_cart[ware_key] = ware

    if ware["number_in_stock"] < number_of_ware:
        shopping_cart["units_addedc_to_cart"] = ware["number_in_stock"]
        return(f"Sorry, we only have {ware['number_in_stock']} in stock. So we only added {ware['number_in_stock']} to your cart")
    else:
        shopping_cart["units_added_to_cart"] = number_of_ware
        return(f"Added {number_of_ware} {ware_key} to your cart")


def calculate_shopping_cart_price(shopping_cart, all_wares, tax = 1.25):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    sum_of_wares_in_cart = 0
    for ware_in_shopping_cart in shopping_cart:
        for ware_in_all_wares in all_wares:
            if ware_in_shopping_cart == ware_in_all_wares:
                sum_of_wares_in_cart += all_wares[ware_in_shopping_cart]["price"]

    sum_with_tax = sum_of_wares_in_cart * tax
    return sum_with_tax

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt
    lommebok for å kjøpe en handlevogn.'''

def buy_shopping_cart():
    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''

    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()
