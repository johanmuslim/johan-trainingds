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

  click_me_btn = st.button('Click Me')
  st.write(click_me_btn) #Return True kalo di Click 
  check_btn = st.checkbox('Klik Jika Setuju')
  if check_btn :
    st.write('Anda Setuju')
    
  radio_button= st.radio('Choose below',[x for x in range(1,3)])
  st.write('Anda Memilih',radio_button)
    
  #slider 
  age_slider = st.slider('Berapa Usia Anda',0,100)
  st.write('Usia Anda',age_slider)
    
  #Input (Typing)
  num_input = st.number_input('Input Berapapun')
  st.write('Kuadrat dari {} adalah {}'.format(num_input,num_input**2))


if __name__ == '__main__' : 
  main()
