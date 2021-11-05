import json
import requests

# TODO
# input data example
with open("data.json", "r") as f:
    data = json.load(f)

# TODO
# read environment variables
base_url = GITLAB_BASE_URL
private_token = GITLAB_PRIVATE_TOKEN
# read project id
project_id = 0

url = "{}/api/v4/projects/{}/variables".format(base_url, project_id)

headers = requests.structures.CaseInsensitiveDict()
headers["PRIVATE-TOKEN"] = private_token

# Add
for e in data:
    data = {
        "key": e['key'],
        "value": e['value'],
        "environment_scope": e['environment_scope']
    }
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)

# Update
for e in data:
    url = "{}/api/v4/projects/{}/variables/{}?filter[environment_scope]={}".format(
        base_url,
        project_id,
        e['key'],
        e['environment_scope']
    )
    data = {"value": e['value']}
    resp = requests.put(url, headers=headers, data=data)
    print(resp.status_code)
