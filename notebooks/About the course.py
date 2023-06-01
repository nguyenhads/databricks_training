# Databricks notebook source
# MAGIC %md
# MAGIC # Overview
# MAGIC ## Course information
# MAGIC * Link: [coursera link](https://www.coursera.org/learn/apache-spark-sql-for-data-analysts/home/week/1)

# COMMAND ----------

# MAGIC %md
# MAGIC ## What is big data
# MAGIC * The massive of data that is being generated every second of every day
# MAGIC * 5V
# MAGIC   * Volume (of data)
# MAGIC   * Velocity (the speed new data is gnerated and moves)
# MAGIC   * Variety (different types and cources of data)
# MAGIC   * Varacity (The quality and accuracy of data)
# MAGIC   * Value (what is the value from data for the business)
# MAGIC
# MAGIC ## Commond struggles with big data
# MAGIC * Eg: Create a dashboard showing customer transaction data
# MAGIC   * Hundreds of data files
# MAGIC   * Various data sources to pull from
# MAGIC   * Lots of different formats to contend with
# MAGIC   * Time limmited
# MAGIC
# MAGIC ## Big Data Needs
# MAGIC * Collecting - Storing - Using data

# COMMAND ----------

# MAGIC %md
# MAGIC ## Apache Spark
# MAGIC * Distributed computing engine
# MAGIC   * `Data -> Driver -> Distribute to many workers`
# MAGIC * Work with a variety of data sources and storage formats
# MAGIC * Accessible from multiple language APIs
# MAGIC * Characteristic of Spark
# MAGIC   * Connect to multiple data stores and BI tools
# MAGIC     * Eg: delta lake, databricks, power bi, sql database, cloud storage, tableau, redash
# MAGIC   * Accessible from multiple language APIs
# MAGIC     * python, sql, r, scala
# MAGIC
# MAGIC #### Spark SQL
# MAGIC * Spark library for structured data preprocessing
# MAGIC * Allows us to use SQL to access Spark
# MAGIC * Ease of use (easy read and write in many kind of format)
# MAGIC * Optimized queries
# MAGIC * Combine with other languages like python, scala, r in a notebook

# COMMAND ----------


