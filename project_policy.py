import json
import requests

# read environment variables
base_url = GITLAB_BASE_URL
private_token = GITLAB_PRIVATE_TOKEN

headers = requests.structures.CaseInsensitiveDict()
headers["PRIVATE-TOKEN"] = private_token

# Get all group information save to file
group_url = "{}/api/v4/groups".format(base_url)
group_resp=requests.get(group_url, headers=headers)
if group_resp.status_code == requests.codes.ok:
    with open("group_data.json" , "w") as f:
        f.write(group_resp.text)

# Read group id
with open("group_data.json", "r") as f:
    group_data = json.load(f)

# Get all projects information save to file
for gid in group_data:
    project_url="{}/api/v4/groups/{}/projects".format(base_url, gid["id"])
    project_resp=requests.get(project_url,headers=headers)
    if project_resp.status_code == requests.codes.ok:
        with open("project_data.json" , "w") as f:
            f.write(project_resp.text)

# Read project id
with open("project_data.json", "r") as f:
    project_data = json.load(f)

# Update continer_expiration_policy
for e in project_data:
    change_poroject_url = "{}/api/v4/projects/{}".format(base_url,e["id"])
    payload = {"container_expiration_policy_attributes": {"cadence": "1d","enabled": "true","keep_n": "5" ,"older_than": "14d" , "name_regex": ".*" }}
    resp = requests.put(change_project_url, headers=headers, json=payload)


