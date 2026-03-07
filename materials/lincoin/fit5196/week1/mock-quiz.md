# FIT5196 Mock Quiz

## Glossary of Key Terms

- **Data Wrangling**: The process of acquiring, cleaning, structuring, and enriching raw data into a format that is directly usable for analysis. It is a critical preparatory step for data analysis.
- **Data Discovery**: The initial step in data wrangling where data scientists identify and access various data sources relevant to analytical objectives, including assessing their availability, suitability, and quality.
- **Data Collection**: The systematic process of gathering and measuring information on variables of interest from identified sources, ensuring it is relevant, accurate, and robust for analysis needs.
- **Data Pre-processing**: Preliminary data preparation tasks performed to make raw data more suitable for analysis, involving selection (subsetting, sampling) and formatting of datasets.
- **Data Cleaning**: A critical step focused on removing or correcting inaccuracies, inconsistencies, duplicates, or irrelevant data points within datasets to ensure quality and reliability for analysis.
- **Data Transformation**: The process of converting data from its original form into a format or structure more appropriate for analysis, including normalization, aggregation, and feature engineering.
- **Data Enrichment**: Enhancing data by adding additional context or merging it with other data sources to make it more complete and informative, through data integration, augmentation, or attribute/temporal/semantic enrichment.
- **Data Validation**: Ensuring that the data is accurate, consistent, and usable for analysis by performing checks to verify data quality and correctness after cleaning and transformation.
- **Data Storing**: The final step in data wrangling, involving saving the wrangled data in a suitable storage system (for example, databases or data warehouses) for easy access and analysis.
- **Regular Expression (Regex)**: A sequence of characters that defines a search pattern, primarily used for finding, replacing, and extracting information from text, or validating text patterns.
- **Character Sets (`[...]`)**: A regex syntax element that matches any one of several characters specified within the brackets.
- **Negative Character Sets (`[^...]`)**: A regex syntax element that matches any character not in the set specified within the brackets.
- **Shorthand Character Sets (`\d`, `\w`, `\s`)**: Special sequences in regex that represent common character types, such as digits, word characters, or whitespace characters.
- **Repetition (`*`, `+`, `?`, `{m,n}`)**: Regex meta-characters that specify how many times the preceding element should be matched.
- **Grouping (`(...)`)**: Regex syntax element that matches the expression inside and creates a capture group, allowing repetition operators to apply to the entire group or for extraction.
- **Alternation (`|`)**: A regex operator that acts as an "OR", matching any string that matches either the expression before or after it.
- **Raw String (`r"..."`)**: A Python string literal prefix that prevents backslashes from being interpreted as escape characters, simplifying regular expression definitions.
- **Primitive Data Types**: Basic, fundamental data types that represent single values directly supported by hardware, such as integers, floats, Booleans, and characters.
- **Non-Primitive Data Types**: More complex data types built from primitive types, designed to store collections of data or represent relationships, such as arrays, lists, queues, and dictionaries.
- **Array**: A linear non-primitive data structure that stores a collection of elements, typically of the same type, in contiguous memory locations, accessible by an index.
- **List (Linked List)**: A linear non-primitive data structure where elements are not necessarily stored contiguously, but are linked using pointers, allowing dynamic insertion and deletion.
- **Queue**: A linear non-primitive data structure that follows the First-In, First-Out (FIFO) principle, where elements are added to one end and removed from the other.
- **Dictionary (Map/Hash Map)**: A non-primitive data structure that stores pairs of unique keys and values, allowing efficient retrieval of values by their corresponding keys, often implemented using hash tables.
- **Graph**: A complex non-linear data structure consisting of a set of nodes (vertices) connected by edges, used to represent relationships between items.
- **Tree**: A complex non-linear data structure with a hierarchical organization, consisting of a root node and child nodes, with no cycles.
- **Binary Tree**: A type of tree where each node has at most two children.
- **Binary Search Tree (BST)**: A binary tree where each node's key is greater than all keys in its left subtree and less than or equal to all keys in its right subtree, enabling efficient searching.
- **Hash Table**: A complex data structure that implements an associative array abstract data type, using a hash function to map keys to values for efficient storage and retrieval.
- **Heap**: A specialized tree-based data structure that satisfies the heap property and is often used to implement priority queues.

## Week 2 Quiz: Data Wrangling Process & Tasks

### Version A

1. What is the primary purpose of data wrangling?
   - a) To create machine learning models
   - b) To visualize data only
   - c) To make raw data directly usable for analysis
   - d) To store large amounts of data
2. Which of the following is not a goal of data wrangling?
   - a) Improving data quality
   - b) Enriching data
   - c) Increasing data complexity
   - d) Supporting decision-making
3. "Improving consistency, accuracy, and completeness" best describes:
   - a) Data transformation
   - b) Data cleaning
   - c) Data storage
   - d) Data enrichment
4. Which of the following is an example of data discovery?
   - a) Filling missing values
   - b) Identifying electronic health records as a data source
   - c) Encoding categorical data
   - d) Normalizing numerical variables
5. A major challenge in data wrangling is:
   - a) Lack of computing hardware
   - b) Data privacy and security concerns
   - c) Easy interpretability of all datasets
   - d) Abundance of metadata
6. Subsetting and sampling are techniques in:
   - a) Data discovery
   - b) Data collection
   - c) Data pre-processing
   - d) Data validation
7. Which step involves converting data into a new format (for example, XML to CSV)?
   - a) Data cleaning
   - b) Data transformation
   - c) Data pre-processing
   - d) Data validation
8. Aggregating customer purchases to compute their total monthly spend is an example of:
   - a) Normalisation
   - b) Aggregation
   - c) Tokenisation
   - d) Enrichment
9. Which of the following tasks aims to add more context or depth to a dataset?
   - a) Data transformation
   - b) Data enrichment
   - c) Data storing
   - d) Data cleaning
10. Ensuring values fall within acceptable ranges is part of:
   - a) Data validation
   - b) Data storage
   - c) Data discovery
   - d) Data collection
11. Converting "Male/Female" into "M/F" is an example of:
   - a) Encoding
   - b) Formatting
   - c) Normalisation
   - d) Tokenisation
12. In which stage would you typically remove duplicate records?
   - a) Data discovery
   - b) Data cleaning
   - c) Data enrichment
   - d) Data validation
13. A "Pilot test" in data wrangling belongs to:
   - a) Data transformation
   - b) Data collection planning
   - c) Data validation
   - d) Data enrichment
14. Transforming a continuous variable like "Age" into categories such as "Youth, Adult, Senior" is:
   - a) Normalisation
   - b) Standardisation
   - c) Discretisation
   - d) Aggregation
15. Which of these is not a data anomaly?
   - a) Outliers
   - b) Missing values
   - c) Normalised values
   - d) Duplicate records
16. Which step focuses on merging multiple datasets for completeness?
   - a) Data transformation
   - b) Data enrichment
   - c) Data pre-processing
   - d) Data discovery
17. Converting USD prices to AUD is an example of:
   - a) Data cleaning
   - b) Data formatting
   - c) Data enrichment
   - d) Data storing
18. Which of the following storage strategies reduces redundancy in relational databases?
   - a) Denormalisation
   - b) Normalisation
   - c) Aggregation
   - d) Indexing
19. Which task involves designing schema and logical structure for efficient query and retrieval?
   - a) Data enrichment
   - b) Data storing
   - c) Data validation
   - d) Data transformation
20. Backups and recovery planning are part of:
   - a) Data discovery
   - b) Data collection
   - c) Data storing
   - d) Data validation

#### Version A Answer Key

1. c
2. c
3. b
4. b
5. b
6. c
7. b
8. b
9. b
10. a
11. b
12. b
13. b
14. c
15. c
16. b
17. b
18. b
19. b
20. c

### Version B

1. What is data wrangling?
   - a) Building machine learning models
   - b) Visualizing datasets only
   - c) Acquiring, cleaning, structuring, and enriching raw data for analysis
   - d) Collecting images for AI training
2. Which of the following is not a main goal of data wrangling?
   - a) Simplifying access to data
   - b) Reducing data complexity
   - c) Supporting decision making
   - d) Maximizing redundancy
3. Which step comes first in the data wrangling process?
   - a) Data cleaning
   - b) Data discovery
   - c) Data storing
   - d) Data validation
4. The task of finding suitable hospital patient datasets to predict readmission risk is an example of:
   - a) Data discovery
   - b) Data cleaning
   - c) Data enrichment
   - d) Data validation
5. Which of the following is not a challenge in data wrangling?
   - a) Volume and scalability
   - b) Lack of standardization
   - c) Data privacy concerns
   - d) High interpretability of all datasets
6. Data collection must always consider:
   - a) Defining objectives and requirements
   - b) Data sources and quality
   - c) Timeframe, ethics, and budget
   - d) All of the above
7. Choosing only rows from 2000-2010 accident records is an example of:
   - a) Sampling
   - b) Subsetting
   - c) Discretisation
   - d) Normalisation
8. Selecting a smaller group of users from billions of Facebook records for analysis is:
   - a) Subsetting
   - b) Sampling
   - c) Aggregation
   - d) Tokenisation
9. Formatting dates into DD/MM/YYYY and converting currency are tasks of:
   - a) Data cleaning
   - b) Data formatting (pre-processing)
   - c) Data validation
   - d) Data enrichment
10. Removing duplicates, missing values, and outliers belongs to which stage?
   - a) Data enrichment
   - b) Data cleaning
   - c) Data discovery
   - d) Data storing
11. Which of the following is not considered a data anomaly?
   - a) Outliers
   - b) Duplicate data
   - c) Missing values
   - d) Normalised values
12. Adjusting data to have mean = 0 and standard deviation = 1 is called:
   - a) Normalisation
   - b) Standardisation
   - c) Discretisation
   - d) Binning
13. Converting continuous variables into categories such as "Low, Medium, High" is:
   - a) Normalisation
   - b) Discretisation
   - c) Sampling
   - d) Transformation
14. Tokenisation, stemming, and vectorisation are examples of transforming:
   - a) Numeric data
   - b) Text data
   - c) Image data
   - d) Time-series data
15. Which transformation technique would group numeric values into bins?
   - a) Aggregation
   - b) Binning/Bucketing
   - c) Discretisation
   - d) Encoding
16. Enhancing patient data with wearable sensor readings is an example of:
   - a) Data cleaning
   - b) Data enrichment
   - c) Data transformation
   - d) Data validation
17. Verifying that gender codes in a dataset are only "M" or "F" is part of:
   - a) Data discovery
   - b) Data validation
   - c) Data enrichment
   - d) Data cleaning
18. Which task ensures no critical values are missing and data makes logical sense?
   - a) Data transformation
   - b) Data cleaning
   - c) Data validation
   - d) Data storing
19. Choosing databases, warehouses, or cloud solutions for long-term data storage occurs in:
   - a) Data enrichment
   - b) Data storing
   - c) Data discovery
   - d) Data cleaning
20. Backups, indexing, and lifecycle management are part of which task?
   - a) Data storing
   - b) Data transformation
   - c) Data validation
   - d) Data cleaning

#### Version B Answer Key

1. c
2. d
3. b
4. a
5. d
6. d
7. b
8. b
9. b
10. b
11. d
12. b
13. b
14. b
15. b
16. b
17. b
18. c
19. b
20. a

## Week 3 Quiz: Regular Expressions

1. What is a regular expression?
   - a) A function for visualizing data
   - b) A set of symbols describing a text pattern
   - c) A type of programming language
   - d) A database query
2. Which is not a common use of regex?
   - a) Validating emails
   - b) Searching log files
   - c) Normalising numeric data
   - d) Replacing text patterns
3. Which regex matches both `gray` and `grey`?
   - a) `gr[a-z]y`
   - b) `gr[ea]y`
   - c) `gr[^ea]y`
   - d) `gr(e|a)y`
4. In regex, `cat` matches:
   - a) Only `cat` exactly
   - b) The first three letters of `cattle`
   - c) The first three letters of `catfish`
   - d) All of the above
5. True or False: Regex matching is case-sensitive by default.
6. Which regex matches a Victorian car plate (for example, `XRA 123`)?
   - a) `[A-Z]{3}[0-9]{3}`
   - b) `[A-Z0-9][A-Z][A-Z]\s[0-9][A-Z0-9][A-Z0-9]`
   - c) `[0-9]{3}[A-Z]{3}`
   - d) `[^A-Z]{3}\s[0-9]{3}`
7. In regex, `[^b]og` matches:
   - a) `hog`, `dog`
   - b) `bog`
   - c) all words ending with `og`
   - d) `log` and `cog`
8. Which of these is a shorthand character set?
   - a) `\d`
   - b) `\w`
   - c) `\s`
   - d) All of the above
9. The regex `\d{4}` matches:
   - a) Exactly four letters
   - b) Exactly four digits
   - c) Up to four digits
   - d) Four whitespace characters
10. What does the `+` quantifier mean?
   - a) Match 0 or more
   - b) Match 1 or more
   - c) Match 0 or 1
   - d) Match exactly one
11. The regex `oo*ps` will match:
   - a) `ops`
   - b) `oops`, `ooops`, `oooops`
   - c) only `oops`
   - d) nothing
12. The regex `oo+ps` will match:
   - a) `ops` only
   - b) `oops`, `ooops`, `oooops`
   - c) `oops` only
   - d) nothing
13. The regex `oo?ps` will match:
   - a) `ops` and `oops`
   - b) `oops`, `ooops`, `oooops`
   - c) `ops` only
   - d) `oooops`
14. Which regex matches numbers from 2 to 4 digits long?
   - a) `\d{2,4}`
   - b) `\d{2-4}`
   - c) `\d{2|4}`
   - d) `\d(2,4)`
15. Which regex will match `assignment_2016_9` but not `assignment_6_9000`?
   - a) `\w+*\d+*\d+`
   - b) `\w+*\d{2,4}*\d{1,2}`
   - c) `\w+*\d{1,}*\d{1,}`
   - d) `\w+\d_\d`
16. What do parentheses `()` do in regex?
   - a) Indicate alternation
   - b) Indicate a group
   - c) Escape characters
   - d) Denote character classes
17. In regex, the pipe symbol `|` means:
   - a) Concatenation
   - b) Optional
   - c) OR
   - d) Range
18. Which regex matches both `weird` and `wierd`?
   - a) `w(ei|ie)rd`
   - b) `w[ei|ie]rd`
   - c) `w(e|i)rd`
   - d) `w^ei^rd`
19. What does the backslash `\` do in regex?
   - a) Acts as a wildcard
   - b) Escapes special characters
   - c) Indicates repetition
   - d) Acts as OR
20. In Python, why use raw strings `r""` for regex?
   - a) To enable Unicode
   - b) To ignore whitespace
   - c) To suppress escape character interpretation
   - d) To simplify compilation

### Week 3 Answer Key

1. b
2. c
3. b
4. d
5. True
6. b
7. a
8. d
9. b
10. b
11. b
12. b
13. a
14. a
15. b
16. b
17. c
18. a
19. b
20. c

## Week 4 Quiz: EDA & Pre-processing

1. What is the main purpose of EDA (Exploratory Data Analysis)?
   - a) To clean the data
   - b) To build predictive models
   - c) To understand patterns, anomalies, and relationships in data
   - d) To collect raw data
2. Which of the following is not a common data type?
   - a) Numerical
   - b) Categorical
   - c) Image
   - d) HTML
3. Discrete data refers to:
   - a) Countable values like number of students
   - b) Any real number within a range
   - c) Data with infinite precision
   - d) Continuous variables
4. In EDA, which measure of central tendency is least affected by outliers?
   - a) Mean
   - b) Median
   - c) Mode
   - d) Variance
5. The range of a dataset is defined as:
   - a) The middle value of the ordered list
   - b) The difference between max and min values
   - c) The square root of variance
   - d) The most frequent value
6. Which of the following is a measure of data dispersion?
   - a) Mean
   - b) Mode
   - c) Variance
   - d) Median
7. Standard deviation is:
   - a) The square of variance
   - b) The square root of variance
   - c) Half the variance
   - d) The average value
8. Which visualization is best for showing distribution of numerical data?
   - a) Histogram
   - b) Pie chart
   - c) Line chart
   - d) Scatter plot
9. Boxplots display:
   - a) Central tendency only
   - b) Five-number summary and potential outliers
   - c) Only variance and standard deviation
   - d) Only mean
10. Which plot is best for showing correlation between two numerical variables?
   - a) Scatter plot
   - b) Box plot
   - c) Histogram
   - d) Pie chart
11. A heatmap is useful for:
   - a) Showing word frequency
   - b) Displaying correlation matrix
   - c) Showing standard deviation
   - d) Visualising categorical proportions
12. In text data analysis, syntax refers to:
   - a) The meaning of words
   - b) The structure of language and grammar rules
   - c) The frequency of words
   - d) The context of sentences
13. In text data analysis, semantics refers to:
   - a) The ordering of characters
   - b) The meaning of words in context
   - c) The punctuation of text
   - d) The grammar of sentences
14. Which encoding method creates binary columns for each category?
   - a) Label encoding
   - b) One-hot encoding
   - c) Vector encoding
   - d) Count encoding
15. Label encoding is most suitable when:
   - a) Categories have no order
   - b) Categories have a meaningful order
   - c) There are too many categories
   - d) Data is continuous
16. Which method converts documents into token count vectors?
   - a) Count Vectorizer
   - b) Label Encoding
   - c) One-hot Encoding
   - d) Word Embedding
17. Breaking text into words, subwords, or characters is called:
   - a) Normalisation
   - b) Tokenisation
   - c) Encoding
   - d) Parsing
18. Removing words like `the`, `a`, and `however` from text is:
   - a) Lemmatization
   - b) Stemming
   - c) Removing stop words
   - d) Case normalization
19. Converting `Watches -> Watch` or `Parties -> Party` is an example of:
   - a) Tokenisation
   - b) Stemming
   - c) Lemmatization
   - d) Normalisation
20. Using context and part-of-speech to reduce words to dictionary form (for example, `better -> good`) is:
   - a) Tokenisation
   - b) Stemming
   - c) Lemmatization
   - d) Encoding

### Week 4 Answer Key

1. c
2. d
3. a
4. b
5. b
6. c
7. b
8. a
9. b
10. a
11. b
12. b
13. b
14. b
15. b
16. a
17. b
18. c
19. b
20. c

## Week 5 Quiz: Data Discovery & Collection

1. What is the main purpose of data discovery?
   - a) To clean raw data
   - b) To identify and understand data sources for analysis
   - c) To store data in databases
   - d) To visualize correlations
2. Which of the following is not a role of data in modern decision-making?
   - a) Strategic planning
   - b) Risk management
   - c) Personal opinion validation
   - d) Customer insight
3. Which is a challenge in data discovery?
   - a) High interpretability
   - b) Dynamic and evolving data
   - c) Abundance of metadata
   - d) Automatic standardization
4. Using government census data in your project is an example of:
   - a) Primary data
   - b) Secondary data
   - c) Quantitative data
   - d) Qualitative data
5. Which is an advantage of secondary data?
   - a) Perfectly fits research questions
   - b) Always high quality
   - c) Time and cost efficiency
   - d) Guaranteed accessibility
6. A dataset collected directly through surveys is considered:
   - a) Secondary data
   - b) Primary data
   - c) Derived data
   - d) Structured data
7. Quantitative data is best described as:
   - a) Observed but not measurable
   - b) Descriptive and conceptual
   - c) Numerical and measurable
   - d) Textual or visual
8. Which of the following is qualitative data?
   - a) Age of students
   - b) Number of patients
   - c) Customer reviews
   - d) Temperature readings
9. A survey questionnaire is a method of collecting:
   - a) Structured data
   - b) Semi-structured data
   - c) Unstructured data
   - d) Secondary data
10. Which is not a method for structured data collection?
   - a) Relational databases
   - b) APIs
   - c) Web scraping
   - d) Sentiment analysis
11. Text mining and NLP are used for:
   - a) Structured data
   - b) Unstructured data
   - c) Semi-structured data
   - d) Metadata only
12. Collecting image and video data requires attention to:
   - a) Annotation and bias
   - b) Diversity and resolution
   - c) Legal compliance
   - d) All of the above
13. Social media and web content collection faces challenges such as:
   - a) Static content only
   - b) API access changes and noise
   - c) Lack of bias
   - d) Universal accessibility
14. Which is a method for semi-structured data collection?
   - a) SQL queries
   - b) JSON and XML extraction
   - c) Web scraping news sites
   - d) NLP text analysis
15. Emails and communication logs are examples of:
   - a) Structured data
   - b) Semi-structured data
   - c) Unstructured data
   - d) Secondary data
16. Metadata that describes the origin of data is called:
   - a) Technical metadata
   - b) Descriptive metadata
   - c) Provenance metadata
   - d) Usage metadata
17. What does data cataloging achieve?
   - a) Automatic cleaning of data
   - b) A searchable inventory of datasets
   - c) Visualization of correlations
   - d) Data normalisation
18. Implementing GDPR compliance in data collection falls under:
   - a) Data cleaning
   - b) Data profiling
   - c) Security and compliance checks
   - d) Data visualization
19. Which activity belongs to data profiling and assessment?
   - a) Data lineage documentation
   - b) Understanding structure and quality of data
   - c) Adding demographic attributes
   - d) Encryption of files
20. Which ethical principle requires participants to know why their data is collected?
   - a) Beneficence
   - b) Transparency & informed consent
   - c) Fairness
   - d) Anonymisation

### Week 5 Answer Key

1. b
2. c
3. b
4. b
5. c
6. b
7. c
8. c
9. a
10. d
11. b
12. d
13. b
14. b
15. b
16. c
17. b
18. c
19. b
20. b

## Week 6 Quiz: Data Structuring

1. What is the primary goal of data structuring?
   - a) To visualise data
   - b) To organise raw data into usable formats
   - c) To collect data from APIs
   - d) To remove outliers
2. Which of the following is structured data?
   - a) Tweets
   - b) A relational database table
   - c) Handwritten notes
   - d) Video recordings
3. JSON and XML are examples of:
   - a) Structured data formats
   - b) Semi-structured data formats
   - c) Unstructured data formats
   - d) Normalised data formats
4. Which is an example of unstructured data?
   - a) SQL tables
   - b) Financial transaction logs
   - c) Images and audio files
   - d) Normalised databases
5. Which step usually comes first in structuring unstructured data?
   - a) Normalisation
   - b) Feature extraction
   - c) Data storage
   - d) Aggregation
6. Which of the following is a schema in data structuring?
   - a) A rule for tokenisation
   - b) A predefined framework for organising data
   - c) A graphical dashboard
   - d) A text mining algorithm
7. Star schema and snowflake schema are commonly used in:
   - a) Machine learning
   - b) Data warehouses
   - c) Data preprocessing
   - d) API design
8. The main difference between star schema and snowflake schema is:
   - a) Snowflake schema has normalized dimension tables
   - b) Star schema has multiple fact tables
   - c) Snowflake schema avoids redundancy completely
   - d) Star schema cannot be queried
9. Fact tables usually contain:
   - a) Descriptive metadata
   - b) Numerical measures and foreign keys
   - c) Raw unprocessed data
   - d) Only categorical attributes
10. Dimension tables typically contain:
   - a) Aggregated metrics
   - b) Contextual information like time, geography, product details
   - c) API keys
   - d) Normalised values only
11. A key benefit of data normalisation is:
   - a) Increasing redundancy
   - b) Reducing data duplication and inconsistency
   - c) Improving web scraping
   - d) Adding metadata
12. Denormalisation is used to:
   - a) Increase query speed at the cost of redundancy
   - b) Remove duplicate attributes
   - c) Create standardised formats
   - d) Enhance data security
13. Which of the following is not a benefit of structured data?
   - a) Easier storage and retrieval
   - b) Standardised format
   - c) Limited scalability with very large datasets
   - d) Simple integration with BI tools
14. Which SQL command is used to create a new table?
   - a) CREATE TABLE
   - b) ADD TABLE
   - c) NEW TABLE
   - d) FORM TABLE
15. Which SQL clause is used to filter rows based on conditions?
   - a) ORDER BY
   - b) WHERE
   - c) GROUP BY
   - d) HAVING
16. Which SQL operation combines rows from two or more tables based on a related column?
   - a) UNION
   - b) JOIN
   - c) SELECT
   - d) FILTER
17. Which SQL clause is used to group rows with the same values?
   - a) SELECT
   - b) GROUP BY
   - c) ORDER BY
   - d) DISTINCT
18. Which of the following best describes a foreign key?
   - a) A unique identifier within its own table
   - b) A reference to a primary key in another table
   - c) An index for faster searching
   - d) A composite attribute
19. In ER diagrams, relationships are typically represented by:
   - a) Rectangles
   - b) Diamonds
   - c) Ovals
   - d) Arrows
20. In ER diagrams, attributes are usually represented by:
   - a) Rectangles
   - b) Diamonds
   - c) Ovals
   - d) Triangles

### Week 6 Answer Key

1. b
2. b
3. b
4. c
5. b
6. b
7. b
8. a
9. b
10. b
11. b
12. a
13. c
14. a
15. b
16. b
17. b
18. b
19. b
20. c
