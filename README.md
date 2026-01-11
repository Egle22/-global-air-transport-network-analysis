# Instructions for Running the Code

This document explains how to reproduce all steps of the analysis.

## 1. Install Neo4j Desktop and create a local database

1. Download Neo4j Desktop:  
   https://neo4j.com/download/
2. Install and open the application.
3. Create a **new local instance**.
4. Use latest stable Neo4j version.

## 2. Install the APOC and GDS plug-ins

1. Go to the instance page in Neo4j Desktop.
2. Under **Plugins**, install:
   - **APOC** (Awesome Procedures On Cypher)
   - **GDS** (Graph Data Science Library)
3. Restart the local instance.

## 3. Place the dataset in the import folder

1. In Neo4j Desktop, open your database.  
2. Click **“…” → Open Folder → Import”**.
3. Copy the provided OpenFlights folder into this folder.

## 4. Import the Cypher code from the provided file

1. Start your database.  
2. On the left click on **Query**.
3. Then click on **Open saved Cypher panel**.
4. Choose **Import saved Cypher** and choose the cypher_queries.csv.
5. Run the queries, starting with the import script.

## 5. Code organisation

All queries are documented and grouped by the research question they answer:

### **RQ1 – Identifying global hubs**
- Degree centrality  
- PageRank  
- Airline airport coverage  
- Airline dominance at airports  
- Airline diversity per airport  

### **RQ2 – Distribution of connectivity across countries**
- International reach per country  
- Concentration ratios (CR5, CR10, CR20, CR50)  
- Lorenz curve and Gini coefficient  

### **RQ3 – Identifying bridging airports**
- Betweenness centrality  
- Louvain community detection  
- Counting how many communities each airport connects  

Each analysis block is clearly separated with comments so they can be run independently (after first running the import dataset query).
