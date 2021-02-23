# Python JSON
# Parse JSON - Convert from JSON to Python
import json

# some JSON
a = '{"name":"Benjamin", "age":48, "city":"Glasgow"}'

# parse x:
b = json.loads(a)

# the result is a Python dictionary
print(b["age"])
print(a)
print()
print(b)
print()

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string
print(y)
print()

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps({"name": "John", "age": 30}, indent=3))
print(json.dumps({"name": "John", "age": 30}, indent=3, separators=(". ", " = ")))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print()

x1 = {
  "name": "Uchenna",
  "age": 48,
  "married": True,
  "divorced": False,
  "children": ("Emmanuel","Shepherd","Mikael"),
  "pets": None,
  "cars": [
    {"model": "Vauxhall Insignia", "mpg": 68.9}
  ],
  "wife" : "Joy"
}

print(json.dumps(x1))
print()
print(json.dumps(x1, indent=4))
print()
print(json.dumps(x1, indent=4, separators=(", ", " = ")))

# Format the Result
print()
print(json.dumps(x1, indent=4))
print()
print(json.dumps(x1, indent=4, separators=(", ", " = ")))
print()
print(json.dumps({"name": "John", "age": 30}, indent=3))
print()
print(jso n.dumps({"name": "John", "age": 30}, indent=3, separators=(". ", " = ")))
print()

# Order the Result
print(json.dumps(x1, indent=4, sort_keys=True))