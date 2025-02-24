'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''

import streamlit as st
import packaging
from io import StringIO
import json

st.title("Batch Package File Processor")

if "file_count" not in st.session_state:
    st.session_state["file_count"] = 0
if "total_lines" not in st.session_state:
    st.session_state["total_lines"] = 0

uploaded_files = st.file_uploader("Upload package files:", accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        filename = file.name
        json_filename = filename.replace(".txt", ".json")
        packages = []
        text = StringIO(file.getvalue().decode("utf-8")).read()
        lines = text.split("\n")
        
        for line in lines:
            line = line.strip()
            if line:
                package = packaging.parse_packaging(line)
                packages.append(package)

        count = len(packages)
        st.session_state["file_count"] += 1
        st.session_state["total_lines"] += len(lines)

        with open(f"./data/{json_filename}", "w") as f:
            json.dump(packages, f, indent=4)
        
        st.success(f"{count} packages written to {json_filename}", icon="💾")
    
    st.info(f"Total files processed: {st.session_state['file_count']}")
    st.info(f"Total lines processed: {st.session_state['total_lines']}")
