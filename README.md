# XiaomiEuRomChecker
Web application for checking for the latest xiaomi.eu stable MIUI or HyperOS roms in sourceforge cloud folders.
It uses requests and BeautifulSoup for web scrapping and json for data storage.
Latest HyperOS Json is automatically updated with github actions and reads the forum image with listed devices using openai.
The list is parsed to json and uploaded to the server.

All users will have:
- access to the available ROMs list
- access to the available devices list
- get the download links
  
Registered users will have additional options:
- to report unsupported or missing devices
(registration doesn't require any personal data and it is only there to prevent bots from filling the form)

Staff users will have an option to use Admin panel based on their permissions

 You can check the demo here:
 https://romchecker.pythonanywhere.com
 

The project is inspired and based on the functionality of this repo (also mine):
https://github.com/chebishev/xiaomi.eu-weekly-roms-checker


The initial version was with educational purposes and some additional features were included, but it wasn't suitable for this free deployment.
There were 5 models (users, devices, links, themes, tips), bit.ly link shortener, registered users had CRUD operations on links, 10 views (some of them with classes), tests, etc. (Requirements of the exam were met),
Functional database with additional tables was used to store the data. For the exam it was postgreSQL.
Fixtures to fill the database with updated devices and ROMs was also used.
It had dockerimage for deployment in aws ec2.

Enjoy the lite version!