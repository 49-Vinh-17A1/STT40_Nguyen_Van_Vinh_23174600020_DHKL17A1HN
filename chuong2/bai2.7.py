import json
dulieu = '{"name": "Nguyễn Văn A", "age": 19, "school": "Uneti"}'
dulieu = json.loads(dulieu)
print(dulieu)
print(type(dulieu))