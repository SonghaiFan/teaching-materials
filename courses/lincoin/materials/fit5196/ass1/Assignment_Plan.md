---
title: "FIT5196 Assessment 1 - EDA Project Plan"
due_date: "23:55, Sunday, 14 September 2025"
weight: 35
---

# FIT5196 Assessment 1 - Exploratory Data Analysis (EDA) Project Plan

## Project Overview

**Due Date:** 23:55, Sunday, 14 September 2025  
**Weight:** 35% of total grade  
**Type:** Group Assessment (Data Wrangling Unit)

## Assessment Objectives

- **Data Familiarisation:** Deep understanding of dataset structure, content, and quality
- **Basic Data Quality Assessment:** Identify missing values, duplicates, invalid values, inconsistencies
- **Visual Exploration:** Use visualization techniques to uncover hidden structures and patterns
- **Research Insight Generation:** Translate EDA findings into potential ML research questions

## Project Structure

### Phase 1: Data Loading, Parsing, and Merging (Step 1)

#### Input Data Files

- `Group<group_number>.xml` - Flickr photo data
- `Group<group_number>.json` - Flickr photo data
- Each photo record contains 18 attributes

#### Tasks

1. **Data Loading**

   - Load data from both XML and JSON files using Python
   - Convert data into suitable objects for manipulation
   - Inspect structure and schema of both datasets

2. **Data Merging**

   - Merge data into single dataset using appropriate methods
   - Ensure well-structured and formatted output

3. **Data Cleaning & Transformation**

   - **Text Processing (5 attributes):** Title, City, Country, Tags, Description
     - Convert to lowercase (exclude 'NaN')
     - Remove XML/JSON tags and emojis
     - Keep only valid UTF-8 characters
     - Remove non-English characters completely
   - **Regular Expressions Required:** Use only regex for text processing
   - **Null Values:** Represent as 'NaN'
   - **Preserve:** Digital numbers and non-English language content (with justification)

4. **Output**
   - Generate `Group<group_number>_dataset.csv`
   - Must have exactly same attributes as sample output file
   - Code must be testable with different datasets

### Phase 2: Exploratory Data Analysis (Step 2)

#### EDA Goals

- Gain in-depth understanding of dataset
- Inform subsequent decisions (preprocessing, model design, hypothesis generation)

#### Analysis Tasks

1. **Dataset Structure Analysis**

   - Overall dimensions and structure
   - Data types and formats
   - Schema understanding

2. **Univariate Analysis**

   - Distribution of individual variables
   - Central tendency and spread
   - Frequency analysis for categorical variables

3. **Bivariate Analysis**

   - Relationships between pairs of variables
   - Correlation analysis
   - Cross-tabulation for categorical variables

4. **Multivariate Analysis**

   - Complex relationships between multiple variables
   - Pattern identification across dimensions

5. **Data Quality Assessment**

   - Missing values analysis
   - Duplicate detection
   - Outlier identification
   - Data consistency checks

6. **Visualization**
   - Create appropriate charts and graphs
   - Support findings with visual evidence
   - Ensure clarity and interpretability

### Phase 3: Insights and Research Questions (Step 3)

#### Key Insights Requirements

- **Minimum 10 key insights** from EDA findings
- Must be data-driven and evidence-based
- Include corresponding visualizations

#### Machine Learning Research Questions Requirements

- **Minimum 5 high-quality ML questions**
- Must be clearly defined with input features and output variables
- Rooted in actual EDA findings (not speculative)
- Consider all available attributes

#### ML Question Types to Consider

- **Supervised Learning:** Classification, Regression
- **Unsupervised Learning:** Clustering, Dimensionality Reduction
- **Semi-supervised Learning**
- **Other:** Time series analysis, Sequential pattern detection, Anomaly detection

#### Quality Criteria for ML Questions

- Data-driven (supported by EDA evidence)
- Clearly defined (specific input/output variables)
- Meaningful value generation
- Appropriate ML technique selection
- Measurable success criteria

## Deliverables

### 1. EDA Methodology (35% of grade)

- `Group<group_number>_solution.ipynb` - EDA process notebook
- `Group<group_number>_solution.py` - Python code for plagiarism check
- `Group<group_number>_dataset.csv` - Merged dataset

### 2. EDA Report (50% of grade)

- `Group<group_number>_EDA.pdf` - Comprehensive EDA report including:
  - EDA design methodology
  - Key findings and insights
  - Machine learning questions with justification
  - Supporting visualizations

### 3. Video Presentation (10% of grade)

- `Group<group_number>_presentation.mp4` - 6-10 minute presentation
- All group members must present
- Communicate EDA findings and ML questions with justification

### 4. AI Tools Documentation (5% of grade)

- `Group<group_number>_AI_declaration.pdf` - Generative AI Tools Declaration Form
- `Group<group_number>_AI_record.pdf` - Complete AI conversation record (if applicable)

## Submission Requirements

### File Naming Convention

- All files must follow exact naming pattern: `Group<group_number>_<type>.<extension>`
- Replace `<group_number>` with actual group number

### Submission Format

1. **Group<group_number>\_A1.zip** containing 6 files:

   - Solution notebook (.ipynb)
   - Python code (.py)
   - Dataset (.csv)
   - Video presentation (.mp4)
   - AI declaration (.pdf)
   - AI record (.pdf)

2. **Group<group_number>\_EDA.pdf** - Separate file (NOT in zip)

### Important Notes

- **5% penalty** if EDA report is placed inside zip file
- Both group members must click 'Submit' on Moodle
- .ipynb file must contain printed output
- .py file must NOT contain any output
- Clear cell output before exporting .py file

## Technical Requirements

### Data Processing

- Use only Regular Expressions for text cleaning
- Handle non-English content appropriately
- Preserve digital numbers
- Maintain data integrity during merging

### Code Quality

- Solution must work with test datasets (not provided)
- Proper error handling and debugging
- Code must be reproducible
- No plagiarism - will be checked automatically

### Visualization Standards

- Clear and interpretable charts
- Support all findings with visual evidence
- Professional presentation quality
- Appropriate chart types for data types

## Timeline and Milestones (Starting August 24, 2025)

### Phase 1: Data Processing (August 24 - September 1) - **CRITICAL PATH**

- Load and parse XML/JSON files
- Implement data cleaning with regex
- Merge datasets
- Generate final CSV output
- **Deadline:** September 1 (must complete before EDA can begin)

### Phase 2: EDA Implementation (September 2-8) - **DEPENDS ON PHASE 1**

- Conduct comprehensive analysis
- Create visualizations
- Document findings and insights
- **Deadline:** September 8 (must complete before research questions)

### Phase 3: Research Questions (September 9-11) - **DEPENDS ON PHASE 2**

- Formulate ML research questions
- Ensure quality and feasibility
- Link to EDA evidence
- **Deadline:** September 11 (must complete before final documentation)

### Phase 4: Documentation and Presentation (September 12-14) - **DEPENDS ON PHASE 3**

- Write EDA report
- Create video presentation
- Prepare AI documentation
- Final review and submission
- **Final Deadline:** September 14, 23:55

## Task Dependencies and Critical Path

### **MUST DO FIRST (No Dependencies):**

1. **Data Loading & Parsing** - Start immediately

   - Load XML and JSON files
   - Understand data structure
   - Identify all 18 attributes

2. **Data Schema Analysis** - Do in parallel with loading
   - Inspect data types
   - Identify relationships between files
   - Plan merging strategy

### **CANNOT START UNTIL DATA IS LOADED:**

3. **Data Cleaning & Transformation** - Requires loaded data

   - Implement regex for text cleaning
   - Handle non-English characters
   - Convert text to lowercase
   - Clean XML/JSON tags and emojis

4. **Data Merging** - Requires cleaned data from both sources
   - Merge XML and JSON datasets
   - Ensure data integrity
   - Validate merged structure

### **CANNOT START UNTIL MERGING IS COMPLETE:**

5. **Dataset Generation** - Requires merged data
   - Export to CSV format
   - Verify output matches sample format
   - Test with different datasets

### **CANNOT START UNTIL CSV IS GENERATED:**

6. **EDA Implementation** - Requires final dataset
   - Univariate analysis
   - Bivariate analysis
   - Multivariate analysis
   - Data quality assessment

### **CANNOT START UNTIL EDA IS COMPLETE:**

7. **Insight Generation** - Requires EDA findings

   - Identify 10+ key insights
   - Create supporting visualizations
   - Document patterns and relationships

8. **ML Research Questions** - Requires insights and EDA evidence
   - Formulate 5+ high-quality questions
   - Ensure data-driven approach
   - Link to specific findings

### **CANNOT START UNTIL RESEARCH QUESTIONS ARE COMPLETE:**

9. **Report Writing** - Requires all analysis and questions

   - Write comprehensive EDA report
   - Include methodology, findings, and ML questions
   - Add visualizations and justifications

10. **Video Presentation** - Requires complete understanding

    - Script presentation based on findings
    - Create slides with visualizations
    - Practice and record presentation

11. **AI Documentation** - Can be done anytime but must be complete
    - Fill out AI declaration form
    - Document AI tool usage (if applicable)

### **FINAL TASKS (All Dependencies Met):**

12. **Submission Preparation** - Requires all deliverables
    - Package files correctly
    - Verify naming conventions
    - Submit both zip and PDF separately

## Success Criteria

### Technical Success

- Clean, merged dataset with correct format
- Reproducible code that passes testing
- Comprehensive EDA covering all requirements

### Analysis Success

- Minimum 10 meaningful insights
- Minimum 5 high-quality ML questions
- Evidence-based conclusions
- Clear visualizations supporting findings

### Documentation Success

- Professional EDA report
- Engaging video presentation
- Complete AI documentation
- Proper file naming and submission

## Risk Mitigation

### Common Pitfalls to Avoid

- Using wrong input data files (results in ZERO marks)
- Incomplete data cleaning (regex only)
- Insufficient insights or ML questions
- Poor visualization quality
- Missing AI declaration (hurdle requirement)
- Incorrect file naming or submission format

### Quality Assurance

- Double-check input file names match group number
- Test code with different datasets
- Review all requirements before submission
- Ensure both group members submit
- Verify file formats and naming conventions
