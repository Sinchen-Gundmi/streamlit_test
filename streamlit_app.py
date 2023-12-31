import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('Whats for Breakfast? 🥣 🥗 🐔 🥑🍞')
streamlit.header('Breakfast Menu') 
streamlit.text('Omega 3 & Blueberry Oatmeal') 
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


# New Section to display fruityvice api response
streamlit. header ('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# Pandas Normalize
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

# # Getting user account data
# # print(streamlit.secrets["snowflake"])
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# Query Data
my_cnx = snowflake.connector.connect (**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor ()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur. fetchall()
streamlit.text ("The fruit load list contains:")
streamlit.text (my_data_row)
