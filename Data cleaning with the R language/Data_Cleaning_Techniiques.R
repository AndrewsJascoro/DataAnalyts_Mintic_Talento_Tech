# Here are examples of code in R for performing various data cleaning techniques:
library(dplyr)  # For handling missing values.
library(ggplot2)  # For creating plots.

#   1.  Handling Missing Values:
#       Removing rows with missing values.
#   Assuming 'df' is your dataset, Remove rows with missing values.
df <- na.omit(df)

# Imputing missing values with mean:
# Assuming 'df$column' is the column with missing values, 
# Impute missing values with mean
mean_value <- mean(df$column, na.rm = TRUE)
df$column[is.na(df$column)] <- mean_value

# Handling Outliers:
# Identifying outliers with the IQR method:
# Assuming 'df$column' is the column with outliers
# Calculate Interquartile Range (IQR)
Q1 <- quantile(df$column, 0.25)
Q3 <- quantile(df$column, 0.75)
IQR <- Q3 - Q1

# Identify outliers
outliers <- df$column < (Q1 - 1.5 * IQR) | df$column > (Q3 + 1.5 * IQR)

# Data Transformation:
# Creating new variables:
# Assuming you want to create a new variable 'new_variable'
# from other variables in 'df'
df$new_variable <- df$variable1 + df$variable2

# Handling Duplicate Data:
# Identifying duplicate rows:
# Assuming 'df' is your dataset
# Identify duplicate rows
duplicated_rows <- df[duplicated(df), ]

# Removing duplicate rows:
# Assuming 'df' is your dataset
# Remove duplicate rows
df <- unique(df)

