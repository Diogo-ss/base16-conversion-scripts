import os
import yaml
from lxml import etree

input_folder = "base16/base16-schemes"
output_folder = "base16/base16-xml"
xml_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"

if not os.path.isdir(input_folder):
    os.system(f"git clone https://github.com/tinted-theming/base16-schemes {input_folder}")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".yaml"):
        with open(os.path.join(input_folder, filename), "r") as f:
            data = yaml.safe_load(f)

        if isinstance(data, dict):
            root = etree.Element("root")
            for key, value in data.items():
                child = etree.SubElement(root, key)
                child.text = str(value)

            xml_tree = etree.ElementTree(root)
            xml_string = etree.tostring(xml_tree, pretty_print=True, encoding="UTF-8", xml_declaration=False)
            xml_string = xml_header + xml_string.decode("UTF-8")

            with open(os.path.join(output_folder, filename[:-5] + ".xml"), "w") as f:
                f.write(xml_string)
        else:
            print(f"Error: {filename} is not a valid YAML file.")

print("XML conversion successful!")
