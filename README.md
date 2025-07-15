# Prodigy InfoTech - Data Science Internship: Task 01
### World Population Analysis Dashboard

This repository contains the solution for the first task of the Data Science Internship at Prodigy InfoTech. The project focuses on data cleaning, analysis, and visualization of world population data obtained from the World Bank.

---

## Task Objective

> "Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population."

While the core task was to create a single chart, this project goes a step further by developing a comprehensive 2x2 dashboard to provide a multifaceted view of the global population in 2020.

---

## Dataset
*   **Source:** The World Bank
*   **File:** `API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`
*   **Description:** This dataset contains the total population for various countries, regions, and income groups from 1960 to 2022.
*   **Data Cleaning:** A crucial part of the analysis involved **data cleaning**, where a custom function was implemented to filter out non-country aggregates (e.g., "World", "Euro area", "Sub-Saharan Africa") to ensure the analysis was performed only on individual countries.

---

## Tools and Libraries Used
*   **Python 3**
*   **Pandas:** For data manipulation and cleaning.
*   **Matplotlib:** For creating the visualizations.
*   **NumPy:** For numerical operations.

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install the required libraries:**
    ```bash
    pip install pandas matplotlib numpy
    ```

3.  **Run the script:**
    Ensure the dataset `API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv` is in the same directory as the script.
    ```bash
    python your_script_name.py
    ```

---

## Analysis and Visualizations

The output is a single figure containing a dashboard of four distinct plots, each providing a unique insight into the world's population in 2020.

**Final Dashboard Output:**

![World Population Dashboard](https://github.com/user-attachments/assets/3f337711-c879-4e6f-9621-685d299ef0ff)

### 1. Top 10 Most Populous Countries (Horizontal Bar Chart)
*   Displays the 10 countries with the highest populations in 2020.
*   A horizontal layout is used for better readability of country names.
*   Data labels (e.g., "1.4B") are added for precise and immediate understanding.

### 2. Distribution of Country Populations (Histogram)
*   Shows the frequency distribution of country populations, highlighting that the data is heavily **right-skewed**.
*   Vertical lines for the **mean** and **median** are included to visually demonstrate the skewness.

### 3. Population Trends (Line Chart)
*   Visualizes the population growth from 2000 to 2020 for the top 5 most populous countries.
*   Adds a time-series dimension to the analysis, showing the consistent upward trend for these nations.

### 4. Countries by Population Range (Bar Chart)
*   Groups countries into logical population brackets (e.g., "<1M", "1M-10M", "10M-50M").
*   Shows that the largest number of countries (89) fall within the 1-10 million population range.

---

## Key Insights

*   **Extreme Skewness:** The global population is not evenly distributed. The mean population (35.8 million) is significantly higher than the median (5.6 million), confirming a few countries have massive populations while most do not.
*   **Dominance of Asia:** The top of the population list is dominated by Asian countries.
*   **Most Common Size:** The most frequent population size for a country is between 1 and 10 million people.
*   **Consistent Growth:** The world's largest countries have continued to experience steady population growth over the last two decades.

---
**Author:** Aaryan
