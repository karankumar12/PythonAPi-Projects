from typing import Dict

import requests
import os
from gtts import gTTS

class Sources:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Articles:
    def __init__(self, title, description):
        self.title = title
        self.description = description

#Function to make the GET request to receive all the Sources
def getSources():
        url = "https://newsapi.org/v1/sources"
        sources = requests.get(url).json()
        return sources

#Function to display all the sources in sourceList and request for a choice
def dispayMenu(sourceList):
    print("Choose a source: ")
    j = 0
    for j in range(len(sourceList)):
        print(str(j+1) + "." + sourceList[j].name)

    while True:
        choice = input()
        choice = int(choice)-1
        if(choice in range(len(sourceList))):
                return choice
        print("The choice was not in the given range, please enter again: ")


#Function to make the GET request to receive the articles if the given source
def receiveArticles(source):
    url = " https://newsapi.org/v1/articles"

    parameters = {
        'apiKey' : '4dbc17e007ab436fb66416009dfb59a8',
        'source': source,
        'sortBy': 'top'
    }

    response = requests.get(url, params= parameters).json()
    articles = response["articles"]
    results = [];

    for ar in articles:
        results.append(Articles(ar["title"], ar["description"]));

    return results

#Function to take in an object of Articles, convert the title and desc into speech and read it out loud
def convertToSpeech(results):

    j=0
    for j in range(len(results)):

        Number = gTTS(text = "Article "+str(j+1), lang='en')
        Number.save("Number.mp3")
        os.system("afplay Number.mp3")

        myObj = gTTS(text = results[j].title, lang='en', slow=False)
        myObj.save("title.mp3")
        os.system("afplay title.mp3")

        myObj2 = gTTS(text = results[j].description, lang='en', slow=False)
        myObj2.save("description.mp3")
        os.system("afplay description.mp3")

sourceJson = getSources()
sources = sourceJson["sources"]
sourceList = []


#Add the source name and the unique Id to the list
for i in sources:
    sourceList.append(Sources(i["name"],i["id"]))

#Display the menu to receive user choice
choice = dispayMenu(sourceList)

#Receive the Source ID for the selected choice
source = sourceList[choice].id

#Receive the articles from the given source
results = receiveArticles(source)

#Convert the articles text to speech and read it
convertToSpeech(results)


