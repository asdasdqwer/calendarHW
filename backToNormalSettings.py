fileContent = open("calendarHW/settings.py").readlines()[:]
fileContent[fileContent.index("DEBUG = False\n")] = "DEBUG = True\n"
fileContent[fileContent.index("ALLOWED_HOSTS = [\"homework-hhg.com\", \"www.homework-hhg.com\"]\n")] = "ALLOWED_HOSTS = [\"*\"]\n"
fileContent.remove("SESSION_COOKIE_SECURE = True\n")
fileContent.remove("SESSION_COOKIE_AGE = 1814400\n")
fileContent.remove("CSRF_COOKIE_SECURE = True\n")
fileContent.remove("CSRF_COOKIE_AGE = 1814400\n")
fileContent.remove("SECURE_SSL_REDIRECT = True\n")
fileContent.remove("# HSTS settings\n")
fileContent.remove("SECURE_HSTS_SECONDS = 31536000 # 1 year\n")
fileContent.remove("SECURE_HSTS_PRELOAD = True\n")
fileContent.remove("SECURE_HSTS_INCLUDE_SUBDOMAINS = True")

fileContent = "".join(fileContent)

file = open("calendarHW/settings.py", "w")
file.write(fileContent)
file.close()