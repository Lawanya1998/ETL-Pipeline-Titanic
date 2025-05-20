
import streamlit as st
import pandas as pd
import sqlite3

st.title("🚢 Titanic ETL Dashboard")

# Load CSV file
df = pd.read_csv("titanic.csv")

# Clean and transform
df = df.dropna(subset=['Age'])
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df['Fare'] = df['Fare'].apply(lambda x: round(x, 2))

# Save to SQLite
conn = sqlite3.connect("passengers.db")
df.to_sql("passenger_data", conn, if_exists="replace", index=False)

# Query results
query = "SELECT Pclass, ROUND(AVG(Fare), 2) as AvgFare FROM passenger_data GROUP BY Pclass"
result_df = pd.read_sql(query, conn)

# Display result
st.subheader("Average Fare by Class")
st.dataframe(result_df)
