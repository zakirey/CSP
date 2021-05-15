from tkinter import *

colors = ['Red', 'Yellow', 'Blue', 'Green', 'Ivory']
pets = ['Dog', 'Fox', 'Snails', 'Horse', 'Zebra']
beverage = ['OrangeJuice', 'Tea', 'Coffee', 'Milk', 'Water']
nationality = ['Englishman', 'Spaniard', 'Norwegian', 'Ukrainian', 'Japanese']
cigarettes = ['Kools', 'Chesterfields', 'OldGold', 'LuckyStrike', 'Parliaments']


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title('Zebra Solution')
        self.root.update()

    def print(self, houses):
        Label(self.root, text="House ").grid(row=0, column=0)
        Label(self.root, text="Color ").grid(row=1, column=0)
        Label(self.root, text="Pet ").grid(row=2, column=0)
        Label(self.root, text="Drink ").grid(row=3, column=0)
        Label(self.root, text="Nationality ").grid(row=4, column=0)
        Label(self.root, text="Smoke ").grid(row=5, column=0)
        for i, house in enumerate(houses, start=1):
            Label(self.root, text=str(i)).grid(row=0, column=i)
            for var in house:
                if var in colors:
                    Label(self.root, text=var).grid(row=1, column=i)
                if var in pets:
                    Label(self.root, text=var).grid(row=2, column=i)
                if var in beverage:
                    Label(self.root, text=var).grid(row=3, column=i)
                if var in nationality:
                    Label(self.root, text=var).grid(row=4, column=i)
                if var in cigarettes:
                    Label(self.root, text=var).grid(row=5, column=i)
