#!/usr/bin/env python3
"""function called filter_datum that
returns the log message obfuscated"""

import re


def filter_datum(fields, redaction, message, separator):
    return re.sub("|".join(fields), redaction, message, flags=re.IGNORECASE)
