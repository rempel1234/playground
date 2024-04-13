
import pandas as pd
import requests
linode_regions_url = "https://api.linode.com/v4/regions"
linode_regions_response = requests.get(linode_regions_url)
linode_regions_response.json()

# get the linode data into a dataframe
pd_linode_regions = pd.DataFrame.from_dict(linode_regions_response.json()['data'])
pd_linode_regions[["id","label","country"]]

vultr_regions_url = "https://api.vultr.com/v2/regions"
vultr_regions_response = requests.get(vultr_regions_url)
vultr_regions_response.json()

# get the vultr data into a dataframe
pd_vultr_regions = pd.DataFrame.from_dict(vultr_regions_response.json()['regions'])
pd_vultr_regions[["id","city","country"]]
# """
# 0   ams       Amsterdam      NL
# 1   atl         Atlanta      US
# 2   blr       Bangalore      IN
# ...
# """


# figure out how to pick the cheapest type in the region that has the required CPU/RAM/Hard disk
linode_types_url = "https://api.linode.com/v4/linode/types"
linode_types_response = requests.get(linode_types_url)
linode_types_response.json()

for i in linode_types_response.json()['data']:
  print(i)

# Need to review this
https://dev.to/holger/python-list-all-current-and-planned-azure-regions-29pk
