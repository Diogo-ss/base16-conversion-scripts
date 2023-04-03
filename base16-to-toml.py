import os
import yaml

input_folder = "base16/base16-schemes"
output_folder = "base16/base16-toml"
toml_header = "# This file was automatically generated from a YAML file.\n\n"

if not os.path.isdir(input_folder):
    os.system(f"git clone https://github.com/tomasiser/base16-schemes {input_folder}")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".yaml"):
        with open(os.path.join(input_folder, filename), "r") as f:
            data = yaml.safe_load(f)

        if isinstance(data, dict):
            toml_table = toml_header
            for key, value in data.items():
                if ":" in key:
                    toml_table += f'"{key}" = "{value}"\n'
                else:
                    toml_table += f"{key} = \"{value}\"\n"

            with open(os.path.join(output_folder, filename[:-5] + ".toml"), "w") as f:
                f.write(toml_table)
        else:
            print(f"Error: {filename} is not a valid YAML file.")

print("TOML conversion successful!")
