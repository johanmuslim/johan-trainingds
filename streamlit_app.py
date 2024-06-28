# %%writefile  webapp.py 
import streamlit as st
import pandas as pd 
import requests
# import plotly.express as px 
# import matplotlib.pyplot as plt
# from st_aggrid import AgGrid

#baca dataframe dari file csv 
house = pd.read_csv('house_clean.csv')

def main() : 
  st.header('Halaman Streamlit Johan M.')
  st.subheader('This is SubHeader')
  st.markdown('# Rendering Markdown ')
  st.write('Some Phytagorean Equation : ')
  st.latex('c^2 = a^2+b^2')
  
  st.write('Contoh dataframe')
  st.dataframe(house)
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
 
  #matplotlib chart 
  # fig,ax = plt.subplots()
  # plt.scatter(house['sqft_lot'],house['price'])
  # st.pyplot(fig)
  # plotly_fig = px.scatter(house['sqft_lot'],house['price'])
  # st.plotly_chart(plotly_fig)


if __name__ == '__main__' : 
  main()
