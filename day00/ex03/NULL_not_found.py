def NULL_not_found(object: any) -> int:
    object_type = type(object)

    if object is None:
        print(f"Nothing: None {object_type}")
        return 0
    elif object_type == bool:
        if not object:
            print(f"Fake: False {object_type}")
            return 0
    elif object_type == int and object == 0:
        print(f"Zero: 0 {object_type}")
        return 0
    elif object_type == float and (object != object):
        print(f"Cheese: nan {object_type}")
        return 0
    elif object_type == str and object == '':
        print(f"Empty: {object_type}")
        return 0
    else:
        print("Type not found")
        return 1
