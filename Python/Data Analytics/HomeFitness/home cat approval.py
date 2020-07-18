import pandas as pd


# Opening the responses
df = pd.read_csv("Home Fitness Chatbot (Responses).csv")

# Focus on the users who work out at home
df = df[df["Where do you work out?"] == "Home"]

# Getting the approval rate of each principle
principle = ["Individuals need a specific workout plan to sustain their fitness",
            "I think that having a bot on my phone to ask questions is convenient",
            "A trainee needs a coach to follow up on them and ensure that their progress is adequate",
            "Diet advice and nutrition is important for my workout plan",
            "Chatbot checking on users individually will help them reach their goals"]

for i, p in enumerate(principle):
    print(f"{i + 1}. {p}:")
    # rounding up
    print(round(df[p].mean(), 2))
    print()

# Getting the approval rate of each feature
features = ["A bot showing how to  properly perform exercises",
            "recommending workouts",
            "Creating a custom workout plan",
            "specific workouts for body muscles",
            "calories burned per workout",
            "Video illustrations",
            "daily follow up and checking: reminding the user to work out etc."]

for i, f in enumerate(features):
    print(f"{i + 1}. {f}:")
    print(round(df[f].mean(), 2))
    print()