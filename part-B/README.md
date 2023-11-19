# Solutions Architect Exercise - Part B

## Problem Statement

Koala has a dataset composed of visits to their web site, annotated with session ID, path visited, and attributes about the visitor like "city" and "browser". They want to build dashboards based on this dataset as well as be able to explore this dataset interactively.
An example data point for a single hit is below:

```
{
  "timestamp": "2016-08-04T18:05:07.054Z",
  "session": "S74650219",
  "remote_address": "172.31.3.170",
  "path": "http://www.koalastothemax.com/img/koalas3.jpg",
  "referrer": "Direct",
  "timezone_offset": "-120",
  "language": "it-IT",
  "city": "Borgo San Lorenzo",
  "region": "Province of Florence",
  "country": "Italy",
  "continent": "Europe",
  "latitude": 43.9555,
  "longitude": 11.3856,
  "browser": "Mozilla",
  "browser_version": "rv:11.0",
  "agent_type": "Browser",
  "agent_category": "Personal computer",
  "os": "Windows",
  "platform": "Windows"
}
```

This hit is part of the session "S74650219". The Koalas To The Max site gets roughly 200 million hits per day. Koala wants to load data in real-time and additionally store one year of historical data.

The most important kind of analysis Koala needs to do is counting how many unique sessions match certain parameters. For example, they need to answer queries like:

How many unique sessions were there last month?
How many unique sessions are there per day in each country?
Koala has one type of hardware available in its datacenter, with the following specs:
2x 8-core HT processors (16 cores total, 32 hardware threads) 64GB memory 600GB SSD disk


## Recommendation

In response to Koala's requirements for building an analytics cluster to handle one year of their dataset, we recommend utilizing Apache Druid powered by Imply. Imply provides a user-friendly platform for managing and querying Druid clusters.

### Question 1. How many servers will be necessary for an analytics cluster for one year of this dataset

The number of servers required for the analytics cluster depends on factors like data volume, query complexity, and desired performance. Given Koala's dataset of approximately 200 million hits per day, we can make some educated assumptions:
 
**Assumptions**:
- **Data Volume**
    - Assuming an average data point size of 1KB, the daily data volume is approximately 200 GB (200 million hits * 1KB).
- **Retention Policy**: 
    - Storing one year of data suggests around 73 TB of historical data (200 GB/day * 365 days).
- **Recommendation**:
    - Real-Time Nodes: 4 to 8 nodes for real-time ingestion and indexing.
    - Historical Nodes: 10 to 16 nodes for storing 1 year of data efficiently.
    - Broker Nodes: 2 to 4 nodes for handling query requests.

### Question 2. How these servers should be configured (JVM config, Druid runtime.properties)

**JVM Config (Java Virtual Machine):**:
- **Heap Size**
    - Set heap size based on server memory. For historical nodes, allocate a larger heap size for efficient query processing.

    ```
    -server
    -Xms128m
    -Xmx128m
    ```
- Druid Real-Time Nodes
    ```
    druid.service=druid/realtime
    druid.port=8084
    druid.worker.capacity=8
    ```
    ***Explanation:***
    - druid.service: Specifies that this node is a real-time node.
    - druid.port: Sets the port for communication with the real-time node.
    - druid.worker.capacity: Allocates 8 worker threads to handle the real-time indexing tasks. This value is adjusted based on the number of available hardware threads.
- Druid Historical Runtime properties:
    ```
    druid.service=druid/historical
    druid.port=8083
    druid.worker.capacity=16
    druid.processing.buffer.sizeBytes=2684354560
    ```
    ***Explanation:***
    - druid.service: Specifies that this node is a historical node.
    - druid.port: Sets the port for communication with the historical node.
    - druid.worker.capacity: Allocates 16 worker threads for parallel processing of historical data.
    - druid.processing.buffer.sizeBytes: Sets the size of the processing buffer to 2.5 GB, ensuring efficient handling of queries on historical data.

- Broker Nodes
    ```
    druid.service=druid/broker
    druid.port=8082
    ```
    ***Explanation:***
    - druid.service: Specifies that this node is a broker node.
    - druid.port: Sets the port for communication with the broker node.

NOTE: The values can be further fine-tuned based on actual performance testing and monitoring results.

### Question 3. How Imply can be used to answer the two sample queries provided by Koala.

In order to answer that, I signed up for the Imply account and, for testing purposes, utilized a Python script from the GitHub repository to generate 20,000 records, adhering to the provided data model example of a hit. I then executed two sample queries to evaluate the functionality and capabilities of Imply.


**Query 1: Number of Unique Sessions Last Month**
```
SELECT COUNT(DISTINCT "session") AS unique_sessions
FROM "koala"
WHERE "__time" >= TIMESTAMP '2023-10-01 00:00:00' AND "__time" < TIMESTAMP '2023-11-01 00:00:00'

```
**Number of Unique Sessions per Country in a Particular Day**
```
SELECT
  __time,
  country,
  COUNT(DISTINCT session) AS unique_sessions
FROM "koala"
WHERE "__time" >= TIMESTAMP '2020-10-01 00:00:00' AND "__time" < TIMESTAMP '2023-11-01 00:00:00'
GROUP BY "__time", "country"
ORDER BY 3 DESC

```

These queries can be served as the foundation for creating a dashboard in Imply, showcasing the insights derived from the generated data.