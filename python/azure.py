import requests
import pandas as pd
from re import search

def list_azure_regions():
    url = 'https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/'
    html = requests.get(url).content
    df_list = pd.read_html(html)
    regions_list = []
    locations_list = []
    for df in df_list:
        for dc in list(df):
            if search('Regions', dc):
                pass
            else:
                if search('Coming soon', dc):
                    state = 'planned'
                else:
                    state = 'active'
                az_location = df[dc][0]
                region = dc.removesuffix('  Start free')
                region = region.removesuffix('  Get started')
                region = region.removesuffix('  Coming soon')
                if region in regions_list:
                    pass
                else:
                    regions_list.append(region)
                    locations_list.append(
                        dict({
                            'az_display_name': region,
                            'az_short_name': region.replace(' ','').lower(),
                            'az_location': az_location,
                            'az_state': state
                        })
                    )
    return locations_list

if __name__ == '__main__':
    azure_regions = list_azure_regions()

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    df = pd.DataFrame(azure_regions)

    df_planned_regions = df[df.values == 'planned']
    df_active_regions = df[df.values == 'active']

    # Print only active regions
    print(df_active_regions)

    # Print only planned regions
    print('\n') # Newline
    print(df_planned_regions)

    # Print all regions, regardless of their status
    print('\n') # Newline
    print(df)
