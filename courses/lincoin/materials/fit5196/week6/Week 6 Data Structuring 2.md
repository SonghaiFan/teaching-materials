# FIT5196 Data Wrangling

## Week 6: Data Structuring

Instructor: Jackie Rong  
Faculty of Information Technology, Monash University

## Data Wrangling Tasks (Recap)

- Data discovery
- Data collection
- Data pre-processing
- Data cleaning
- Data structuring
- Data transformation
- Data enrichment
- Data validation

Data structuring is a core step that determines whether data can be accessed, updated, and analyzed efficiently.

## Week 6 Topics

- Overview of data structuring
- Primitive data types
- Non-primitive data types
- Complex data structures
- Key operations on major structures

## What Is Data Structuring

Data structuring is the process of organizing data into systematic formats that support efficient:

- Retrieval
- Update
- Processing
- Management

### Why It Matters in Data Wrangling

- Efficiency: lower computational cost for cleaning and analysis
- Data integrity: better consistency and fewer logic errors
- Scalability: supports larger volumes with acceptable performance

## Types of Data Structures

### 1) Primitive Data Structures

- Integer
- Floating point
- Character
- Boolean

### 2) Non-Primitive Data Structures

- Linear: arrays, lists, stacks, queues
- Non-linear: trees, graphs
- Associative: dictionaries/maps

## Primitive Data Types Summary

| Type | Description | Common Usage |
| --- | --- | --- |
| Integer | Whole numbers | Counting, indexing |
| Floating point | Real numbers with decimals | Scientific and numeric calculations |
| Character | Single text symbol | Text processing |
| Boolean | True/False | Conditions, control flow |

### Primitive Type Notes

- Type-safe operations reduce many runtime errors
- Fast operations due to hardware-level support
- Low memory footprint and fixed size

## Non-Primitive Data Types Summary

| Type | Description | Typical Scenario |
| --- | --- | --- |
| Array | Same-type elements in contiguous memory | Fast indexed access |
| String | Sequence of characters | Text storage and manipulation |
| List/Linked List | Dynamically linked elements | Frequent insert/delete |
| Queue | FIFO structure | Scheduling and buffered processing |
| Dictionary/Map | Key-value pairs | Fast lookup and caching |

## Complex Data Structures

Complex structures combine primitive and non-primitive types to optimize specific operations.

Common structures covered:

- Graphs
- Trees
- Hash tables
- Heaps

## Graphs

A graph consists of nodes (vertices) and connections (edges).

Types:

- Directed graph
- Undirected graph
- Weighted graph

Use cases:

- Social networks
- Transport networks
- Communication routing

## Trees

Trees are hierarchical, acyclic structures with one root and multiple levels of children.

Types mentioned:

- Binary trees
- Binary search trees (BST)
- B-trees
- AVL trees
- Red-black trees
- Suffix trees
- Segment trees
- Trie
- Quad-trees
- k-d trees

## Binary Search Tree (BST)

BST rule:

- Left subtree keys < parent key
- Right subtree keys > (or >= depending on convention) parent key

### BST Operations

- Insertion
- Searching
- Deletion
- Traversal:
  - Inorder
  - Preorder
  - Postorder

### BST Pros and Cons

Advantages:

- Efficient average-case search (balanced tree)
- Ordered structure
- Supports dynamic insert/delete

Limitations:

- Unbalanced trees can degrade performance
- Pointer overhead
- Less suitable without balancing for very large datasets

## B-Tree

A B-tree generalizes BST by allowing more than two children per node.  
It is widely used in storage and database indexing due to good block/page efficiency.

## Hash Tables

A hash table maps keys to values via a hash function.

Core parts:

- Hash function
- Buckets/slots
- Collision resolution (chaining or open addressing)

### Applications of Hash Tables

- Database indexing
- Caching
- Set-like unique membership checks
- Counting/frequency dictionaries
- Associative arrays
- Lookup tables
- User session tracking

### Hash Table Trade-offs

Advantages:

- Near O(1) average lookup/insert/delete
- Flexible key design

Limitations:

- Bad hash function causes collisions and slowdowns
- Collision handling adds memory overhead

## Heaps

A heap is a tree-based structure (usually array-implemented) that maintains heap property.

Types:

- Max-heap: parent >= children
- Min-heap: parent <= children

### Heap Applications

- Priority queues
- Heapsort (O(n log n))
- Graph algorithms (for example, Dijkstra, Prim)

### Heap Operations

- Insert
- Extract max/min
- Heapify

## Week 6 Summary

- Data structuring is foundational to efficient wrangling
- Primitive and non-primitive types are building blocks
- Graphs, trees, hash tables, and heaps solve different access and processing problems
- Choosing the right structure directly affects performance and maintainability

## To-do

- Review Week 6 concepts and examples
- Continue Group Assessment 1
- Attend applied session preparation for Quiz 1
- Prepare for Week 7: Data Quality and Anomalies
