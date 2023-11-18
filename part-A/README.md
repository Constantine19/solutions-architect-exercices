# Solutions Architect Exercise - Part A

## Problem Statement

You are provided with 3 source files: `CityListA.json`, `CityListB.avro`, and `CityListC.csv`. Each file contains data in 3 columns:

- `name: string`
- `code: string`
- `population: long`

The goal is to combine these files, eliminate duplicates, and write the resulting dataset to a single `.CSV` file sorted alphabetically by the city name. Also, the following questions must be answered:
 - What is the count of all rows?
 - What is the city with the largest population?
 - What is the total population of all cities in Brazil (CountryCode == BRA)?
 - What changes could be made to improve your program's performance.
 - How would you scale your solution to a much larger dataset (too large for a single machine to store)?

## Solution

### Requirements

- Python 3.9 or higher

### Code Organization

The solution is organized into modular components to improve readability, maintainability, and scalability.

- **File Parsers:**
  - `csv_parser.py`: Handles parsing CSV files.
  - `avro_parser.py`: Handles parsing Avro files.
  - `json_parser.py`: Handles parsing JSON files.

- **Data Models:**
  - `city.py`: Defines and validates a city.

- **Main Script:**
  - `main.py`: Executes the data processing pipeline, combining datasets, removing duplicates, sorting, and generating the answers to the questions.

- **Requirements:**
  - `requirements.txt`: File that contains the requirements that need to be installed prior to executing the main script.

### Execution

1. Clone the repo and navigate into it
    ```
    clone <Repo URL>
    cd solutions-architect-exercise
    ```
2. Install the dependencies
    ```
    pip3 install -r part-A/requirements.txt
    ```
3. Run the script as a module from the repo's root:
    ```
    python3 -m part-A.run
    ```

    It should provide the following output:
    ```
    Q1. All rows count: 2084
    Q2. The city with the largest population: {'name': 'Mumbai (Bombay)', 'code': 'IND', 'population': '10500000'}
    Q3. Total population of all cities in Brazil: 55955012
    ```

    And also generate an output csv file that contains the combined record from all 3 files: `final_results.csv`


### Questions 4-5
4. What changes could be made to improve your program's performance?

    - `Parallel Processing` can be a good idea to implement to concurrently handle data from multiple files or cities. This can significantly speed up the data processing pipeline.
    - `Stream Processing` is another way to utlize instead of loading the entire datasets into memory. Streaming allows processing data in chunks, which is useful for large datasets that may not fit into memory.
    - `Optimization Algorithms` can be beneficial here. Some algorithms may need to be adapted to work efficiently in a distributed setting.
5. How would you scale your solution to a much larger dataset (too large for a single machine to store)?
    - `Distributed Computing Frameworks` like Apache Spark can be used to process data across multiple machines. These frameworks provide parallel processing capabilities, allowing the program to scale horizontally.
    - `Cloud Services` such as AWS, GCP or Azure could be used to distribute the workload across multiple nodes.
    - `Batch Processing` can be used to process data in smaller chunks or batches which will allow handling large datasets in manageable portions.
    

 

