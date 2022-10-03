from pydantic import BaseModel


class Message_404(BaseModel):
    msg:str

    class Config:
        schema_extra = {
            "example":{
                "msg": "Character not Found"
            }
        }


class Message_500(BaseModel):
    msg:str 

    class Config:
        schema_extra = {
            "example":{
                "msg": "The data sent is not valid"
            }
        }

class Message_422(BaseModel):
    msg:str 

    class Config:
        schema_extra = {
            "example":{
                "msg": "We can't process the requested"
            }
        }

class Message_Delete(BaseModel):
    msg:str 

    class Config:
        schema_extra = {
            "example":{
                "msg": "Successfully deleted"
            }
        }