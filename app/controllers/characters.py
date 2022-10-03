from config.db import character_collection
from bson.objectid import ObjectId
from .helpers.character import character_helper
from models.character import Model_Character

db = character_collection


async def create_character(character_data: dict) -> dict:
    character = await db.insert_one(character_data)
    new_character = await db.find_one({"_id": character.inserted_id})
    return character_helper(new_character)


async def retrieved_characters() -> tuple:
    list_characters = [character_helper(x) async for x in db.find()]
    return tuple(list_characters)


async def retrive_character(id: str) -> dict:
    character = await db.find_one({"_id": ObjectId(id)})
    if character:
        return character_helper(character)


async def update_character(id: str, data: Model_Character) -> dict:
    retrieve_character = await db.find_one({'_id': ObjectId(id)})

    if retrieve_character:
        character_model = dict(Model_Character(**retrieve_character))
        character_model.update(data.dict(exclude_unset=True))
        update_character = await db.update_one({"_id": ObjectId(id)}, {"$set": character_model})

        if update_character:
            data_ = await db.find_one({"_id": ObjectId(id)})
            return character_helper(data_)
        else:
            return False
        return False

async def delete_character(id: str) -> dict:
    
    retrieve_character = await db.find_one({'_id': ObjectId(id)})

    if retrieve_character:
        await db.delete_one({'_id': ObjectId(id)})
        return retrieve_character.get('name')
    return False
    
        


    