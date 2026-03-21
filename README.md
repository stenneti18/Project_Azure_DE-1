# Spotify End-To-End Azure Data Engineering Project

## Project Overview
This is a comprehensive end-to-end portfolio project designed to provide a thorough mastery of the Azure data stack.

Approached with the same rigor as a real-world organizational project, it transitions through the complete data engineering lifecycle—from dynamic data ingestion and big data processing to building sophisticated dimensional models and implementing CI/CD with industry standards.

The project is designed to be accessible for beginners while providing high-level technical challenges for experienced developers.

## Architecture
The project follows the **Medallion Architecture**, which is a standard for organizing data through three distinct layers:

- **Bronze (Raw):** Dynamic ingestion of raw data from cloud-hosted sources
- **Silver (Enriched):** Processing data using modern frameworks like Spark Structured Streaming and Autoloader
- **Gold (Curated):** Final star schema and dimensional models built using Delta Live Tables (DLT) and Lakeflow pipelines

## Tech Stack

- **Cloud Provider:** Azure
- **Data Ingestion:** Azure Data Factory (ADF)
- **Data Storage:** Azure Data Lake Storage (ADLS) Gen2
- **Database:** Azure SQL Database
- **Data Processing:** Azure Databricks, Spark Structured Streaming, and Autoloader
- **Data Governance:** Unity Catalog (Metastore, Catalogs, and Schemas)
- **Transformation Framework:** Delta Live Tables (DLT) and Lakeflow Pipelines
- **CI/CD:** GitHub and Databricks Asset Bundles (DAB)
- **Monitoring:** Azure Logic Apps for automated email alerts
- **Languages:** Python (PySpark), SQL, and Jinja templating

## Key Features & Requirements

- **Incremental Data Loading:** Pipelines process only new data
- **Backfilling Capabilities:** Back-dated refresh support
- **Metadata-Driven Pipelines:** Jinja templating for dynamic SQL
- **Slowly Changing Dimensions (SCD):** SCD Type 2 implementation
- **Data Quality Checks:** DLT Expectations
- **Custom Python Utilities:** Reusable modular code

## Implementation Details

### 1. Environment Setup
- Azure Resource Group organization
- ADLS Gen2 with Hierarchical Namespace
- Unity Catalog with Metastore

### 2. Data Ingestion (Bronze Layer)
- Azure SQL Database as source
- JSON watermarking for CDC
- Parameterized pipelines and For-Each loops

### 3. Big Data Processing (Silver Layer)
- Autoloader for incremental ingestion
- PySpark transformations
- Delta Tables in Unity Catalog
- Jinja templating for SQL

### 4. Dimensional Modeling (Gold Layer)
- Star Schema:
  - Dimensions: *DimUser, DimTrack, DimDate*
  - Fact: *FactStream*
- SCD Type 2 using `APPLY CHANGES INTO`

### 5. CI/CD & Monitoring
- GitHub version control
- Databricks Asset Bundles (DAB)
- Azure Logic Apps alerting
