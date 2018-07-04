import argparse
from dashboardApi import *
from commons import *

parser = argparse.ArgumentParser()
parser.add_argument('path', help='folder path to save dashboards', nargs='?', default='dashboards/latest')
args = parser.parse_args()

folder_path = args.path


def get_all_dashboards_in_grafana():
    content_of_all_dashboards = search_dashboard()
    dashboards = json.loads(content_of_all_dashboards)
    print u"There are {0} dashboards:".format(len(dashboards))
    for board in dashboards:
        print board['title']
    return dashboards


def save_dashboard_setting(file_name, dashboard_settings):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = folder_path + '/' + file_name + '.dashboard'
    with open(file_path, 'w') as f:
        f.write(dashboard_settings)
    print u"dashboard:{0} are saved to {1}".format(file_name, file_path)


def get_individual_dashboard_setting_and_save(dashboards):
    for board in dashboards:
        status_code_and_content = get_dashboard(board['uri'])
        if status_code_and_content[0] == 200:
            # print(status_code_and_content[1])
            save_dashboard_setting(board['title'], status_code_and_content[1])
            # save_dashboard_setting(board['title'], json.dumps(status_code_and_content[1]))


dashboards = get_all_dashboards_in_grafana()
print_horizontal_line()
dashboard_settings = get_individual_dashboard_setting_and_save(dashboards)
print_horizontal_line()
