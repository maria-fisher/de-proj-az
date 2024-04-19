# To work on data processing in dbt

#### The following tasks were performed:
1. Create a new project in dbt for data transformation,
2. Establish dependencies, and configure connections with DataBricks on the cloud. This involves setting up a project in dbt specifically for data transformation tasks.
3. Define the project structure, including directories for models, tests, and documentation.
4. Additionally, establish dependencies between different models to ensure the correct order of execution.
5. Finally, configure connections with DataBricks on the cloud to access the necessary data sources.


#### Set up the DataBricks CLI to connect with DataBricks
1. In order to connect with DataBricks, you will need to set up the DataBricks Command Line Interface (CLI).
This involves installing the CLI and configuring it with the necessary credentials.
2. Once set up, you can test the connection to DataBricks and verify that you can successfully list the file system,
which allows you to access and manipulate files stored in DataBricks.

#### Initialize the project 
1. Starting a new project by using the "dbt init" command, provide project details, database information, DataBricks host, access token, and default schema.
This command sets up the necessary files and directories for your project. During initialization, you will need to provide project details such as the project name and description,
as well as database information, including the DataBricks host and access token. You will also need to specify the default schema to be used for your project.

#### Snapshots 
I have created sql files to capture snapshots of different tables within the data schema,  
These sql files contain the necessary queries to extract the data and create the source tables that will be stored in the bronze layer and Azure Databricks.
