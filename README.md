# gitlab-utils

1. 搞一個自動打 Gitlab API 的 python container
2. 讀取 yaml 檔案，自動打 environment variables 進去該 Gitlab Repository
3. yaml 檔案是放在該專案的 .gitlab/variables.yaml
4. 這裡只是一個 executable python container，供該專案在 CICD 時呼叫執行

Run some Gitlab maintaince jobs via CI/CD.

## Config

All configuration values are in shell environment.

```
GITLAB_BASE_URL
GITLAB_PRIVATE_TOKEN
```

## TODO

- List all projects name/id
- List all groups name/id
- Backup project variables
- Backup group variables
- Add project variables
- Add group variables

## References

- https://docs.gitlab.com/ee/api/project_level_variables.html
