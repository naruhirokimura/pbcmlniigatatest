import pickle
import numpy as np
import pandas as pd
import streamlit as st
with open('model.pickle', 'rb') as f:
    model = pickle.load(f)

PT = st.sidebar.slider('PT (%)',min_value=0, max_value=130,value=100)
ALT = st.sidebar.slider(label='ALT (IU/L)', min_value=0, max_value=400,value=40)
Tbil = st.sidebar.slider(label='T-Bil (mg/dL)', min_value=0.1, max_value=10.0,value=1.0, step = 0.1)
BUN = st.sidebar.slider(label='BUN (mg/dL)', min_value=0, max_value=130,value=30)

sample = np.array([['PT', 'ALT', 'Tbil','BUN'],
              [PT, ALT, Tbil, BUN]])
dfsample = pd.DataFrame(data=[[PT, ALT, Tbil, BUN]], columns=['PT(%)', 'ALT (IU/l)', 'T-Bil (md/dl)', 'BUN (mg/dl)'])
st.write(dfsample)
pd1=model.predict_proba(dfsample)
if pd1[0,1] <0.841:
  st.write("This patient will not archieve Paris II criteria")
else:
  st.write('This patient will archieve Paris II criteria')
