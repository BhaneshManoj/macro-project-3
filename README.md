# Macro-project-3: Business Fluctuations and Firm-Level Responses to Economic Crises

## Project Overview
This project analyzes business fluctuations and firm-level responses to economic crises, focusing on macroeconomic trends and microeconomic outcomes. The study is structured into three main parts:

   Cross-Country Business Cycle Analysis
   
   Event Study – The Global Financial Crisis & COVID-19 Recession (U.S.)
   
   Firm-Level Responses Using WRDS Compustat Data
   
The project combines macroeconomic trend analysis with firm-level data evaluation to understand the effects of economic downturns and how different economies and firms responded.

## Project Structure
### Part 1: Cross-Country Business Cycle Analysis

Overview
Analyzes business cycle dynamics in the United States, Switzerland, and Japan from 2000 to 2024. Focuses on the cyclical relationships between output, labor, markets, and commodities. Utilizes data from FRED and applies the Hodrick-Prescott filter to decompose macroeconomic trends from short-term fluctuations. The analysis highlights procyclicality, volatility, and correlation patterns in manufacturing output, labor force participation, equity markets, and energy prices across the three countries.

### Part 2: Event Study – The Global Financial Crisis & COVID-19 Recession (U.S.)

Overview
The analysis uses historical data from FRED and Yahoo Finance to track Real GDP Growth, Unemployment Rates, and the S&P 500 Index before, during, and after each recession. The study describes the severity, duration, and recovery speed of both recessions. It incorporates references from prior research and macroeconomic reasoning to explain observed patterns. Policy responses—both fiscal and monetary—are documented, including the American Recovery and Reinvestment Act (ARRA) during the GFC and over $5 trillion in fiscal stimulus during COVID-19. 

### Part 3: Firm-Level Responses Using WRDS Compustat Data

Overview
Examines the responses of Apple, General Electric (GE), Ford, and Walmart to the Global Financial Crisis (2007–2009) using quarterly financial data from 2004 to 2012 (WRDS Compustat). The analysis focuses on Revenue Growth, Capital Expenditure (Capex), and Debt-to-Equity Ratios. It highlights sectoral differences in how firms managed demand shocks, investment decisions, and financial leverage, with insights into their resilience and recovery paths post-crisis.

## Data Sources
### Macroeconomic Data
   Real GDP Growth (%), Unemployment Rate (%) (2000–2024)

#### Source
   Federal Reserve Economic Data (FRED)

### Financial Market Data
   S&P 500 Index (converted to percentage changes) (2000–2024)

#### Source
	Yahoo Finance (^GSPC)

 ### Firm-Level Financial Data
    Revenue, Capex, Debt-to-Equity Ratio for selected firms (2004–2012)

#### Source
   WRDS Compustat Database

## File Descriptions



## How to Reproduce the Analyses

### General Requirements:
RStudio / R  for part 1 and 2 

Packages: ggplot2, dplyr, zoo, readxl

Python for part 3

### Part 1: Cross-Country Business Cycle Analysis
Upload 'Rscript Part1 Project3.txt'

### Part 2: Event Study – GFC & COVID-19 (U.S.)
Open 'Part2_event_study_GFC_COVID.R'

Run scripts to process U.S. macroeconomic data from FRED and Yahoo Finance

Analyze GFC and Covid-19 

Generate plot of GDP Growth, Unemployment, and S&P 500 trends

### Part 3: Firm-Level Responses
Open 'final_firmlevelresponse.py'

Analyze firm-level financial metrics for Apple, GE, Ford, and Walmart

Generate plots of revenue growth, Capex trends, and debt-equity ratios

## Key Findings

### Part 1
Labor force participation is pro-cyclical in the U.S. but appears acyclical in Switzerland and Japan. Commodity prices show pro-cyclicality with manufacturing output but vary in volatility across countries.

### Part 2
The GFC was a prolonged recession (18 months) with a slow recovery, driven by financial market failures and credit contraction. The COVID-19 recession was abrupt but short-lived (2 months), followed by a faster recovery, supported by aggressive fiscal and monetary responses.

### Part 3
Firm responses varied by sector: Apple and Walmart showed resilience, while GE and Ford faced significant challenges. Investment decisions and leverage ratios reflected different levels of financial stress and strategic priorities across industries.

##  References
Bernanke, B. S., Gertler, M., & Gilchrist, S. (1999). The Financial Accelerator in a Quantitative Business Cycle Framework.

Committee for a Responsible Federal Budget. (2022). COVID Money Tracker.

Congressional Budget Office. (2015, 2022). Economic Outlook and ARRA Reports.

Federal Reserve. (2011, 2021). Monetary Policy Reports.

Furman, J., & Powell, W. (2021). US Economic Policy Response to COVID-19.

IMF. (2009). World Economic Outlook: Crisis and Recovery.

National Bureau of Economic Research (NBER). US Business Cycle Dating Announcements.

Bureau of Economic Analysis (BEA), Bureau of Labor Statistics (BLS), OECD

##  Notes
This project adheres to the guidelines and page limits outlined in the ECON 8020 Macroeconomics Project 3 Assignment.
