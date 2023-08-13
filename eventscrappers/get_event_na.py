import requests
from bs4 import BeautifulSoup
import psycopg2
import toml

# EVENT STANDARD INFO
EVENT_CATEGORY = {"event_category": "muziek", "event_category_id": 1}
# een event bestaat uit:
# event_name -> naam event (a.vc_gitem-link)
# event_date -> datum event (div.vc_gitem-acf.date-agenda.vc_gitem-align-center.field_60a2681523738)
# event_time -> tijd event (div.vc_gitem-acf.time-agenda.vc_gitem-align-center.field_60a26624c6c72)
# event_price -> prijs event (div.vc_gitem-acf.price-agenda.vc_gitem-align-center.field_60a2682d23739)
# event_link -> link naar event (a.vc_gitem-link)
EVENT_INFO = {
    "event_name": "",
    "event_date": "",
    "event_time": "",
    "event_price": "",
}

# URL TO SCRAPE
URL = "https://denieuweanita.nl/"


# get page
page = requests.get(URL)
# parse page
soup = BeautifulSoup(page.content, "html.parser")

# save to file to better inspect
with open("na.html", "w") as file:
    file.write(soup.prettify())

# get all events
events = soup.find_all("div", "vc_grid-item vc_clearfix vc_col-sm-12")
with open("na_events.html", "w") as file:
    file.write(soup.prettify())


# get event details
for event in events:
    event_name = event.find("a", "vc_gitem-link").text
    event_date = event.find(
        "div", "vc_gitem-acf date-agenda vc_gitem-align-center field_60a2681523738"
    ).text
    event_time = event.find(
        "div", "vc_gitem-acf time-agenda vc_gitem-align-center field_60a26624c6c72"
    ).text

    event_info = {
        "event_name": event_name,
        "event_date": event_date,
        "event_time": event_time,
        "event_price": "",
    }
    print(event_info)

# connect to database
# read data from toml file

# with open("python_scrappers/backend/eventscrappers/db_settings.toml", "r") as f:
#     db_settings = toml.load(f)["development"]

# # conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")
# conn = psycopg2.connect(
#     f"dbname={db_settings['database']} user={db_settings['user']} password={db_settings['password']}"
# )
# print(conn)
# # insert event into databasest
# # close connection
# conn.close()
