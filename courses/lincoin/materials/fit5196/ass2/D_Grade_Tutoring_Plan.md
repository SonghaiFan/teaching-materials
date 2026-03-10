# FIT5196 Assignment 2 - Tutoring Plan (Targeting Distinction Grade)

## Marking Rubric Analysis - What You Need for Distinction (D)

### Task 1 & 2 Output Requirements (30/40 marks)

#### **Dirty Data Cleaning** (30% of output) - Target: 75-89% accuracy
- Need to fix 75-89% of errors correctly
- Focus on systematic approach rather than perfection
- Document your methodology clearly

#### **Outlier Detection** (10% of output) - Target: 75-89% removal
- Remove 75-89% of outliers from delivery_charges
- Use standard statistical methods (IQR, Z-score)
- Show clear justification for outlier definition

#### **Missing Data Imputation** (15% of output) - Target: 75-89% accuracy  
- Impute 75-89% of missing values correctly
- Try 2-3 different imputation methods
- Choose the most reasonable method with justification

#### **Task 1 Methodology** (10%) - Target: D Level
- "Methodology consists of all required steps and produces output with above C scores"
- Include all steps but focus on core requirements
- Minor errors acceptable for D grade

#### **Task 2 Data Reshaping** (25%) - Target: D Level
- "Different methods reasonably analysed"
- "Effects of data-reshaping methods demonstrated"
- "Uses different attributes to evaluate performance with detailed explanation"
- "Reasonable recommendation based on analysis"

#### **Documentation** (10%) - Target: D Level
- "Report has proper sections and subsections"
- "Methodology explained fairly, code fairly commented"
- "Report can be improved" (acknowledges room for improvement)

## Simplified Implementation Strategy (Targeting D Grade)

### **Phase 1: Setup & Basic EDA (Week 1)**

#### Day 1-2: Project Setup
```python
# Essential libraries only
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
```

#### Day 3-4: Data Understanding
- Load all datasets
- Basic descriptive statistics
- Simple visualizations (histograms, box plots)
- Identify obvious issues

### **Phase 2: Core Data Cleaning (Week 2)**

#### **Dirty Data Strategy (Aim for 80% accuracy)**

**Focus Areas:**
1. **Date Format Issues**: Check YYYY-MM-DD format
2. **Coordinate Validation**: Ensure lat/long are reasonable for Melbourne
3. **Warehouse Name Consistency**: Cross-check with warehouse.csv
4. **Order Calculation Errors**: Verify order_total = order_price × (1-discount) + delivery
5. **Boolean Field Issues**: Ensure true/false values are consistent

**Implementation Approach:**
```python
# Example: Simple date validation
def fix_date_format(date_str):
    # Try common date formats and convert to YYYY-MM-DD
    # Return fixed date or original if no clear fix
    pass

# Example: Coordinate validation  
def validate_coordinates(lat, lon):
    # Check if coordinates are within Melbourne bounds
    # Melbourne roughly: lat -38.5, lon 144.5-145.5
    pass
```

#### **Missing Data Strategy (Aim for 80% accuracy)**

**Simple but Effective Methods:**
1. **Numerical Data**: Use median imputation (robust to outliers)
2. **Categorical Data**: Use mode imputation
3. **Location Data**: Use KNN imputation based on similar customers
4. **Business Logic**: Use warehouse.csv to infer missing nearest_warehouse

```python
# Example approach
from sklearn.impute import SimpleImputer, KNNImputer

# For numerical columns
num_imputer = SimpleImputer(strategy='median')

# For categorical columns
cat_imputer = SimpleImputer(strategy='most_frequent')
```

#### **Outlier Detection (Aim for 80% removal)**

**Focus on delivery_charges only:**
```python
# Simple but effective outlier detection
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (data[column] < lower_bound) | (data[column] > upper_bound)
```

### **Phase 3: Task 2 - Data Reshaping (Week 3)**

#### **Reasonable Analysis for D Grade:**

**Step 1: Feature Scale Analysis**
```python
# Check scales of different features
suburb_data[['aus_born_perc', 'number_of_units', 'number_of_houses', 
             'population', 'median_income']].describe()
```

**Step 2: Try 3 Transformation Methods**
1. **Standardization (Z-score)**
2. **Min-Max Normalization** 
3. **Log Transformation** (for skewed data)

**Step 3: Evaluate Linearity**
```python
# Simple correlation analysis
correlations = scaled_data.corr()['median_house_price'].sort_values()
```

**Step 4: Make Reasonable Recommendation**
- "Based on correlation improvements and scale normalization, we recommend standardization for this dataset"
- Show before/after correlation plots
- Simple justification sufficient for D grade

### **Phase 4: Documentation Strategy**

#### **Report Structure (D Grade Standard):**

**Task 1 Notebook Structure:**
```markdown
# 1. Introduction
- Brief overview of assignment goals
- Dataset description

# 2. Data Understanding
- Basic statistics and visualizations
- Initial problem identification

# 3. Dirty Data Cleaning
## 3.1 Error Detection Methods
## 3.2 Fixing Approach
## 3.3 Results and Validation

# 4. Missing Data Imputation  
## 4.1 Missing Pattern Analysis
## 4.2 Imputation Methods Tried
## 4.3 Selected Method and Justification

# 5. Outlier Detection
## 5.1 Detection Method
## 5.2 Results

# 6. Conclusion
- Summary of fixes applied
- Limitations and potential improvements
```

**Task 2 Notebook Structure:**
```markdown
# 1. Data Exploration
- Load and examine suburb data
- Initial visualizations

# 2. Feature Analysis
- Scale comparison
- Distribution analysis  
- Correlation with target

# 3. Transformation Methods
## 3.1 Standardization
## 3.2 Min-Max Normalization
## 3.3 Log Transformation

# 4. Evaluation and Comparison
- Before/after comparisons
- Linear regression assumptions check

# 5. Recommendation
- Selected approach with justification
```

## **Realistic Timeline (3 weeks to D grade)**

### **Week 1: Foundation**
- Days 1-2: Setup, data loading, basic EDA
- Days 3-4: Understand business rules and requirements  
- Days 5-7: Start dirty data analysis

### **Week 2: Core Implementation**
- Days 1-3: Dirty data cleaning (aim for 80% accuracy)
- Days 4-5: Missing data imputation (median/mode methods)
- Days 6-7: Outlier detection and removal

### **Week 3: Task 2 & Documentation**
- Days 1-3: Task 2 implementation (3 transformation methods)
- Days 4-5: Report writing and documentation
- Days 6-7: Testing, validation, and final submission prep

## **Key Success Tips for D Grade:**

1. **Focus on Core Requirements**: Don't overcomplicate - solid basics beat fancy methods
2. **Document Everything**: Clear explanations more important than perfect code
3. **Show Your Work**: Include intermediate steps and reasoning
4. **Test Your Outputs**: Make sure CSV files are readable and properly formatted
5. **Prepare for Interview**: Understand what you submitted, even if not perfect

## **Common Pitfalls to Avoid:**

- ❌ Trying to achieve 100% accuracy (HD requirement)
- ❌ Using overly complex methods without justification
- ❌ Poor documentation (automatic grade reduction)
- ❌ Not testing output file formats
- ❌ Forgetting the interview preparation

## **D Grade Mindset:**

> **"Good enough with solid justification is better than perfect methods you can't explain"**

Focus on:
- ✅ Reasonable approaches with clear reasoning
- ✅ Solid documentation and structure
- ✅ Meeting file format requirements exactly
- ✅ Being able to explain your choices in the interview
- ✅ 75-89% accuracy targets rather than perfection

This approach should reliably achieve Distinction (D) grade while being manageable for tutoring purposes.


**打包命令（含所有必交文件，AI声明表补全后可直接用）：**
```sh
zip Group_032_ass2.zip \
Group_032_dirty_data_solution.csv \
Group_032_missing_data_solution.csv \
Group_032_outlier_data_solution.csv \
Group_032_ass2_task1.ipynb \
Group_032_ass2_task1.py \
Group_032_ass2_task2.ipynb \
Group_032_ass2_task3.pdf \
Group_032_AI_Records.pdf
```
（如未用AI，可省略AI_Records.pdf）

**请补全AI声明表后再执行上述命令，即可完成作业打包。**  
如需AI声明模板、对话导出说明或自动化脚本，请继续告知。