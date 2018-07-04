#!/bin/bash

current_path=`pwd`
current_time=`date +"%Y-%m-%d_%H-%M-%S"`
compressed_dashboards_name="dashboards.tar.gz"
compressed_datasources_name="datasources.tar.gz"



echo $current_time

dashboard_backup_folder="dashboards/$current_time"
datasource_backup_folder="datasources/$current_time"

if [ ! -d "$dashboard_backup_folder" ]; then 
  mkdir -p "$dashboard_backup_folder" 
fi

if [ ! -d "$datasource_backup_folder" ]; then 
  mkdir -p "$datasource_backup_folder" 
fi

source venv/bin/activate && python "${current_path}/saveDashboards.py" $dashboard_backup_folder
source venv/bin/activate && python "${current_path}/saveDatasources.py" $datasource_backup_folder

tar -zcvf "/tmp/$compressed_dashboards_name" $dashboard_backup_folder
tar -zcvf "/tmp/$compressed_datasources_name" $datasource_backup_folder
