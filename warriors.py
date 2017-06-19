from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import numpy as np


url = 'http://www.espn.com/nba/team/stats/_/name/gs/golden-state-warriors'
uClient = req(url)#opening connection, grabbing page
page_html = uClient.read()
uClient.close()#close connection
page_soup = soup(page_html, "html.parser") #parsing html page_html


#shooting statistics for GSW Steph, KD, Klay, and Dray for the 16-17 season
shooting_percentage = page_soup.findAll("div", {"class":"mod-content"})
players = page_soup.findAll("table", {"cellspacing":"1", "cellpadding":"3", "class":"tablehead"})[1]
team_info = []
for player in players:
	team_info.append(player)
team_info.pop(0)

FG_per = []
names = []
for teammate in team_info:
	try:
		names.append(teammate.a.text)
		FG_per.append(teammate.findAll("td")[3].text)

	except AttributeError:
		print()

names.pop(0)
FG_per.pop(0)
x = 0
while x < len(names):
	print(names[x], FG_per[x])
	x+=1

pos=np.arange(len(names))
plt.plot(pos,FG_per)
plt.xticks(pos, names,rotation="vertical",fontsize= 7)
plt.xlabel('Player')
plt.ylabel('Field Goal %')
plt.title('Warriors 16-17 FG%')
plt.subplots_adjust(bottom=0.3)

plt.show()


print()
#finding the leaders of the GSW for the 16-17 season
team_leaders = page_soup.findAll("div",{"class":"mod-content"})
leaders = ['Points Leader|', 'Rebounds Leader|', 'Assists Leader|', 'Steals Leader|', 'Blocks Leader|']
for i in range(5):
    print(leaders[i],team_leaders[i].find("li", {"class":"name"}).text,'|', team_leaders[i].find("li", {"class":"stat"}).text)


print()

#my-players-table > div.mod-container.mod-table > div:nth-child(3) > table > tbody > tr.oddrow.player-46-3975
