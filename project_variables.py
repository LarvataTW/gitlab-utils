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

headers = requests.structures.CaseInsensitiveDict()
headers["PRIVATE-TOKEN"] = private_token

# Read
url = "{}/api/v4/projects/{}/variables?sort_by_key&per_page=100000"
resp = requests.get(url, headers=headers)
# TODO
# save to file?
# export to somewhere?
print(resp.status_code)

# Add
url = "{}/api/v4/projects/{}/variables".format(base_url, project_id)
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
