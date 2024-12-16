import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset from GitHub
@st.cache_data
def load_data():
    url = 'https://github.com/programmarself/Air-Quality-Index-Water-Pollution-In-Major-Cities-of-Pakistan-2020/blob/main/water-air-quality-big-cities-of-pakistan-2020.csv'
    return pd.read_csv(url)

# Streamlit app layout
st.title("Water and Air Quality in Big Cities of Pakistan (2020)")

# Load the dataset
data = load_data()

# Clean the dataset
data.columns = data.columns.str.strip().str.replace('"', '')
data['population'] = data['population'].str.replace(',', '').astype(float)

# Sidebar for user input
st.sidebar.header("User Input Features")
selected_city = st.sidebar.selectbox("Select a City", data['City'].unique())

# Filter data based on user selection
city_data = data[data['City'] == selected_city]

# Display selected city data
st.subheader(f"Data for {selected_city}")
st.write(city_data)

# Bar Chart for Air Quality
st.subheader("Air Quality Bar Chart")
sns.barplot(x='City', y='AirQuality', data=city_data)
plt.xticks(rotation=45)
st.pyplot()

# Scatter Plot for Water Pollution vs Air Quality
st.subheader("Scatter Plot: Water Pollution vs Air Quality")
sns.scatterplot(x='WaterPollution', y='AirQuality', data=data)
st.pyplot()

# Histogram for Air Quality
st.subheader("Air Quality Histogram")
sns.histplot(data['AirQuality'], bins=10, kde=True)
st.pyplot()

# Box Plot for Air Quality by Region
st.subheader("Box Plot: Air Quality by Region")
sns.boxplot(x='Region', y='AirQuality', data=data)
plt.xticks(rotation=45)
st.pyplot()

# Heatmap for Correlation
st.subheader("Heatmap of Correlation")
correlation = data[['AirQuality', 'WaterPollution', 'population']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
st.pyplot()

# Pair Plot for Air and Water Quality
st.subheader("Pair Plot")
sns.pairplot(data[['AirQuality', 'WaterPollution', 'population']])
st.pyplot()

# Violin Plot for Water Pollution by Region
st.subheader("Violin Plot: Water Pollution by Region")
sns.violinplot(x='Region', y='WaterPollution', data=data)
plt.xticks(rotation=45)
st.pyplot()

# Sunburst chart
st.subheader("Sunburst Chart for Population by Region and City")
fig = px.sunburst(data, path=['Region', 'City'], values='population', title="Population Distribution")
st.plotly_chart(fig)

# Footer
st.write("Data Source: Big Cities of Pakistan (2020)")
