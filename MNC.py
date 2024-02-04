import random

class MNCGroup:
    def __init__(self, name):
        self.name = name
        self.categories = {
            "Definition of MNC": "A multinational corporation (MNC) is a company that operates in its home country, as well as in other countries around the world. It maintains a central office located in one country, which coordinates the management of all of its other offices, such as administrative branches or factories.",
            "Reasons for becoming an MNC": "Setting up production in other countries, especially in developing economies, usually translates to spending significantly less on production costs. ...",
            "MNC models": "1. Centralized model\n2. Regionalized model\n3. Multinational model",
            "Benefits of being an MNC": "In terms of efficiency, multinational companies are able to reach their target markets more easily because they manufacture in the countries where the target markets are. ...",
            "Disadvantages of being an MNC": "A multinational corporation will face increased legal complexity due to operating in multiple jurisdictions. ...",
            "Foreign direct investments": "Foreign direct investments are prevalent within multinational corporations. The investments occur when an investor or company from one country makes an investment outside the country of operation.",
            "Examples of well-known MNCs": "Coca-Cola, Microsoft, Toyota, McDonald's, IBM, General Electric, and Procter & Gamble"
        }

    def display_categories(self):
        print(f"Welcome to the {self.name} group! Here are the categories we cover:")
        for category in self.categories:
            print(f"- {category}")

    def ask_question(self):
        category = random.choice(list(self.categories.keys()))
        print(f"\nQuestion: What is the definition of a multinational corporation (MNC)?")
        answer = input(f"Answer: ")
        if answer.lower() == self.categories[category].split('.')[0].lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {self.categories[category]}")

def main():
    group_name = "MNCs: Scaling the Globe"
    mnc_group = MNCGroup(group_name)
    mnc_group.display_categories()
    mnc_group.ask_question()

if __name__ == "__main__":
    main()