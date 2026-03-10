# FIT5196 Assignment 2 - Data Wrangling Project Plan

## Assignment Overview
- **Weight**: 40% of total mark
- **Due Date**: Monday 20 Oct 2025, 11:55pm
- **Type**: Group Assignment
- **Interview**: Week 12 during allocated Applied sessions (HURDLE requirement)

## Task Breakdown

### Task 1: Data Cleansing (21/40 marks)

#### 1.1 Project Setup
- [ ] Download group-specific dataset files from course folder
- [ ] Create working directory structure
- [ ] Set up Jupyter notebook environment
- [ ] Import required libraries:
  - pandas, numpy for data manipulation
  - matplotlib, seaborn for visualization
  - sklearn.linear_model.LinearRegression
  - nltk.sentiment.vader.SentimentIntensityAnalyzer
  - numpy.linalg for solving equations

#### 1.2 Data Understanding & EDA (Exploratory Data Analysis)
- [ ] **Load and examine all input files**:
  - `Group<group_id>_dirty_data.csv`
  - `Group<group_id>_missing_data.csv`
  - `Group<group_id>_outlier_data.csv`
  - `warehouse.csv`

- [ ] **Understand the business context**:
  - DigiCO: Online electronics store in Melbourne
  - 3 warehouses around Melbourne
  - 10 branded items sold
  - Seasonal business rules for delivery charges

- [ ] **Column Analysis** (refer to Table 2 in requirements):
  - order_id, customer_id (unique identifiers)
  - date (YYYY-MM-DD format)
  - nearest_warehouse (warehouse names)
  - shopping_cart (list of tuples: item, quantity)
  - order_price, coupon_discount, delivery_charges, order_total
  - customer_lat, customer_long (coordinates)
  - distance_to_nearest_warehouse (Haversine distance)
  - season (seasonal classification)
  - is_expedited_delivery (boolean)
  - latest_customer_review (text)
  - is_happy_customer (boolean based on sentiment analysis)

#### 1.3 Data Cleaning Tasks

##### 1.3.1 Dirty Data Cleaning
- [ ] **Systematic Error Detection**:
  - Check data types and formats
  - Validate date formats (YYYY-MM-DD)
  - Verify warehouse names against warehouse.csv
  - Validate coordinate ranges (lat/long)
  - Check seasonal classifications
  - Verify boolean fields
  - Analyze shopping_cart format consistency

- [ ] **Business Rule Validation**:
  - Cross-check nearest_warehouse with actual distances
  - Validate order calculations: order_total = order_price × (1 - coupon_discount/100) + delivery_charges
  - Check if delivery charges follow seasonal linear models
  - Verify distance calculations using Haversine formula (radius = 6378 KM)

- [ ] **One-by-One Error Fixing**:
  - Remember: only one anomaly per row maximum
  - Each anomaly has exactly one possible fix
  - Error-free columns: coupon_discount, delivery_charges, quantities in shopping_cart, order_id, customer_id, latest_customer_review

##### 1.3.2 Missing Data Imputation
- [ ] **Missing Value Analysis**:
  - Identify patterns in missing data
  - Analyze Missing Completely at Random (MCAR), Missing at Random (MAR), Missing Not at Random (MNAR)
  - Visualize missing data patterns

- [ ] **Imputation Strategy**:
  - Try multiple imputation methods:
    - Mean/Median/Mode imputation
    - Forward/Backward fill
    - Linear interpolation
    - KNN imputation
    - Multiple imputation
  - Choose best method based on data characteristics and performance
  - Document reasoning for method selection

##### 1.3.3 Outlier Detection and Removal
- [ ] **Focus on delivery_charges only**
- [ ] **Outlier Detection Methods**:
  - Statistical methods (Z-score, IQR)
  - Visualization (box plots, scatter plots)
  - Consider business context (reasonable delivery charges)
- [ ] **Remove outlier rows** (not just the outlier values)

#### 1.4 Advanced Analysis Requirements

##### 1.4.1 Sentiment Analysis Implementation
- [ ] Use `nltk.sentiment.vader.SentimentIntensityAnalyzer`
- [ ] Extract compound polarity scores
- [ ] Classify: positive if compound ≥ 0.05, negative otherwise
- [ ] Update `is_happy_customer` field accordingly

##### 1.4.2 Delivery Charge Model Building
- [ ] **Linear Regression Model** (seasonal variations):
  - Features: distance_to_nearest_warehouse, is_expedited_delivery, is_happy_customer
  - Target: delivery_charges
  - Build separate models for each season
  - Use sklearn.LinearRegression
  - Achieve R² > 0.97 for validation

- [ ] **Model Training Strategy**:
  - Use clean data for training
  - Validate model performance
  - Use model to verify/correct delivery charges in dirty data

##### 1.4.3 Distance Calculations
- [ ] Implement Haversine distance formula
- [ ] Verify customer coordinates against nearest warehouse
- [ ] Cross-reference with warehouse.csv locations

#### 1.5 Documentation Requirements (1.5/21 marks)
- [ ] **Jupyter Notebook Structure**:
  - Clear section headers and subheaders
  - Executive summary
  - Data understanding section
  - EDA with visualizations
  - Methodology for each cleaning task
  - Results and validation
  - Conclusions

- [ ] **Code Documentation**:
  - Proper commenting (not excessive)
  - Clear variable names
  - Explanation of complex logic
  - Justification for methodological choices

### Task 2: Data Reshaping (9/40 marks)

#### 2.1 Data Loading and Understanding
- [ ] Load `suburb_info.xlsx`
- [ ] Understand columns:
  - suburb (index)
  - number_of_houses, number_of_units
  - municipality
  - aus_born_perc
  - median_income
  - median_house_price (target variable)
  - population

#### 2.2 Exploratory Data Analysis
- [ ] **Target Variable Analysis**:
  - Distribution of median_house_price
  - Descriptive statistics
  - Outlier detection

- [ ] **Feature Analysis**:
  - Distribution analysis for: aus_born_perc, number_of_units, number_of_houses, population, median_income
  - Scale comparison between features
  - Correlation analysis with target variable
  - Linearity assessment

#### 2.3 Transformation and Normalization
- [ ] **Scaling Methods to Test**:
  - Standardization (Z-score normalization)
  - Min-Max normalization
  - Robust scaling

- [ ] **Transformation Methods to Test**:
  - Log transformation
  - Power transformation
  - Box-Cox transformation
  - Square root transformation

- [ ] **Evaluation Criteria**:
  - Features on same scale
  - Improved linearity with target variable
  - Linear regression assumptions satisfaction:
    - Linearity
    - Independence
    - Homoscedasticity
    - Normality of residuals

#### 2.4 Documentation and Reporting
- [ ] **Exploration Journey Documentation**:
  - Initial data exploration
  - Transformation rationale
  - Before/after comparisons
  - Visual evidence (plots, charts)
  - Quantitative metrics

- [ ] **Recommendations**:
  - Best transformation approach
  - Justification for choices
  - Impact on linear regression readiness

### Task 3: Declaration and Interview (10/40 marks)

#### 3.1 Generative AI Declaration (HURDLE)
- [ ] Complete Generative AI Tools Declaration Form
- [ ] Download as PDF: `Group<group_id>_ass2_task3.pdf`
- [ ] If AI tools used:
  - Document all conversations
  - Save as `Group<group_id>_AI_Records.pdf/docx`
  - Ensure all conversations are in English

#### 3.2 Interview Preparation (10/40 + HURDLE)
- [ ] **Content Review**:
  - Understand every line of submitted code
  - Be able to explain methodology choices
  - Know results and their interpretation
  - Understand specific functions used

- [ ] **Logistics**:
  - Week 12, during allocated Applied sessions
  - 5-10 minutes per group
  - All members must attend and participate
  - Bring signed attendance sheet

## Deliverables Checklist

### Required Files
- [ ] `Group<group_id>_dirty_data_solution.csv`
- [ ] `Group<group_id>_missing_data_solution.csv`
- [ ] `Group<group_id>_outlier_data_solution.csv`
- [ ] `Group<group_id>_ass2_task1.ipynb` (with outputs visible)
- [ ] `Group<group_id>_ass2_task1.py` (outputs cleared)
- [ ] `Group<group_id>_ass2_task2.ipynb` (with outputs visible)
- [ ] `Group<group_id>_ass2_task3.pdf`
- [ ] `Group<group_id>_AI_Records.pdf` (if applicable)

### Final Submission
- [ ] Zip all files into `Group<group_id>_ass2.zip`
- [ ] Verify file naming conventions
- [ ] Test file readability (reload CSV files in Python)
- [ ] Both group members submit on Moodle
- [ ] Ensure .ipynb files have outputs, .py files don't

## Timeline Suggestion (assuming 3+ weeks)

### Week 1: Setup and Understanding
- Days 1-2: Project setup, data loading, initial EDA
- Days 3-5: Deep dive into business rules and data understanding
- Days 6-7: Start dirty data analysis

### Week 2: Core Implementation
- Days 1-3: Complete dirty data cleaning
- Days 4-5: Missing data imputation
- Days 6-7: Outlier detection and removal

### Week 3: Advanced Tasks and Documentation
- Days 1-2: Task 2 (data reshaping)
- Days 3-4: Final validation and testing
- Days 5-6: Documentation and report writing
- Day 7: Final review and submission preparation

## Key Success Factors

1. **Accuracy**: Follow requirements exactly, use correct file names
2. **Documentation**: Clear, well-structured reports with proper justifications
3. **Validation**: Test all outputs, ensure models achieve required performance
4. **Understanding**: Be ready to explain every aspect during interview
5. **Academic Integrity**: Proper AI tool declaration if used

## Common Pitfalls to Avoid

- Wrong file naming conventions
- Clearing outputs in .ipynb files
- Not achieving R² > 0.97 for delivery charge models
- Insufficient documentation
- Not preparing adequately for interview
- Missing hurdle requirements
- Using wrong dataset files for your group