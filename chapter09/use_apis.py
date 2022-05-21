# use_apis.json

import json

serialized = """
{
    "title": "Data Science Book",
    "author": "Joel Grus",
    "publicationYear": 2019,
    "topics": ["data", "science", "data science"]
}
"""

# parse the JSON to create a Python dict
deserialized = json.loads(serialized)
assert deserialized['publicationYear'] == 2019
assert "data science" in deserialized['topics']
