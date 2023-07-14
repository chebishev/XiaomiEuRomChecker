import os

# To turn of webdriver-manager logs:
# import logging
# os.environ['WDM_LOG'] = str(logging.NOTSET)

# To turn off the progress bar which is displayed on downloads:
# os.environ['WDM_PROGRESS'] = str(0)

# To save binaries to project.root/.wdm.:
os.environ['WDM_LOCAL'] = '1'
