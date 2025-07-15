import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)

# Filter out aggregate rows
def is_actual_country(country_name):
    if pd.isna(country_name):
        return False
    name_lower = str(country_name).lower()
    exclude_patterns = [
        'world', 'income', 'dividend', 'ida', 'ibrd', 'oecd', 'euro area',
        'european union', 'arab world', 'east asia', 'south asia', 'latin america',
        'middle east', 'north america', 'sub-saharan', 'caribbean', 'pacific',
        'central europe', 'fragile', 'least developed', 'small states', 'blend',
        'members', 'situations', 'heavily indebted', 'post-demographic',
        'pre-demographic', 'late-demographic', 'early-demographic', 'other small'
    ]
    for pattern in exclude_patterns:
        if pattern in name_lower:
            return False
    if ':' in country_name or len(country_name.strip()) < 3:
        return False
    return True

df_countries = df[df['Country Name'].apply(is_actual_country)]

# Prepare data
df_subset = df_countries[['Country Name', '2020']].dropna()
df_sorted = df_subset.sort_values(by='2020', ascending=False).head(10)

# Create subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
fig.subplots_adjust(hspace=0.4, wspace=0.3)

# --- 1. Horizontal Bar Chart ---
y_pos = np.arange(len(df_sorted))
bars = ax1.barh(y_pos, df_sorted['2020'], color='teal', alpha=0.8, edgecolor='black')
ax1.set_yticks(y_pos)
ax1.set_yticklabels(df_sorted['Country Name'], fontsize=11)
ax1.invert_yaxis()
ax1.set_title("Top 10 Most Populous Countries (2020)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Population", fontsize=12, labelpad=15)
ax1.grid(axis='x', alpha=0.3)

for i, (bar, pop) in enumerate(zip(bars, df_sorted['2020'])):
    ax1.text(pop + pop*0.02, i, f'{pop/1e9:.1f}B', va='center', fontsize=10)

# --- 2. Histogram ---
populations = df_countries['2020'].dropna()
ax2.hist(populations, bins=40, color='skyblue', edgecolor='black', alpha=0.7)
ax2.set_title("Distribution of Country Populations (2020)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Population", fontsize=12, labelpad=10)
ax2.set_ylabel("Number of Countries", fontsize=12)
ax2.grid(axis='y', alpha=0.3)

mean_pop = populations.mean()
median_pop = populations.median()
ax2.axvline(mean_pop, color='red', linestyle='--', alpha=0.7, label=f'Mean: {mean_pop/1e6:.1f}M')
ax2.axvline(median_pop, color='orange', linestyle='--', alpha=0.7, label=f'Median: {median_pop/1e6:.1f}M')
ax2.legend()

# --- 3. Population Trends ---
years = [col for col in df.columns if col.isdigit() and int(col) >= 2000]
if len(years) > 1:
    top_5_countries = df_sorted.head(5)['Country Name'].tolist()
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

    for i, country in enumerate(top_5_countries):
        country_data = df_countries[df_countries['Country Name'] == country]
        if not country_data.empty:
            country_values = country_data[years].values.flatten()
            valid_indices = ~np.isnan(country_values)
            valid_years = np.array([int(y) for y in years])[valid_indices]
            valid_values = country_values[valid_indices]
            if len(valid_values) > 1:
                ax3.plot(valid_years, valid_values/1e9, marker='o',
                         label=country, linewidth=2.5, markersize=4,
                         color=colors[i])
    ax3.set_title("Population Trends (Top 5 Countries)", fontsize=14, fontweight='bold')
    ax3.set_xlabel("Year", fontsize=12)
    ax3.set_ylabel("Population (Billions)", fontsize=12)
    ax3.legend(loc='upper left', fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim(bottom=0)
else:
    ax3.text(0.5, 0.5, 'Time series data not available',
             ha='center', va='center', transform=ax3.transAxes, fontsize=12)

# --- 4. Population Ranges ---
pop_ranges = pd.cut(populations, bins=[0, 1e6, 10e6, 50e6, 100e6, 500e6, 1.5e9],
                    labels=['<1M', '1M-10M', '10M-50M', '50M-100M', '100M-500M', '500M+'])
range_counts = pop_ranges.value_counts().sort_index()

bars = ax4.bar(range_counts.index, range_counts.values, color='lightcoral', alpha=0.8, edgecolor='black')
ax4.set_title("Countries by Population Range (2020)", fontsize=14, fontweight='bold')
ax4.set_xlabel("Population Range", fontsize=12, labelpad=10)
ax4.set_ylabel("Number of Countries", fontsize=12)
ax4.grid(axis='y', alpha=0.3)

for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             int(height), ha='center', va='bottom', fontsize=10)

# Final layout adjustment
plt.tight_layout(pad=3.0)
plt.show()

# --- Summary Statistics ---
print(f"\n=== Summary Statistics ===")
print(f"Countries analyzed: {len(populations)}")
print(f"Most populous: {df_sorted.iloc[0]['Country Name']} ({df_sorted.iloc[0]['2020']/1e9:.2f}B)")
print(f"Least populous: {df_subset.sort_values('2020').iloc[0]['Country Name']} "
      f"({df_subset.sort_values('2020').iloc[0]['2020']:,.0f})")
print(f"Mean population: {populations.mean()/1e6:.1f} million")
print(f"Median population: {populations.median()/1e6:.1f} million")
