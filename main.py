import streamlit as st
import pickle
import pandas as pd



def predict_rating(name,category,sentiment,Price,size,total_install,review):
  list1=[category_list.index(category),review,size,total_install,Price,sentiment_list.index(sentiment)]
  print(f"Rating of {name} is")
  return App.predict([list1])

st.title('Predict App Rating')
App=pickle.load(open('App_Rating.pkl','rb'))
category_list=['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FAMILY', 'FINANCE', 'FOOD_AND_DRINK', 'GAME', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'MAPS_AND_NAVIGATION', 'MEDICAL', 'NEWS_AND_MAGAZINES', 'PARENTING', 'PERSONALIZATION', 'PHOTOGRAPHY', 'PRODUCTIVITY', 'SHOPPING', 'SOCIAL', 'SPORTS', 'TOOLS', 'TRAVEL_AND_LOCAL', 'VIDEO_PLAYERS', 'WEATHER']
sentiment_list=['Negative', 'Neutral', 'Positive']
name= st.text_input('Enter app Name')
category=st.selectbox('category', category_list)
sentiment=st.selectbox('sentiment', sentiment_list)
Price = st.number_input('Enter Price')
total_install = st.number_input('Enter total_install')
size = st.number_input('Enter App size')
review=st.number_input('Enter no of review given')
if st.button('Predict'):
    App_rating= predict_rating(name,category,sentiment,Price,size,total_install,review)
    
    
    st.text(f'The rating of {name} is {App_rating[0]}')
        
  

