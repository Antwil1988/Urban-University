import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.ussein = Runner('Усэйн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        if cls.all_results:
            for tournament_name in ["Usein vs Nick", "Andrew vs Nick", "Usein vs Andrew vs Nick"]:
                tournament_results = cls.all_results[tournament_name]
                print(tournament_name)
                for place, winner in tournament_results.items():
                    print(f"{place}: {winner.name}")

    def test_ussein_nick(self):
        tournament = Tournament(90, self.ussein, self.nick)
        self.all_results["Usein vs Nick"] = tournament.start()
        self.assertEqual(
            list(self.all_results["Usein vs Nick"].values())[-1].name, self.nick.name)

    def test_andrew_nick(self):
        tournament = Tournament(90, self.andrew, self.nick)
        self.all_results["Andrew vs Nick"] = tournament.start()
        self.assertEqual(
            list(self.all_results["Andrew vs Nick"].values())[-1].name, self.nick.name)

    def test_ussein_andrew_nick(self):
        tournament = Tournament(90, self.ussein, self.andrew, self.nick)
        self.all_results["Usein vs Andrew vs Nick"] = tournament.start()
        self.assertEqual(list(
            self.all_results["Usein vs Andrew vs Nick"].values())[-1].name, self.nick.name)


if __name__ == '__main__':
    unittest.main()
