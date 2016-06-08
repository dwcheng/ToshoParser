class Menu(object):

    def __init__(self, name, buttons=None):
        self.name = name
        if buttons is None:
            self.buttons = []
        else:
            self.buttons = buttons

    def display(self):
        print(self.name)

        for button in self.buttons:
            print("    ", button.nav, button.name)

        self.user_input()

    def add(self, button):
        self.buttons.append(button)

    def user_input(self):
        error_count = 0

        selection = input("> ")

        for button in self.buttons:
            if selection == str(button.nav):
                button.do()
            else:
                error_count += 1

        if error_count >= len(self.buttons):
            print("Invalid selection")
            self.display()


class Button(object):

    def __init__(self, name, function, nav):
        self.name = name
        self.function = function
        self.nav = nav

    def do(self):
        self.function()