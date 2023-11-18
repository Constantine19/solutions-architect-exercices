import csv

from . import _parser


class CSVParser(
    _parser.BaseParser,
):      
    def __init__(
        self,
        file_path: str,
    ):
        super().__init__(file_path)
    
    def parse(
        self,
    ) -> list:
        cities_data = []
        
        with open(
            self.file_path, 
            'r', 
            newline='', 
            encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                city_data = {
                    'name': row['Name'],
                    'code': row['CountryCode'],
                    'population': row['Population']
                }
                
                city = self.validate_city(**city_data)
                cities_data.append(city)

        return cities_data