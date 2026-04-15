# Credit Scoring Dataset - Data Dictionary

## Overview
This document provides comprehensive descriptions of all variables in the credit scoring dataset, including data types, value ranges, business definitions, and data quality notes.

**Dataset Name**: Credit Scoring Training Dataset  
**File**: `cs-training.csv`  
**Records**: 150,000 borrowers  
**Features**: 11 (10 predictors + 1 target)  
**Last Updated**: April 2026

---

## Target Variable

### SeriousDlqin2yrs
**Description**: Binary indicator of whether the borrower experienced serious delinquency (90+ days past due) or worse within the next two years.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer (Binary) |
| **Values** | 0 = No default, 1 = Default |
| **Business Definition** | A borrower is considered in default if they were 90 or more days past due on any credit obligation within the 2-year observation window |
| **Missing Values** | 0 (0%) |
| **Distribution** | Class 0: ~93%, Class 1: ~7% |
| **Business Importance** | PRIMARY - This is the outcome we aim to predict |
| **Data Quality** | ✓ No issues |

**Usage Notes**:
- This is the dependent variable for model training
- Significant class imbalance requires special handling (SMOTE, class weights)
- Consider cost-sensitive learning due to asymmetric misclassification costs

---

## Predictor Variables

### 1. RevolvingUtilizationOfUnsecuredLines
**Description**: Total balance on unsecured credit lines (credit cards, personal lines) divided by the sum of credit limits.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Float |
| **Value Range** | 0 to >1 (values >1 indicate over-utilization) |
| **Business Definition** | Credit utilization ratio = (Total Balance) / (Total Credit Limit) |
| **Missing Values** | 0 (0%) |
| **Mean** | ~0.35 |
| **Median** | ~0.15 |
| **Business Importance** | HIGH - Strong predictor of default risk |
| **Data Quality** | ⚠️ Contains outliers (values >1 indicate maxed out credit) |

**Interpretation**:
- **0-0.30**: Low utilization (good credit management)
- **0.30-0.70**: Moderate utilization (acceptable)
- **0.70-1.00**: High utilization (warning sign)
- **>1.00**: Over-utilization (maxed out, very high risk)

**Usage Notes**:
- Values >1 are valid and indicate borrower has exceeded credit limits
- Consider binning into categories for interpretability
- Strong candidate for feature engineering (e.g., binary flag for >1)

---

### 2. age
**Description**: Age of the borrower in years at the time of data collection.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 18 to 109 years |
| **Business Definition** | Chronological age of the borrower |
| **Missing Values** | 0 (0%) |
| **Mean** | ~52 years |
| **Median** | ~52 years |
| **Business Importance** | MEDIUM - Age correlates with financial stability |
| **Data Quality** | ⚠️ Some extreme values (>100) may be data errors |

**Interpretation**:
- **18-30**: Young borrowers (higher risk, less credit history)
- **31-50**: Prime borrowers (stable income, established credit)
- **51-65**: Mature borrowers (lower risk, approaching retirement)
- **65+**: Senior borrowers (fixed income considerations)

**Usage Notes**:
- Consider age groups for non-linear relationships
- Interaction with income may be informative
- Verify extreme ages (>100) for data quality

---

### 3. NumberOfTime30-59DaysPastDueNotWorse
**Description**: Number of times the borrower was 30-59 days past due (but not worse) in the last 2 years.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 0 to 98 |
| **Business Definition** | Count of billing cycles where payment was 30-59 days late |
| **Missing Values** | 0 (0%) |
| **Mean** | ~0.42 |
| **Median** | 0 |
| **Business Importance** | HIGH - Direct indicator of payment behavior |
| **Data Quality** | ⚠️ Extreme values (>10) may indicate data quality issues |

**Interpretation**:
- **0**: No late payments (excellent payment history)
- **1-2**: Occasional late payments (acceptable)
- **3-5**: Frequent late payments (warning sign)
- **>5**: Chronic payment issues (high risk)

**Usage Notes**:
- Highly predictive of default
- Consider capping extreme values
- Combine with other delinquency features for aggregate score

---

### 4. DebtRatio
**Description**: Monthly debt payments (including mortgage, credit cards, loans) divided by monthly gross income.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Float |
| **Value Range** | 0 to >1 (values >1 indicate debt exceeds income) |
| **Business Definition** | Debt-to-Income Ratio = (Monthly Debt Payments) / (Monthly Gross Income) |
| **Missing Values** | 0 (0%) |
| **Mean** | ~353 (likely data quality issue) |
| **Median** | ~0.37 |
| **Business Importance** | HIGH - Key measure of financial burden |
| **Data Quality** | ⚠️ Contains extreme outliers (>1000) |

**Interpretation**:
- **<0.36**: Manageable debt (lender comfort zone)
- **0.36-0.43**: Moderate debt (acceptable for most lenders)
- **0.43-0.50**: High debt (borderline)
- **>0.50**: Excessive debt (high risk)

**Usage Notes**:
- Extreme outliers require treatment (winsorization, capping)
- Consider log transformation due to skewness
- Industry standard threshold is 43% for mortgage lending

---

### 5. MonthlyIncome
**Description**: Monthly gross income of the borrower in local currency.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Float |
| **Value Range** | 0 to ~3,000,000 |
| **Business Definition** | Total monthly gross income before taxes and deductions |
| **Missing Values** | ~29,731 (~20%) |
| **Mean** | ~6,670 |
| **Median** | ~5,400 |
| **Business Importance** | HIGH - Fundamental measure of repayment capacity |
| **Data Quality** | ⚠️ Significant missing values, extreme outliers |

**Interpretation**:
- **<3,000**: Low income (higher risk)
- **3,000-7,000**: Middle income (moderate risk)
- **7,000-15,000**: Upper-middle income (lower risk)
- **>15,000**: High income (lowest risk)

**Usage Notes**:
- **CRITICAL**: 20% missing values require imputation strategy
- Consider median imputation by age group or occupation
- Extreme values may be legitimate (high earners) or errors
- Interaction with DebtRatio is highly informative

---

### 6. NumberOfOpenCreditLinesAndLoans
**Description**: Total number of open credit lines (credit cards, personal lines) and loans (auto, mortgage, student).

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 0 to 58 |
| **Business Definition** | Count of all active credit accounts |
| **Missing Values** | 0 (0%) |
| **Mean** | ~8.5 |
| **Median** | 8 |
| **Business Importance** | MEDIUM - Indicates credit access and management |
| **Data Quality** | ✓ Reasonable distribution |

**Interpretation**:
- **0-3**: Limited credit access (thin file)
- **4-10**: Normal credit portfolio (healthy)
- **11-20**: Extensive credit use (monitor)
- **>20**: Excessive credit accounts (potential risk)

**Usage Notes**:
- Non-linear relationship with default (both too few and too many can be risky)
- Consider quadratic term or binning
- Interaction with utilization may be informative

---

### 7. NumberOfTimes90DaysLate
**Description**: Number of times the borrower was 90 days or more past due in the last 2 years.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 0 to 98 |
| **Business Definition** | Count of billing cycles where payment was 90+ days late |
| **Missing Values** | 0 (0%) |
| **Mean** | ~0.27 |
| **Median** | 0 |
| **Business Importance** | VERY HIGH - Strongest predictor of future default |
| **Data Quality** | ⚠️ Extreme values (>10) may indicate chronic issues |

**Interpretation**:
- **0**: No serious delinquencies (excellent)
- **1**: One serious delinquency (major red flag)
- **2+**: Multiple serious delinquencies (very high risk)

**Usage Notes**:
- **CRITICAL**: Most predictive feature
- Even one occurrence significantly increases default risk
- Consider binary flag (any vs none) in addition to count
- May have data leakage concerns (closely related to target)

---

### 8. NumberRealEstateLoansOrLines
**Description**: Number of mortgage and real estate loans, including home equity lines of credit.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 0 to 54 |
| **Business Definition** | Count of all real estate-secured credit accounts |
| **Missing Values** | 0 (0%) |
| **Mean** | ~1.0 |
| **Median** | 1 |
| **Business Importance** | LOW-MEDIUM - Indicates asset ownership |
| **Data Quality** | ⚠️ Extreme values (>10) unusual |

**Interpretation**:
- **0**: No real estate loans (renter or owns outright)
- **1-2**: Primary residence and/or investment property (normal)
- **3-5**: Multiple properties (investor or wealthy)
- **>5**: Unusual, may indicate data quality issue

**Usage Notes**:
- Real estate ownership can be protective (asset backing)
- Extreme values may be errors or unique cases (real estate investors)
- Consider binary flag (any vs none)

---

### 9. NumberOfTime60-89DaysPastDueNotWorse
**Description**: Number of times the borrower was 60-89 days past due (but not worse) in the last 2 years.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 0 to 98 |
| **Business Definition** | Count of billing cycles where payment was 60-89 days late |
| **Missing Values** | 0 (0%) |
| **Mean** | ~0.24 |
| **Median** | 0 |
| **Business Importance** | HIGH - Serious payment behavior indicator |
| **Data Quality** | ⚠️ Extreme values (>10) may indicate issues |

**Interpretation**:
- **0**: No moderate delinquencies (good)
- **1-2**: Occasional serious late payments (concerning)
- **3+**: Frequent serious late payments (high risk)

**Usage Notes**:
- More serious than 30-59 day delinquencies
- Consider combining with other delinquency features
- Aggregate delinquency score may be more informative

---

### 10. NumberOfDependents
**Description**: Number of dependents in the borrower's household, excluding the borrower.

| Attribute | Details |
|-----------|---------|
| **Data Type** | Integer |
| **Value Range** | 0 to 20 |
| **Business Definition** | Count of financial dependents (children, elderly parents, etc.) |
| **Missing Values** | ~3,924 (~3%) |
| **Mean** | ~0.76 |
| **Median** | 0 |
| **Business Importance** | LOW-MEDIUM - Indicates financial obligations |
| **Data Quality** | ⚠️ Some missing values, extreme values (>10) unusual |

**Interpretation**:
- **0**: No dependents (single or dual-income household)
- **1-3**: Typical family size (normal)
- **4-6**: Large family (higher financial burden)
- **>6**: Very large family or data error

**Usage Notes**:
- Missing values (~3%) require imputation (mode = 0)
- Interaction with income may be informative (income per capita)
- Extreme values (>10) should be investigated

---

## Data Quality Summary

### Missing Values
| Feature | Missing Count | Missing % | Imputation Strategy |
|---------|---------------|-----------|---------------------|
| MonthlyIncome | 29,731 | 19.8% | Median by age group |
| NumberOfDependents | 3,924 | 2.6% | Mode (0) |
| All Others | 0 | 0% | N/A |

### Outliers
| Feature | Outlier % | Treatment Recommendation |
|---------|-----------|--------------------------|
| DebtRatio | 15% | Winsorization at 99th percentile |
| RevolvingUtilization | 8% | Cap at 2.0 (200% utilization) |
| MonthlyIncome | 5% | Log transformation |
| Delinquency Features | 3% | Cap at 10 occurrences |
| age | 1% | Investigate values >100 |

### Data Anomalies
1. **DebtRatio**: Some values >1000 (likely data entry errors)
2. **age**: Some values >100 (possible errors or centenarians)
3. **Delinquency counts**: Values >50 seem unrealistic for 2-year window
4. **NumberRealEstateLoans**: Values >10 unusual (investigate)

---

## Feature Engineering Recommendations

### Derived Features
1. **total_delinquency_score**: Weighted sum of all late payment features
   ```
   = 1×(30-59 days) + 2×(60-89 days) + 3×(90+ days)
   ```

2. **utilization_category**: Binned credit utilization
   - Low: 0-30%
   - Medium: 30-70%
   - High: 70-100%
   - Over: >100%

3. **age_group**: Age brackets
   - Young: 18-30
   - Prime: 31-50
   - Mature: 51-65
   - Senior: 65+

4. **income_per_capita**: MonthlyIncome / (NumberOfDependents + 1)

5. **debt_burden_index**: DebtRatio × (1 + total_delinquency_score)

6. **credit_experience**: NumberOfOpenCreditLinesAndLoans / age

### Transformation Recommendations
- **Log Transform**: MonthlyIncome, DebtRatio (after handling zeros)
- **Square Root**: Delinquency counts (reduce skewness)
- **Binning**: age, MonthlyIncome (for interpretability)
- **Standardization**: All numerical features (for distance-based models)

---

## Business Rules and Thresholds

### Industry Standards
- **Debt-to-Income Ratio**: <43% for qualified mortgages (US standard)
- **Credit Utilization**: <30% recommended for good credit health
- **Delinquency**: Any 90+ day late payment is severe negative

### Risk Categories (Proposed)
Based on model score, borrowers can be categorized:
- **Low Risk**: Score 0-0.10 (approve with standard terms)
- **Medium Risk**: Score 0.10-0.25 (approve with conditions)
- **High Risk**: Score 0.25-0.50 (manual review required)
- **Very High Risk**: Score >0.50 (decline or require collateral)

---

## Regulatory and Compliance Notes

### Fair Lending Considerations
- **Protected Attributes**: Age is included but must be used carefully to avoid discrimination
- **Disparate Impact**: Monitor model performance across demographic groups
- **Explainability**: Ensure model decisions can be explained to borrowers

### Data Privacy
- **Anonymization**: Dataset is anonymized (no PII)
- **Retention**: Follow data retention policies
- **Access Control**: Restrict access to authorized personnel only

### Audit Trail
- Document all data transformations
- Maintain version control for datasets
- Log all model predictions for review

---

## References

### Data Source
- Original dataset from credit scoring challenge
- Anonymized and aggregated for privacy protection

### Industry Standards
- FICO Credit Score methodology
- Basel III capital requirements
- Consumer Financial Protection Bureau (CFPB) guidelines

---

*Last Updated: April 15, 2026*  
*Version: 1.0*  
*Maintained by: Data Science Team*
