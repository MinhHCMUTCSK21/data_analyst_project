from bs4 import BeautifulSoup
import requests
import pandas as pd

world_cup_years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018]
def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup';
    res = requests.get(web)
    content = res.text
    soup = BeautifulSoup(content, 'lxml')

    matches_2014 = soup.find_all('div', class_='footballbox')
    home = []
    away = []
    score = []


    for match in matches_2014:
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    df = pd.DataFrame({'home': home, 'score': score, 'away': away})
    df['year'] = year
    return df

all_matches = [get_matches(year) for year in world_cup_years]

df = pd.concat(all_matches, ignore_index=True)
df.to_csv('world_cup.csv', index=False)

