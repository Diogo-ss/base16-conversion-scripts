# Base16 scheme conversion
This conversion script allows you to convert [Base16 scheme](https://github.com/tinted-theming/base16-schemes) YAML files to other formats such as `JSON`, `Lua`, `TOML` and `XML`.

## Requirements
Before getting started, you need to have Python installed. Additionally, you need to install the PyYAML package.
```bash
pip install pyyaml

# for XML conversion
pip install lxml
```

## Step-by-Step
Clone the repository and navigate to it:

```bash
git clone https://github.com/Diogo-ss/base16-conversion-scripts.git
```

```bash
cd base16-conversion-scripts
```

Execute the script with the following command:
```bash
python <script_name>.py
```

The script will create the `base16` folder with the converted files in the same directory as the YAML files.

## Supported Output Formats
The script supports conversion of Base16 schemes to the following formats:
- JSON
- Lua
- TOML
- XML

> Other formats will be added soon.

## Notes
- Make sure you have installed PyYAML before running the script.
- Make sure you have navigated to the correct directory before running the script.
