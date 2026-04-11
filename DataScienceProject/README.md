# Data Science Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a historical insurance claims dataset for AlphaCare Insurance Solutions (ACIS). The aim of this analysis is to help optimize the marketing strategy and identify "low-risk" targets where premiums can be reduced to attract new clients.

## Dataset

The dataset used in this analysis contains historical insurance claim data for car insurance policies. Below is a summary of key columns in the dataset:

- **UnderwrittenCoverID**: Unique identifier for the insurance coverage
- **PolicyID**: Unique identifier for the insurance policy
- **TransactionMonth**: Date of the transaction (policy start date)
- **IsVATRegistered**: Whether the policyholder is VAT registered
- **Citizenship**: Citizenship status of the policyholder
- **LegalType**: The legal type of the policyholder
- **Gender**: Gender of the policyholder
- **Country**: Country of residence for the policyholder
- **PostalCode**: Postal code (Zip code) for the policyholder's address
- **TotalPremium**: The total premium paid by the policyholder
- **TotalClaims**: The total claims made by the policyholder

The dataset includes both numerical and categorical features, and the analysis includes methods to explore the relationships between variables and trends over time and geography.

## Project Structure

```
DataScienceProject/
├── data/              # Dataset files
├── notebooks/         # Jupyter notebooks for analysis
├── src/              # Python source code
├── outputs/          # Generated plots and reports
└── README.md         # This file
```

## Getting Started

1. Place your dataset in the `data/` folder
2. Install required dependencies: `pip install -r requirements.txt`
3. Run the EDA notebook in `notebooks/eda_analysis.ipynb`
