# Project ZoomCamp - 2024 

The Data Engineering couse by DataTalksClub ZoomCamp has been transformative, providing invaluable insights and essential skills for contemporary data engineering positions.
We explored concepts like data pipelines, ETL processes, and cloud-based architectures, and applied our knowledge through a hands-on project. I have a deeper comprehension of
data engineering fundamentals and the confidence to address complex data-related issues after the ZoomCamp course. 
I appreciate the guidance from our instructors and peers and are excited to utilize our newly acquired skills in future ventures.
Thank you DataTalksClub!

## The main goal of this data engineering project is to simulate environmental data gathered by sensors in order to analyze the risk of mycotoxins.
### Problem:
Mycotoxins, toxic compounds produced by certain fungi, pose a significant risk to human and animal health. 
These toxins can contaminate various food and feed crops, leading to serious health problems upon ingestion. 

### Major Fungi, Mycotoxins, and Associated Problems:

| Fungi         | Mycotoxin      | Health Problems                      |
|---------------|----------------|--------------------------------------|
| Aspergillus   | Aflatoxins     | Liver damage, carcinogenic effects   |
| Fusarium      | Fumonisins     | Neural tube defects, cancer          |
| Fusarium      | Deoxynivalenol | Gastrointestinal issues, vomiting    |
| Penicillium   | Ochratoxin A   | Kidney damage, immune suppression    |

### Data source 
I have created synthetic environmental data for this project to simulate sensor readings. 
The datasets I generated simulate various environmental conditions such as temperature, humidity, water activity, and CO2 levels.
These environmental data are crucial in providing insights into the potential risk of fungus development and mycotoxin contamination. 
You can find the code to create the datasets in the 'data' folder.

### Project setup 
This project was create on the Azure cloud platform involved designing a three-layer architecture consisting of bronze, silver, and gold layers. 
The bronze layer served as the raw data storage, the silver layer as the cleaned and transformed data storage, and the gold layer as the final processed data storage.

### IoC
The infrastructure needed for the project was created with Terraform. 

### Data orchestration
For data orchestration, I used Azure Data Factory, because it is possible to automate and schedule the movement of data between different layers of the architecture.


![de-proj-az33](https://github.com/maria-fisher/de-proj-az/assets/33252792/87262906-9df5-48af-9b93-513af2a87f9f)


### Data transformation
For data transformation, I employed dbt-databricks python library, a combination of dbt (data build tool) and Databricks, a unified analytics platform.
dbt-databricks allowed us to transform the data in the silver layer into a format suitable for analysis and reporting in the gold layer. 
This transformation process involved cleaning, aggregating, and structuring the data to make it more accessible and useful for stakeholders.

# Dashboard 

![de-proj-az1](https://github.com/maria-fisher/de-proj-az/assets/33252792/5b68e64a-58e6-4b3c-bf2e-f83c4b737d96)


