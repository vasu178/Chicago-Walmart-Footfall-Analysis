# 🛒 Chicago Walmart Closure Analysis

### A Data Analytics Case Study on Walmart's Chatham Store Closure (2018–2024)

## 📌 Project Overview

This project investigates the factors that may have contributed to the closure of the Walmart Supercenter located in **Chatham, Chicago**. Instead of relying on assumptions, the analysis combines demographic trends, crime statistics, competitor presence, and customer reviews to understand how the surrounding environment changed between **2018 and 2024**.

The project follows a complete data analytics workflow—from raw data collection and cleaning to SQL analysis, Python-based review analytics, geospatial analysis, and an interactive Power BI dashboard.

---

# 🎯 Objectives

* Analyze demographic changes around the Walmart location.
* Study crime trends over multiple years.
* Examine the competitive retail landscape.
* Analyze customer sentiment from online reviews.
* Build a PostgreSQL data warehouse for analytical queries.
* Develop interactive Power BI dashboards to communicate business insights.
* Demonstrate an end-to-end real-world Business Intelligence workflow.

---

# 🏗️ Project Architecture

```
Raw Data
│
├── Census Data (ACS)
├── Chicago Crime Data
├── Competitor Data
└── Walmart Reviews
        │
        ▼
Python Data Cleaning
        │
        ▼
Cleaned CSV Files
        │
        ▼
PostgreSQL Database
        │
        ├── SQL Cleaning
        ├── Analytical Views
        ├── KPI Views
        └── Master Tables
        │
        ▼
Python Analysis
        │
        ├── Correlation Analysis
        ├── Review Sentiment Analysis
        └── Geospatial Analysis
        │
        ▼
Power BI Dashboard
```

---

# 🗂️ Repository Structure

```
Chicago-Walmart-Footfall-Analysis/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── sql/
│   ├── schema/
│   ├── views/
│   ├── master_tables/
│   └── kpis/
│
├── python/
│   ├── data_cleaning/
│   ├── sentiment_analysis/
│   ├── correlation_analysis/
│   └── geospatial_analysis/
│
├── dashboard/
│   └── PowerBI.pbix
│
├── images/
│
└── README.md
```

---

# 📊 Datasets Used

## 1. American Community Survey (ACS)

Annual demographic datasets collected from the U.S. Census Bureau.

Includes:

* Population
* Age Distribution
* Educational Attainment
* Household Income
* Employment
* Housing Characteristics
* Poverty Indicators
* Race & Ethnicity

Years Covered:

* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024

---

## 2. Chicago Crime Dataset

Historical crime records for the Chatham community area.

Metrics analyzed include:

* Total Crimes
* Arrest Rate
* Crime Categories
* Yearly Crime Trends
* Crime Density

---

## 3. Competitor Dataset

Nearby retail stores around Walmart were collected and analyzed.

Analysis includes:

* Distance from Walmart
* Store Density
* Brand Distribution
* Geographic Spread

---

## 4. Walmart Customer Reviews

Customer reviews were collected for sentiment analysis.

Analysis includes:

* Positive Reviews
* Negative Reviews
* Frequently Mentioned Topics
* Customer Satisfaction Trends
* Keyword Analysis

---

# 🧹 Data Cleaning

Python scripts were developed to automate preprocessing for every dataset.

Cleaning steps included:

* Removing unnecessary metadata
* Standardizing column names
* Handling missing values
* Correcting data types
* Removing duplicate records
* Cleaning ACS margin-of-error columns
* Exporting analysis-ready CSV files

---

# 🗄️ Database Design

The cleaned datasets were imported into PostgreSQL.

The database contains:

* Census tables
* Crime tables
* Competitor tables
* Review tables
* Master analytical tables
* SQL Views
* KPI Views

---

# 📈 SQL Analysis

Several analytical SQL views were created to support reporting.

Examples include:

* Demographic Trends
* Crime Trends
* Arrest Rate Analysis
* Population Growth
* Income Growth
* Education Statistics
* Housing Analysis
* Master Dashboard Views
* Executive KPIs

SQL concepts used:

* JOINs
* CTEs
* Window Functions
* Aggregate Functions
* CASE Statements
* Views
* Common Table Expressions

---

# 🐍 Python Analysis

Python was used for advanced analytics beyond SQL.

### Correlation Analysis

* Correlation Matrix
* Heatmaps
* Regression Analysis

### Review Sentiment Analysis

* Text Cleaning
* Sentiment Classification
* Word Frequency
* Topic Extraction

### Geospatial Analysis

* Competitor Distance Calculation
* Store Density
* Folium Interactive Maps
* Geographic Visualization

---

# 📊 Power BI Dashboard

The final dashboard was developed in Power BI.

Dashboard pages include:

* Executive Summary
* Demographic Analysis
* Crime Analysis
* Competitor Analysis
* Customer Review Analysis

Interactive Features:

* Year Slicers
* KPI Cards
* Drill-through
* Dynamic Charts
* Interactive Maps
* Tooltips
* Filters

---

# 📈 Key Business Questions

This project answers questions such as:

* How did demographics change around the Walmart store?
* Did crime increase before the store closure?
* Was income increasing or decreasing?
* Did educational attainment improve over time?
* Was the market saturated with competitors?
* What were customers saying about the store?
* Which factors appear to have contributed most to the closure?

---

# 🛠️ Technologies Used

| Category             | Tools                      |
| -------------------- | -------------------------- |
| Programming          | Python                     |
| Database             | PostgreSQL                 |
| SQL IDE              | pgAdmin                    |
| Data Processing      | Pandas, NumPy              |
| Visualization        | Power BI                   |
| Geospatial           | Folium                     |
| Statistical Analysis | Matplotlib, Seaborn, SciPy |
| Version Control      | Git & GitHub               |

---

# 📷 Dashboard Preview

*(Add screenshots of your Power BI dashboard here.)*

Example:

```
images/
    executive_summary.png
    demographics.png
    crime_analysis.png
    competitors.png
    review_analysis.png
```

---

# 🚀 Future Improvements

* Predictive modeling for store performance.
* Machine learning-based closure risk prediction.
* Interactive web dashboard using Streamlit.
* Real-time crime data integration.
* Automated ETL pipeline.

---

# 📚 Skills Demonstrated

* Data Cleaning
* Data Wrangling
* SQL Analytics
* PostgreSQL
* Python
* Power BI
* Business Intelligence
* KPI Development
* Dashboard Design
* Data Visualization
* Geospatial Analysis
* Customer Sentiment Analysis
* Statistical Analysis
* Data Storytelling

---

# 👨‍💻 Author

**Vasu Sharma**

* Data Analytics
* Business Intelligence
* SQL | Python | PostgreSQL | Power BI

Feel free to connect or explore the project!
