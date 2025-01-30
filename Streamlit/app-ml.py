import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("First ml Dashboard")

st.sidebar.header("Input Parameters")

def user_input_features():
    sepal_length=st.sidebar.slider("sepal length",4,7,5)
    petal_length=st.sidebar.slider("sepal length",2,6,3)
    sepal_width=st.sidebar.slider("sepal length",1,10,8)
    petal_width=st.sidebar.slider("sepal length",0.1,2.5,0.2)

    data={'sepal_length':sepal_length,
          'sepal_width':sepal_width,
          'petal_length':petal_length,
          'petal_width':petal_width}
    features=pd.DataFrame(data,index=[0])
    return features

df=user_input_features()


st.subheader('your input data:')
st.dataframe(df)

iris=datasets.load_iris()
X=iris.data
y=iris.target


clf=RandomForestClassifier()
clf.fit(X,y)

prediction=clf.predict(df)

st.subheader("final result of data from machine learning model")
# st.write(iris.target_names)

# st.subheader("predictions")
st.write(prediction)
st.write(iris.target_names[prediction])

# st.balloons()

import time
my_bar=st.progress(0)
for percent_complete in range(100):
   time.sleep(0.1)
   my_bar.progress(percent_complete+1)