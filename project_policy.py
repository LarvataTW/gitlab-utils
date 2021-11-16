import requests
import json

# read environment variables
base_url = GITLAB_BASE_URL
private_token = GITLAB_PRIVATE_TOKEN

headers = requests.structures.CaseInsensitiveDict()
headers["PRIVATE-TOKEN"] = private_token

# Get all group information save to file
group_url = "{}/api/v4/groups".format(base_url)
group_resp=requests.get(group_url, headers=headers)
group_data=json.dumps(group_resp.json(), indent=4)

#Check status if ok write to file
if group_resp.status_code == requests.codes.ok:
    with open("group_data.json" , "w" , encoding='utf-8') as f:
        f.write(group_data)

# Read group id
with open("group_data.json", "r" , encoding='utf-8') as f:
    group_data = json.load(f)

# Get all projects information save to file
for gid in group_data:
    project_url="{}/api/v4/groups/{}/projects".format(base_url, gid["id"])
    project_resp=requests.get(project_url,headers=headers)
    project_data=json.dumps(project_resp.json(), indent=4)
    if project_resp.status_code == requests.codes.ok:
        with open("project_data.json" , "w", encoding='utf-8') as f:
            f.write(project_data)

# Read project id
with open("project_data.json", "r", encoding='utf-8') as f:
    project_data = json.load(f)

# Update continer_expiration_policy
for e in project_data:
    project_url = "{}/api/v4/projects/{}".format(base_url,e["id"])
    payload = {"container_expiration_policy_attributes": {"cadence": "1d","enabled": "true","keep_n": "5" ,"older_than": "14d" , "name_regex": ".*" }}
    resp = requests.put(project_url, headers=headers, json=payload)
    print(resp.status_code)

