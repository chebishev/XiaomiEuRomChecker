"""
This file only populates jsons in order to fill the database with external data
We will use the command "python manage.py loaddata <fixturename>"
The fixture name is "some_file.json" and it will be placed in core.fixtures
Before that a setting was added in settings.py:
FIXTURE_DIRS = (
    BASE_DIR / 'core.fixtures',
)
"""
import json
import pandas as pd
from XiaomiEuRomChecker.core.functionality import get_url, files_list_info


# gets two parameters: Value from function (as list with dictionaries) and the name of the output file
# writes the data in json format in order to be used with /manage.py loaddata
def write_json(data, file):
    # if the doesn't
    with open(file, 'w') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')


def excel_to_json(file):
    # at this time we have only this one: 'XiaomiEuRomChecker/core/initial_devices_list.xlsx'
    # initially this file contains all available devices with four columns of data
    excel_data = pd.read_excel(file)
    devices = []

    for row in excel_data.itertuples():
        code_name, market_name, rom_name, rom_options, slug = row[1], row[2], row[3], row[4], row[5]
        devices.append(
            {
                'model': 'core.AvailableDevicesModel',
                'fields': {
                    'code_name': code_name,
                    'market_name': market_name,
                    'rom_name': rom_name,
                    'rom_options': rom_options,
                    'slug': slug,
                }
            }
        )

    # devices will be used as first argument in "write_json" function
    return devices


def list_to_json():

    url = get_url('weekly')

    # all folder names from
    # "https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/files/xiaomi.eu/MIUI-WEEKLY-RELEASES/"
    folders = files_list_info(url, "tr", "folder")
    folders_list = []

    for folder in folders:
        info = folder.text.split()
        folder_name, last_modification_date = info[0], info[1]
        folders_list.append(
            {
                'model': 'core.FoldersModel',
                'fields': {
                    'folder_name': folder_name,
                    'last_modification_date': last_modification_date
                }
            }
        )

    # this variable will be used in order to populate the "folders.json" using the function "write_json"
    # the first element (folders_list[0]) is "Parent folder" and we don't need it, so we skip it
    return folders_list[1:]


# Both functions work properly and the json files are filled with needed data

# write_json(excel_to_json('initial_devices_list.xlsx'), 'fixtures/devices.json')
# write_json(list_to_json(), 'fixtures/folders.json')

print(list_to_json())
