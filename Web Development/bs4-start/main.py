from bs4 import BeautifulSoup
# import lxml might need to use this instead depending on the website

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# represents entire html code now
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())
print(soup)