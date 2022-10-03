def character_helper(character) -> dict:
    return {
        "id": str(character["_id"]),
        "name": character["name"],
        "house": character["house"],
        "age": character["age"],
        "image": character["image"],
    }
