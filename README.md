Prodigy InfoTech - Data Science Internship: Task 01
World Population Analysis Dashboard
This repository contains the solution for the first task of the Data Science Internship at Prodigy InfoTech. The project focuses on data cleaning, analysis, and visualization of world population data obtained from the World Bank.
Task Objective
"Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population."
While the core task was to create a single chart, this project goes a step further by developing a comprehensive 2x2 dashboard to provide a multifaceted view of the global population in 2020.
Dataset
Source: The World Bank
File: API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv
Description: This dataset contains the total population for various countries, regions, and income groups from 1960 to 2022.
A crucial part of the analysis involved data cleaning, where a custom function was implemented to filter out non-country aggregates (e.g., "World", "Euro area", "Sub-Saharan Africa") to ensure the analysis was performed only on individual countries.
Tools and Libraries Used
Python 3
Pandas: For data manipulation and cleaning.
Matplotlib: For creating the visualizations.
NumPy: For numerical operations.
Setup and Installation
Clone the repository:
Generated bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Use code with caution.
Bash
Install the required libraries:
Generated bash
pip install pandas matplotlib numpy
Use code with caution.
Bash
Run the script:
Ensure the dataset API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv is in the same directory as the script.
Generated bash
python your_script_name.py
Use code with caution.
Bash
Analysis and Visualizations
The output is a single figure containing a dashboard of four distinct plots, each providing a unique insight into the world's population in 2020.
(Note: You should replace this link with a link to your actual output image after you upload it somewhere like Imgur or directly to your GitHub repo).
1. Top 10 Most Populous Countries (Horizontal Bar Chart)
This chart clearly displays the 10 countries with the highest populations in 2020.
A horizontal layout is used for better readability of country names.
Data labels (e.g., "1.4B") are added to each bar for precise and immediate understanding.
2. Distribution of Country Populations (Histogram)
This histogram shows the frequency distribution of country populations.
It highlights that the data is heavily right-skewed, with a vast majority of countries having smaller populations.
Vertical lines for the mean and median are included, visually demonstrating the skewness (mean is significantly larger than the median).
3. Population Trends (Line Chart)
This plot visualizes the population growth from 2000 to 2020 for the top 5 most populous countries.
It adds a time-series dimension to the analysis, showing the consistent upward trend in population for these nations.
4. Countries by Population Range (Bar Chart)
This chart groups countries into logical population brackets (e.g., "<1M", "1M-10M", "10M-50M").
It provides a simplified and clear summary of the population distribution, showing that the largest number of countries (89) fall within the 1-10 million population range.
Key Insights
Extreme Skewness: The global population is not evenly distributed. A few countries (China, India) account for a massive portion of the world's population, while the vast majority of countries have relatively small populations. This is confirmed by the mean population (35.8 million) being much higher than the median (5.6 million).
Dominance of Asia: The top of the population list is dominated by Asian countries.
Most Common Size: The most frequent population size for a country is between 1 and 10 million people.
Consistent Growth: The world's largest countries have continued to experience steady population growth over the last two decades.
