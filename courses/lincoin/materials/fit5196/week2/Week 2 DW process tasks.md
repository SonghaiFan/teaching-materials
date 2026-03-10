# Week 2 DW process tasks

> Source: `Week 2 DW process tasks.pdf`
> Pages: 45
> Conversion: extracted embedded PDF text with `pdftotext`

---
## Page 1

### FIT5196 DATA WRANGLING
### Week 2
Data Wrangling Process & Tasks
### By Jackie Rong

Faculty of Information Technology
Monash University

---

## Page 2

Data Wrangling
- 

Data Wrangling is the process of acquiring, cleaning, structuring, and enriching raw data into a format that is directly usable for analysis.
Data Wrangling
### Data
Collection

### Data
Analysis

?
Problem
Identification

### Data
Cleaning

Result
Interpretation

---

## Page 3

Goals of Data Wrangling
- 

The goals of data wrangling are multifaceted, aiming to simplify data analysis and maximize the value extracted from the data.
- Improving Data Quality
- Data Formatting and Standardization
Raw data
Tidy data
- Simplifying Access to Data
- Enriching Data
- Reducing Data Complexity
- Facilitating Data Integration
Data + Wrangling + Analysis
- Increasing Analytical Efficiency
= Data Product (Knowledge)
- Supporting Decision Making

---

## Page 4

Challenges in Data Wrangling
- 

Challenges arise from the nature of the data itself, the complexity of data sources, and the goals of the data analysis projects.
- Volume of Data & Scalability
- Data Quality Issues
- Data from Diverse Sources
- Complexity of Data Structures
- Lack of Standardization & Interpretability
- Highly Time-Consuming
- Skill and Tool Requirements
- Data Privacy and Security

Andrew Kamau, https://blog.google/products/chrome/5-tips-to-stay-safer-online-with-chrome/

---

## Page 5

Data Wrangling Tasks
- 

Data Wrangling is the process of acquiring, cleaning, structuring, and enriching raw data into a format that is directly usable for analysis.
Data Preprocessing

### Data
Discovery
### Data
Collection

### Data
Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

---

## Page 6

Outline
- Data Wrangling Process
- Main Tasks in Data Wrangling
- Data Discovery
- Data Collection
- Data Pre-processing
- Data Cleaning
- Data Transformation
- Data Enrichment
- Data Structuring
- Data Validation

---

## Page 7

Overview of Data Wrangling Process
Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

---

## Page 8

Overview of Data Wrangling Process
Data Discovery

### Data
Transformation

The initial step where data scientists identify and access various data sources relevant to the analytical objectives.

### Data
Enrichment

This includes determining the availability, suitability, and quality of data.

Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

Data wrangling is the process of making data useful.

---

## Page 9

Example – Data Discovery
Project: Predictive Analysis for Patient Readmissions
- 

Objective – Aims to develop a predictive model to identify patients at high risk of readmission within
30 days of discharge

- 

Goal – To improve patient outcomes and reduce healthcare cost

- 

Your tasks in a healthcare analytics team
- Identifying relevant data sources
- Understanding data availability and accessibility
- Assessing data quality and suitability

John Russell, 2021, Hospitals face big fines for frequent readmission, https://www.ibj.com/articles/hospitals-face-big-fines-for-frequent-readmissions

---

## Page 10

Example – Data Discovery (cont.)
Your tasks
- Identifying relevant data sources
Patient Health
Histories

Treatment plans

Wearable Device
### Data
Insurance Claim
### Data
Hospital Admission,
Discharge and
Transfer Systems

Electronic Health
Records

Medications
Diagnoses
Outcomes

Dates and reasons for admissions, discharges, and transfers within the hospital

Patient claims
Procedure performed

Reimburse ment rates
Billing items

Patient-generated health data tracking vital signs like heart rate and activity levels.

---

## Page 11

Example – Data Discovery (cont.)
Your tasks
- Identifying relevant data sources
- Understanding data availability and accessibility
Insurance Companies

Hospital IT Department

Doctors, Nurses, other
Clinicians or Health worker

Health Monitoring Programs

---

## Page 12

Example – Data Discovery (cont.)
Your tasks
- Identifying relevant data sources
- Understanding data availability and accessibility
- Assessing data quality and suitability

Electronic Health
Records

Wearable Device
### Data
Insurance Claim
### Data

Hospital Admission,
Discharge and
Transfer Systems

Completeness
Accuracy
Electronic health record, Wikipedia, https://en.wikipedia.org/wiki/Electronic_health_record

Formatting
Structuring
Multi-data sources

Quality

Zhou, Shengyao & He, Jie & Yang, Hui & Chen, Donghua & Zhang, Runtong. (2020). Big Data-Driven Abnormal Behavior
Detection in Healthcare Based on Association Rules. IEEE Access. PP. 1-1. 10.1109/ACCESS.2020.3009006.

Coverage

---

## Page 13

Overview of Data Wrangling Process
Data Collection
This phase involves gathering the identified data from its sources.

Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

The data can be collected from multiple sources like databases, spreadsheets, APIs, and external datasets.

---

## Page 14

Data Collection
- 

To collect data that is relevant, accurate and robust for data analysis needs, we need to consider
- Define objective – what to achieve with the data collection?
- Data requirements – what the specific data needed to meet the objective?
- Data sources – where to obtain the data?
- Data quality – ensure the data collected is of high quality
- Data volume – assess the volume of data needed and the capacity of handling
- Ethics – ensure ethical practices complying with legal standards and permissions
- Data format – what format to be used?
- Collection methods and tools – choose appropriate methods and right tools
- Timeframe and budget – align with project deadlines and budget constraints
- Data privacy and security – protect privacy from individuals and secure storage and handling of data
- Documentation – keep detailed documentation of the data collection process
- Pilot test – validate data collection process and instruments
- Review and adaptation – regularly review the process for any necessary adjustments

---

## Page 15

Overview of Data Wrangling Process
Data Pre-processing

### Data
Transformation

At this stage, preliminary data preparation tasks are performed to make raw data more suitable for analysis.

### Data
Enrichment

It involves selecting, and formatting datasets to ensure they are in a usable state.

Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

Data wrangling is the process of making data useful.

---

## Page 16

Data Pre-Processing
- 

Selection
- Subsetting o Choosing a subset of data that is relevant to the analysis, which may involve filtering rows or columns based on certain criteria.

---

## Page 17

Example - Subsetting
Objective: To analyse accidents happened from 2000 to 2010.

AirCrashes

2000 2010

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

Airline_flight
Casualties
Circumstances
Country
### Crew
### Data
Ground
Latitude
Longtitude
Passengers
### Dead

---

## Page 18

Data Pre-Processing
- 

Selection
- Subsetting o Choosing a subset of data that is relevant to the analysis, which may involve filtering rows or columns based on certain criteria.
- Sampling o If the dataset is too large to process or if you want to perform initial exploratory analysis, you might draw a representative sample of the data.

---

## Page 19

Example - Sampling
- 

Objective: To analyse Facebook active customers’ behaviours in December 2023
### Facebook monthly active users:
3.05 billion monthly users access
Facebook’s platform, a 7.18% increase year-over-year.
- India has the most Facebook users with over 385.65 million
- US (188.6 million)
- Indonesia (136.35 million)
- Brazil (111.75 million)
- Mexico (94.8 million)
- …

Brian Dean, Facebook User & Growth Statistics, Backlinko, https://backlinko.com/facebook-users

Sampled dataset of 3.05 million users
0.1% of original dataset

12.64%
6.18%
4.47%
3.66%
3.11%

---

## Page 20

Data Pre-Processing
- 

Selection

- 

Formatting
- Date formatting
- DD/MM/YYYY
- MM/DD/YYYY
- YYYY/MM/DD
- …

- Numeric formatting
- Decimal points
- Thousands separators

- Text formatting
- Upper, lower, title case, whitespace, symbols

- Categorical data formatting
- ‘Male’ vs ‘M’; ‘Female’ vs ‘F’

- Currency conversion
- USD, AUD, EUR, CNY…

- Unit conversion
- Miles to kilometres
- Fahrenheit to Celsius

- Text encoding standardisation
- UTF-8
- Time zone alignment
- Address formatting
- File format conversion
- XML à CSV
- JSON à XML

---

## Page 21

Overview of Data Wrangling Process
### Data Cleaning:
Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

A critical step focused on removing or correcting inaccuracies, inconsistencies, duplicates, or irrelevant data points within datasets.
This step ensures the quality and reliability of data for analysis.

---

## Page 22

Data Cleaning
- 

Data anomalies
- Items within a dataset that deviate from a typical pattern or expectation.
- They can indicate errors.
- They can also reveal insights or new patterns.
Missing Values

The Switzerland heart disease data set from
UCI machine learning data repository

Outliers

---

## Page 23

Data Cleaning
- 

Data anomalies
- Items within a dataset that deviate from a typical pattern or expectation.
- They can indicate errors.
- They can also reveal insights or new patterns.
Duplicate Data

Consistency Issue
Employer Database

Staff Database

---

## Page 24

Overview of Data Wrangling Process
Data Transformation
Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

This involves converting data from its original form into a format or structure that is more appropriate for analysis.
Transformation can include normalization, aggregation, and feature engineering to enhance data analysis.

---

## Page 25

Data Transformation
- 

Numeric data
- Normalisation o Rescales numeric data to fall within a specified range, often between 0 and 1, to ensure that no variable dominates due to its scale.

---

## Page 26

Data Transformation (cont.)
- 

Numeric data
- Normalisation
- Standardization o Adjusts the distribution of data so that it has a mean of 0 and a standard deviation of 1.
This is useful for algorithms that assume data is normally distributed.

---

## Page 27

Data Transformation (cont.)
- 

Numeric data
- Normalisation
- Standardization
- Aggregation o Summarizing or aggregating data, such as computing summary statistics (mean, median, sum) for groups of data. This can be particularly useful in reducing data dimensionality and extracting insights from the data.

---

## Page 28

Data Transformation (cont.)
- 

Numeric data
- Normalisation
- Standardization
- Aggregation
- Discretisation o Converts continuous variables into discrete ones by creating a set number of equal-width or equal-frequency intervals, which can be useful for certain types of models.

Discretisation

---

## Page 29

Data Transformation (cont.)
- 

Numeric data
- Normalisation
- Standardization
- Aggregation
- Discretisation
- Binning/Bucketing o Converts numeric variables into categorical counterparts by grouping values into bins or categories, which can simplify the model and help in identifying trends.

Binning/Bucketing

---

## Page 30

Data Transformation (cont.)
- 

Text data
- Tokenisation o Breaking text into individual words or phrases

Utkarsh Kant, Tokenization – A complete guide, Medium, https://medium.com/@utkarsh.kant/tokenization-a-complete-guide-3f2dd56c0682

---

## Page 31

Data Transformation (cont.)
- 

Text data
- Tokenisation
- Stemming/lemmatisation o Reducing words to their root form

Botpenguin, Stemming, https://botpenguin.com/glossary/stemming

---

## Page 32

Data Transformation (cont.)
- 

Text data
- Tokenisation
- Stemming/lemmatisation
- Vectorisation o Converting text into numerical format for analysis

---

## Page 33

Data Transformation (cont.)
- 

Image data
- Resize

- Chopping

---

## Page 34

Data Transformation (cont.)
- 

Image data
- Resize
- Chopping
- Normalization
- Colour space conversion

### Red

Green

Grayscale/ Black & White

### Blue

### Cyan

Magenta

Yellow

Black

---

## Page 35

Data Transformation (cont.)
- 

Image data
- Resize
- Chopping
- Normalization
- Colour space conversion
- Rotation
- Flipping
- Translation

---

## Page 36

Data Transformation (cont.)
- 

Image data
- Resize
- Chopping
- Normalization
- Colour space conversion
- Rotation
- Flipping
- Translation
- Noise injection
- Brightness adjustment
- Contrast adjustment

Noise

Brightness +150

Contrast +150

Brightness -150

Contrast -150

---

## Page 37

Overview of Data Wrangling Process
Data Enrichment
Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

Enhancing the data with additional context or merging it with other data sources to make it completer and more informative.
This step can involve adding demographic information, geographical tags, or combining datasets to provide more depth.

---

## Page 38

Data Enrichment
- 

Data integration
- Combining data from different sources to create a more comprehensive dataset.

- 

Data augmentation
- Adding information to existing records to enhance the depth of data on each data point.

- 

Attribute enrichment
- Enhancing existing datasets by adding new attributes or features that were not previously included.

- 

Temporal enrichment
- Adding time-related data to datasets.

- 

Semantic enrichment
- Adding metadata or other semantic information to make data more understandable and usable.

---

## Page 39

Overview of Data Wrangling Process
Data Validation
Ensuring that the data is accurate, consistent, and usable for analysis.

Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

Validation checks are performed to verify data quality and correctness after cleaning and transformation.

---

## Page 40

Data Validation
- 

Define Validation Rules and Criteria
- Establish the standards that your data must meet.

- 

Check for accuracy
- Ensure that the data accurately reflects the real-world entities or values it represents.

- 

Ensure consistency
- Verify that the data is consistent within the dataset and across related datasets.

- 

Validate data completeness
- Ensure no critical data is missing, which could impact analysis.

- 

Test for logical integrity
- Confirm that the data makes logical sense and adheres to known constraints or relationships.

- 

Validate range and constraints
- Ensure that data values fall within acceptable ranges or constraints.

---

## Page 41

Data Validation (cont.)
- 

Format validation
- Verify that the data is in the expected format or structure, which is essential for automated processing.

- 

Uniqueness checks
- Ensure that entries that are supposed to be unique do not have duplicates.

- 

Cross-validation
- Use related datasets or data sources to validate the data.

- 

Automate validation processes
- Streamline validation to make it efficient and repeatable, especially for large datasets or ongoing data collection.

- 

Document validation issues and resolutions
- Keep track of identified issues and how they were resolved for future reference and accountability.

---

## Page 42

Overview of Data Wrangling Process
Data Storing
Data Preprocessing

### Data
Discovery
### Data
Collection

Data Storing

### Data
Cleaning

### Data
Validation

### Data
Transformation

### Data
Enrichment

Data wrangling is the process of making data useful.

The final step involves saving the wrangled data in a suitable storage system for easy access and analysis.
This could be databases, data warehouses, or cloud storage solutions, depending on the scale and purpose of the data analysis project.

---

## Page 43

Data Storing
- 

Selection of Storage Solution
- Choose an appropriate data storage solution that aligns with the data's nature, size, and intended use.

- 

Data Modelling and Schema Design
- Design a logical structure for the data that supports efficient storage, query, and retrieval.

- 

Normalization and Denormalization
- Organize the data to reduce redundancy and improve integrity in relational databases through normalization, or optimize performance and read efficiency through denormalization, especially in
NoSQL databases or data warehouses.

- 

Data Formatting and Encoding
- Ensure that data is stored in a consistent and appropriate format that matches the storage system’s requirements.

- 

Implementing Data Security Measures
- Protect data from unauthorized access and ensure privacy and compliance with data protection regulations (e.g., GDPR, HIPAA).

---

## Page 44

Data Storing (cont.)
- 

Data Indexing and Optimization
- Enhance the speed and efficiency of data retrieval.

- 

Backup and Recovery Planning
- Ensure data durability and the ability to recover from data loss or corruption.

- 

Data Lifecycle Management
- Manage the lifecycle of data from creation to deletion, aligning with data retention policies and legal requirements.

- 

Documentation and Metadata Management
- Provide context and understanding for the data and how it’s stored, facilitating easier data management, governance, and use.

- 

Monitoring and Maintenance
- Ensure the storage system remains efficient, scalable, and reliable as data volume grows and access patterns change.

---

## Page 45

Summary & To-do List
- 

Please download and read materials provided on Moodle.

- 

Watch the video introducing Pandas basic functions.

- 

Next week: Regular Expression
