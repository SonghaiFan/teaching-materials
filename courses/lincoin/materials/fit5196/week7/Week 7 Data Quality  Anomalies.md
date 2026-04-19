# FIT5196 Data Wrangling

## Week 7: Data Quality and Anomalies

## Data Wrangling Tasks (Recap)

Data wrangling typically includes the following stages:

- Data discovery
- Data collection
- Data storing
- Data pre-processing
- Data cleaning
- Data validation
- Data transformation
- Data enrichment

Data structuring is a critical part of data management and organization. The main goal is to make data easier to access and process efficiently while minimizing resource usage.

## Data Quality

### Topics Covered

- Definition of data quality
- Impact of poor data quality
- Data quality dimensions and measures
- Data quality challenges
- Data anomalies and data quality issues
- Data quality management frameworks

### Definition

Data quality refers to the condition of data based on factors such as:

- Accuracy
- Completeness
- Reliability
- Relevance
- Timeliness

High-quality data is essential for informed decision-making, operational efficiency, and competitive advantage.

## Importance of Data Quality

### Enhanced Decision-Making

- Better decisions are made when data is accurate and complete.
- Trustworthy data reduces costly mistakes.

### Regulatory Compliance and Risk Management

- Strong data quality helps organizations comply with regulations.
- Reliable data helps identify and mitigate risks.

### Operational Efficiency

- Clean data reduces rework and verification effort.
- Reliable data enables better resource allocation.

### Customer Satisfaction

- High-quality data supports personalized customer experiences.
- Accurate insights improve service quality and customer loyalty.

### Financial Health

- Fewer errors reduce operating costs.
- Better data can uncover new revenue opportunities.

### Reputation and Trust

- Consistent data quality builds trust among customers, investors, and partners.
- Good data practices improve brand reputation.

### Innovation and Growth

- High-quality data supports analytics and business intelligence.
- Faster, better insights help organizations stay competitive.

## Impacts of Poor Data Quality

- Inaccurate decision-making
- Reduced efficiency and productivity
- Increased costs
- Damaged reputation
- Compliance and legal risks
- Customer dissatisfaction
- Misguided strategic initiatives
- Loss of competitive edge
- Data breaches and security issues
- Analytical and forecasting errors

## Data Quality Dimensions

Data quality dimensions are the broad criteria used to evaluate data quality:

- Accuracy
- Completeness
- Reliability
- Consistency
- Relevance
- Timeliness

These dimensions clarify what needs to be measured and managed.

## Data Quality Measures

Data quality measures are quantitative indicators used to assess performance against those dimensions.

Examples:

- Error rate
- Fill rate
- Duplicate rate
- Latency

## Data Quality Challenges

Data quality challenges can arise from technical, organizational, and process factors.

### Volume and Variety of Data

- Large volumes and diverse formats increase management complexity.
- Cross-source consistency becomes harder to maintain.

### Data Silos

- Isolated data systems lead to inconsistency and redundancy.
- Breaking silos is necessary for an integrated data view.

### Evolving Data

- Data changes over time with business and market conditions.
- Quality management must adapt continuously.

### Human Error

- Data entry and interpretation errors are common.
- Small errors can propagate and become systemic problems.

### Lack of Comprehensive Data Governance

- Without governance, standards and procedures are unclear.
- Governance provides the structure for sustained quality.

### Complexity of Data Integration

- Merging sources with different schemas and formats introduces errors.

### Inadequate Data Quality Tools

- Weak tooling reduces detection and prevention capability.

### Poor Data Quality Awareness

- If teams undervalue data quality, initiatives are under-prioritized.

### Regulatory Compliance Pressure

- Constantly changing regulations increase quality-management burden.

### Resource Constraints

- Limited time, budget, and skilled staff can block quality improvements.

## Data Anomalies

Data anomalies are irregular values or patterns that differ from expected behavior.

### Types of Data Anomalies

- Point anomalies
- Contextual anomalies
- Collective anomalies

### Point Anomalies

A point anomaly is a single record that significantly deviates from others.

- Typical causes: data entry errors, fraud, or rare events.

Example table:

| Staff_ID | First_Name | Last_Name  | Level | Work_Hour |
| -------- | ---------- | ---------- | ----- | --------- |
| S001     | John       | Smith      | D     | 6         |
| S002     | Kate       | Joyce      | C     | 8         |
| S003     | Mary       | Wen        | D     | 6         |
| S004     | Jenny      | Wood       | D     | 6         |
| S005     | Jon        | Dolly      | E     | 4         |
| S006     | Amy        | Yeewood    | A     | 10        |
| S007     | Addy       | Zhang      | B     | 9         |
| S008     | Allen      | Fan        | B     | 9         |
| S009     | James      | Vu         | A     | 10        |
| S010     | Anddy      | Lee        | D     | 500       |
| S011     | Jane       | Jones      | C     | 8         |
| S012     | Mike       | Giacometti | C     | 8         |
| S013     | Anna       | Nord       | E     | 4         |
| S014     | Sunny      | Johnson    | E     | 4         |
| S015     | Ross       | Hart       | A     | 10        |

### Contextual Anomalies

A contextual anomaly appears abnormal only within a specific context (for example, a particular hour).

| Property | 0:00 | 1:00 | 2:00 | 3:00 | 4:00 | 5:00 | 6:00 | 7:00 | 8:00 | 9:00 | 10:00 | 11:00 | 12:00 | 13:00 | 14:00 | 15:00 | 16:00 | 17:00 | 18:00 | 19:00 | 20:00 | 21:00 | 22:00 | 23:00 |
| -------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| P0001    | 24   | 13   | 7    | 4    | 2    | 6    | 25   | 37   | 47   | 58   | 36    | 43    | 46    | 36    | 35    | 32    | 56    | 68    | 86    | 84    | 94    | 65    | 55    | 34    |
| P0002    | 12   | 21   | 11   | 4    | 5    | 3    | 16   | 24   | 35   | 63   | 66    | 76    | 34    | 42    | 32    | 23    | 34    | 56    | 67    | 86    | 74    | 58    | 34    | 21    |
| P0003    | 34   | 22   | 9    | 3    | 3    | 1    | 11   | 21   | 33   | 21   | 37    | 35    | 23    | 43    | 23    | 29    | 35    | 32    | 30    | 45    | 67    | 84    | 89    | 90    |
| P0004    | 56   | 43   | 21   | 35   | 37   | 32   | 43   | 26   | 11   | 21   | 35    | 14    | 22    | 17    | 16    | 9     | 23    | 97    | 63    | 59    | 66    | 46    | 78    | 89    |

### Collective Anomalies

A collective anomaly is an unusual group pattern, even if individual records seem normal.

| Date     | Merchant     | Amount |
| -------- | ------------ | ------ |
| 3/2/2022 | Tasty Burger | $16.99 |
| 3/2/2022 | Tasty Burger | $16.99 |
| 4/2/2022 | Tasty Burger | $24.99 |
| 4/2/2022 | Tasty Burger | $16.99 |
| 4/2/2022 | KFC          | $18.98 |
| 5/2/2022 | Tasty Burger | $16.99 |
| 6/2/2022 | Tasty Burger | $2.50  |
| 6/2/2022 | Tasty Burger | $16.99 |
| 6/2/2022 | Tasty Burger | $21.99 |
| 6/2/2022 | Tasty Burger | $47.98 |
| 7/2/2022 | Tasty Burger | $16.99 |
| 7/2/2022 | Tasty Burger | $21.98 |
| 7/2/2022 | Tasty Burger | $16.99 |

### Detection Notes

- Detecting anomalies can be difficult in large or complex datasets.
- Methods include statistical techniques, machine learning, and domain-specific rules.
- After detection, root-cause investigation is critical.

## Data Quality Issues

Data quality issues reduce data reliability, usefulness, and decision value.

### Typical Error-Focused Issues

- Incomplete data
- Inaccurate data
- Inconsistent data
- Duplicate data

### Additional Common Issues

- Poor data standardization
- Lack of data timeliness
- Data relevance issues
- Poor data security and privacy
- Complex data structures
- Data accessibility issues

### Source-Based Categorization

- Single-source problems
- Multi-source problems

## Single-Source Problems

### Example Set 1

| Scope       | Problem                         | Dirty Data Example                                                                   | Reason/Remark                     |
| ----------- | ------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------- |
| Attribute   | Illegal values                  | `bdate=30.13.70`                                                                     | Outside valid domain range        |
| Record      | Violated attribute dependencies | `age=22, bdate=12.02.70`                                                             | Age and birth date should match   |
| Record type | Uniqueness violation            | `emp1=(name="John Smith", SSN="123456")`, `emp2=(name="Peter Miller", SSN="123456")` | SSN uniqueness violated           |
| Source      | Referential integrity violation | `emp=(name="John Smith", deptno=127)`                                                | Referenced department not defined |

### Example Set 2

| Scope       | Problem               | Dirty Data Example                    | Reason/Remark                           |
| ----------- | --------------------- | ------------------------------------- | --------------------------------------- |
| Attribute   | Missing values        | `phone=9999-999999`                   | Dummy/unavailable value                 |
| Attribute   | Misspellings          | `city="Liipzig"`                      | Typo or phonetic error                  |
| Attribute   | Embedded values       | `name="J. Smith 12.02.70 New York"`   | Multiple values in one field            |
| Attribute   | Misfielded values     | `city="Germany"`                      | Value placed in wrong field             |
| Record      | Violated dependencies | `city="Redmond", zip=77777`           | City and ZIP should correspond          |
| Record type | Word transpositions   | `"J. Smith"` vs `"Miller P."`         | Free-form ordering inconsistency        |
| Record type | Duplicated records    | `John Smith` and `J. Smith`           | Same entity captured twice              |
| Record type | Contradicting records | Different birth dates for same person | Conflicting values for same entity      |
| Source      | Wrong references      | `deptno=17` but wrong department      | Reference exists but semantically wrong |

From "Data Cleaning: Problems and Current Approaches" (Rahm and Do).

## Multi-Source Problems

### Source Table A

| CID | Name            | Street      | City                 | Sex |
| --- | --------------- | ----------- | -------------------- | --- |
| 11  | Kristen Smith   | 2 Hurley Pl | South Fork, MN 48503 | 0   |
| 24  | Christian Smith | Hurley St 2 | S Fork MN            | 1   |

### Source Table B

| Cno | LastName | FirstName | Gender | Address                                   | Phone/Fax                   |
| --- | -------- | --------- | ------ | ----------------------------------------- | --------------------------- |
| 24  | Smith    | Christoph | M      | 23 Harley St, Chicago IL, 60633-2394      | 333-222-6542 / 333-222-6599 |
| 493 | Smith    | Kris L.   | F      | 2 Hurley Place, South Fork MN, 48503-5998 | 444-555-6666                |

### Consolidated Table

| No  | LName | FName      | Gender | Street           | City       | State | ZIP        | Phone        | Fax          | CID | Cno |
| --- | ----- | ---------- | ------ | ---------------- | ---------- | ----- | ---------- | ------------ | ------------ | --- | --- |
| 1   | Smith | Kristen L. | F      | 2 Hurley Place   | South Fork | MN    | 48503-5998 | 444-555-6666 |              | 11  | 493 |
| 2   | Smith | Christian  | M      | 2 Hurley Place   | South Fork | MN    | 48503-5998 |              |              | 24  |     |
| 3   | Smith | Christoph  | M      | 23 Harley Street | Chicago    | IL    | 60633-2394 | 333-222-6542 | 333-222-6599 |     | 24  |

From "Data Cleaning: Problems and Current Approaches" (Rahm and Do).

## Type-Based Data Quality Problems

### Syntactical Anomalies (Format and Values)

- Lexical errors
  - Spelling and typo issues
- Domain format errors
  - Inconsistent value format across records
- Irregularities
  - Inconsistent units, abbreviations, or conventions

### Semantic Anomalies (Comprehensiveness and Non-Redundancy)

- Integrity constraint violations
- Contradictions across related attributes (for example, AGE vs DOB)
- Duplicate observations of the same entity
- Invalid observations

### Coverage Anomalies (Missingness)

- Missing values
- Missing observations

## Dirty Data

Dirty data commonly appears in three forms:

- Missing data
- Not missing but wrong data
- Not missing and not wrong but unusable data

### Missing Data

- Missing where null should be allowed
- Missing where null should not be allowed

### Not Missing but Wrong Data

- Integrity issues:
  - Data type/range violations
  - Non-null uniqueness violations (duplicates)
  - Referential integrity violations
  - Wrong categorical data
  - Outdated temporal data
  - Inconsistent spatial data
- Data entry errors in a single table:
  - Single-field errors (misspelling, extraneous values)
  - Multi-field errors (wrong field mapping, incorrect derived values)

### Not Missing and Not Wrong but Unusable Data

- Ambiguous abbreviations
- Incomplete context
- Aliases/nicknames
- Encoding inconsistencies
- Representation inconsistencies (precision, fraction, negative sign)
- Unit inconsistencies (currency, time, weight, area)
- Special-character inconsistency in concatenated fields

## Data Quality Management Frameworks

A data quality management framework is a structured approach to ensure data is accurate, complete, reliable, and fit for purpose.

### Core Components

- Data quality dimensions
- Data governance
- Data quality standards
- Data quality assessment
- Data quality monitoring
- Data quality improvement
- Data quality tools and technologies
- Training and awareness
- Compliance and regulatory considerations

### Implementation Notes

- Implementation is iterative and cross-functional.
- It starts with understanding organizational data quality needs.
- Success depends on governance, communication, technology, and continuous improvement.

## The Role of Machine Learning in Data Quality

Machine learning increasingly helps automate and enhance data quality processes.

- Automated error detection
- Data cleansing
- Predictive data quality
- Enhanced data matching and merging
- Natural language processing (NLP)
- Data governance and metadata management
- Data enrichment
- Continuous monitoring and improvement
