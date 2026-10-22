# Insurance Data Pipeline

## Project Overview

The Insurance Data Pipeline is a Python-based data engineering project developed to automate the processing of insurance-related data. The pipeline ingests raw data from multiple sources, performs data preprocessing and transformation, and generates structured datasets suitable for analysis and reporting.

The project is designed to provide a systematic approach to handling insurance data related to customers, policies, claims, payments, and agents while maintaining data quality, traceability, and organized data storage.

## Objectives

The primary objectives of this project are:

- Automate the ingestion of raw insurance data
- Perform data validation and preprocessing
- Transform raw datasets into structured and analysis-ready formats
- Maintain separate stages for ingestion, preprocessing, curated data, and retention
- Generate Parquet files for efficient data storage and analysis
- Maintain processing logs and audit information
- Archive processed data for better data lifecycle management
- Generate key business metrics from the processed datasets

## Technologies Used

Python

Pandas

PyArrow

JSON

Parquet

File Handling

Data Cleaning

Data Transformation

Logging and Auditing

## Data Sources

The pipeline processes the following insurance data entities:

Customers

Policies

Claims

Payments

Agents

The input data is provided in JSON format and processed through different stages of the pipeline.

## Data Pipeline Architecture

The pipeline follows a structured processing workflow:

```text
Raw JSON Data
      |
      v
Data Ingestion
      |
      v
Data Preprocessing
      |
      v
Data Transformation
      |
      v
Curated Data
      |
      v
Semantic Data
      |
      v
Parquet Output
      |
      v
Analysis and Reporting
```

## Project Structure

```text
devInsureDataPipeline/
|
|-- config/
|   |-- control_files/
|
|-- data/
|   |-- ingestion/
|   |-- preprocessed/
|   |-- curated/
|   |-- semantic/
|   |-- retention/
|
|-- logs/
|
|-- src/
|   |-- ingestion_manager.py
|   |-- preprocessing_engine.py
|   |-- transformation_engine.py
|   |-- retention_manager.py
|   |-- audit_logger.py
|   |-- utils.py
|
|-- main.py
|-- requirements.txt
```

## Core Components

### Data Ingestion

The ingestion component manages the collection and initial processing of raw insurance data. It handles datasets related to customers, claims, policies, payments, and agents.

### Data Preprocessing

The preprocessing component performs data cleaning and preparation to ensure that the datasets are consistent and suitable for further processing.

### Data Transformation

The transformation component converts preprocessed data into structured and analysis-ready datasets. It also derives relevant business metrics from the available insurance data.

### Retention Management

The retention component manages processed files and supports organized storage and archiving of historical data.

### Audit Logging

The audit logging component records important processing activities and pipeline execution details to support monitoring and traceability.

## Key Business Metrics

The pipeline generates important insurance-related metrics, including:

```text
Total Customers
Total Policies
Total Claims
Total Claim Amount
Total Premium
```

These metrics can be used for further analysis, reporting, and business decision-making.

## Installation

Clone the repository using Git:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd devInsureDataPipeline
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Execution

Run the main pipeline using:

```bash
python main.py
```

The pipeline processes the available input data and generates the required outputs in the designated data directories.

## Skills Demonstrated

This project demonstrates practical knowledge of:

Python programming

Pandas and data manipulation

Data ingestion

Data preprocessing

Data cleaning

Data transformation

JSON data processing

Parquet data handling

File and directory management

Data pipeline development

Logging and auditing

Data lifecycle and retention management

Business metric generation

## Project Outcome

The project provides an automated and structured approach to processing insurance datasets. It reduces manual data preparation, improves consistency across datasets, and produces structured outputs that can be used for downstream analytics and reporting.

## Author

Prabha Shelake

B.Sc. Information Technology

Aspiring Data Analyst
