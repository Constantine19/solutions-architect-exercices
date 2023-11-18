import csv
import os
import typing

from . import parsers

DATASETS_DIRECTORY_PATH = 'DataSets'
CSV_FILE_OUTPUT_PATH = 'part-A/final_results.csv'

extension_by_parser = {
    '.csv': parsers.csv_parser.CSVParser,
    '.avro': parsers.avro_parser.AvroParser,
    '.json': parsers.json_parser.JSONParser,
}


def combine_datasets() -> typing.List[typing.Dict[str, typing.Any]]:
    """
    Combine data from multiple datasets using different file parsers.

    Returns:
    - A list of dictionaries representing cities.
    """
    combined_cities_data = []
    
    for filename in os.listdir(DATASETS_DIRECTORY_PATH):
        file_path = os.path.join(DATASETS_DIRECTORY_PATH, filename)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename.lower())
            
            if file_extension in extension_by_parser.keys():
                parser = extension_by_parser[file_extension](
                    file_path=file_path,
                )
                
            else:
                print(
                    f'File extension "{file_extension}" if not supported',
                )
                break
            
            cities_data = parser.parse()
            combined_cities_data.extend(cities_data)
            
    return [
        city.dict() for city in combined_cities_data
    ]

def remove_duplicates(
    cities_list: typing.List[typing.Dict[str, typing.Any]],
) -> typing.List[typing.Dict[str, typing.Any]]:
    """
    Remove duplicate cities from the provided list.

    Args:
    - cities_list: List of dictionaries representing cities.

    Returns:
    - A list of dictionaries representing unique cities.
    """
    seen_combinations = set()
    unique_cities_list = []
    
    for city in cities_list:
        key = (city['name'], city['code'], city['population'])
        if key not in seen_combinations:
            unique_cities_list.append(city)
            seen_combinations.add(key)
            
    return unique_cities_list

def sort_by_column(
    data: typing.List[typing.Dict[str, typing.Any]],
    column: str,
) -> typing.List[typing.Dict[str, typing.Any]]:
    """
    Sort the list of dictionaries by a specified column.

    Args:
    - data: List of dictionaries representing cities.
    - column: The column to use for sorting.

    Returns:
    - A list of dictionaries representing cities sorted by the specified column.
    """
    return sorted(
        data, 
        key=lambda x: x[column],
    )

def output_into_csv(
    data: typing.List[typing.Dict[str, typing.Any]],
) -> None:
    """
    Output data into a CSV file.

    Args:
    - data: List of dictionaries representing cities.
    """
    columns = [
        'name',
        'code',
        'population',
    ]
    
    with open(
        CSV_FILE_OUTPUT_PATH, 
        'w', 
        newline='', 
        encoding='utf-8',
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file, 
            fieldnames=columns,
        )
        writer.writeheader()
        writer.writerows(data)
        
def get_all_rows_count() -> int:
    """
    Get the total number of rows in the CSV file.

    Returns:
    - int: The total number of rows.
    """
    with open(CSV_FILE_OUTPUT_PATH, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = sum(1 for row in csv_reader)

    return row_count

def get_largest_population_city() -> typing.Dict[str, typing.Any]:
    """
    Get the city with the largest population from the CSV file.

    Returns:
    - largest_population_city: A dictionary representing the city with the largest population.
    """
    largest_population_city = None
    largest_population = 0

    with open(CSV_FILE_OUTPUT_PATH, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            population = int(row['population'])
            if population > largest_population:
                largest_population = population
                largest_population_city = row

    return largest_population_city

def get_total_population_city_by_code(
    code: str,
) -> int:
    """
    Get the total population of cities with a specific code from the CSV file.

    Args:
    - code: The city code.

    Returns:
    - total_population: The total population of cities with the specified code.
    """
    total_population = 0

    with open(CSV_FILE_OUTPUT_PATH, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row['code'] == code:
                total_population += int(row['population'])

    return total_population


if __name__ == '__main__':
    combined_datasets = combine_datasets()
    unique_data = remove_duplicates(combined_datasets)
    sorted_unique_data_by_name = sort_by_column(
        data=unique_data, 
        column='name',
    )
    output_into_csv(
        data=sorted_unique_data_by_name,
    )
    print(f'Q1. All rows count: {get_all_rows_count()}')
    print(f'Q2. The city with the largest population: {get_largest_population_city()}')
    print(f'Q3. Total population of all cities in Brazil: {get_total_population_city_by_code(code="BRA")}')
