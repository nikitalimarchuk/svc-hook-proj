#!/usr/bin/env python

import os
import re
import logging

invalid_test_names = []

for root, directory, files in os.walk("files"):
    for file in files:
        if file != "__init__.py" and file != "conftest.py" and not bool(re.match(r".*_test\.py", file)):
            invalid_test_names.append(f"{root}\{file}")

if len(invalid_test_names) != 0:
    for item in invalid_test_names:
        logging.log(logging.WARNING, item)
