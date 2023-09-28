def NULL_not_found(object: any) -> int:
    object_type = type(object)

    object_type_msg = {
        bool: "Fake: False",
        int: "Zero: 0",
        float: "Cheese: nan",
        str: "Empty:"
    }
    msg = object_type_msg.get(object_type)
    if object is None:
        print(f"Nothing: None {object_type}")
        return 0
    elif msg and (not object or object != object):
        print(f"{msg} {object_type}")
        return 0
    else:
        print("Type not found")
        return 1
