"""
core functionality needed for my web scrapping
including driver, url, date checking
"""

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver():
    # options - in order to make headless search with Edge
    options = Options()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--log-level=3')  # remove errors about "Error with Feature-Policy header

    # get and install the newest, needed driver in .root/.wdm
    service = EdgeService(EdgeChromiumDriverManager().install())

    return webdriver.Edge(service=service, options=options)


def get_url(release, folder=''):
    """
    Gives a link for the chosen release
    if it is 'weekly' or 'stable' second parameters isn't used,
    otherwise it is used in order to concatenate it at the end of the generated link
    :return: URL
    """
    # initial URL that can be modified with various suffixes depending on the release
    static_url = 'https://sourceforge.net/projects/xiaomi-eu-multilang-miui-roms/files/xiaomi.eu/'

    available_urls = {
        'stable': static_url + 'MIUI-STABLE-RELEASES/MIUIv14/',
        'weekly': static_url + 'MIUI-WEEKLY-RELEASES/',
        'last_weekly': static_url + 'MIUI-WEEKLY-RELEASES/' + folder,
    }
    return available_urls[release]


def get_table_by_xpath(driver, xpath):
    return driver.find_element("xpath", xpath)


def get_date(string):
    """
    Extracts year, month and day from string in format YYYY-MM-DD
    :param string:
    :return: list of integers [2023, 06, 29]
    """
    date_for_splitting = string
    return [int(x) for x in date_for_splitting.split("-")]


def get_date_difference(date):
    """
    :param date: is a string in format "2023-06-29"
    :return: timedelta in days, seconds and microseconds as kwargs
    """
    # getting the difference in days (it gave something like "2 days, 14:05:28.657927", which is translated to
    # number with ".days" in the "if" statement)
    difference = datetime.now() - datetime(*get_date(date))
    return difference


def check_date(folder_date_list, new_folder_checker):
    # folder_name is in format "V14.0.23.4.31.DEV" which is MIUI Version, and date in format yy.m.d
    # date is a string in format "2023-04-31"
    folder_name, date = folder_date_list

    # getting the kwargs (days="", seconds="", microseconds="") from get_date_difference function
    difference = get_date_difference(date)
    if difference.days < 4:
        new_folder_checker = True
        date = '-'.join(*get_date(date))
    return folder_name, date, new_folder_checker


def get_last_weekly_folder(driver, target_url):
    driver.get(target_url)  # opens the url in headless mode in order to get the info from sourceforge
    # this one is getting the first([1]) element of the table(by XPath) which is the last added folder
    table = get_table_by_xpath(driver, '//*[@id="files_list"]/tbody/tr[1]')

    # table.text returns string separated by new lines
    # splitting the string into list, because the 1st element (index 0)
    # contains the last folder name and last date of modification
    full_info = table.text.split("\n")[0]

    # creating variables for the founded elements - folder, date (or hours) since last modification
    current_name = ""
    found_date = ""

    # this will change if the folder is newly created
    new_folder_found = False

    # checking if the folder is newly created ( last 24 hours )
    if " < " in full_info:
        current_name, found_date = full_info.split(" < ")
        new_folder_found = True
    else:
        current_name, found_date, new_folder_found = check_date(full_info.split(), new_folder_found)

    if new_folder_found:
        output = f"Modified folder found!\nName: {current_name}\nDate: {found_date}\n" \
                 f""f"Download link: {target_url + current_name}"
    else:
        output = f"Everything is the same as in {found_date}\n" \
                 f"Last created folder is {current_name} ({get_url('last_weekly', current_name)})\n" \
                 f"Better luck next time!"

    return output, current_name, found_date


def get_link_for_specific_device(device, release):
    """
    :param device: gets device rom name in order to search for it in the folder and to find the first match
    :param release: is needed for the right url to be given to the driver
    :return: download link or None
    """
    driver = get_driver()
    if release == "weekly":
        target_url = get_url('last_weekly', (get_last_weekly_folder(driver, get_url('weekly'))[1]))
    else:
        target_url = get_url('stable')
    driver.get(target_url)
    table = get_table_by_xpath(driver, '//*[@id="files_list"]')
    for item in table.text.split("\n")[5:]:
        if f"xiaomi.eu_{device}_V14" in item:
            download_part = item.split(" ")[0]
            return target_url + "/" + download_part
    else:
        return "Nothing found in the last weekly folder!"
