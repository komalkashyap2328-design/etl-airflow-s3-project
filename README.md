# 🚀 E-Commerce Data Engineering Pipeline

## 📌 Overview

Designed and implemented an end-to-end data engineering pipeline to process and transform real-world e-commerce transaction data.
The pipeline ingests raw CSV data, performs data cleaning and transformation, and loads structured data into a PostgreSQL database for downstream analytics.

---

## 🧰 Tech Stack

* **Programming:** Python (Pandas)
* **Database:** PostgreSQL
* **Containerization:** Docker
* **Query Language:** SQL

---

## 🔄 Pipeline Architecture

**Source → Processing → Storage**

1. **Extract**

   * Ingested raw e-commerce dataset from Kaggle (CSV format)

2. **Transform**

   * Removed null values and duplicates
   * Filtered invalid records (e.g., negative quantities)
   * Converted data types (e.g., datetime parsing)
   * Engineered new feature: `TotalPrice = Quantity × UnitPrice`

3. **Load**

   * Loaded processed data into PostgreSQL using `psycopg2`
   * Designed relational table schema for structured storage

---

## 📊 Key Highlights

* Built a **production-style ETL pipeline** from scratch
* Handled **real-world data issues** (encoding errors, missing values, inconsistencies)
* Implemented **database integration and batch insertion logic**
* Containerized workflow using Docker for environment consistency

---

## ▶️ Execution Steps

1. Place dataset in the `/data` directory
2. Run the ETL pipeline:

```bash
python3 etl/etl_pipeline.py
```

---

## 📈 Business Value

* Enables structured storage of raw transactional data
* Supports downstream analytics such as:

  * Revenue analysis
  * Customer behavior insights
  * Sales trend tracking

---

## 🏁 Outcome

Successfully developed a scalable and modular ETL pipeline that simulates real-world data engineering workflows, demonstrating strong proficiency in data processing, database management, and system design.

---

## 🔮 Future Enhancements

* Automate pipeline using Apache Airflow
* Integrate cloud storage using AWS S3
* Optimize performance for large-scale datasets

---

