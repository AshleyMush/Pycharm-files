from bs4 import BeautifulSoup
import requests





# year = input("Which year do  you want to travel to? Type the date in this format YYYY-MMM-DD:\n")

year = "2005-06-18"

URL =f"https://www.billboard.com/charts/hot-100/{year}/"

response = requests.get(URL)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")

#TODO 2. Using what you've learnt about BeautifulSoup, scrape the top 100  from billboard song titles on that date into a Python List.

# Find the outermost ul
chart_list_row = soup.find(name="ul", class_="o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-100 lrv-u-background-color-white a-chart-has-chart-detail")

print(chart_list_row)

#TODO find all song titles

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)




# Find all the h3 tags with the specified id within the outer_ul
# song_titles = outer_ul.find_all("h3", id="title-of-a-story")
#
# for title in song_titles:
#     print(title.text.strip())
