# Shopping

An AI that predicts whether online shopping customers will complete a purchase. [Watch it in action!](https://youtu.be/GIOaLuQ9TCg)

## Usage

```bash
$ python shopping.py shopping.csv
Correct: 4138
Incorrect: 794
True Positive Rate: 39.58%
True Negative Rate: 91.95%
```

Pass a csv file containing teh data as a second argument. The AI return the number of correct and incorrect prediction as well as a positive rate and a negative rate.

- Positive Rate: the proportion of users who did go through with a purchase who were correctly identified.
- Negative Rate: the proportion of users who did not go through with a purchase who were correctly identified.

## Table of content

- [Shopping](#shopping)
  - [Usage](#usage)
  - [Table of content](#table-of-content)
  - [Background](#background)
  - [Algorithm](#algorithm)
  - [Sensitivity and specificity](#sensitivity-and-specificity)
  - [Shopping.csv](#shoppingcsv)
  - [Shopping.py](#shoppingpy)
  - [Acknowledgements](#acknowledgements)

## Background

When users are shopping online, not all will end up purchasing something. Most visitors to an online shopping website, in fact, likely don’t end up going through with a purchase during that web browsing session. It might be useful, though, for a shopping website to be able to predict whether a user intends to make a purchase or not: perhaps displaying different content to the user, like showing the user a discount offer if the website believes the user isn’t planning to complete the purchase. How could a website determine a user’s purchasing intent? That’s where machine learning will come in.

## Algorithm

We can think of this problem as a **supervised learning** task. Specifically, a **classification** task where we want to identify if a customer will complete a purchase given a list of parameters. Using the **k-nearest neighbor** algorithm this program will classify any new data based on training set given.

## Sensitivity and specificity

we’ll measure two values:

- **Sensitivity** (also known as the “true positive rate”): the proportion of positive examples that were correctly identified:
  - in other words, the proportion of users who did go through with a purchase who were correctly identified.
- **Specificity** (also known as the “true negative rate”): the proportion of negative examples that were correctly identified:
  - in this case, the proportion of users who did not go through with a purchase who were correctly identified.

---

## [Shopping.csv](shopping.csv)

There are about 12,000 user sessions represented in this spreadsheet: represented as one row for each user session. The first six columns measure the different types of pages users have visited in the session: the `Administrative`, `Informational`, and `ProductRelated` columns measure how many of those types of pages the user visited, and their corresponding `_Duration` columns measure how much time the user spent on any of those pages.

The `BounceRates`, `ExitRates`, and `PageValues` columns measure information from Google Analytics about the page the user visited. `SpecialDay` is a value that measures how closer the date of the user’s session is to a special day (like Valentine’s Day or Mother’s Day). `Month` is an abbreviation of the month the user visited. `OperatingSystems`, `Browser`, `Region`, and `TrafficType` are all integers describing information about the user themselves. `VisitorType` will take on the value Returning_Visitor for returning visitors and some other string value for non-returning visitors. `Weekend` is TRUE or FALSE depending on whether or not the user is visiting on a weekend.

Perhaps the most important column, though, is the last one: the `Revenue` column - our output. This is the column that indicates whether the user ultimately made a purchase or not: TRUE if they did, FALSE if they didn’t. This is the column that we’d like to learn to predict (the “label”), based on the values for all of the other columns (the “evidence”).

---

## [Shopping.py](shopping.py)

The `main` function loads data from a CSV spreadsheet by calling the `load_data` function and splits the data into a training and testing set. The `train_model` function is then called to train a machine learning model on the training data. Then, the model is used to make predictions on the testing data set. Finally, the `evaluate` function determines the sensitivity and specificity of the model, before the results are ultimately printed to the terminal.

---

## Acknowledgements

Data set provided by [Sakar, C.O., Polat, S.O., Katircioglu, M. et al. Neural Comput & Applic (2018)](https://link.springer.com/article/10.1007/s00521-018-3523-0).

the `main` function was implemented by the CS50AI staff.
