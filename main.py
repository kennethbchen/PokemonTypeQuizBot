from webbot import Browser
from itertools import combinations_with_replacement

q1 = ["I won", "I visited", "I explored", "I made", "I took"]
q2 = ["Adventure", "Relaxation", "Knowledge", "Friends and Family", "Competition"]
q3 = ["Historical", "Hot", "Theme", "Oceanside", "Botanical"]
q4 = ["Friendly", "Passionate", "Resourceful", "Adventurous", "Cool"]
q5 = ["Sour", "Chips", "Blueberries" , "Smoothies", "Chocolate"]
q6 = ["My glasses", "My smile", "My backpack", "My headphones", "My sneakers"]

#q1 = ["I won a contest", "I visited a neat museum", "I explored a new trail", "I made a new friend", "I took a spa day"]
#q2 = ["Adventure", "Relaxation", "Knowledge", "Friends and Family", "Competition"]
#q3 = ["Historical Site", "Hot springs", "Theme Park", "Oceanside", "Botanical garden"]
#q4 = ["Friendly", "Passionate", "Resourceful", "Adventurous", "Cool"]
#q5 = ["Sour gummies—um…YUM", "Chips & salsa—I like it spicy", "Blueberries" , "Smoothies—to keep it cool", "Chocolate chip cookies—a classic snack"]
#q6 = ["My glasses", "My smile", "My backpack", "My headphones", "My sneakers"]

messages = ["You’re a Grass-type Pokémon!", "You’re a Fire-type Pokémon!", "You’re a Water-type Pokémon!", "You’re an Electric-type Pokémon!", "You’re a Normal-type Pokémon!"]

type = ["Grass", "Fire", "Water", "Electric", "Normal"]


results = []

web = Browser()


def process():
    for x in range(5):
        if web.exists(text=type[x], tag="p"):
            print(type[x])
            break
    web.click("Take the quiz again")


def parse_combo(combo):
    web.click(q1[combo[0] - 1], tag="span")
    web.click(q2[combo[1] - 1], tag="span")
    web.click(q3[combo[2] - 1], tag="span")
    web.click(q4[combo[3] - 1], tag="span")
    web.click(q5[combo[4] - 1], tag="span")
    web.click(q6[combo[5] - 1], tag="span")
    print(combo[0], end="\t")
    print(combo[1], end="\t")
    print(combo[2], end="\t")
    print(combo[3], end="\t")
    print(combo[4], end="\t")
    print(combo[5], end="\t")
    process()

web.go_to("https://play.nintendo.com/activities/personality-quizzes/what-pokemon-are-you/")


comb = combinations_with_replacement([1, 2, 3, 4, 5], 6)
ls = list(comb)

for combo in ls:
    parse_combo(combo)





