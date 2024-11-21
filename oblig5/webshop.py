def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"Name: {ware['name']}")
    print(f"Price: {int(ware['price'])},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Dscription: {ware['description']}")

def calculate_average_ware_rating(ware):
    '''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    for rating in ware["ratings"]:
        average_rating = sum(ware["ratings"]) / len(ware["ratings"])
        return round(average_rating, 1)

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    wares_in_stock = {}
    for key, value in all_wares.items():
        if value["number_in_stock"] > 0:
            wares_in_stock[key] = value

    return wares_in_stock
    

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.'''
    return ware["number_in_stock"] >= number_of_ware

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware = 1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.'''
    if is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart[ware_key] = number_of_ware
    elif ware["number_in_stock"] > 0:
        shopping_cart[ware_key] = ware["number_in_stock"]

def calculate_shopping_cart_price(shopping_cart, all_wares, tax = 1.25):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    sum_of_wares_in_cart = 0
    for cartWare, amount in shopping_cart.items():
        if cartWare in all_wares:
            sum_of_wares_in_cart += all_wares[cartWare]["price"] * amount

    return sum_of_wares_in_cart * tax

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
