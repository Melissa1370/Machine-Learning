

# st.title("Hello, Streamlit!")
# st.write("This is a simple Streamlit app.")
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Title of the dashboard
st.title("Titanic Dashboard")

# Add a header
st.header("Welcome to My Dashboard!")

# Add some text
st.write("This is a simple dashboard created using Streamlit.")
    
# Display the dataframe
st.write("Titanic dataset:")

data=pd.read_csv(r"E:\data course\6-Python\Week02\titanic.csv")

# download csv button
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

csv = convert_df(data)
st.download_button(
    label="Download Titanic data as CSV",
    data=csv,
    file_name="Titanic.csv",
    mime="text/csv",)

# showing dataframe
st.dataframe(data)

# Add sidebar
st.sidebar.title("Filters")
selected_col = st.sidebar.selectbox("Choose a column", ["Sex", "Pclass"])

# Display chart based on selection
if selected_col == "Sex":
    #st.bar_chart(data['sex'])
    st.bar_chart(data['sex'])
elif selected_col == "Pclass":
    st.bar_chart(data['pclass'])

# Create a Seaborn plot
# st.subheader("Scatter Plot")
# fig, ax = plt.subplots()
# sns.scatterplot(data=data, x="fare", y="tip", hue="time", ax=ax)
# st.pyplot(fig)

# Create a Seaborn boxplot
st.subheader("Boxplot")
fig, ax = plt.subplots()
sns.boxplot(data=data, x="pclass", y="fare", hue="sex", ax=ax)
st.pyplot(fig)

# Add a chart
# st.line_chart(data.set_index('x'))

# Add a slider for interactivity
# slider_value = st.slider("Select a value", 0, 100, 50)
# st.write(f"You selected: {slider_value}")

# Add a button
if st.button("Click Me"):
    st.write("Button clicked!")
    
