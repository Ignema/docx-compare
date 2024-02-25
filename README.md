# docx-compare 🔍

## Overview

docx-compare is a Python script designed to facilitate the comparison of two Microsoft Word documents in a quick and straightforward manner. Leveraging the power of the `python-docx` library for parsing Word documents and Git's `git-diff` utility for comparison, this tool provides a simple yet effective means of identifying differences between two .docx files.

## Features

- **Easy Comparison**: Quickly compare two Microsoft Word documents.
- **Detailed Diffing**: Identify differences at a granular level, including text changes, additions, and deletions.
- **Git Integration**: Utilizes Git's `git-diff` for robust document comparison.
- **Pythonic**: Written in Python, making it easily extensible and modifiable.
- **Simple Usage**: Minimal setup and intuitive command-line interface.

## Prerequisites

Before using docx-compare, ensure you have the following installed:

- Python 3.x
- `python-docx` library
- Git (for `git-diff`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/docx-compare.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To compare two Word documents, use the following command:

```bash
python compare.py path/to/document1.docx path/to/document2.docx
```

This command will output a diff folder that contains the textual content of the two documents and two command files that will launch the comparison:

```bash
# Windows
diff/compare.bat

# Linux or Mac
. diff/compare.sh
```

## Example

```bash
python compare.py document_old.docx document_new.docx
diff/compare.bat
```

Output:

```diff
--- a/diff/document_old.txt
+++ b/diff/document_new.txt
@@ -1,4 +1,4 @@
This is [-an-]{+a revised+} example document.
It contains some text.
This text [-might-]{+may+} change in [-the future.-]{+future revisions.+}
Please review it carefully.
```

> Made with ❤️ by Ignema