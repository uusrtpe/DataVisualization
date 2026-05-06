import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## PAGE CONFIG
st.set_page_config(
    page_title="Data Visualization App",
    layout="wide"
)

st.title("📊 CSV / Excel Data Visualization & Analysis App")


## FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is None:
    st.info("Please upload a CSV or Excel file to start.")
    st.stop()


## LOAD DATA

if uploaded_file.name.endswith(".csv"):
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_excel(uploaded_file)

st.success("File uploaded successfully ✅")

st.subheader("🔍 Data Preview")
st.dataframe(df)
st.subheader("ℹ️ Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Shape (Rows, Columns):**", df.shape)
    st.write("**Column Names:**")
    st.write(list(df.columns))

with col2:
    st.write("**Missing Values per Column:**")
    st.write(df.isnull().sum())


## FILTER DATA

st.subheader("🎯 Data Filtering")

filter_column = st.selectbox(
    "Select a column to filter",
    df.columns
)

filter_values = df[filter_column].dropna().unique()

filter_value = st.selectbox(
    "Select a value",
    filter_values
)

filtered_df = df[df[filter_column] == filter_value]

st.write("Filtered Data")
st.dataframe(filtered_df)

st.subheader("📈 Descriptive Statistics")
st.write(df.describe(include="all"))

st.subheader("📊 Data Visualization")

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

if len(numeric_columns) == 0:
    st.warning("No numeric columns available for visualization.")
    st.stop()

chart_type = st.selectbox(
    "Select chart type",
    ["Line Chart", "Bar Chart", "Histogram", "Box Plot", "Scatter Plot"]
)

x_col = st.selectbox(
    "Select X-axis",
    df.columns
)


if chart_type != "Histogram":
    y_col = st.selectbox(
        "Select Y-axis",
        numeric_columns
    )

fig, ax = plt.subplots()

if chart_type == "Line Chart":
    ax.plot(df[x_col], df[y_col])

elif chart_type == "Bar Chart":
    ax.bar(df[x_col], df[y_col])

elif chart_type == "Histogram":
    ax.hist(df[x_col], bins=20)
    ax.set_ylabel("Frequency")

elif chart_type == "Box Plot":
    sns.boxplot(x=df[x_col], y=df[y_col], ax=ax)

elif chart_type == "Scatter Plot":
    ax.scatter(df[x_col], df[y_col])

ax.set_xlabel(x_col)

if chart_type != "Histogram":
    ax.set_ylabel(y_col)

st.pyplot(fig)


st.subheader("⚖️ Data Comparison")

compare_col = st.selectbox(
    "Select a numeric column for comparison",
    numeric_columns
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Mean", round(df[compare_col].mean(), 2))
col2.metric("Median", round(df[compare_col].median(), 2))
col3.metric("Min", round(df[compare_col].min(), 2))
col4.metric("Max", round(df[compare_col].max(), 2))


st.subheader("🔗 Correlation Matrix")

corr = df[numeric_columns].corr()

fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)
