import random

houses = {
    "a": "Ravenclaw",
    "b": "Slytherin",
    "c": "Hufflepuff",
    "d": "Gryffindor"
}

questions = [
    {
        "question": "You enter a magical garden. What do you look at first?",
        "choices": [
            "a. Luminous Pool with something in its depths",
            "b. Statue with a twinkling eye",
            "c. A silver tree with golden apples",
            "d. Talking Toadstools"
        ]
    },
    {
        "question": "What smell is most appealing to you?",
        "choices": [
            "a. Home",
            "b. The sea",
            "c. Fresh parchment",
            "d. A log fire"
        ]
    },
    {
        "question": "Which of the following do you have the most trouble dealing with?",
        "choices": [
            "a. Hunger",
            "b. Being ignored",
            "c. Cold",
            "d. Boredom"
        ]
    },
    {
        "question": "Who would you pick as your partner?",
        "choices": [
            "a. William Dalton",
            "b. Pilar Herce",
            "c. Wilfredo Ocampo",
            "d. William Dalton"
        ]
    },
    {
        "question": "Which subject at Hogwarts would you be most interested in studying?",
        "choices": [
            "a. Apparition",
            "b. Hexes/Jinxes",
            "c. Secrets about the castle",
            "d. Broom Flying"
        ]
    },
    {
        "question": "A Muggle approaches you and says you’re a wizard. How do you react?",
        "choices": [
            "a. Ask them why they think so",
            "b. Agree and offer a sample of a jinx",
            "c. Agree and walk away, bluffing",
            "d. Express your concern and offer to call a mental hospital"
        ]
    },
    {
        "question": "Which path do you take?",
        "choices": [
            "a. Twisting leafy path through the woods",
            "b. A dark, lantern-lit alley",
            "c. A wide, sunny, grassy path",
            "d. A cobblestone street lined with ancient buildings"
        ]
    },
    {
        "question": "Which nightmare would scare you most?",
        "choices": [
            "a. None of your friends or family know who you are",
            "b. Being trapped in a dark room with an eye peering at you through a keyhole",
            "c. Being caught up high with no handholds",
            "d. Being forced to speak in a funny voice so that everyone laughs at you"
        ]
    }
]

scores = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}

answers = []

# START ASKING QUESTIONS

print("WELCOME TO HOGWARTS!!")
print("Please answer some questions so that Sorting Hat identifies which House to put you\n\n")

picked_questions = random.sample(questions, k=5)
for i, question in enumerate(picked_questions):
    display = f"\nQ{i+1} {question.get('question')}\n"
    display += ("\n").join([f"{choice}" for choice in question.get("choices")])
    display += "\nAnswer: "
    valid_answer = False
    retries = 0
    while valid_answer is False:
        if retries > 0:
            display = "\nPlease select only from a, b, c, or d. Answer: "
        answer = input(display).lower()

        if answer in ['a', 'b', 'c', 'd']:
            valid_answer = True
        else:
            retries += 1

    answers.append(answer)

# COMPUTE AND DOCUMENT SCORES

for i, answer in enumerate(answers):
    if answer in answers[i:]:
        scores[answer] += 1

# GET LETTER THAT IS MOST ANSWERED

print(f"\n\nYou are going to {houses[max(scores, key=scores.get)]}. CONGRATULATIONS!!!")
