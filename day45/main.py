from bs4 import BeautifulSoup
import requests

# Pull data from the website
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Find all the movie titles
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]

# Loop through the movies and extract the title text and append to the list
# for movie in movies: 
#     movie_titles.append(movie.getText())

# Reverse the list of movie titles
movie_titles.reverse()

# Write the movie titles to a text file
with open("movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")