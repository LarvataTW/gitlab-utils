# gitlab-utils

Run some Gitlab maintaince jobs via CI/CD.

## Config

Essential configuration should set with shell environment variables:

```
GITLAB_BASE_URL
GITLAB_PRIVATE_TOKEN
GITLAB_SETTING_FILE (.gitlab/settings.yaml)
```

## References

- https://docs.gitlab.com/ee/api/project_level_variables.html
- https://github.com/python-gitlab/python-gitlab/blob/9897c982f0d10da94692b94d8585216c4553437e/gitlab/base.py
- https://github.com/python-gitlab/python-gitlab/blob/9897c982f0d10da94692b94d8585216c4553437e/gitlab/mixins.py
