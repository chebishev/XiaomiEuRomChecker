import pandas as pd
from XiaomiEuRomChecker.core.models import AvailableDevicesModel

excel_data = pd.read_excel('XiaomiEuRomChecker/core/initial_devices_list.xlsx')
for row in excel_data.itertuples():
    code_name, market_name, rom_name, rom_options = row[1], row[2], row[3], row[4]
    device = AvailableDevicesModel(
        code_name=code_name,
        market_name=market_name,
        rom_name=rom_name,
        rom_options=rom_options
    )
    device.save()
