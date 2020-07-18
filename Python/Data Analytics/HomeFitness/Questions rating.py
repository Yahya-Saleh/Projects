import pandas as pd


# Opening the responses
df = pd.read_csv("Home Fitness Chatbot (Responses).csv")

features = ["A bot showing how to  properly perform exercises",
            "recommending workouts",
            "Creating a custom workout plan",
            "specific workouts for body muscles",
            "calories burned per workout",
            "Video illustrations",
            "daily follow up and checking: reminding the user to work out etc."]

# Getting the approval rate of each feature
for i, f in enumerate(features):
    print(f"{i + 1}. {f}:")
    print(round(df[f].mean(), 2))
    print()