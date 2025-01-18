import json
from datetime import datetime

data = {
    "name": "vinayak",
    "age": "21",
    "registered_at": datetime.now(),
    "fruits": ["apple", "mango"],
    "place": {
        "country": "India",
        "state": "Rajasthan"
    },
    "task": " \n \\ \'abc\' 'HELLO' "
}

# custom serialization function for unsupported types
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"object {str(obj)} is not serializable")

json_data = json.dumps(data, default=custom_serializer, indent=4)
print(json_data)

"""
    {
        "name": "vinayak",
        "age": "21",
        "registered_at": "2024-10-18T12:29:51.869412",
        "fruits": [
            "apple",
            "mango"
        ],
        "place": {
            "country": "India",
            "state": "Rajasthan"
        },
        "task": " \n \\ 'abc' 'HELLO' "
    }
"""