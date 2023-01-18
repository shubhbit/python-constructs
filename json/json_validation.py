import json
from jsonschema import validate

schema_file = "json/schema.json"
employees_file = "json/employees.json"

with open(schema_file, "r") as f:
    schema = json.load(f)

with open(employees_file, "r") as f:
    employees = json.load(f)

validate(instance=employees, schema=schema)
