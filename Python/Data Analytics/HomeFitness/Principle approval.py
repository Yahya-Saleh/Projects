import pandas as pd


# Opening the responses
df = pd.read_csv("Home Fitness Chatbot (Responses).csv")

principle = ["Individuals need a specific workout plan to sustain their fitness",
            "I think that having a bot on my phone to ask questions is convenient",
            "A trainee needs a coach to follow up on them and ensure that their progress is adequate",
            "Diet advice and nutrition is important for my workout plan",
            "Chatbot checking on users individually will help them reach their goals"]

# Getting the approval rate of each principle
for i, p in enumerate(principle):
    print(f"{i + 1}. {p}:")
    # rounding up
    print(round(df[p].mean(), 2))
    print()