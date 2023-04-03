import subprocess

scripts = [
    "base16-to-csv.py",
    "base16-to-json.py",
    "base16-to-lua.py",
    "base16-to-toml.py",
    "base16-to-xml.py"
]

for script in scripts:
    subprocess.run(["python", script])
