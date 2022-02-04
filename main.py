#!/usr/bin/env python

import gitlab
import os

gitlab_url=''
gitlab_private_token = ''
gitlab_project_id = 424

gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_private_token)
gl.auth()

project = gl.projects.get(gitlab_project_id)

if not project.variables.get('TEST', filter={'environment_scope': '*'}):
    project.variables.create({
        'key': 'TEST',
        'value': 'zx1986',
        'environment_scope': '*',
        'protected': 'false',
        'marked': 'false'
    })

project.variables.list()

if __name__ == "__main__":
    # 從 ENV 取得 Gitlab Project 參數與授權
    # 讀取 yaml 檔案載入要設定的環境變數
    # 透過 Gitlab API 開始配置環境變數
    ## 僅新增尚未建立的環境變數
    ## 已存在同環境同名的變數不要動
    ## 不要移除其他已經存在的變數
    ## 回報執行結果，注意敏感資訊問題
    pass
