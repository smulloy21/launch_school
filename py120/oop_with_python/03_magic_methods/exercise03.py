class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __str__(self):
        return self.name

    def __iadd__(self, votes):
        if not isinstance(votes, int):
            return NotImplemented

        self.votes += votes

    def __gt__(self, other):
        if not isinstance(other, Candidate):
            return NotImplemented

        return self.votes > other.votes


class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        for candidate in self.candidates:
            print(f'{candidate}: {candidate.votes} votes')

        winner = self._winner()
        winning_percentage = self._vote_percentage(winner)
        print(f'{winner.name} won: {winning_percentage}% of votes')

    def _winner(self):
        return max(self.candidates)

    def _vote_percentage(self, winner):
        total_votes = sum([candidate.votes for candidate in self.candidates])
        return winner.votes / total_votes * 100


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()


# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes
