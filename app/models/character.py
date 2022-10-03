from pydantic import BaseModel

class Model_Character(BaseModel):
    name:str = None
    house:str = None
    age:int = None
    image:str = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Criston Cole",
                "house": "Cole",
                "age": 23,
                "image": "https://static.wikia.nocookie.net/hieloyfuego/images/7/7c/Criston_Cole_HBO.png/revision/latest?cb=20220913160738"
                }
        }
        
