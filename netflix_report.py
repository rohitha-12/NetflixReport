import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Data Cleaning
df = df.dropna(subset=['date_added', 'rating', 'country'])
df['date_added'] = df['date_added'].str.strip()  # Remove leading/trailing spaces
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')  # Convert to datetime
df['year_added'] = df['date_added'].dt.year

# Plot 1: Distribution of Content Types (Movies vs TV Shows)
content_type_count = df['type'].value_counts()
plt.figure(figsize=(8, 5))
sns.barplot(x=content_type_count.index, y=content_type_count.values, palette='Blues_d')
plt.title('Distribution of Content Types on Netflix')
plt.xlabel('Content Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('plot1_content_type.png')
plt.show()

# Plot 2: Number of Titles Added Over the Years
titles_per_year = df.groupby('year_added').size()
plt.figure(figsize=(10, 6))
sns.lineplot(x=titles_per_year.index, y=titles_per_year.values, marker='o', color='red')
plt.title('Number of Titles Added to Netflix Over the Years')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig('plot2_titles_per_year.png')
plt.show()

# Plot 3: Top 10 Countries with Most Titles
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries with Most Titles on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('plot3_top_countries.png')
plt.show()
