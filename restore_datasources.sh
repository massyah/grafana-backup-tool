#!/bin/bash

current_path=`pwd`
datasource_folder="$1"

find "$datasource_folder" -mindepth 1 | while read f ; do
  echo "$f"
  source venv/bin/activate && python $current_path/createDatasource.py "$f"
done

