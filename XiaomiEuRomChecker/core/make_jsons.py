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
from XiaomiEuRomChecker.core.functionality import get_driver, get_url, get_table_by_xpath


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
        code_name, market_name, rom_name, rom_options = row[1], row[2], row[3], row[4]
        devices.append(
            {
                'model': 'core.AvailableDevicesModel',
                'fields': {
                    'code_name': code_name,
                    'market_name': market_name,
                    'rom_name': rom_name,
                    'rom_options': rom_options
                }
            }
        )

    # devices will be used as first argument in "write_json" function
    return devices


def list_to_json():
    current_driver = get_driver()
    url = get_url('weekly')
    current_driver.get(url)
    # getting all data in the page by id 'files_list'
    folders = get_table_by_xpath(current_driver, '//*[@id="files_list"]')
    # cutting first 5 items, because are neither folder name nor date
    all_data = folders.text.split("\n")[5:]
    # making list with all odd items in the all_data and cutting the last 2 elements, because they are not relevant
    all_folders = [all_data[index] for index in range(len(all_data)) if index % 2 == 0][:-2]
    folders_list = []

    for item in all_folders:
        folder_name, last_modification_date = item.split(" ")
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
    return folders_list


# Both functions work properly and the json files are filled with needed data

# write_json(excel_to_json('initial_devices_list.xlsx'), 'fixtures/devices.json')
# write_json(list_to_json(), 'fixtures/folders.json')
