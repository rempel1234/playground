azure_vms_response['offers']['linux-nv36adsv5-standard']
{'cores': 36, 'ram': 440.0, 'diskSize': 720, 'gpu': '1X A10', 'series': 'NVv5', 'isVcpu': True, 'prices': {'australia-east': {'value': 4.64}, 'brazil-south': {'value': 6.4}, 'canada-central': {'value': 3.84}, 'central-india': {'value': 4.48}, 'us-central': {'value': 3.936}, 'asia-pacific-east': {'value': 4.96}, 'us-east': {'value': 3.2}, 'us-east-2': {'value': 3.2}, 'france-central': {'value': 4.0}, 'germany-west-central': {'value': 4.16}, 'israel-central': {'value': 4.576}, 'italy-north': {'value': 4.16}, 'japan-east': {'value': 4.64}, 'korea-central': {'value': 4.32}, 'korea-south': {'value': 4.0}, 'us-north-central': {'value': 3.84}, 'europe-north': {'value': 3.84}, 'poland-central': {'value': 4.576}, 'qatar-central': {'value': 4.576}, 'south-africa-north': {'value': 4.672}, 'us-south-central': {'value': 3.84}, 'asia-pacific-southeast': {'value': 4.16}, 'sweden-central': {'value': 4.16}, 'uae-north': {'value': 4.576}, 'united-kingdom-south': {'value': 4.0}, 'usgov-virginia': {'value': 4.0}, 'europe-west': {'value': 4.16}, 'us-west': {'value': 4.16}, 'us-west-2': {'value': 3.2}, 'us-west-3': {'value': 3.2}}, 'pricingTypes': 'WebDirect'}
>>> azure_vms_response['offers']['linux-nv36adsv5-standard'].keys()
dict_keys(['cores', 'ram', 'diskSize', 'gpu', 'series', 'isVcpu', 'prices', 'pricingTypes'])

# get all the VM types

# if the cpu is 4 or above

# if the RAM is 8 or above

# save the price
for regions in  azure_vms_response['offers']['linux-nv36adsv5-standard']['prices']:
  azure_vms_response['offers']['linux-nv36adsv5-standard']['prices'][regions]['value']

for sku in  azure_vms_response['offers']:
  azure_vms_response['offers'][sku]
  if 'windows' not in sku and azure_vms_response['offers'][sku]['cores']>3 and azure_vms_response['offers'][sku]['cores']<31:
    for regions in azure_vms_response['offers'][sku]['prices']:
      sku
      regions
      azure_vms_response['offers'][sku]['prices'][regions]['value']




for sku in  azure_vms_response['offers']:
  if 'windows' not in sku and 'transactions' not in sku:
    if azure_vms_response['offers'][sku]['cores']>3 and azure_vms_response['offers'][sku]['cores']<16:
      if azure_vms_response['offers'][sku]['ram']>7 and azure_vms_response['offers'][sku]['ram']<31:
        for regions in azure_vms_response['offers'][sku]['prices']:
          sku
          regions
          azure_vms_response['offers'][sku]['prices'][regions]['value']

