import pydantic


class City(
    pydantic.BaseModel,
):
    """
    Pydantic model representing a city.
    
    Attributes:
    - name (str): The name of the city.
    - code (str): The code associated with the city.
    - population (int): The population of the city.
    """
    name: str
    code: str
    population: int
