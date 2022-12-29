
import streamlit 
import pandas as pd 

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
streamlit.multiselect('Pick', list(df))

streamlit.dataframe(df)
