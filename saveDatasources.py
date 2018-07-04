import argparse
import pprint as pp
import sys

from dashboardApi import *
from commons import *

parser = argparse.ArgumentParser()
parser.add_argument('path', help='folder path to save datasources', default="datasources/latest", nargs='?')
args = parser.parse_args()

folder_path = args.path


def save_datasource(file_name, datasource_setting):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = folder_path + '/' + file_name + '.datasource'
    with open(file_path, 'w') as f:
        f.write(json.dumps(datasource_setting))
        print "datasource:{0} is saved to {1}".format(file_name, file_path)


def get_all_datasources_and_save():
    content_of_datasources = search_datasource()
    datasources = json.loads(content_of_datasources)
    if 'name' not in datasources[0]:
        print "CRITICAL: Couldn't access datasources, response is {0}".format(datasources)
        sys.exit(1)
    print "There are {0} datasources:".format(len(datasources))
    pp.pprint(datasources)
    for datasource in datasources:
        # print datasource['name']
        save_datasource(datasource['name'], datasource)


datasources = get_all_datasources_and_save()
print_horizontal_line()
