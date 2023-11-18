import typing

from .. import data_models


class BaseParser:
    """
    Base class for various file parsers (csv, json, avro and etc)

    Attributes:
    - file_path (str): The path to the file to be parsed.
    """
    def __init__(
        self,
        file_path: str,
    ) -> None:
        self.file_path = file_path
    
    def parse(
        self,
    ) -> typing.Any:
        """
        Abstract method to be implemented by subclasses for parsing the file.
        """
        raise('Not Implemented')
    
    def validate_city(
        self,
        **kwargs: dict,
    ) -> data_models.city.City:
        """
        Validates and creates a City instance from the provided 
        data using the pydantic data_models.City model.
        """
        return data_models.city.City(**kwargs)
