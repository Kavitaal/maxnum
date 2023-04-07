import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# App to find the largest among three numbers

This app finds the lagest among three numbers
""")

#Get Input

st.header('Enter Three Numbers')

def user_input_numbers():
    num_1 = st.number_input("FIRST_NUMBER", min_value=0, max_value=100000, step=1)
    num_2 = st.number_input("SECOND_NUMBER", min_value=0, max_value=100000, step=1)
    num_3 = st.number_input("THIRD_NUMBER", min_value=0, max_value=100000, step=1)
    
    data = {'FIRST_NUMBER':num_1,
            'SECOND_NUMBER':num_2,
            'THIRD_NUMBER':num_3
            }
    numbers = pd.DataFrame(data, index=[0])
    return numbers
    
df = user_input_numbers()

st.subheader('Enter Three Numbers')
st.write(df.to_dict())
max_num = 0
if (df['FIRST_NUMBER'] > df['SECOND_NUMBER']).bool():
    max_num = df['FIRST_NUMBER'] 
else:
    max_num = df['SECOND_NUMBER'] 

if (df['THIRD_NUMBER'] > max_num).bool():
    max_num = df['THIRD_NUMBER']


st.write("Maximum number is:")
st.write(max_num)
