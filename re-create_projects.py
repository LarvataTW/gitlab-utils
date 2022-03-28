#!/usr/bin/env python

import gitlab
import yaml
import os

if __name__ == "__main__":

    gl_private_token = os.environ['GITLAB_PRIVATE_TOKEN']
    gl_base_url = os.environ['CI_SERVER_URL']

    gl = gitlab.Gitlab(gl_base_url, private_token=gl_private_token)

    groups = gl.groups.list(per_page=100)

    result = {}
    result['groups'] = []

    for g in groups:
        group = {}
        group['name'] = g.name
        group['path'] = g.path
        group['projects'] = []

        for p in g.projects.list():
            project = {}
            project['name'] = p.name
            project['path'] = p.path
            group['projects'].append(project)

        sg = g.subgroups.list()
        if sg:
            print("%s has subgroup" % g.name)

        result['groups'].append(group)

    with open('result.yml', 'w') as output:
        yaml.dump(result, output, default_flow_style=False)
