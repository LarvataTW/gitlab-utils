#!/usr/bin/env python

import gitlab
import yaml
import os

if __name__ == "__main__":

    gl_base_url = os.environ['GITLAB_BASE_URL']
    gl_setting_file = os.environ['GITLAB_SETTING_FILE']
    gl_job_token = os.environ['CI_JOB_TOKEN']
    gl_project_id = os.environ['CI_PROJECT_ID']
    gl_ci_project_dir = os.environ['CI_PROJECT_DIR']

    gl = gitlab.Gitlab(gl_base_url, job_token=gl_job_token)
    project = gl.projects.get(gl_project_id)

    print('---------')
    print(gl_base_url)
    print(gl_job_token)
    print(gl_project_id)
    print('---------')

    # 從 ENV 取得 Gitlab Project 參數與授權
    # 讀取 yaml 檔案載入要設定的環境變數
    yaml_file = "%s/%s" % (gl_ci_project_dir, gl_setting_file)
    with open(yaml_file, 'r') as stream:
        try:
            yaml_settings = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise e

    # 將 settings.yaml 內的環境變數結構重組
    # 改成配合 Gitlab library object 的結構
    # 為何不一開始就設計成 Gitlab library object 的結構？
    # 因為那個結構寫起來不方便，如果不優化環境變數設定寫法，那這個工具就沒意義了
    yaml_variables = []
    for environment in yaml_settings['environments']:
        for variable in environment['variables']:
            _var = {}
            for key in variable:
                _var['key'] = key
                _var['value'] = variable[key]
                _var['environment_scope'] = environment['name']
                _var['protected'] = environment['protected']
                _var['masked'] = environment['masked']
            yaml_variables.append(_var)

    # 將既有環境變數跟 yaml 讀取進來的環境變數進行比較
    # 已經存在的環境變數不做任何處理
    # 僅新增尚未存在 key 與 environment_scope 搭配組合
    for yaml_var in yaml_variables:
        try:
            project.variables.create({
                'key': yaml_var['key'],
                'value': yaml_var['value'],
                'environment_scope': yaml_var['environment_scope'],
                'protected': yaml_var['protected'],
                'masked': yaml_var['masked']
            })
        except Exception as e:
            print(e)

    for project_var in project.variables.list():
        print("[%s] Key: %s, Value: %s" % (project_var.environment_scope, project_var.key, project_var.value))
