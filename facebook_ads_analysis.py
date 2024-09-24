import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from a CSV file
df = pd.read_csv('facebook_ads_data (2.0).csv')

# Display the first few rows of the dataframe
df.head()

# Filter the data for the year 2021
df_2021 = df[df['ad_date'].str.startswith('2021')]

# Group the data by date and calculate total spend and average ROMI
group_spend = df_2021.groupby('ad_date')['total_spend'].sum()
group_romi = df_2021.groupby('ad_date')['romi'].mean()

# Set up the figure size for the first set of plots
plt.figure(figsize=(14, 6))

# Plot total ad spend by date
plt.subplot(1, 2, 1)
group_spend.plot(kind='line', color='lightgreen')
plt.title('Daily Ad Spend in 2021')
plt.ylabel('Total Spend ($)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

# Plot ROMI and its 7-day rolling average
plt.subplot(1, 2, 2)
group_romi.plot(kind='line', color='skyblue', label='ROMI')
group_romi.rolling(window=7).mean().plot(kind='line', color='red', linestyle='--', label='Rolling ROMI (7-day)')
plt.title('Daily ROMI in 2021')
plt.ylabel('ROMI')
plt.legend()
plt.xticks(rotation=45)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

# Group the data by campaign name to calculate total spend and average ROMI
campaign_spend = df.groupby('campaign_name')['total_spend'].sum()
campaign_romi = df.groupby('campaign_name')['romi'].mean()

# Set up the figure size for the second set of plots
plt.figure(figsize=(14, 6))

# Plot total ad spend by campaign
plt.subplot(1, 2, 1)
campaign_spend.plot(kind='bar', color='skyblue')
plt.title('Total Ad Spend by Campaign')
plt.xlabel('Campaign')
plt.ylabel('Total Spend ($)')
plt.xticks(rotation=45)

# Plot average ROMI by campaign
plt.subplot(1, 2, 2)
campaign_romi.plot(kind='bar', color='lightgreen')
plt.title('Total ROMI by Campaign')
plt.xlabel('Campaign')
plt.ylabel('ROMI')
plt.xticks(rotation=45)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()

# Boxplot to show daily ROMI distribution by campaign
plt.figure(figsize=(14, 6))
sns.boxplot(x='campaign_name', y='romi', data=df, hue='campaign_name', palette='Set3')
plt.title('Daily ROMI by Campaign')
plt.xlabel('Campaign')
plt.ylabel('ROMI')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()

# Histogram of ROMI
plt.figure(figsize=(14, 6))
plt.hist(df['romi'], edgecolor='black')
plt.title('ROMI')
plt.xlabel('ROMI')
plt.ylabel('Frequency')
plt.grid(True)  # Add grid for better readability
plt.show()

# Calculate correlation matrix for total_spend and other numerical columns
cor_df = df.loc[:, 'total_spend':].corr()

# Heatmap to visualize correlation between variables
fig, ax = plt.subplots(1, 1, figsize=(18, 8))
sns.heatmap(cor_df, annot=True, fmt='1.1%', cmap='crest_r', ax=ax, linewidths=.5, center=0)
plt.title('Correlation Heatmap')
plt.show()

# Scatter plot with linear regression line for total spend vs. total value
sns.lmplot(x='total_spend', y='total_value', data=df, height=8)
plt.title('Total Spend vs Total Value')
plt.xlabel('Total Spend')
plt.ylabel('Total Value')
plt.show()