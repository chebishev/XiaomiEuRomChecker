from XiaomiEuRomChecker.auth_app.scraper import scrape_config_by_url


def telegram_message():
    soup = scrape_config_by_url("https://xiaomi.eu/community/link-forums/roms-download.73/")
    output = [soup.find('h1').text]
    all_links = soup.find_all("a", href=True, class_="link link--external")
    for link in all_links:
        if "sourceforge.net" in link.text:
            output.append(link['href'])
        if "androidfilehost.com" in link.text:
            output.append(link['href'])
    changelog = soup.find_all('div', class_="bbWrapper")
    for c in changelog:
        current_result = c.text.split(".")
        if current_result[0].startswith("CHANGELOG"):
            output.append(current_result[0])
    return output


# or print the result directly in the console:
# print(*telegram_message(), sep="\n")
