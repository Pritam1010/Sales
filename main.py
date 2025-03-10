import streamlit as st
import pandas as pd
import os

# Define dataset path dynamically
dataset_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop", "projects", "Sales", "dataset", "ecommerce_dataset_final.csv")

def load_data():
    try:
        df = pd.read_csv(dataset_path)
        df.columns = df.columns.str.strip().str.lower()  # Normalize column names
        st.write("Columns in dataset:", df.columns.tolist())  # Debugging line
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None

# Streamlit UI
st.title("E-Commerce Product Analytics Dashboard")

# Load data
df = load_data()
if df is not None:
    st.write("### Product Data Table")
    st.dataframe(df)
    
    # Sidebar Filters
    st.sidebar.header("Filters")
    category_col = "category" if "category" in df.columns else df.columns[0]  # Fallback to first column
    brand_col = "brand" if "brand" in df.columns else df.columns[1]  # Fallback to second column
    
    category_filter = st.sidebar.selectbox("Select Category", ["All"] + list(df[category_col].unique()))
    brand_filter = st.sidebar.selectbox("Select Brand", ["All"] + list(df[brand_col].unique()))
    
    # Apply Filters
    if category_filter != "All":
        df = df[df[category_col] == category_filter]
    if brand_filter != "All":
        df = df[df[brand_col] == brand_filter]
    
    # Display Filtered Data
    st.write("### Filtered Data")
    st.dataframe(df)
    
    # Summary Statistics
    st.write("### Summary Statistics")
    st.write(df.describe())
    
    # Data Visualization
    st.write("### Price Distribution")
    st.bar_chart(df["price"])
    
    st.write("### Rating Distribution")
    st.bar_chart(df["rating"])
