import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/programmarself/Air-Quality-Index-Water-Pollution-In-Major-Cities-of-Pakistan-2020/main/water-air-quality-big-cities-of-pakistan-2020.csv, encoding='latin-1'"
data = pd.read_csv(url)

# Streamlit App
st.title("Data Visualization Dashboard")
st.sidebar.title("Visualization Settings")

# Display Dataset
if st.sidebar.checkbox("Show Dataset"):
    st.write("### Dataset Overview:")
    st.dataframe(data.head())

# Select Visualization Type
vis_type = st.sidebar.selectbox(
    "Choose Visualization Type",
    ["Bar Chart", "Scatterplot", "Histogram", "Boxplot", "Heatmap", "Regplot", "Pairplot", "Violinplot", "Sunburst"]
)

# General Settings for Plot Customization
st.sidebar.subheader("Plot Settings")
x_col = st.sidebar.selectbox("Select X-axis", data.columns)
y_col = st.sidebar.selectbox("Select Y-axis", [None] + list(data.columns))
hue_col = st.sidebar.selectbox("Select Hue (Optional)", [None] + list(data.columns))

# Generate Plots
if vis_type == "Bar Chart":
    st.write("### Bar Chart")
    if y_col:
        fig = px.bar(data, x=x_col, y=y_col, color=hue_col, title="Bar Chart")
    else:
        fig = px.bar(data, x=x_col, color=hue_col, title="Bar Chart")
    st.plotly_chart(fig)

elif vis_type == "Scatterplot":
    st.write("### Scatterplot")
    fig = px.scatter(data, x=x_col, y=y_col, color=hue_col, title="Scatterplot")
    st.plotly_chart(fig)

elif vis_type == "Histogram":
    st.write("### Histogram")
    fig = px.histogram(data, x=x_col, color=hue_col, title="Histogram")
    st.plotly_chart(fig)

elif vis_type == "Boxplot":
    st.write("### Boxplot")
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x=x_col, y=y_col, hue=hue_col, ax=ax)
    st.pyplot(fig)

elif vis_type == "Heatmap":
    st.write("### Heatmap")
    corr = data.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

elif vis_type == "Regplot":
    st.write("### Regplot")
    fig, ax = plt.subplots()
    sns.regplot(data=data, x=x_col, y=y_col, ax=ax, scatter_kws={'color':'blue'}, line_kws={'color':'red'})
    st.pyplot(fig)

elif vis_type == "Pairplot":
    st.write("### Pairplot")
    fig = sns.pairplot(data, hue=hue_col)
    st.pyplot(fig)

elif vis_type == "Violinplot":
    st.write("### Violinplot")
    fig, ax = plt.subplots()
    sns.violinplot(data=data, x=x_col, y=y_col, hue=hue_col, split=True, ax=ax)
    st.pyplot(fig)

elif vis_type == "Sunburst":
    st.write("### Sunburst Chart")
    fig = px.sunburst(data, path=[x_col, y_col] if y_col else [x_col], color=hue_col, title="Sunburst Chart")
    st.plotly_chart(fig)

# Download Filtered Data
st.sidebar.subheader("Download Filtered Data")
st.sidebar.download_button(
    label="Download CSV",
    data=data.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv"
)

st.write("### Thank you for exploring the dataset!")
