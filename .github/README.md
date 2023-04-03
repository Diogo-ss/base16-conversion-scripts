# Base16 scheme conversion
This conversion script allows you to convert [Base16 scheme](https://github.com/tinted-theming/base16-schemes) YAML files to other formats such as `JSON`, `Lua`, `TOML`, `CSV` and `XML`.

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
<details>
<summary>JSON</summary>

```json
{
    "scheme": "standardized-dark",
    "author": "ali (https://github.com/ali-githb/base16-standardized-scheme)",
    "base00": "222222",
    "base01": "303030",
    "base02": "555555",
    "base03": "898989",
    "base04": "898989",
    "base05": "c0c0c0",
    "base06": "e0e0e0",
    "base07": "ffffff",
    "base08": "e15d67",
    "base09": "fc804e",
    "base0A": "e1b31a",
    "base0B": "5db129",
    "base0C": "21c992",
    "base0D": "00a3f2",
    "base0E": "b46ee0",
    "base0F": "b87d28"
}
```
</details>

<details>
<summary>Lua</summary>

```lua
-- This file was automatically generated from a YAML file.

return {
	scheme = "standardized-dark",
	author = "ali (https://github.com/ali-githb/base16-standardized-scheme)",
	base00 = "222222",
	base01 = "303030",
	base02 = "555555",
	base03 = "898989",
	base04 = "898989",
	base05 = "c0c0c0",
	base06 = "e0e0e0",
	base07 = "ffffff",
	base08 = "e15d67",
	base09 = "fc804e",
	base0A = "e1b31a",
	base0B = "5db129",
	base0C = "21c992",
	base0D = "00a3f2",
	base0E = "b46ee0",
	base0F = "b87d28",
}
```
</details>

<details>
<summary>TOML</summary>

```toml
# This file was automatically generated from a YAML file.

scheme = "standardized-dark"
author = "ali (https://github.com/ali-githb/base16-standardized-scheme)"
base00 = "222222"
base01 = "303030"
base02 = "555555"
base03 = "898989"
base04 = "898989"
base05 = "c0c0c0"
base06 = "e0e0e0"
base07 = "ffffff"
base08 = "e15d67"
base09 = "fc804e"
base0A = "e1b31a"
base0B = "5db129"
base0C = "21c992"
base0D = "00a3f2"
base0E = "b46ee0"
base0F = "b87d28"
```
</details>

<details>
<summary>XML</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <scheme>standardized-dark</scheme>
  <author>ali (https://github.com/ali-githb/base16-standardized-scheme)</author>
  <base00>222222</base00>
  <base01>303030</base01>
  <base02>555555</base02>
  <base03>898989</base03>
  <base04>898989</base04>
  <base05>c0c0c0</base05>
  <base06>e0e0e0</base06>
  <base07>ffffff</base07>
  <base08>e15d67</base08>
  <base09>fc804e</base09>
  <base0A>e1b31a</base0A>
  <base0B>5db129</base0B>
  <base0C>21c992</base0C>
  <base0D>00a3f2</base0D>
  <base0E>b46ee0</base0E>
  <base0F>b87d28</base0F>
</root>
```
</details>

<details>
<summary>CSV</summary>

```csv
Key,Value
scheme,standardized-dark
author,ali (https://github.com/ali-githb/base16-standardized-scheme)
base00,222222
base01,303030
base02,555555
base03,898989
base04,898989
base05,c0c0c0
base06,e0e0e0
base07,ffffff
base08,e15d67
base09,fc804e
base0A,e1b31a
base0B,5db129
base0C,21c992
base0D,00a3f2
base0E,b46ee0
base0F,b87d28
```
</details>

> Other formats will be added soon.

## Notes
- Make sure you have installed PyYAML before running the script.
- Make sure you have navigated to the correct directory before running the script.
