# To identify the lowest cost VM that meets the specs in a given city... 
# https://www.oracle.com/cloud/public-cloud-regions/
# https://www.oracle.com/cloud/price-list/#pricing-compute
# https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm

rom bs4 import BeautifulSoup
import requests
import pandas as pd

oracle_locations_url = "https://www.oracle.com/cloud/public-cloud-regions/"
oracle_locations_response = requests.get(oracle_locations_url)

# get the response text. in this case it is HTML
html = oracle_locations_response.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

df_oracle_zones = pd.DataFrame(columns=['region', 'zone'])
for zone in soup.findAll('th'):
  if 'zone' in str(zone):
    zone_str=zone.contents[0]
    for region in zone.findAll('span'):
      region_str = region.text[1:-1]
      df_temp = pd.DataFrame(columns=['region', 'zone'])
      df_temp.loc[0,'region'] = region_str
      df_temp.loc[0,'zone'] = zone_str
      df_oracle_zones = pd.concat([df_oracle_zones, df_temp], ignore_index=True)
      df_oracle_zones.reset_index()

# parses badly, and would require "invoiced billing"
df_oracle_zones
