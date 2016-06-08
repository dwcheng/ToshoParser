import re


class Filter (object):

    def __init__(self, name, conditions=None):
        self.name = name
        if conditions is None:
            self.conditions = []
        else:
            self.conditions = conditions

    def __str__(self):
        return self.name

    def add(self, condit):
        self.conditions.append(condit)

    def check(self, match_against):
        for condit in self.conditions:
            if not condit.check(match_against):
                return False
        return True


class Condition (object):

    def __init__(self, match_string, operation):
        self.match_string = match_string
        self.operation = operation

    def __str__(self):
        return str(self.match_string, " ", self.operation)

    def check(self, match_against):
        if self.operation == "include":
            if re.search(self.match_string, match_against, flags=re.I):
                return True
            else:
                return False
        elif self.operation == "exclude":
            if re.search(self.match_string, match_against, flags=re.I):
                return False
            else:
                return True