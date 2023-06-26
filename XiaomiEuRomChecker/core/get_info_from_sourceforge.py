from XiaomiEuRomChecker.core.functionality import get_driver, get_url, check_date, get_last_weekly_folder

target_url = get_url('weekly')  # "weekly", "stable" and "last_weekly" options only
driver = get_driver()    # returns configured webdriver (service(path) + options(headless, etc.)
driver.get(target_url)   # opens the url in headless mode in order to get the info from sourceforge

output = get_last_weekly_folder(driver, target_url)
