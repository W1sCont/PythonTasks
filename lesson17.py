# JSON - JavaScript Object Notation
import json

# python_data = {
#     "key1": 10,
#     "key2": True,
#     "key3": [1,2,3,4],
#     "key4": None,
#     "key5": "Hello, world!"
#     }

# # запис даних
# with open("files\\data.json", "w") as json_file:
#     json.dump(python_data, json_file, indent=4)


# відрикання і читання файлу
# with open("files\\data.json", "r") as json_file:
#     python_data = json.load(json_file)

# print(python_data)

python_data = {
    "key1": True,
    "key2": False
}

# для оброблення вихідних і вхідних даних JSON
json_data = json.dumps(python_data, indent=4)

print(json_data)
# 
result = json.loads(json_data)
print(result)