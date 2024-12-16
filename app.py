import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Custom Styles
st.set_page_config(
    page_title="Air Quality Index & Water Pollution In Major Cities of Pakistan (2020)",
    page_icon="📊",
    layout="wide",
)

# Header Section
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #2E86C1;
    }
    .sub-title {
        font-size: 1.2rem;
        text-align: center;
        color: #566573;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        color: #566573;
        margin-top: 50px;
    }
    a {
        text-decoration: none;
        color: #2874A6;
        font-weight: bold;
    }
    a:hover {
        color: #1ABC9C;
    }
    </style>
    <div class="main-title">Data Visualization Dashboard</div>
    <div class="sub-title">Explore and Visualize Data with Interactive Plots</div>
    """,
    unsafe_allow_html=True,
)

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/programmarself/Air-Quality-Index-Water-Pollution-In-Major-Cities-of-Pakistan-2020/main/water-air-quality-big-cities-of-pakistan-2020.csv"
data = pd.read_csv(url, encoding="ISO-8859-1")

# Sidebar Settings
st.sidebar.title("🔧 Visualization Settings")

# Display Dataset
if st.sidebar.checkbox("Show Dataset"):
    st.write("### Dataset Overview:")
    st.dataframe(data.head(10))

# Select Visualization Type
vis_type = st.sidebar.selectbox(
    "Choose Visualization Type",
    ["Bar Chart", "Scatterplot", "Histogram", "Boxplot", "Heatmap", "Regplot", "Pairplot", "Violinplot", "Sunburst"],
)

# General Settings for Plot Customization
st.sidebar.subheader("Plot Settings")
x_col = st.sidebar.selectbox("Select X-axis", data.columns)
y_col = st.sidebar.selectbox("Select Y-axis", [None] + list(data.columns))
hue_col = st.sidebar.selectbox("Select Hue (Optional)", [None] + list(data.columns))

# Generate Plots
st.markdown(f"### {vis_type}")
if vis_type == "Bar Chart":
    if y_col:
        fig = px.bar(data, x=x_col, y=y_col, color=hue_col, title="Bar Chart")
    else:
        fig = px.bar(data, x=x_col, color=hue_col, title="Bar Chart")
    st.plotly_chart(fig)

elif vis_type == "Scatterplot":
    fig = px.scatter(data, x=x_col, y=y_col, color=hue_col, title="Scatterplot")
    st.plotly_chart(fig)

elif vis_type == "Histogram":
    fig = px.histogram(data, x=x_col, color=hue_col, title="Histogram")
    st.plotly_chart(fig)

elif vis_type == "Boxplot":
    fig, ax = plt.subplots()
    sns.boxplot(data=data, x=x_col, y=y_col, hue=hue_col, ax=ax)
    st.pyplot(fig)

elif vis_type == "Heatmap":
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

elif vis_type == "Regplot":
    fig, ax = plt.subplots()
    sns.regplot(data=data, x=x_col, y=y_col, ax=ax, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
    st.pyplot(fig)

elif vis_type == "Pairplot":
    fig = sns.pairplot(data, hue=hue_col)
    st.pyplot(fig)

elif vis_type == "Violinplot":
    fig, ax = plt.subplots()
    sns.violinplot(data=data, x=x_col, y=y_col, hue=hue_col, split=True, ax=ax)
    st.pyplot(fig)

elif vis_type == "Sunburst":
    fig = px.sunburst(data, path=[x_col, y_col] if y_col else [x_col], color=hue_col, title="Sunburst Chart")
    st.plotly_chart(fig)

# Download Filtered Data
st.sidebar.subheader("Download Filtered Data")
st.sidebar.download_button(
    label="📥 Download CSV",
    data=data.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv",
)

# Footer Section
st.markdown(
    """
    <div class="footer">
        <p>Developed By: <b>IRFAN ULLAH KHAN</b></p>
        <p>Connect with me on <a href="https://www.linkedin.com/in/iukhan/" target="_blank">LinkedIn</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
