import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import plotly as plt
import plotly.express as px
import streamlit as st
from datetime import time, datetime
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components
import matplotlib
from ydata_profiling import ProfileReport
import csv


st.header('st.write')

st.write('Hello, i can write now')
st.write('1, 2, 3')

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Ejemplo 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
print(df2.head())

c = alt.Chart(df2).mark_point().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.write(px.scatter(df2))

st.header('st.slider')

st.write(st.slider('Volumen', min_value=0,max_value=100,))

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Ejemplo 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Ejemplo 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     min_value=datetime(2020, 1, 1, 9, 30),max_value =datetime(2024, 12, 30, 12, 00),
     value = (datetime(2020, 1, 1, 9, 30),datetime(2021, 1, 1, 9, 30)),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

r_values = np.random.randint(low= 20, high= 40, size = 10)
print('random_values ' + str(r_values))
S_Slider = st.select_slider('Select Slider', options=range(0,11),value = 5)

st.header('Day 9: st.line_chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('Select box ( st.selectbox() )')
options = st.selectbox('Options',['Option 1', 'Option 2','Option 3'])
st.write('the opttion you choose is ', options)

st.header('Multiselect : st.multiselect()')
multiselect = st.multiselect('which options you´d like',['Option 1','Option 2','Option 3','Option 4'])

st.write('You selected this options:', multiselect)

st.header('Checkbox: st.checkbox()')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
else:
    st.write('Please select one above')
    
# =============================================================================
# st.header('`streamlit_pandas_profiling`')
# 
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# 
# pr = df.profile_report()
# st_profile_report(pr)
# st.header('st.latex')
# =============================================================================

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.header('Coloring')
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

# =============================================================================
# profile = ProfileReport(df, title="Pandas Profiling Report")
# components.iframe(src=profile.to_notebook_iframe(),scrolling=True)
# =============================================================================

# =============================================================================
# st.title('Secrets')
# st.write(st.secrets('message'))
# =============================================================================
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  with uploaded_file as csv_file:
      muestra = csv_file.read(64)
  # comprobar si el fichero csv tiene cabecera
      hay_cabecera = csv.Sniffer().has_header(muestra)
      print(hay_cabecera)
  # obtener el dialecto del fichero csv
      dialecto = csv.Sniffer().sniff(muestra)

# =============================================================================
#   df = pd.read_csv(uploaded_file,delimiter=';')
#   df2 = df.sample(frac = 0.5)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Descriptive Statistics')
#   st.write(df2.describe())  
#   pr = df2.profile_report()
#   st_profile_report(pr)
# =============================================================================
else:
  st.info('☝️ Upload a CSV file')
