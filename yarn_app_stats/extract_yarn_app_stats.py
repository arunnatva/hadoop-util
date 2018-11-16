
#!/usr/bin/python

import requests,csv
import subprocess
import sys,glob,os
import pathlib
from datetime import datetime




def load_configs(config_file_path):
    props = {}
    with open(config_file_path,'r') as conf_file:

        for line in conf_file:
             line = line.rstrip()
             if '=' not in line: continue
             if line.startswith("#"): continue
             key,value = line.split("=",1)
             props[key] = value

    return props



def get_rm_active_host(props):
    params = (
       ('HostRoles/component_name', 'RESOURCEMANAGER'),
       ('HostRoles/ha_state', 'ACTIVE'),
     )

    username = props['username']
    password = props['password']
    request_uri = 'http://' + props['ambari_server'] + ':8080/api/v1/clusters/' + props['cluster'] + '/host_components'
    print("here is request uri : ",request_uri)
    response = requests.get(request_uri, params=params, auth=(username, password))
    response_json = response.json()
    rm_host = response_json['items'][0]['HostRoles']['host_name']
    return rm_host


def build_app_stats_row(app,app_stat_columns):
    start_ts_epoch = app['startedTime']/1000
    app['startedTime'] = datetime.fromtimestamp(start_ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
    end_ts_epoch = app['finishedTime']/1000
    app['finishedTime'] = datetime.fromtimestamp(end_ts_epoch).strftime('%Y-%m-%d %H:%M:%S')
    delimited_row = ''
    stat_value = ''
    for col in app_stat_columns:
        try:
            stat_value = str(app[col])
        except KeyError:
            stat_value = ''
        if delimited_row == '':
            delimited_row = stat_value
        else:
            delimited_row = delimited_row + '|' + stat_value
    return delimited_row


if __name__ == '__main__':
    print ("Welcome to Yarn App Statistics Module")

    config_file_path = sys.argv[1]
    props = load_configs(config_file_path)
    app_stat_columns = ['id','name','queue','user','applicationType','state','elapsedTime','memorySeconds','vcoreSeconds','startedTime','finishedTime','finalStatus','trackingUrl']
    rm_host = get_rm_active_host(props)
    rm_apps_url = 'http://' + rm_host + ':8088/ws/v1/cluster/apps'
    print ("rm apps url ",rm_apps_url)

    rm_apps_json = requests.get(rm_apps_url).json()
    yarn_app_list = rm_apps_json['apps']['app']

    outfile_path = str(pathlib.Path.home()) +'/'+ props['output_file']

    with open(outfile_path,'w') as yarn_apps_data:
        for app in yarn_app_list:
            delimited_row = build_app_stats_row(app,app_stat_columns)
            yarn_apps_data.write(delimited_row+'\n')

