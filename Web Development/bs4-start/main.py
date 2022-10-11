from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.findAll(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link_line = article_tag.find(name="a")
    link = link_line.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) if score else 0 for score in soup.findAll(name="span", class_="score") ]
print(article_upvotes)
largest_number = max(article_upvotes)
print(largest_number)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])
# print(article_texts)
# print(article_links)
# print(article_upvotes)





















# import lxml might need to use this instead depending on the website
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# # represents entire html code now
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
# all_anchor_tags = soup.findAll(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)