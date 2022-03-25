# gitlab-utils

Run some Gitlab project level maintaince jobs via Gitlab CI/CD.

## Config

Essential Gitlab CI/CD Variables:

```
GITLAB_PRIVATE_TOKEN
GITLAB_SETTING_FILE (.gitlab/settings.yaml)
```

## References

- https://docs.gitlab.com/ee/api/project_level_variables.html
- https://github.com/python-gitlab/python-gitlab/blob/9897c982f0d10da94692b94d8585216c4553437e/gitlab/base.py
- https://github.com/python-gitlab/python-gitlab/blob/9897c982f0d10da94692b94d8585216c4553437e/gitlab/mixins.py
