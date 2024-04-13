import requests
linode_regions_url = "https://api.linode.com/v4/regions"
linode_regions_response = requests.get(linode_regions_url)
linode_regions_response.json()

for i in linode_regions_response.json()['data']:
  print(i['country'])
  print(i['label'])

# figure out how to pick the cheapest type in the region that has the required CPU/RAM/Hard disk
linode_types_url = "https://api.linode.com/v4/linode/types"
linode_types_response = requests.get(linode_types_url)
linode_types_response.json()

for i in linode_types_response.json()['data']:
  print(i)
