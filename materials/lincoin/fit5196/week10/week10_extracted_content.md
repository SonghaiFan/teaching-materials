FIT5196 DATA WRANGLING
Week 10
Data Integration & Enrichment
By Jackie Rong

Faculty of Information Technology

Monash University

Data Wrangling Tasks (Recap)

In the Data Pre-processing stage, preliminary data preparation tasks are performed to make raw data
more suitable for analysis.

Data
Discovery

• Overview of Data Transformation

• Data Normalisation

• Data Discretisation

• Data Construction

▪ Feature Engineering
▪ Data Sampling

Data
Collection

Data
Storing

Last Week

Data
Transformation

Data
Enrichment

Data Pre-
processing

Data
Cleaning

Data
Validation

Data Transformation

• Data transformation involves cleaning and converting raw data into a format that is more suitable

for analysis.

•

The goal of data transformation is to ensure the data is in usable and efficient format that makes
analysis straightforward and reliable.

• Reasons for data transformation

▪ Fix skewness in data
▪ Enhance data visualisation
▪ Better interpretability
▪ Improve the compatibility of data with assumptions underlying a modelling process

Data Transformation

• Data transformation involves
▪ Data Normalisation
▪ Linear Transformation
▪ Power Transformation
▪ Data Discretisation
▪ Data Construction
▪ Data Reduction

Data Enrichment

• Overview of Data Enrichment
•

Schema Integration
• Data-level Integration

Data Enrichment

• Data enrichment refers to the process of enhancing existing data by appending additional context

or information from external sources.

•

This process enhances the quality, depth, and value of the data, making it more useful for detailed
analysis and informed decision-making.
▪ Contextual Addition: Adding data that provides more insight into the existing data, such as

demographic information, geographic details, or industry-specific metrics.

▪ Quality Improvement: Enhancing the quality of data by adding more accurate or timely

information, which can improve the granularity or accuracy of analysis.

▪ Value Enhancement: Directly increasing the utility of the data for analytical or operational

purposes, making it more comprehensive for decision-making processes.

Data Integration

• Data integration is a crucial component of the data wrangling process, which involves combining

data from different sources to create a unified view.

•

This process is essential for data analysis and decision-making, particularly in environments where
data is collected from multiple sources or systems.
▪ Source Diversity: Data comes from multiple sources, such as different databases, spreadsheets,

or external APIs.

▪ Schema Merging: Integrating various data schemas into a single, unified schema that represents

all data consistently.

▪ Entity Resolution: Identifying and consolidating records that refer to the same entities across

datasets.

▪ Centralization: Often results in a centralized data repository that facilitates easier access and

analysis.

Data Enrichment vs. Data Integration

Purpose

Output

Process

Data Enrichment

Data Integration

Enrichment is about enhancing the
data's value by adding more detailed
information to the existing dataset.

Integration is primarily about combining
data to create a unified database or
dataset, focusing on consistency and
accessibility.

The result of data enrichment is an
enhanced dataset with additional layers
of information.

The result of data integration is a
consolidated dataset from multiple
sources.

Enrichment involves appending relevant
data to existing records to provide
deeper insights.

Integration involves merging and
reconciling data from various sources
into one coherent set, addressing
conflicts in data structure or format.

Data Integration is Challenging

• Heterogeneous data

▪ Data coming from different sources is often developed independently (e.g., different schema,

different objectives)

• Various formats

▪ Text, web logs, social networks, sensors, astronomy, genomics, medical records, surveillance,

etc.

•

Incompatible Taxonomies
▪ Different object identity and separate schema

o Different definitions of a customer, an account, etc.

• Time synchronisation

▪ Each source might have a time window that is different from each other.
▪ Synchronisation of data collected in different time windows

Data Integration is Challenging

• Dealing with legacy data

▪ Historical data stored in legacy form, such as IMS, spreadsheets, and other ad-hoc structure
▪ Combine historical data with modern data

• Abstraction levels

▪ Different data sources might provide data at different level of abstraction,
▪ e.g.,

o suburb level vs. state level
o annual vs. weekly

• Data Quality

▪ Data is often erroneous, and combining data often aggravates the problems. Erroneous data has

potentially devastating impact on the overall quality of the integrated data.

• The number of sources

▪ e.g., web-scale integration.

Applications of Data Enrichment

Google’s knowledge graph

Map mashup: HousingMaps

Map mashup: TrendMaps
shows the latest trend in twitter

Steps of Data Enrichment

Choose appropriate external sources based on
the reliability, accuracy, and relevance of the data
they offer. Common sources include demographic
information, geographic data, social media data,
industry-specific databases, and more.

Select Data
Sources

Define
Objectives

Integrate Data

Merge the external data with your existing
dataset. This might involve complex ETL
(Extract, Transform, Load) processes,
especially if the data structures differ
significantly.

Continuous
Updating

Ensure Data
Quality

Conduct thorough checks to verify the
quality of the enriched data. This includes
validating the accuracy, completeness, and
timeliness of the data.

Determine what specific
information is missing from
your current dataset and what
you need to enhance its value
for particular uses, such as
targeted marketing, customer
relationship management, or
advanced analytics.

Periodically update the enriched
data to maintain its relevance,
especially for dynamically
changing datasets like consumer
behaviour or market trends.

Data Integration Category

Data Enrichment

• Overview of Data Enrichment
•

Schema Integration
• Data-level Integration

Schema

• Relational databases

▪ A schema specifies a set of tables.
▪ A table contains a set of attributes
associated with their data types.

This figure is from http://www.datanamic.com/support/lt-dez005-introduction-db-modeling.html

Schema

• Relational databases

▪ A schema specifies a set of tables.
▪ A table contains a set of attributes
associated with their data types.

• Data models like XML and JSON

▪ A schema is defined as a set of tags,

classes and properties.

Schema

• Relational databases

▪ A schema specifies a set of tables.
▪ A table contains a set of attributes
associated with their data types.

• Data models like XML and JSON

▪ A schema is defined as a set of tags,

classes and properties.

• Data science

▪ A data schema is defined as the

representation of the data arrangement,
relationships and contents.

Why Need Schema Integration?

Schema Mapping

•

The linkage between each data source and the mediate schema is done through semantic mapping
▪ Specifies how attributes in the sources correspond to attributes in the mediated schema (when

such correspondences exist)

▪ Specifies how the different groupings of attributes into tables are resolved.
▪ Specifies how to resolve schema conflict from different sources

Problems with Schema integration

•

Structure conflicts
▪ Inconsistencies in the data
structure among schemas,
which include

o Different data source
origins: Data can be
represented in a structure
form (e.g., XML, HMTL,
JSON, semi-structured, or
completely unstructured
data.

▪ Inconsistencies among the set

of elements inside the
different schemas

Figures are from http://www.urremote.com/untethering-the-queue-2

Problems with Schema integration

• Naming conflicts

▪ homonyms vs synonyms

o The same name is used for

different objects.

o Different names are used for

the same object.

▪ Examples

o Homonyms: ID can refer to

customer ID, product ID, store
ID, etc.

o Synonyms: Customer ID and

Client ID can refer to the same
real-world object, i.e.,
customer/client.

Figure is from "Semantic-Integration Research in the Database community" by AnHai Doan and Alon Y. Halevy

Problems with Schema integration

•

Entity resolution/conflict resolution
▪ Different units:

o Temperature units: Celsius and Fahrenheit
o Currencies

▪ Data type heterogeneity

o Same kind of attributes with different data types

• phone number can be stored as string in one database and integer in another database

▪ Value heterogeneity

o The use of Abbreviations: Professor vs. Prof, Street vs. St, Road vs. Rd

▪ Level of abstraction: different aggregation levels for an attributes

o Address can be split into multiple fields, street number, street name, suburb, city, post-

code, etc.

Problems with Schema integration

•

Entity resolution/conflict resolution
▪ Semantic heterogeneity: differences in meaning and interpretation of data values1

o Naming

• Case sensitivity
• Synonyms/Homonyms
• Acronyms

o Generalisation/Specialisation: one schema may refer to "phone", but the other schema has

multiple elements such as "home phone", "work phone" and "cell phone"

▪ Different points of time

o Fortnight and monthly payment

Schema Matching

•

Semantic matching: relates a set of elements in schema 𝑆 to a set of elements in schema 𝑇.

▪ One-to-One matching

o Movies.title ≈ Items.name
o Movies.year ≈ Items.year
o Product.rating ≈ Items.classification

▪ One-to-Many matching

o Items.price ≈ Products.basePrices ×(1 + Locations.taxRate)

Name-Based Matching

• Name-Based Matcher: compares the names of attributes (or column headers) in the hope that the

names convey the true semantics of the elements.
▪ Split names according to certain delimiters, such as capitalization, numbers, or special symbols.

o ClientName ⇒ Client Name
o saleLocID ⇒ Sale Loc ID

▪ Expand known abbreviations or acronyms

o loc ⇒ location
o cust ⇒ customer
o St ⇒ Street
o DOB ⇒ Date of Birth

▪ Expand a string with its synonyms

o Location ⇒ Address
o Cost ⇒ Price

Name-Based Matching

▪ Expand a string with its hypernyms
o product ⇒book, DVD, etc.

▪ Remove articles, propositions, and conjunctions

o Exclude words like “in”, “at”

Instance-based Matching

• Data-Based Matcher makes use of the data values.

▪ Rule-based matching method

o Handcrafted rules exploit schema information such as element names, data types,

structures, number of sub-elements, and integrity constraints.

o For DVD-vendor database:

• All possible classification: G, PG, PG-13, R, etc
• Given a new attribute, if most of its values appear in the list above.

▪ Advantages

o Relatively inexpensive, do not require training

▪ Disadvantages:

o Cannot exploit data instances effectively (e.g., value format, frequently occurring values,

etc.)

Instance-based Matching

• Data-Based Matcher makes use of the data values.

▪ Learning-based matching method: learning techniques that can exploit both schema and data

information.

o Classification-based methods
o (semi-)automated but Needs training

Data Enrichment

• Overview of Data Enrichment
•

Schema Integration
• Data-level Integration

Data-Level Integration

• Data-Level Integration: related to the integrated contents/values of data not the schema
• Categories

▪ Attribute-level (columns)

o Redundancy
o Correlation
▪ Tuple-level (rows)
o Duplication
o Inconsistency

Attribute-Level Integration

• Problems: combining different data sources might result in a redundant representation
•

Examples
▪ When any of the attributes can be calculated from others

o e.g., annual salary from fortnight payment

▪ When different values represent the same attribute but with different units

o e.g., weight in kg and lb

•

Techniques to find correlation between attributes
▪ Chi-square Test for categorial variable
▪ Correlation Coefficient for numerical attributes

Chi-square test

• Chi-square test for categorial variables

▪ Test for independence compares two variables in a contingency table to see if they are related.
▪ Hypothesis statements:

o Null Hypothesis: The two categorical variables are independent.
o Alternative Hypothesis: The two categorical variables are dependent.

▪ The chi-square test statistic

𝑥2 = ෍
𝑖

2

𝑂𝑖 − 𝐸𝑖
𝐸𝑖

where 𝑂 represents the observed frequency, and 𝐸 is the expected frequency under the null
hypothesis:

𝐸 =

𝑅𝑜𝑤 𝑇𝑜𝑡𝑎𝑙  ×  𝐶𝑜𝑙𝑢𝑚𝑛 𝑇𝑜𝑡𝑎𝑙
𝑆𝑎𝑚𝑝𝑙𝑒 𝑆𝑖𝑧𝑒

Chi-square test

• Chi-square test for categorial variables: Is gender independent of education level?

• Null Hypothesis: Gender and Education

Level are independent.

• Alternative Hypothesis: Gender and

Education Level are dependent

50.886 =

100 × 201
395

𝑥2 =

60 − 50.886 2
50.886

+

54 − 49.868 2
49.868

+ ⋯

= 8.006

Chi-square test

• Chi-square test for categorial variables: Is gender independent of education level?

𝑥2 = 8.006

The degree of freedom:

𝑟 − 1 𝑐 − 1 = 3

The critical value of 𝑥2 at a 5% level of significance: 7.815

Chi-square test

• Chi-square test for categorial variables: Is gender independent of education level?

• 𝑥2 = 8.006 > 7.815 (The critical value of

2 with 3 degree of freedom)

• Reject the null hypothesis and conclude
that the education level depends on
gender at a 5% level of significance

Correlation Coefficient

• Correlation Coefficient, 𝑟 , also called Pearson correlation coefficient

▪ Measures the strength and the direction of a linear relationship between two variables

𝑟 =

𝑛 σ 𝑥𝑦 − (σ 𝑥)(σ 𝑦)

𝑛 σ 𝑥2 − σ 𝑥 2 𝑛 σ 𝑦2 − σ 𝑦 2

▪ The value of 𝑟 is such that −1  < 𝑟 < +1

o Positive correlation: If 𝑥 and 𝑦 have a strong positive linear correlation, 𝑟 is close to +1
o Negative correlation: If 𝑥 and 𝑦 have a strong negative linear correlation, 𝑟 is close to -1.
o No correlation: If there is no linear correlation or a weak linear correlation, 𝑟 is close to 0.

Coefficient of Determination

• Coefficient of determination

▪ The proportion of the variance (fluctuation) of one variable that is predictable from the other

variable.

▪ 0  <   𝑟2 <  1 denotes the strength of the linear association between 𝑥 and 𝑦.
▪ The coefficient of determination is a measure of how well the regression line represents the
data. If the regression line passes exactly through every point on the scatter plot, it would be
able to explain all of the variation. The further the line is away from the points, the less it is able
to explain.

Coefficient of Determination

𝑟 =

𝑛 σ 𝑥𝑦 − (σ 𝑥)(σ 𝑦)

𝑛 σ 𝑥2 − σ 𝑥 2 𝑛 σ 𝑦2 − σ 𝑦 2

= 0.676747624

𝑟2 = 0.676747624 2 = 0.457987347

Coefficient of Determination

• Regression Sum of Squares (SSR) (or explained sum of squares)

𝑛

• Residual Sum of Squares (RSS)

•

Total Sum of Squares (TSS)

• 𝑅2 is defined as

𝑆𝑆𝑅 =   ෍
𝑖=1

ෝ𝑦𝑖 − ത𝑦 2

𝑛

𝑅𝑆𝑆 = ෍
𝑖=1

𝑦𝑖 − ෝ𝑦𝑖

𝑛
2 = ෍
𝑖=1

2
𝑒𝑖

𝑛

𝑇𝑆𝑆 = ෍
𝑖=1

𝑦𝑖 − ത𝑦 2

𝑅2 = 1 −

𝑅𝑆𝑆
𝑇𝑆𝑆

𝑇𝑆𝑆 = 𝑅𝑆𝑆 + 𝑆𝑆𝑅?

Tuple-level Integration

• Duplicates

•

•

•

▪ Two or more rows (i.e., tuples) refer to the same object.

Inconsistent update
▪ Duplicated records are not updated simultaneously.

Issues with tuple-level integration
▪ Formatting convertors
▪ Different naming conventions
▪ ...

Tuple Matching methods
▪ String Matching
▪ Data Matching

String Matching

• Problems:

▪ Given two sets of strings 𝑋 and 𝑌 , find all pairs of strings (𝑥, 𝑦), where 𝑥 ∈ 𝑋 and 𝑦 ∈ 𝑌 , such

that 𝑥 and 𝑦 refer to the same entity.

Figure is from chapter 4 of “Principles of Data Integration”

String Matching

• Methods: Similarity Measures

▪ Sequence-based Similarity Measures: View strings as sequences of characters, compute a cost of transforming

one string into the other.

o Edit Distance
o The Needleman-Wunch measure
o The Affine Gap measure
o The Smith-Waterman measure

▪ Set-based Similarity Measures: View strings as sets or multi-sets of tokens and use set-related properties to

compute similarity scores.
o The Overlap measure
o The TF/IDF measure

▪ Hybrid Similarity Measures: combines sequence-based and set-based measures

o The Generalised Jaccard measure
o The Soft TF/IDF measure

▪ Phonetic Similarity Measure: matches strings based on their sound.

Edit Distance

•

•

The minimum edit distance between two strings

Is minimum number of editing operations
▪ Insertion
▪ Deletion
▪ Substitution

• Needed to transform one to another.

Edit Distance

•

Transform string 𝑥1, … , 𝑥𝑖, … , 𝑥𝑛to 𝑦1, … , 𝑦𝑗, … , 𝑦𝑚
▪ Transform 𝑥1, … , 𝑥𝑖−1into 𝑦1, … , 𝑦𝑗−1 if 𝑥𝑖 = 𝑦𝑗
▪ Transform 𝑥1, … , 𝑥𝑖−1 into 𝑦1, … , 𝑦𝑗−1, then substituting 𝑥𝑖 with 𝑦𝑖 if 𝑥𝑖 ≠ 𝑦𝑖
▪ Deleting 𝑥𝑖, then transform 𝑥1, … , 𝑥𝑖−1 into 𝑦1, … , 𝑦𝑗
▪ Transform 𝑥1, … , 𝑥𝑖 into 𝑦1, … , 𝑦𝑗−1, then insert 𝑦𝑗

Edit Distance

Figure is from chapter 4 of “Principles of Data Integration”

Needleman-Wunch Measure

Figure is from chapter 4 of “Principles of Data Integration”

TF/IDF Measure

Figure is from chapter 4 of “Principles of Data Integration”

Data Matching

• Data Matching is challenging due to variations in

▪ formatting conventions
▪ use of abbreviations, shortening
▪ different naming conventions,
▪ omissions
▪ errors

Figure is from chapter 7 of “Principles of Data Integration”

Data Matching

• Methods

▪ Rules-based method
▪ Learning-based methods
o Supervised learning
o Clustering
o probabilistic approach

Figure is from chapter 7 of “Principles of Data Integration”

Rule-based Data Matching

• A linearly weighted combination of the individual similarity scores between 𝑥 and 𝑦:

𝑛

𝑠𝑖𝑚 𝑥, 𝑦 = ෍
𝑖=1

𝛼𝑖𝑠𝑖𝑚𝑖(𝑥, 𝑦)

• A rule for the example in the figure

𝑠𝑖𝑚 𝑥, 𝑦 = 0.3𝑠𝑛𝑎𝑚𝑒 𝑥, 𝑦 + 0.3𝑠𝑝ℎ𝑜𝑛𝑒 𝑥, 𝑦 + 0.1𝑠𝑐𝑖𝑡𝑦 𝑥, 𝑦 + 0.3𝑠𝑠𝑡𝑎𝑡𝑒(𝑥, 𝑦)

Figure is from chapter 7 of “Principles of Data Integration”

Rule-based Data Matching

Figure is from chapter 7 of “Principles of Data Integration”

Learning-based Data Matching

•

Supervised learning: learn a matching model with training data

𝑇 = { 𝑥1, 𝑦1, 𝑙1 , 𝑥2, 𝑦2, 𝑙2 , … , (𝑥𝑛, 𝑦𝑛, 𝑙𝑛)}

where (𝑥𝑖, 𝑦𝑖) indicates a tuple pair, and 𝑙𝑖 indicates the Boolean label.

▪ Define a set of features 𝑓1, 𝑓2, … , 𝑓𝑚
▪ Convert each training sample  𝑥𝑖, 𝑦𝑖, 𝑙𝑖  into a feature vector
(< 𝑓1 𝑥𝑖, 𝑦𝑖 , 𝑓2 𝑥𝑖, 𝑦𝑖 , … , 𝑓𝑚(𝑥𝑖, 𝑦𝑖) >, 𝑐𝑖)

▪ Apply supervised learning algorithms

Learning-based Data Matching

•

Supervised learning: learn a matching model with training data

Figure is from chapter 7 of “Principles of Data Integration”

Learning-based Data Matching

•

Supervised learning: learn a matching model with training data

Figure is from chapter 7 of “Principles of Data Integration”

Learning-based Data Matching

• Clustering approach: tuples in the same cluster match

▪ The problem of constructing entities(that is, clusters): only tuples within a cluster match.
▪ An iterative process: leverage what we have known so far (in the previous iterations) to build

“better” entities.

▪ Generating a canonical tuple: “merge” all matching tuples within each cluster to construct an

“entity profile”

Figure is from chapter 7 of “Principles of Data Integration”

Summary & To-do List

• Please download and read materials provided on Moodle.
• Review content learnt from Week10.

• Assessments

▪ Read the tasks in Assessment 2 and continue to work on it.

• Next week: Data Validation

