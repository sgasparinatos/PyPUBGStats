import requests
from bs4 import BeautifulSoup

PLAYER_NAME = "int2ag0"

class PubgStats():

    def __init__(self, player, autorefresh=False, interval=0):
        self.player = player
        self.auto = autorefresh
        self.interval = interval
        self.url = "https://pubg.me/player/" + self.player
        self.kills = -1
        self.wins = -1
        self.rounds = -1
        self.distance = -1

    def refresh_data(self):
        r = requests.get(self.url)
        if r.status_code != 200:
            return False

        soup = BeautifulSoup(r.text, 'lxml')
        stat_table = soup.find_all('table', class_='table simple-stat-table')
        soup2 = BeautifulSoup(stat_table.__str__(), 'lxml')
        for row in soup2.find_all('tr'):
            txt = row.get_text(":")
            if "Kills" in txt:
                self.kills = int(txt.split(":")[1])
            elif "Wins" in txt:
                self.wins = int(txt.split(":")[1])
            elif "Rounds" in txt:
                self.rounds = int(txt.split(":")[1])
            elif "Distance" in txt:
                self.distance = int(txt.split(":")[1].replace(" km", ""))

        return True

    def get_kills(self):
        return self.kills

    def get_wins(self):
        return self.wins

    def get_rounds(self):
        return self.rounds

    def get_summary(self):
        return self.kills, self.wins, self.rounds

    def print_summary(self):
        print(20 * "-")
        print("KILLS\t" + str(self.kills))
        print("WINS\t" + str(self.wins))
        print("ROUNDS\t" + str(self.rounds))
        print("DIST\t" + str(self.distance))
        print(20 * "-")

if __name__ == '__main__':

    ps = PubgStats(PLAYER_NAME)
    ps.refresh_data()
    ps.print_summary()
