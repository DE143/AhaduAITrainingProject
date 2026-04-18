# 🚀 Quick Start Guide - Credit Scoring Project

**Get started with the Credit Scoring EDA in 5 minutes!**

---

## 📋 Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Basic understanding of data science and credit risk

---

## ⚡ Quick Setup (3 Steps)

### Step 1: Install Dependencies
```bash
cd DataScienceProject
pip install -r requirements.txt
```

### Step 2: Launch Jupyter
```bash
jupyter notebook
```

### Step 3: Open the EDA Notebook
Navigate to: `notebooks/eda_analysis.ipynb`

**That's it!** You're ready to run the analysis.

---

## 📚 Essential Reading (5 Minutes)

Before running the notebook, quickly review:

1. **README.md** (2 min) - Project overview and objectives
2. **DATA_DICTIONARY.md** (3 min) - Understand the 11 features

---

## 🎯 What You'll Get

Running the EDA notebook will provide:

✅ **Data Quality Report**
- Missing value analysis
- Outlier detection
- Data type validation

✅ **Target Variable Analysis**
- Class distribution (default vs non-default)
- Imbalance assessment

✅ **Feature Analysis**
- Distribution plots for all 11 features
- Statistical summaries
- Business interpretations

✅ **Risk Factor Identification**
- Feature-target relationships
- Statistical significance tests
- Predictive power (Information Value)

✅ **Correlation Analysis**
- Feature correlations
- Multicollinearity detection
- Target correlation ranking

✅ **Actionable Insights**
- Key risk factors
- Feature engineering recommendations
- Model development strategy

---

## 📊 Key Features in the Dataset

| Feature | What It Measures | Importance |
|---------|------------------|------------|
| **SeriousDlqin2yrs** | Default indicator (TARGET) | 🎯 Primary |
| **RevolvingUtilization** | Credit card usage | 🔴 High |
| **age** | Borrower age | 🟡 Medium |
| **30-59 Days Late** | Payment history | 🔴 High |
| **DebtRatio** | Debt burden | 🔴 High |
| **MonthlyIncome** | Income level | 🔴 High |
| **OpenCreditLines** | Credit access | 🟡 Medium |
| **90+ Days Late** | Serious delinquency | 🔴 Very High |
| **RealEstateLoans** | Property ownership | 🟢 Low |
| **60-89 Days Late** | Payment history | 🔴 High |
| **NumberOfDependents** | Family size | 🟢 Low |

---

## 🔧 Utility Functions Available

The `src/eda_utils.py` module provides:

```python
# Data Loading
load_data(filepath)

# Data Quality
basic_info(df)
data_quality_report(df)
detect_outliers(df, column, method='iqr')

# Visualization
plot_distribution(df, column, title, hue, bins)
plot_categorical(df, column, title, top_n)
plot_target_relationship(df, feature, target)

# Statistical Analysis
correlation_analysis(df, numerical_cols, method)
calculate_woe_iv(df, feature, target, bins)
statistical_test(df, feature, target)
```

---

## 📖 Documentation Structure

```
DataScienceProject/
├── 📄 QUICK_START.md              ← You are here!
├── 📄 README.md                   ← Project overview
├── 📄 PROJECT_DOCUMENTATION.md    ← Complete technical guide
├── 📄 DATA_DICTIONARY.md          ← Feature reference
├── 📄 CODE_REVIEW_SUMMARY.md      ← Review details
└── 📄 REVIEW_COMPLETE.md          ← Summary of improvements
```

**Reading Order**:
1. ✅ QUICK_START.md (this file) - 5 min
2. ✅ README.md - 10 min
3. ✅ DATA_DICTIONARY.md - 15 min
4. ⏭️ Run notebooks/eda_analysis.ipynb - 30 min
5. ⏭️ PROJECT_DOCUMENTATION.md - 30 min (for deep dive)

---

## 🎓 Learning Path

### Beginner (New to Credit Scoring)
1. Read README.md for business context
2. Review DATA_DICTIONARY.md to understand features
3. Run the notebook cell-by-cell
4. Focus on visualizations and interpretations

### Intermediate (Familiar with Data Science)
1. Skim README.md and DATA_DICTIONARY.md
2. Run the entire notebook
3. Review statistical tests and WoE/IV analysis
4. Explore feature engineering recommendations

### Advanced (Credit Risk Expert)
1. Jump straight to the notebook
2. Focus on Information Value and statistical tests
3. Review PROJECT_DOCUMENTATION.md for methodology
4. Plan feature engineering and model development

---

## 💡 Pro Tips

### Tip 1: Start Small
Run the notebook section by section. Don't execute all cells at once on first run.

### Tip 2: Customize Analysis
Modify the utility functions in `src/eda_utils.py` for your specific needs.

### Tip 3: Document Findings
Add markdown cells in the notebook to document your insights as you go.

### Tip 4: Save Outputs
Plots and reports will be saved to `outputs/` directory automatically.

### Tip 5: Version Control
Commit your changes regularly to track your analysis progress.

---

## 🐛 Troubleshooting

### Issue: Missing Dependencies
**Solution**: 
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Jupyter Not Found
**Solution**:
```bash
pip install jupyter
```

### Issue: Data File Not Found
**Solution**: Ensure `data/cs-training.csv` exists in the correct location.

### Issue: Import Errors
**Solution**: Check that you're running Jupyter from the `DataScienceProject` directory.

---

## 📞 Need Help?

### Documentation
- 📖 README.md - Project overview
- 📖 DATA_DICTIONARY.md - Feature details
- 📖 PROJECT_DOCUMENTATION.md - Complete guide

### Code
- 💻 src/eda_utils.py - Utility functions (with docstrings)
- 📓 notebooks/eda_analysis.ipynb - Analysis workflow

### Review
- 📋 CODE_REVIEW_SUMMARY.md - What was improved
- ✅ REVIEW_COMPLETE.md - Final summary

---

## 🎯 Next Steps After EDA

Once you complete the EDA:

1. ✅ **Document Findings** - Add insights to notebook
2. ✅ **Feature Engineering** - Create derived features
3. ✅ **Preprocessing** - Handle missing values, outliers
4. ✅ **Model Development** - Train baseline models
5. ✅ **Evaluation** - Assess model performance
6. ✅ **Deployment** - Build MaaS API

---

## 🏆 Success Checklist

Before moving to the next phase, ensure:

- [ ] EDA notebook runs without errors
- [ ] All visualizations generated successfully
- [ ] Key findings documented in notebook
- [ ] Data quality issues identified
- [ ] Feature importance assessed (WoE/IV)
- [ ] Statistical tests completed
- [ ] Feature engineering plan created
- [ ] Model development strategy defined

---

## 🚀 Ready to Start?

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch Jupyter
jupyter notebook

# 3. Open notebooks/eda_analysis.ipynb

# 4. Run and explore!
```

**Happy Analyzing!** 📊🎉

---

*Last Updated: April 15, 2026*  
*For questions or issues, refer to PROJECT_DOCUMENTATION.md*
