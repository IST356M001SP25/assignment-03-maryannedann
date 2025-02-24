'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Package File Processor")
file = st.file_uploader("Upload package file:")

if file:
    filename = file.name
    json_filename = filename.replace(".txt",".json")
    packages = []
    text = StringIO(file.getvalue().decode("utf-8")).read()
    for line in text.split("\n"):
        line = line.strip()
        package = packaging.parse_packaging(line)
        total = packaging.calc_total_units(package)
        unit = packaging.get_unit(package)
        packages.append(package)
        st.info(f"{line} ➡️ Total 📦 Size = {total} {unit}")
    count = len(packages)

    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)
    st.success(f"{count} packages are in {json_filename}", icon="💾")