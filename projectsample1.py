import re
import urllib.request
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd
import sys
import re
from GoogleNews import GoogleNews


r = urllib.request.urlopen("https://news.google.co.in/")
html = r.read()
parse = "html.parser"
soup = BeautifulSoup(html,parse)

#HEADLINES
headlines = []
content_headline = []
for head1 in soup.findAll("a", attrs={"class":"DY5T1d RZIKme"}, href = True):
    headlines.append(head1.get_text(strip=True))
    ct = head1.get("href")
    if ct is None:
        pass
    content_headline.append("https://news.google.com" + ct)
df1 = pd.DataFrame(list(zip(headlines, content_headline)), columns=["Headlines", "Link"])
df1.to_csv("headlines.csv")

#COVID SECTION
r1 = urllib.request.urlopen("https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
html = r1.read()
parse = "html.parser"
soup = BeautifulSoup(html,parse)

headline1 = []
content_link = []
for head2 in soup.findAll("a", attrs={"class":"DY5T1d RZIKme"}, href = True):
    headline1.append(head2.get_text(strip=True))
    ct1 = head2.get("href")
    if ct1 is None:
        pass
    content_link.append("https://news.google.com" + ct1)
df2 = pd.DataFrame(list(zip(headline1, content_link)), columns=["Covid Headlines", "Link"])
df2.to_csv("covid_headline.csv")

#INDIA SECTION
r1 = urllib.request.urlopen("https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
html = r1.read()
parse = "html.parser"
soup = BeautifulSoup(html,parse)

headline2 = []
content_link1 = []
for head3 in soup.findAll("a", attrs={"class":"DY5T1d RZIKme"}, href = True):
    headline2.append(head3.get_text(strip=True))
    ct2 = head3.get("href")
    if ct2 is None:
        pass
    content_link1.append("https://news.google.com" + ct2)
df3 = pd.DataFrame(list(zip(headline2, content_link1)), columns=["India Headlines", "Link"])
df3.to_csv("india_headline.csv")

#WORLD SECTION
r2 = urllib.request.urlopen("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen")
html = r2.read()
parse = "html.parser"
soup = BeautifulSoup(html,parse)

headline3 = []
content_link2 = []
for head4 in soup.findAll("a", attrs={"class":"DY5T1d RZIKme"}, href = True):
    headline3.append(head4.get_text(strip=True))
    ct3 = head4.get("href")
    if ct3 is None:
        pass
    content_link2.append("https://news.google.com" + ct3)
df4 = pd.DataFrame(list(zip(headline3, content_link2)), columns=["World Headlines", "Link"])
df4.to_csv("world_headline.csv")

#BUSINESS SECTION
r3 = urllib.request.urlopen("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen")
html = r3.read()
parse = "html.parser"
soup = BeautifulSoup(html,parse)

headline4 = []
content_link3 = []
for head5 in soup.findAll("a", attrs={"class":"DY5T1d RZIKme"}, href = True):
    headline4.append(head5.get_text(strip=True))
    ct4 = head5.get("href")
    if ct4 is None:
        pass
    content_link3.append("https://news.google.com" + ct4)
df5 = pd.DataFrame(list(zip(headline4, content_link3)), columns=["Business Headlines", "Link"])
df5.to_csv("business_headline.csv")
