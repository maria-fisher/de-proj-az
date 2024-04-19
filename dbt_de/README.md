# Data processing in dbt and Databricks

#### The tasks completed were as follows:
1. Started a fresh project in dbt for data transformation,
2. Configured dependencies and set up DataBricks on the cloud.
3. Outlined the project structure, with directories for models, tests, and documentation.
4. Ensured proper model dependencies for correct execution order.

#### To connect with DataBricks, 
The DataBricks Command Line Interface (CLI) was installed and configured with the required credentials. 
The connection was verified by listing the file system in the command line.

#### For project initialization, 
The "dbt init" command was used to create a new project. 
Details such as project specifics, database information, DataBricks host, access token, and default schema were provided.

#### Snapshots
Were created using sql files to capture different tables within the data schema. 
These files contain queries to extract data and create source tables stored in the bronze layer and Azure Databricks.
