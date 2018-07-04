#!/bin/bash

current_path=`pwd`
dashboard_folder="$1"

find "$dashboard_folder" -mindepth 1 | while read f ; do
  echo "$f"
  source venv/bin/activate && python $current_path/createDashboard.py "$f"
done
