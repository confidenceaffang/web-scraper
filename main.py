import requests
from bs4 import BeautifulSoup


for year in range(1824,2020,4):
    url = f"https://en.wikipedia.org/wiki/{year}_United_States_presidential_election"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(year)

    table = soup.find_all('table')[3]

    table3 = soup.find_all("table")[0]

    table2 = soup.find("table", class_= "wikitable sortable")

    years = []
    states = []
    candidate_names = []
    parties = []
    popular_votes = []
    electoral_votes = []



    for row in table2.find_all('tr')[0:]:
        h = table2.find_all("th")
        data = row.find_all('td')
        for u in h:
            t = u.text.strip()
            print(t)
        w = [i.text.strip() for i in data]
        print(w)


        if data:
            year = data[0].text.strip()
            state = data[1].text.strip()
            candidate_name = data[2].text.strip()
            party = data[3].text.strip()
            popular_vote = data[4].text.strip()
            electoral_vote = data[5].text.strip()

            years.append(year)
            states.append(state)
            candidate_names.append(candidate_name)
            parties.append(party)
            popular_votes.append(popular_vote)
            electoral_votes.append(electoral_vote)
            if IndexError(data):
                pass
    w =table.text

    b = table3.text[184:]
    print(b)

    with open('ElectionScrape.txt', 'a') as f:
        f.write(f"{b}")
        f.write(f"{w}")
        for i in range(len(years)):
            f.write(f"{years[i]},{states[i]},{candidate_names[i]},{parties[i]},{popular_votes[i]},{electoral_votes[i]}\n")
