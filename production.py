fileContent = open("calendarHW/settings.py").readlines()[:]

fileContent[fileContent.index("DEBUG = True\n")] = "DEBUG = False\n"
fileContent[fileContent.index("ALLOWED_HOSTS = [\"*\"]\n")] = "ALLOWED_HOSTS = [\"homework-hhg.com\", \"www.homework-hhg.com\"]\n"
fileContent.append("SESSION_COOKIE_SECURE = True\nSESSION_COOKIE_AGE = 1814400\nCSRF_COOKIE_SECURE = True\nCSRF_COOKIE_AGE = 1814400\nSECURE_SSL_REDIRECT = True\n# HSTS settings\nSECURE_HSTS_SECONDS = 31536000 # 1 year\nSECURE_HSTS_PRELOAD = True\nSECURE_HSTS_INCLUDE_SUBDOMAINS = True")

fileContent = "".join(fileContent)

file = open("calendarHW/settings.py", "w")
file.write(fileContent)
file.close()
