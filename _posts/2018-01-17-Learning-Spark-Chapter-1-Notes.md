---
layout: post
title:  "Learning Spark Chapter 1 Notes"
date:   2018-01-17
desc: "Reading notes of Learning Spark Chapter 1"
keywords: "Spark,Hadoop,Chapter 1,Learning Spark,blog,easy"
categories: []
tags: [Spark,Notes]
icon: icon-html
---
### 1.  What is spark?
Apache Spark is an open source **cluster computing system** that makes data analytics fast to write and fast to run. Spark can help to tackle big datasets quickly through simple APIs in Python, Java, and **Scala**. It can help to solve problems ranging from: **interactive queries, streaming, machine learning, and graph processing**.
<br><br>
<br><br>
![enter image description here](https://spark.apache.org/images/spark-stack.png)
<br><br>
### 2. Who should read the book?
 * Data scientist: Use the same mathematical approaches to solve problems **much faster and on a much larger scale**.
 * Software engineers: Know how to **set up a Spark cluster**, use the Spark shell, and write Spark applications to solve **parallel processing problems.** 

All the code in the book: https://github.com/databricks/learning-spark
<br><br>
### 3. Spark features overview
 * Spark beats MapReduce not only because it uses in-memory computations but it is more efficient in computing in hard drive too.
 * Spark reduces the management burden of maintaining separate tools.
 * Spark has simple APIs rich libraries.
 * Spark can run in Hadoop clusters and access any Hadoop data source, including Cassandra.
 <br><br>
### 4. Spark components
Reasons for this tight integration: 
 * Top level components benefits from lower level ones; 
 * Costs include deployment, maintenance, testing, support, etc are minimized.  
 * Able to run different tasks on the same data at the same time. 
![enter image description here](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/assets/lnsp_0101.png)
<br><br>
#### Spark core
 * Contains the basic functionality of Spark, including components for task scheduling, memory management, fault recovery, interacting with storage systems;
 * Spark Core is also home to the API that defines resilient distributed data‐sets (RDDs), which are Spark’s main programming abstraction. **One Side note of RDD**: RDDs represent a collection of items distributed across many compute nodes that can be ***manipulated in parallel***. 
 <br><br>
#### Spark SQL
 * Spark’s package for working with structured data.
 * Spark SQL supports many sources of data, including Hive tables, Parquet(https://parquet.apache.org/), and JSON. 
 * It also allows intermix SQL queries with the programmatic data manipulations supported by RDDs in Python, Java, and Scala all within a single application.
 <br><br>
#### Spark Streaming
 * A Spark component that enables processing of live streams of data (e.g. logfiles from web servers).
 <br><br>
#### MLlib
 * A library containing common machine learning functionality.
 * Suports algorithms including classification, regression, clustering, and collaborative filtering, as well as supporting functionality such as model evaluation and data import.
 * It also provides some lower-level ML primitives, including a generic gradient descent optimization algorithm. 
 <br><br>
#### GraphX
 * A library for manipulating graphs (e.g., a social network’s friend graph) and performing graph-parallel computations.
 * GraphX also provides various operators for manipulating graphs (e.g., subgraph and mapVertices) and a library of common graph algorithms (e.g., PageRank and triangle counting).
 <br><br>
#### Cluster Managers
 * Spark runs over a variety of cluster managers, including **Hadoop YARN**, **Apache Mesos**, and a simple cluster manager included in Spark itself called the **Standalone Scheduler.**
 <br><br>
### 5. Storage Layers for Spark
* Spark can create distributed datasets from any file stored in the Hadoop distributed filesystem (HDFS) or other storage systems supported by the Hadoop APIs (including your local filesystem, Amazon S3, Cassandra, Hive, HBase, etc.). 
*  Spark does not require Hadoop; it simply has support for storage systems implementing the Hadoop APIs.
<br><br>
### 6. A brief history of Spark
 * Spark started in 2009 as a research project in the UC Berkeley RAD Lab, later to become the AMPLab.
 * The researchers in the lab had previously been working on Hadoop Map‐Reduce, and observed that MapReduce was inefficient for iterative and interactive computing jobs. 
 * After its creation in 2009, Spark was already 10–20× faster than MapReduce for certain jobs.
 * Spark was first open sourced in March 2010, and was transferred to the Apache Software Foundation in June 2013, where it is now a top-level project.
 * Till today, lots lots of big companies use Spark.(http://spark.apache.org/powered-by.html)
