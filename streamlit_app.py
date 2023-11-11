# app.py

'''import streamlit as st

from pages.page1 import RestaurantA as RA
from pages.page2 import RestaurantA as RB
from pages.page3 import RestaurantA as RC

# Mock data for restaurants
restaurants_data = [
    {"id": 1, "name": "Restaurant A", "image_path": "./public/r1.jpg"},
    {"id": 2, "name": "Restaurant B", "image_path": "./public/r2.jpg"},
    {"id": 3, "name": "Restaurant C", "image_path": "./public/r3.jpg"},
]


# Streamlit app
def homepage():
    st.title("Food Delivery Website - Home")

    # Display restaurant information on the homepage in rows of three
    for i in range(0, len(restaurants_data), 3):
        row = st.columns(3)  # Create three columns for each row

        for j, restaurant in enumerate(restaurants_data[i:i+3]):
            with row[j]:
                # Display restaurant image
                st.image(restaurant['image_path'], width=200)

                # Display page functionality buttons
                if st.button(f"View Menu - {restaurant['name']}"):
                    # Use HTML to clear the screen
                    st.markdown("<div style='height: 0px;'></div>", unsafe_allow_html=True)

                    # Display the content of the selected subpage
                    if restaurant['name'] == "Restaurant A":
                        RA()
                    elif restaurant['name'] == "Restaurant B":
                        RB()
                    elif restaurant['name'] == "Restaurant C":
                        RC()

# Run the app
if _name_ == "_main_":
    homepage()'''

# app.py

import streamlit as st
from pages.page1 import RestaurantA as RA
from pages.page2 import RestaurantB as RB
from pages.page3 import RestaurantC as RC

# Mock data for restaurants
restaurants_data = [
    {"id": 1, "name": "Restaurant A", "image_path": "./public/r1.jpg"},
    {"id": 2, "name": "Restaurant B", "image_path": "./public/r2.jpg"},
    {"id": 3, "name": "Restaurant C", "image_path": "./public/r3.jpg"},
]

def homepage():
    st.header("Welcome to the Food Delivery Website!")
    # Display restaurant information on the homepage in rows of three
    for i in range(0, len(restaurants_data), 3):
        row = st.columns(3)  # Create three columns for each row

        for j, restaurant in enumerate(restaurants_data[i:i+3]):
            with row[j]:
                # Display restaurant image
                st.image(restaurant['image_path'], width=200)

def show_page1():
    RA()

def show_page2():
    RB()

def show_page3():
    RC()

def main():
    st.title("Food Delivery Website")

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ["Home", "Page 1", "Page 2", "Page 3"])

    if page == "Home":
        homepage()
    elif page == "Page 1":
        show_page1()
    elif page == "Page 2":
        show_page2()
    elif page == "Page 3":
        show_page3()

# Run the app
if __name__ == "__main__":
    main()