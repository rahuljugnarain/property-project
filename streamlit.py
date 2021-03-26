import pandas
import numpy
import config
import streamlit as st
from zoopla import Zoopla
zoopla = Zoopla(config.api_key)

def get_property_listing(postcode,num_rooms):
    property_listing = zoopla.property_listings({
        'area':postcode,
        'listing_status':'sale',
        'maximum_beds':num_rooms, 
        'minimum_beds':num_rooms,
        'page_number':1, 
        'property_type':"houses",
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

st.title('Property Prices')

postcode = st.text_input('Enter your postcode:')
num_rooms = st.select_slider('Number of rooms:', ['1','2','3','4','5','6'])
house_or_flat = st.selectbox('House or flat?',['houses','flats'])

# postcode = str(input("Enter your postcode: "))
# num_rooms = str(input("Number of rooms: "))
# house_or_flat = str(input("'houses'/'flats': "))

if st.button('Calculate'):
    search_listings = get_property_listing(postcode,num_rooms)
    average_price = '£{:.2f}'.format(calculate_average_price(search_listings))
    st.write('The average house price is ', average_price)



# print("The average house price for", num_rooms, "bedroom(s) in",postcode,"is £",average_price)



#print(search_listings[0]['price'])
#print(len(search_listings))
#average_property_price = zoopla.average_area_sold_price({'area':postcode})
#print("The average property price in this area is £", average_property_price.average_sold_price_1year)
#print(property_listing.result_count) #check results are inline




