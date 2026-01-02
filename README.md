# Data Visualization Dashboard Report

## 1. Introduction

This report describes the design and implementation of a Streamlit-based data visualization dashboard. The application allows users to upload CSV or Excel files and perform basic data analysis, visualization, and comparison tasks through an interactive web interface. The goal of the project is to provide a simple yet effective tool for exploratory data analysis without requiring advanced programming knowledge from the user.

## 2. Objectives

The main objectives of this project are:

* To support uploading and reading CSV and Excel datasets.
* To automatically preprocess and handle different data types.
* To provide descriptive statistics and data summaries.
* To visualize data using multiple chart types.
* To enable basic data comparison and correlation analysis.

## 3. Technologies Used

The following technologies and libraries were used in this project:

* **Python**: Core programming language.
* **Streamlit**: Web framework for building interactive data applications.
* **Pandas**: Data manipulation and preprocessing.
* **Matplotlib**: Basic plotting and chart rendering.
* **Seaborn**: Advanced statistical visualizations (box plots and heatmaps).

## 4. Data Handling and Preprocessing

After uploading a file, the dataset is loaded into a Pandas DataFrame. Since many real-world datasets store numeric values as strings (e.g., values containing commas, currency symbols, or percentage signs), an automatic data cleaning step is applied:

* Removal of common non-numeric characters such as `,`, `$`, `€`, and `%`.
* Conversion of numeric-like columns into appropriate numeric data types.

This preprocessing step ensures that numeric columns can be correctly detected and used for visualization and statistical analysis.

## 5. Application Features

### 5.1 Data Preview

The dashboard displays the uploaded dataset in a table format, allowing users to quickly inspect rows, columns, and values.

### 5.2 Dataset Information

Basic information about the dataset is shown, including:

* Number of rows and columns.
* Column names.
* Missing values per column.

### 5.3 Data Filtering

Users can filter the dataset by selecting a column and a specific value. The filtered result is displayed in a separate table, enabling focused analysis on a subset of the data.

### 5.4 Descriptive Statistics

The application provides descriptive statistics such as count, mean, standard deviation, minimum, and maximum values for numeric columns. This helps users understand the overall distribution of the data.

### 5.5 Data Visualization

The dashboard supports multiple chart types:

* Line Chart
* Bar Chart
* Histogram
* Box Plot
* Scatter Plot

Users can select the chart type and relevant axes dynamically. The application ensures that numeric columns are used where required to prevent runtime errors.

### 5.6 Data Comparison

For a selected numeric column, key metrics are displayed, including:

* Mean
* Median
* Minimum value
* Maximum value

These metrics allow quick comparison and evaluation of numeric data.

### 5.7 Correlation Analysis

A correlation matrix is generated for numeric columns and visualized using a heatmap. This feature helps identify relationships between variables and supports deeper analytical insights.

## 6. Error Handling and Robustness

The application includes safeguards to prevent common runtime errors:

* Validation to ensure that numeric columns exist before visualization.
* Conditional logic to handle chart types that do not require a Y-axis (e.g., histograms).
* Graceful warnings instead of application crashes when data is not suitable for a specific operation.

## 7. Conclusion

The developed Streamlit dashboard successfully meets the project objectives by providing a flexible and user-friendly data analysis tool. It enables users to upload datasets, clean and preprocess data, explore statistics, and generate meaningful visualizations. The application is suitable for academic assignments, portfolio projects, and basic business data analysis tasks. Future improvements may include interactive Plotly charts, time-series analysis, multi-file comparison, and exportable reports.
