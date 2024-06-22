# XiaomiEuRomChecker
Web application for checking for the latest xiaomi.eu weekly or stable HyperOS roms in sourceforge cloud folders.

All users will have:
- access to the available devices list
- an option to get info about selected device
- access to the download links section
  
Registered users will have additional options:
- CRUD for the links
- option to shorten the links with bit.ly API
- to report unsupported or missing devices

Staff users will have an option to use Admin panel based on their permissions

 You can check the demo here:
 https://romchecker.pythonanywhere.com
 
 Deployment server bugs:
- Unfortunately, bit.ly service returns Server Error (500), because of the hosting on pythonanywhere.
 So it redirects to index page if when error occurs
- When sending email for missing/unsupported devices, it returns Server Error (500), but the email is sent.
- It can't make requests to xiaomiui.net/all-xiaomi-codenames-5137/ because it returns 403. (it can't be whitelisted)
 So I've made the Market Name field to be free text instead of dynamically generated dropdown

The project is inspired and based on the functionality of this repo (also mine):
https://github.com/chebishev/xiaomi.eu-weekly-roms-checker
