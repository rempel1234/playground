
import pandas as pd
import requests

capitalize_all = lambda x: x.upper()
# Define a lambda function to remove commas and everything after them
def remove_comma_and_after(text):
    return text.split(',')[0]

linode_regions_url = "https://api.linode.com/v4/regions"
linode_regions_response = requests.get(linode_regions_url)
linode_regions_response.json()

# get the linode data into a dataframe
pd_linode_regions = pd.DataFrame.from_dict(linode_regions_response.json()['data'])
pd_linode_regions=pd_linode_regions[["id","label","country"]]

# Capitalize the countries
pd_linode_regions['country'] = pd_linode_regions['country'].apply(capitalize_all)

# Remove the country from the label
pd_linode_regions['label'] =  pd_linode_regions['label'].apply(remove_comma_and_after)
pd_linode_regions=pd_linode_regions.rename(columns={"id": "region"})
pd_linode_regions['cloud']='Linode'

#               id        label country
# 0        ap-west       Mumbai      IN
# 1     ca-central      Toronto      CA
# 2   ap-southeast       Sydney      AU

vultr_regions_url = "https://api.vultr.com/v2/regions"
vultr_regions_response = requests.get(vultr_regions_url)
vultr_regions_response.json()

# get the vultr data into a dataframe
pd_vultr_regions = pd.DataFrame.from_dict(vultr_regions_response.json()['regions'])
pd_vultr_regions=pd_vultr_regions[["id","city","country"]]
pd_vultr_regions=pd_vultr_regions.rename(columns={"city": "label", "id": "region"})
pd_vultr_regions['cloud']='Vultr'
# """
#     id            city  country
# 0   ams       Amsterdam      NL
# 1   atl         Atlanta      US
# 2   blr       Bangalore      IN
# ...
# """

frames=[pd_vultr_regions,pd_linode_regions]
pd.Concat(frames)

# Get the cost for the VM
vultr_plans_url = "https://api.vultr.com/v2/plans"

vultr_plans_response = requests.get(vultr_plans_url)
vultr_plans_response.json()
# make a separate row for each location
pd_vultr_plans = pd.DataFrame(vultr_plans_response.json()['plans']).explode('locations')

# pick the VMs with 8 GB or more
pd_vultr_plans = pd_vultr_plans[pd_vultr_plans['ram'] > 8000].reset_index(drop=True)

# pick the VMs with 4 CPU or more
pd_vultr_plans = pd_vultr_plans[pd_vultr_plans['vcpu_count'] > 3].reset_index(drop=True)

# pick the lowest price for each region that meets the specs
pd_vultr_plans = pd_vultr_plans.loc[pd_vultr_plans.groupby('locations').monthly_cost.idxmin()].reset_index(drop=True)

# get rid of unnessary information
# id is needed for IaaS, monthly_cost to get estimate, location to avoid duplication
pd_vultr_plans = pd_vultr_plans[["id","monthly_cost","locations"]]


# figure out how to pick the cheapest type in the region that has the required CPU/RAM/Hard disk
linode_types_url = "https://api.linode.com/v4/linode/types"
linode_types_response = requests.get(linode_types_url)
linode_types_response.json()

for i in linode_types_response.json()['data']:
  print(i)

# Need to review this
https://dev.to/holger/python-list-all-current-and-planned-azure-regions-29pk
