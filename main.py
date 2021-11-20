import pandas
import numpy
import config
from zoopla import Zoopla
zoopla = Zoopla(config.api_key)

def get_property_listing(postcode,num_rooms, house_or_flat):
    property_listing = zoopla.property_listings({
        'area':postcode,
        'listing_status':'sale',
        'maximum_beds':num_rooms, 
        'minimum_beds':num_rooms,
        'page_number':1, 
        'property_type':house_or_flat,
        'page_size':100, 
        'order_by':'age'
        })
    listings = property_listing.listing
    return listings

def calculate_average_price(searching_listings):
    count = 0
    price = 0
    while count < (len(search_listings)-1):
        price = price + search_listings[count]['price']
        count = count + 1
    return(price/(len(search_listings)))

def get_property_rental_listing(postcode,num_rooms, house_or_flat):
    property_rental_listing = zoopla.property_listings({
        'area':postcode,
        'listing_status':'rent',
        'maximum_beds':num_rooms, 
        'minimum_beds':num_rooms,
        'page_number':1, 
        'property_type':house_or_flat,
        'page_size':100, 
        'order_by':'age'
        })
    rental_listings = property_rental_listing.listing
    return rental_listings
    

def calculate_average_rental_price(searching_rental_listings):
    count = 0
    price = 0
    while count < (len(searching_rental_listings)-1):
        price = price + searching_rental_listings[count]['price']
        count = count + 1
    return(price/(len(searching_rental_listings)))

postcode = str(input("Enter your postcode: "))
num_rooms = str(input("Number of rooms: "))
house_or_flat = str(input("'houses'/'flats': "))

search_listings = get_property_listing(postcode,num_rooms, house_or_flat)
search_rental_listings = get_property_rental_listing(postcode,num_rooms, house_or_flat)
average_price = float('{:.2f}'.format(calculate_average_price(search_listings)))
average_rental_price = float('{:.2f}'.format(calculate_average_rental_price(search_rental_listings)))
average_monthly_rental_price = float('{:.2f}'.format((calculate_average_rental_price(search_rental_listings)*52)/12))
average_rental_yield = float('{:.2f}'.format(((average_rental_price*52)/average_price)*100))
print("The average house price for", num_rooms, "bedroom(s) in",postcode,"is £",average_price)
print("The average rental price for", num_rooms, "bedroom(s) in",postcode,"is £",average_rental_price, "per week or £", average_monthly_rental_price, "per month")
print("Potential Yearly Rental Yield: ", average_rental_yield,"%")

# print(search_listings[0]['price'])
# print(len(search_listings))
# average_property_price = zoopla.average_area_sold_price({'area':postcode})
# print("The average property price in this area is £", average_property_price.average_sold_price_1year)
# print(property_listing.result_count) #check results are inline




