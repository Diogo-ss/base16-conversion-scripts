import os
import json
import yaml

input_folder = "base16/base16-schemes"
output_folder = "base16/base16-json"

if not os.path.isdir(input_folder):
    os.system(f"git clone https://github.com/tinted-theming/base16-schemes {input_folder}")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".yaml"):
        with open(os.path.join(input_folder, filename), "r") as f:
            data = yaml.safe_load(f)

        if isinstance(data, dict):
            with open(os.path.join(output_folder, filename[:-5] + ".json"), "w") as f:
                json.dump(data, f, indent=4)
        else:
            print(f"Error: {filename} is not a valid YAML file.")

print("JSON conversion successful!")
