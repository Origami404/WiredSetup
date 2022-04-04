#!/bin/sh

echo "Now running..."

mitmdump --mode "reverse:${UPSTREAM}" -s /run.py