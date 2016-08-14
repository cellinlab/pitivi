#!/usr/bin/env python3
"""Print the content of an environment variable on stdout."""
import os
import sys


print(os.environ.get(sys.argv[1], ''))
