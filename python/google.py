from bs4 import BeautifulSoup
import requests
import pandas as pd

gce_locations_url = "https://cloud.google.com/about/locations"
gce_locations_response = requests.get(gce_locations_url)

# get the response text. in this case it is HTML
html = gce_locations_response.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

for child in soup.descendants:
  if child.name
  if 'th' in child.name:
    print(child.name)

df_gce_zones = pd.DataFrame(columns=['region', 'zone'])
for zone in soup.findAll('th'):
  if 'zone' in str(zone):
    zone_str=zone.contents[0]
    for region in zone.findAll('span'):
      region_str = region.text[1:-1]
      df_temp = pd.DataFrame(columns=['region', 'zone'])
      df_temp.loc[0,'region'] = region_str
      df_temp.loc[0,'zone'] = zone_str
      df_gce_zones = pd.concat([df_gce_zones, df_temp], ignore_index=True)
      df_gce_zones.reset_index()

# parses badly, and would require "invoiced billing"
df_gce_zones=df_gce_zones[df_gce_zones['region']!='me-central2']
df_gce_zones
