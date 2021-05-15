# Market Property Price

This is a simple calculator using Zoopla's API to calculate the average house price with a specific number of rooms within a specific area.
### Example
<img src="https://user-images.githubusercontent.com/41843104/112622815-77cf3580-8e23-11eb-9e87-5f4dbc54fe25.png" width="685" height="450">

# How to Set Up
* main.py - initial python script version
* streamlit.py - using streamlit to create a deployable page

## API Access
1. Request a Zoopla API key from https://developer.zoopla.co.uk/
2. Create a file named config.py, with variable "api_key" assigned to Zoopla API key (e.g. api_key = "2x36df73hsd723ka674c")

## Using Streamlit
1.  ```pip install streamlit```
2.  ```streamlit run [filename]```

# How to Use
3. Enter a Postcode (e.g. SW11)
4. Enter the number of rooms 
5. Click "Calculate"

# Progress Tracker

## :checkered_flag: Completed:
* Connected Zoopla API
* Returns average price in a postcode by number of rooms
* Streamlit set up and working (image below)

## :black_nib: In Progress:
* Breakdown property type (detached, semi, terraced)
* Rental Analysis

## :books: Backlog:
* Streamlit visualisation
* Extra optional variables
* Comparison between selections

