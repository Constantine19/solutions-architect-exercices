import fastavro

from . import _parser


class AvroParser(
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
        
        with open(self.file_path, 'rb') as avro_file:
            avro_reader = fastavro.reader(avro_file)
            for record in avro_reader:
                city_data = {
                    'name': record['Name'],
                    'code': record['CountryCode'],
                    'population': record['Population']
                }
                city = self.validate_city(**city_data)
                cities_data.append(city)

        return cities_data
