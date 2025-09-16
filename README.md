# Data Pipeline Project: Delimited txt file to Delta Lake

This project demonstrates a complete data engineering workflow, from data extraction and transformation to automated scheduling, using a hybrid local and cloud-based approach. The entire process is version-controlled with Git and hosted on GitHub.

***

## **Features & Workflow**

The project automates a data pipeline to:

* **Extract Data**: Connect to a Csv file to pull raw car sales data.
* **Transform Data**: Clean and analyze the data using the **Pandas** library.
* **Load Data**: Write the processed data into a **Delta Lake** table on **Databricks**, ensuring a reliable and ACID-compliant storage format.
* **Automate**: Schedule the notebook to run every hour using Databricks Jobs.
* **Version Control**: Manage all the source code in a single **GitHub repository**.

***

## **Technologies Used**

* **Python**: The core programming language for the entire pipeline.
* **PyCharm**: The local development environment (IDE) used to write and test the code.
* **Pandas**: A Python library for data manipulation and analysis.
* **PySpark**: A Python library to connect spark engine for data processing.
* **Databricks**: A cloud-based platform used for running Spark jobs, storing data in Delta Lake, and scheduling workflows.
* **Git & GitHub**: Used for version control and collaborative development.

***
