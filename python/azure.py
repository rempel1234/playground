import requests
import pandas as pd

skip=0
# while(skip < 1000000)
while(skip < 2000):
  azure_regions_url = "https://prices.azure.com/api/retail/prices?$filter=priceType%20eq%20%27Consumption%27%20and%20contains(meterName,%20%27Spot%27%29&$skip="+str(skip)
  print(azure_regions_url)
  skip = 1000 + skip
  azure_regions_response = requests.get(azure_regions_url)
  azure_regions_response.json()
  pd_azure_regions = pd.DataFrame.from_dict(azure_regions_response.json()['Items'])


