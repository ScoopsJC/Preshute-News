# scam call centre

from twilio.rest import Client
import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import time

while True:
    today = date.today()
    today = today.strftime("%d-%m-%Y")

    url = "https://www.theguardian.com/uk"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    headlines = soup.find("body").find_all("h3")[:10]

    f = open("news.txt","w")
    f.write("...\n")
    f.write("\n")
    f.write("Top 10 News Headlines for Today: ")
    f.write("\n")

    counter = 1
    for i in headlines:
        f.write("\n%s. %s"%(counter,i.text.strip()))
        f.write("\n")
        counter += 1
    f.close()

    texting = ""
    with open('news.txt') as f:
        for i in range(30):
            texting += str(f.readline())

    client = Client("ACcb8f6c440f2041759e77a90c91ed5e6a","bf9fc96f7cb1e72e2f45d63de1cbc220")

    client.messages.create(to = "+447944190204",
    from_ = "+12058836732",
    body = texting)

    print("Messages Sending")
    time.sleep(60)
