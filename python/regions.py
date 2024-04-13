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

linode_types_url = "https://api.linode.com/v4/linode/types"
linode_types_response = requests.get(linode_types_url)
linode_types_response.json()
pd_linode_types=pd.DataFrame(linode_types_response.json()['data'])
pd_linode_types['monthly']=pd.json_normalize(pd_linode_types['price'])['monthly']
pd_linode_types = pd_linode_types.explode('region_prices')
pd_linode_types = pd_linode_types[pd_linode_types['memory'] > 8000].reset_index(drop=True)
pd_linode_types = pd_linode_types[pd_linode_types['vcpus'] > 3].reset_index(drop=True)
# get rid of unneeded columns
pd_linode_types = pd_linode_types[['id', 'region_prices', 'monthly']]
pd_linode_types['region'] = pd.json_normalize(pd_linode_types['region_prices'])['id']
pd_linode_types['region_monthly'] = pd.json_normalize(pd_linode_types['region_prices'])['monthly']
pd_linode_types = pd_linode_types[['id', 'monthly', 'region','region_monthly']]
pd_linode_types.loc[pd_linode_types['region_monthly'].isnull(),'region_monthly'] = pd_linode_types['monthly']
pd_linode_regions = pd_linode_regions.merge(pd_linode_types, how='outer', left_on='region', right_on='region')

pd_cross = pd_linode_regions.merge(pd_linode_types, how='outer', left_on='region', right_on='region')
pd_linode_other = pd_cross[pd_cross['region_x']!=pd_cross['region_y']]
pd_linode_other = pd_linode_other.rename(columns={"monthly": "monthly_cost", "id": "compute_type"})

pd_linode_markup = pd_cross[pd_cross['region_x']==pd_cross['region_y']]
pd_linode_markup=pd_linode_markup[['region_x','label','country','cloud','id','region_monthly']]
pd_linode_markup = pd_linode_markup.rename(columns={"region_monthly": "monthly_cost", "id": "compute_type"})
frames=[pd_linode_other,pd_linode_markup]
pd_cross = pd.concat(frames)
pd_cross.sort_values('region_x', ascending=False).drop_duplicates('A').sort_index()

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

# make the id more descriptive
pd_vultr_plans = pd_vultr_plans.rename(columns={"id": "compute_type"})

# add the monthly cost and compute type to the region table
pd_vultr_regions = pd_vultr_regions.merge(pd_vultr_plans, left_on='region', right_on='locations').drop(['locations'], axis=1)


# figure out how to pick the cheapest type in the region that has the required CPU/RAM/Hard disk
linode_types_url = "https://api.linode.com/v4/linode/types"
linode_types_response = requests.get(linode_types_url)
linode_types_response.json()

for i in linode_types_response.json()['data']:
  print(i)

# Need to review this
https://dev.to/holger/python-list-all-current-and-planned-azure-regions-29pk
