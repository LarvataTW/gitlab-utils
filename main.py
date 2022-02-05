#!/usr/bin/env python

import gitlab
import yaml
import os

if __name__ == "__main__":

    try:
        gl = gitlab.Gitlab(os.environ['GITLAB_URL'], private_token=os.environ['GITLAB_PRIVATE_TOKEN'])
        project = gl.projects.get(os.environ['GITLAB_PROJECT_ID'])
    except Exception as e:
        raise 'GitLab authentication failed or Project not found.'

    # 從 ENV 取得 Gitlab Project 參數與授權
    # 讀取 yaml 檔案載入要設定的環境變數

    # 將既有環境變數跟 yaml 讀取進來的環境變數進行比較
    # 已經存在的環境變數不做任何處理
    # 僅新增尚未存在 key 與 environment_scope 搭配組合
    for yaml_var in yaml_variables:
        for project_var in project.variables.list():
            if yaml_var.key == project_var.key and yaml_var.environment_scope == project_var.environment_scope:
                print("Key: %s [%s] existed." % (yaml_var.key, yaml_var.environment_scope))
            else:
                project.variables.create({
                    'key': yaml_var.key,
                    'value': yaml_var.value,
                    'environment_scope': yaml_var.environment_scope,
                    'protected': yaml_var.protected,
                    'marked': yaml_var.marked
                })

    for project_var in project.variables.list():
        print("[%s] Key: %s, Value: %s" % (project_var.environment_scope, project_var.key, project_var.value))
