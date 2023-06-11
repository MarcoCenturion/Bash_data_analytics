#!/usr/bin/env bash
sed '1,6d' | tr '[:lower:]' '[:upper:]' | grep PROD | tr '/' ' ' | cut -d ' ' -f3,7 | cut -d ',' -f1
