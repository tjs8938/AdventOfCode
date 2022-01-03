import json

doc = json.load(open("input.txt"))


def process_element(doc):
    object_sum = 0
    if isinstance(doc, dict):
        for k, v in doc.items():
            value = process_element(v)
            if value is None:
                return 0
            else:
                object_sum += value
    elif isinstance(doc, list):
        for item in doc:
            value = process_element(item)
            object_sum += value if value else 0
    elif isinstance(doc, str):
        return None if doc == 'red' else 0
    elif isinstance(doc, int):
        return doc
    else:
        print("Unexpected type: " + str(doc) + " = " + type(doc))
        return 0
    return object_sum


print(process_element(doc))
