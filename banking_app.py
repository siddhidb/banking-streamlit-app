import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Banking Analytics App", layout="wide")

st.title("🏦 Banking Customer Analytics Dashboard")

df = pd.read_csv("bank_customers.csv")

st.subheader("Sample Data")
st.dataframe(df.head())

st.subheader("Customer Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Customer_Age'], kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Attrition by Gender")
gender_plot = df.groupby("Gender")["Attrition_Flag"].value_counts().unstack().plot(kind='bar', stacked=True)
st.pyplot(gender_plot.figure)
