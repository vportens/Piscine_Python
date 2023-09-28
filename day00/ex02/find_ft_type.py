def all_thing_is_obj(object: any) -> int:
    type_msg = {
        str: "Brian is in the kitchen",
        dict: "Dict",
        set: "Set",
        tuple: "Tuple",
        list: "List",
    }

    msg = type_msg.get(type(object))
    if (msg):
        print(msg, ":", type(object))
    else:
        print("Type not found")
    return 42
