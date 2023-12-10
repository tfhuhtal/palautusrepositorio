from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matseri = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matseri, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matseri, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matseri, HasFewerThan(value, attr)))

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def notPlaysIn(self, team):
        return QueryBuilder(And(self._matseri, Not(PlaysIn(team))))

    def build(self):
        return self._matseri