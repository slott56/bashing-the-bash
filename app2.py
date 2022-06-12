#!/usr/bin/env python3
"""app2.py"""
import sys
data = list(sys.stdin)
for line in reversed(data):
    print(line.rstrip())