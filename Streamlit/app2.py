import streamlit as st
import numpy as np
import pandas as pd
#-----------------------------------------------
st.text("This is a simple Streamlit Dashboard")
st.write("Hello")
st.markdown("text H1")
st.markdown("text H2")
st.title("Dashboard")
st.latex(r'a+ar+f^2{n-1}')
#-------------------------------------------------
df=pd.read_csv(r"Social_Network_Ads.csv")
st.dataframe(df)
#--------------------------------------------------
from PIL import Image
photo=Image.open("pip vs conda.png")
st.image(photo)
#-------------------------------------
st.error("Error Message")
st.warning("Warning")
st.success("Congradulations")
#-----------------------------------
x=st.button("click here")
st.write(x)
if x:
    st.write("you re clicked")
#----------------------------------
x1=st.checkbox("check1"),
x2=st.checkbox("check2")   
x3=st.checkbox("check3")   
x4=st.checkbox("check4")  
st.write(x1,x2,x3,x4)
if x1 and x3:
    st.write("hoora")    
#--------------------------------
y=st.radio("choose",[1,2,3,4])
if y==4:
    st.write("the highest")
#--------------------------------
y2=st.slider("Slider",10,100) 
st.write(y2)   
#--------------------------------









