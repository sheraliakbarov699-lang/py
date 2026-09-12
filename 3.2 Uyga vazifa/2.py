import json
import yaml

yaml_data = """
server:
  host: 127.0.0.1
  port: 8000
"""

# YAML -> JSON
parsed_yaml = yaml.safe_load(yaml_data)
json_output = json.dumps(parsed_yaml, indent=4)
print("YAML -> JSON:")
print(json_output)

# JSON -> YAML
yaml_output = yaml.dump(parsed_yaml, default_flow_style=False)
print("\nJSON -> YAML:")
print(yaml_output)
