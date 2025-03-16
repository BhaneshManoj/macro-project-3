#Part 2 
df = read.csv("Part2.csv")

colnames(df) <- c("Date", "GDP_growth", "Unemployment", "SP500")

df$Date <- as.Date(df$Date, format = "%d/%m/%Y") # Ensure it's in Date format

write.csv(df, "cleaned_data.csv", row.names = FALSE)

library(ggplot2)
library(dplyr)
library(zoo)


# GFC Data (2004–2014)
df_gfc <- df %>% filter(Date >= as.Date("2004-01-01") & Date <= as.Date("2014-12-31"))


# COVID-19 Data (2014–2024)
df_covid <- df %>% filter(Date >= "2015-01-01" & Date <= "2024-12-31")

# Graph for GFC (2004–2014)
ggplot(df_gfc, aes(x = Date)) +
  geom_line(aes(y = GDP_growth, color = "Real GDP Growth (percent)")) +
  geom_line(aes(y = Unemployment, color = "Unemployment Rate")) +
  geom_line(aes(y = SP500, color = "S&P 500 Index")) +
  geom_line(aes(y = SP500, color = "S&P 500 Index")) + 
  geom_hline(yintercept = 0, color = "black", size = 0.5)+
  scale_x_date(date_breaks = "2 year",date_labels = "%Y") +
  labs(title = "Figure 2.1: Global Financial Crisis (2007–2009)", y = "Value", color = "Indicator") +
  theme_minimal()

# Graph for COVID-19 (2014–2024)
ggplot(df_covid, aes(x = Date)) +
  geom_line(aes(y = GDP_growth, color = "Real GDP Growth (percent)")) +
  geom_line(aes(y = Unemployment, color = "Unemployment Rate")) +
  geom_line(aes(y = SP500, color = "S&P 500 Index")) +
  geom_hline(yintercept = 0, color = "black", size = 0.5)+
  scale_x_date(date_breaks = "2 year",date_labels = "%Y") +
  labs(title = "Figure 2.2: COVID-19 Pandemic (2019-2021)", y = "Value", color = "Indicator") +
  theme_minimal()

# Part Three

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("compdatafinancial.csv")

# Convert date column to datetime and sort by company and date
df['datadate'] = pd.to_datetime(df['datadate'], format='%m/%d/%y')
df = df.sort_values(by=['tic', 'datadate'])

# Convert necessary columns to numeric format to avoid type issues
numeric_cols = ['TotRev', 'TotAssets', 'TotLiab', 'TotalEq', 'Capex']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')  # Convert non-numeric values to NaN

# Handle missing and extreme values
df[numeric_cols] = df[numeric_cols].replace([np.inf, -np.inf], np.nan)  # Remove infinite values
df[numeric_cols] = df[numeric_cols].fillna(0)  # Replace NaN with 0 for visualization

# Calculate revenue growth
df['revgrwth'] = df.groupby('tic')['TotRev'].pct_change() * 100  # Revenue growth as a percentage
df['revgrwth'] = df['revgrwth'].fillna(0)  # Fill NaN values for the first period with 0

# Calculate Debt-to-Equity ratio
df['DebttoEq'] = df['TotLiab'] / df['TotalEq']
df['DebttoEq'] = df['DebttoEq'].replace([np.inf, -np.inf], np.nan)  # Remove infinite values from DebttoEq

# Clean extreme debt-to-equity values
# Remove rows where DebttoEq is less than or equal to 0 (negative or zero debt-to-equity is not valid)
df = df[df['DebttoEq'] > 0]

# Optionally, you can replace extreme outliers with the median or a reasonable threshold
# For example, we can replace any DebttoEq values greater than 100 with the median DebttoEq
debt_to_eq_median = df['DebttoEq'].median()
df['DebttoEq'] = np.where(df['DebttoEq'] > 100, debt_to_eq_median, df['DebttoEq'])

# Calculate Capex Ratio
df['CapexRatio'] = df['Capex'] / df['TotRev']

# Apply log transformation safely (avoiding log of negative numbers)
df['revgrwth_log'] = np.log1p(df['revgrwth'].clip(lower=0))  # Ensure values are non-negative
df['DebttoEq_log'] = np.log1p(df['DebttoEq'].clip(lower=0))
df['CapexRatio_log'] = np.log1p(df['CapexRatio'].clip(lower=0))

# Smooth trends using a rolling average (4-quarter moving average)
df['revgrwth_smooth'] = df.groupby('tic')['revgrwth'].transform(lambda x: x.rolling(4, min_periods=1).mean())
df['DebttoEq_smooth'] = df.groupby('tic')['DebttoEq'].transform(lambda x: x.rolling(4, min_periods=1).mean())
df['CapexRatio_smooth'] = df.groupby('tic')['CapexRatio'].transform(lambda x: x.rolling(4, min_periods=1).mean())

# Normalize Debt-to-Equity ratio to make comparison easier
df['DebttoEq_norm'] = df.groupby('tic')['DebttoEq_smooth'].transform(lambda x: x / x.max())

# Get unique ticker symbols
unique_tickers = df['tic'].unique()

# Create a single plot for Revenue Growth
plt.figure(figsize=(12, 6))
for tic in unique_tickers:
    subset = df[df['tic'] == tic]
    plt.plot(subset['datadate'], subset['revgrwth_smooth'], marker='o', linestyle='-', label=f"Revenue Growth - {tic}")

plt.title("Revenue Growth Trend for All Companies")
plt.xlabel("Year")
plt.ylabel("Revenue Growth (%)")
plt.legend()
plt.grid(True)

# Mark Global Financial Crisis (GFC) Period (2007-2009)
plt.axvspan('2007-01-01', '2009-12-31', color='gray', alpha=0.3, label="GFC Period (2007-2009)")
plt.legend(loc='best')

plt.tight_layout()
plt.show()

# Create a single plot for Debt-to-Equity ratio (Normalized)
plt.figure(figsize=(12, 6))
for tic in unique_tickers:
    subset = df[df['tic'] == tic]
    plt.plot(subset['datadate'], subset['DebttoEq_norm'], marker='s', linestyle='-', label=f"Debt-to-Equity - {tic}")

plt.title("Debt-to-Equity Trend for All Companies (Normalized)")
plt.xlabel("Year")
plt.ylabel("Normalized Debt-to-Equity Ratio")
plt.legend()
plt.grid(True)

# Mark Global Financial Crisis (GFC) Period (2007-2009)
plt.axvspan('2007-01-01', '2009-12-31', color='gray', alpha=0.3, label="GFC Period (2007-2009)")
plt.legend(loc='best')

plt.tight_layout()
plt.show()

# Create a single plot for Capex Ratio
plt.figure(figsize=(12, 6))
for tic in unique_tickers:
    subset = df[df['tic'] == tic]
    plt.plot(subset['datadate'], subset['CapexRatio_smooth'], marker='^', linestyle='-', label=f"Capex Ratio - {tic}")

plt.title("Capex Ratio Trend for All Companies")
plt.xlabel("Year")
plt.ylabel("Capex Ratio")
plt.legend()
plt.grid(True)

# Mark Global Financial Crisis (GFC) Period (2007-2009)
plt.axvspan('2007-01-01', '2009-12-31', color='gray', alpha=0.3, label="GFC Period (2007-2009)")
plt.legend(loc='best')

plt.tight_layout()
plt.show()
