import requests
import pandas as pd


azure_vms_url = "https://azure.microsoft.com/api/v2/pricing/virtual-machines-base/calculator/"
azure_vms_response = requests.get(azure_vms_url).json()
pd_azure_vms = pd.DataFrame.from_dict(azure_vms_response['offers'])
pd_azure_vms = pd_azure_vms.transpose()

# get the VMS with 4 or more cores
pd_azure_vms = pd_azure_vms[pd_azure_vms['cores']>3]

# get the VMs with 8 or more GiBs of RAM
pd_azure_vms = pd_azure_vms[pd_azure_vms['ram']>7]

# expand the prices
pd_azure_vms = pd_azure_vms.prices.apply(pd.Series)

pd_azure_vms = pd_azure_vms['prices']
pd_azure_vms['sku']=pd_azure_vms.index   
pd_azure_vms.transpose()
pd_azure_vms['region']=pd_azure_vms.index

# pd_azure_vms = pd_azure_vms.explode('prices')

for sku in pd_azure_vms:
  for key in sku.keys():
     print(key)
     sku[key].values()
 sum(pd_azure_vms['linux-a4-basic'].iloc[50].values())    

skip=0
# while(skip < 1000000)
while(skip < 2000):
  azure_regions_url = "https://prices.azure.com/api/retail/prices?$filter=priceType%20eq%20%27Consumption%27%20and%20contains(meterName,%20%27Spot%27%29&$skip="+str(skip)
  print(azure_regions_url)
  skip = 1000 + skip
  azure_regions_response = requests.get(azure_regions_url)
  azure_regions_response.json()
  pd_azure_regions = pd.DataFrame.from_dict(azure_regions_response.json()['Items'])


