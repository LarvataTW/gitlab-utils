# gitlab-utils

Run some Gitlab maintaince jobs via CI/CD.

## Config

All configuration values are in shell environment.

```
GITLAB_BASE_URL
GITLAB_SETTING_FILE (.gitlab/settings.yaml)
```

## References

- https://docs.gitlab.com/ee/api/project_level_variables.html
- https://github.com/python-gitlab/python-gitlab/blob/9897c982f0d10da94692b94d8585216c4553437e/gitlab/base.py
- https://github.com/python-gitlab/python-gitlab/blob/9897c982f0d10da94692b94d8585216c4553437e/gitlab/mixins.py
