import json

from . import _parser


class JSONParser(
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
            encoding='utf-8',
        ) as json_file:
            json_data = json.load(json_file)

            for record in json_data:
                city_data = {
                    'name': record['Name'],
                    'code': record['CountryCode'],
                    'population': record['Population']
                }
                city = self.validate_city(**city_data)
                cities_data.append(city)

        return cities_data
