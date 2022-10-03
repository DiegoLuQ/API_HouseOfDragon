from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from bson.errors import InvalidId
# models
from models.character import Model_Character
from models.message import Message_Delete
# controllers
from controllers.characters import (
    create_character,
    retrieved_characters,
    retrive_character,
    update_character,
    delete_character)

router = APIRouter()

@router.post('/register', responses={200:{"model": Model_Character, "description":"Character added successfully "}})
async def character_register(character_data: Model_Character = Body(...)):
    """
    This path operation register a character in the App

    Parameters

        - request Body parameter
            -character : Model_Character

    return a Model Character with status code 200

        - name: str
        - house: str
        - age: int
        - image: str

    """
    character = jsonable_encoder(character_data)
    new_character = await create_character(character)
    return new_character

@router.get('/characters', responses={200:{"model":List[Model_Character], "description": "Characters retrived successfully"}})
async def characters():
    """
    This path operation retrived a characters in the App

    Parameters

        - Without Parameters

    return a List of Characters with status code 200

        - name: str
        - house: str
        - age: int
        - image: str

    """
    characters = await retrieved_characters()
    if len(characters) == 0:
        return {"status": status.HTTP_404_NOT_FOUND, "msg": "no tenemos registros"}
    else:
        print(type(characters))
        return characters

@router.get('/character/{id}', responses={200:{"model": Model_Character, "description": "Character retrive successfully"}})
async def character(id: str):
    """
    This path operation retrive a character in the App

    Parameters

        - id : int

    return a Model with status code 200

        - name: str
        - house: str
        - age: int
        - image: str

    """
    character = await retrive_character(id)

    if character:
        return character
    else:
        return {"status": status.HTTP_404_NOT_FOUND, "msg": "no tenemos registros"}

@router.patch('/update_character/{id}', responses={200:{"model": Model_Character, "description": "Character modified successfully"}})
async def character_update(id: str, req: Model_Character):
    """
    This path operation update a character in the App

    Parameters

        - id : int

    return a Model with status code 200

        - name: str
        - house: str
        - age: int
        - image: str

    """
    req_ = await update_character(id, req)
    if req_:
        return req_
    else:
        return {"status": status.HTTP_404_NOT_FOUND, "msg": "no tenemos registros"}

@router.delete('/delete_character/{id}', responses={200: {"model": Message_Delete, "description": "Character eliminated successfully" }})
async def character_delete(id:str):
    """
    This path operation delete a character in the App

    Parameters:
        -

    return a message with status code 200

        - msg : character eliminated succefully: <character name>

    """
    try:
        req_ = await delete_character(id)
        print(responses_[500]['description'])
        data = JSONResponse(status_code=200, content={"msg": "character eliminated succefully: " + req_}) if req_ else JSONResponse(status_code=404, content={"msg": "Character not found"})
    except InvalidId:
        # print(dir(InvalidId))
        # print(InvalidId.__dict__)
        return JSONResponse(status_code=500, content={"msg":responses_[500]['description']})
    return data

