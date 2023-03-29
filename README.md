# Data pipeline with neo4j for customer subscription to telecom service
#author george fundi
#setting up the pipeline
### 1. load a file with customer subscribed service
### 2. create node for each customer and service available
### 3. create relationship of type subscribed to service by each customer. 
### 4. the customer node properties are: customer id. service node properties are: service_id. subscribed to relationship between customer and service properties
###   are subscription id, subscription start date, subscription end date,price for the service.
#Transformation done on the data
### 1. ensure the date properties are datetime type and remove any missing values.
