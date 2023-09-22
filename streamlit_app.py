import streamlit
streamlit.title ('Samay New Healty Breakfast')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled free range egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#lets put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pic some fruits:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
