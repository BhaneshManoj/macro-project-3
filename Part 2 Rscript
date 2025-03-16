rm(list=ls())

df = read.csv("Part2.csv")

colnames(df) <- c("Date", "GDP_growth", "Unemployment", "SP500")

df$Date <- as.Date(df$Date, format = "%d/%m/%Y") 

write.csv(df, "cleaned_data.csv", row.names = FALSE)

#load the libraries
library(ggplot2)
library(dplyr)
library(zoo)

# GFC Data (2004–2014)
df_gfc <- df %>% filter(Date >= as.Date("2004-01-01") & Date <= as.Date("2014-12-31"))

# Define recession period as a data frame
recession_period <- data.frame(
  start = as.Date("2007-12-01"),
  end = as.Date("2009-06-30"))

# COVID-19 Data (2014–2024)
df_covid <- df %>% filter(Date >= "2015-01-01" & Date <= "2024-12-31")

# Define the COVID-19 recession period (official NBER period)
recession_covid <- data.frame(
  start = as.Date("2020-02-01"),
  end = as.Date("2020-04-30"))

# Graph for GFC (2004–2014)
ggplot(df_gfc, aes(x = Date)) +
  geom_rect(data = recession_period,aes(xmin = start, xmax = end, ymin = -Inf, ymax = Inf),
            fill = "gray", alpha = 0.3, inherit.aes = FALSE) +
  geom_line(aes(y = GDP_growth, color = "Real GDP Growth (%)")) +
  geom_line(aes(y = Unemployment, color = "Unemployment Rate (%)")) +
  geom_line(aes(y = SP500, color = "S&P 500 (%)")) + 
  geom_hline(yintercept = 0, color = "black", size = 0.5)+
  scale_x_date(date_breaks = "2 year",date_labels = "%Y") +
  labs(title = "Figure 2.1: Global Financial Crisis (2007–2009)", y = "Percentage Change (%)", color = "Macroeconomic Indicators") +
  theme_minimal()

# Graph for COVID-19 (2014–2024)
ggplot(df_covid, aes(x = Date)) + 
  geom_rect(data = recession_covid, aes(xmin = start, xmax = end, ymin = -Inf, ymax = Inf),
            fill = "gray", alpha = 0.3, inherit.aes = FALSE) +
  geom_line(aes(y = GDP_growth, color = "Real GDP Growth (%)")) +
  geom_line(aes(y = Unemployment, color = "Unemployment Rate (%)")) +
  geom_line(aes(y = SP500, color = "S&P 500 (%)")) +
  geom_hline(yintercept = 0, color = "black", size = 0.5)+
  scale_x_date(date_breaks = "2 year",date_labels = "%Y") +
  labs(title = "Figure 2.2: COVID-19 Pandemic (2019-2021)", y = "Percentage Change (%)", color = "Macroeconomic Indicators") +
  theme_minimal()
