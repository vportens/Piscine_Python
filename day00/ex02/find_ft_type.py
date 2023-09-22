def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    if object_type == int:
        print("Type not found")
    if object_type == str:
        print(f"Brian is in the kitchen : {object_type}")
    if object_type == dict:
        print(f"Dict : {object_type}")
    if object_type == set:
        print(f"Set : {object_type}")
    if object_type == tuple:
        print(f"Tuple : {object_type}")
    if object_type == list:
        print(f"list : {object_type}")
    return 42
