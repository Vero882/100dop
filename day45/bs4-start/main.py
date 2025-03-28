from bs4 import BeautifulSoup
import requests 

######## Remote Web Scraping ########
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_link = article.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_upvote = max(article_upvotes)
highest_index = article_upvotes.index(highest_upvote)
print(f"Article with the highest upvote: {article_texts[highest_index]} at {article_links[highest_index]} with {highest_upvote} upvotes.")

# article_link = soup.find_all(name="a", class_="storylink").get("href")
# article_upvote = soup.find_all(name="span", class_="score").getText()







######## Local HTML File ########
# with open("./bs4-start/website.html") as file:
#     contents = file.read()

#     soup = BeautifulSoup(contents, "html.parser")
    # print(soup.title)
    # print(soup.title.string)

    # print(soup.prettify()) # Prints the HTML in a more readable format utilizing the prettify method

    # print(soup.a) # Prints the first <a> tag in the website

    # print(soup.find_all(name="a")) # Prints all <a> tags in the website

    # for tag in soup.find_all(name="a"):
        # print(tag.getText()) # This will loop through and print all the text in each anchor tag on the page
        # print(tag.get("href")) # This will loop through and print all the links in each anchor tag on the page

    # heading = soup.find(name="h1", id="name")
    # print(heading)

    # section_heading = soup.find(name="h3", class_="heading") # Since class is a reserved word in Python, we use class_ instead
    # print(section_heading.getText()) 

    # company_url = soup.select_one(selector="p a") # This will select the first <a> tag inside a <p> tag, similar to CSS selectors
    # print(company_url) 

    # name_id = soup.select_one(selector="#name") # You can also utilize normal class and id CSS selectors
    # print(name_id)

    # headings = soup.select(selector=".heading")
    # print(headings) # This will print as a list for multiple selected elements


