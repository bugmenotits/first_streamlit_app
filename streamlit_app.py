
import streamlit 
import pandas as pd 
import requests 
import snowflake.connector 
from urllib.error import URLError

streamlit.title('first ever')

streamlit.text('testing')
streamlit.text('testing2')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(df)

df = df.set_index('Fruit')
df_select=streamlit.multiselect('Pick', list(df.index),['Avocado','Strawberries'])
df_to_show = df.loc[df_select]
streamlit.dataframe(df_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)




def fruit_data(this):
  fruit_repsonse= requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruitvice_normalized = pd.json_normalize(fruit_repsonse.json())
  return fruitvice_normalized

streamlit.header('Fruit')

try:
  fruit_choice = streamlit.text_input('What fruit')
  if not fruit_choice:
    streamlit.error('Please select a fruit')
  else:
    back_function = fruit_data(fruit_choice)
    streamlit.dataframe(back_function)
except URLError as e:
  streamlit.error()

streamlit.header('The fruit list')

def get_fruit_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruitvice")
    return my_cur.fetchall()

if streamlit.button('Get fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data=get_fruit_list()
  streamlit.dataframe(my_data)
  
#add_my_fruit = streamlit.text_input('Add a fruit')


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert fruit('from streamlit')")
    return "Thanks for adding" + new_fruit
  
add_my_fruit = streamlit.text_input('What add fruit')
if streamlit.button('add a fruit'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  steamlit.text(back_from_function)

