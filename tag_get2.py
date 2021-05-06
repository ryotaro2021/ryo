from selenium import webdriver
import time
#import pandas as pd

browser = webdriver.Chrome()
browser.implicitly_wait(3)


url = "https://yomou.syosetu.com/rank/list/type/daily_total/"

browser.get(url)
time.sleep(3)
print("Show the Ranking")

novel_inf = browser.find_elements_by_link_text("小説情報")
novel_url = []
for n in range(len(novel_inf)):
	novel_url.append(novel_inf[n].get_attribute("href"))
print("Ranking top 300 URL get")

for n in range(10):
	browser.get(novel_url[n])
	print("best" + str(n+1))

	element = browser.find_elements_by_tag_name('td')
	keyword = element[2].text
	genre = element[3].text
	print("		GENRE", genre)
	print("		KEYWORD",keyword)
	time.sleep(2)
	with open("keyword.dat", mode = "a") as f:
		f.write(keyword)

browser.quit()
