import csv
import sys

# For splitting the data set into a training and testing sets
from sklearn.model_selection import train_test_split

# K-nearest neighbor algorithm
from sklearn.neighbors import KNeighborsClassifier

# to convert a month abbreviation into an int
from time import strptime

TEST_SIZE = 0.4

# Index of columns that should be stored as a float
FLOATS = [1, 3, 5, 6, 7, 8, 9]
# Index of columns that should be stored as an int
INTS = [0, 2, 4, 11, 12, 13, 14]
# Column indexes
MONTHS_COLUMN = 10
VISTORTYPE_COLUMN = 15
WEEKEND_COLUMN = 16


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Read data in from file
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)

        # 1 means the customer made a purchase otherwise not
        labels = []
        # holds lists containing all of the paramters
        evidence = []
        for row in reader:
            # Add the numeric label
            if row[-1] == "TRUE":
                labels.append(1)
            else:
                labels.append(0)

            # Add numeric evidence
            evidence.append(get_numeric_evidence(row[:-1]))

        return (evidence, labels)


def get_numeric_evidence(evidence):
    """
    returns given evidence formatted numerically
    """
    numeric_evidence = []
    for i, value in enumerate(evidence):
        if i in FLOATS:
            numeric_evidence.append(float(value))

        elif i in INTS:
            numeric_evidence.append(int(value))

        elif i == MONTHS_COLUMN:
            # strptime doesn't have June, but Jun instead
            value = "Jun" if value == "June" else value

            month_index = strptime(value, "%b").tm_mon
            numeric_evidence.append(month_index)

        elif i == VISTORTYPE_COLUMN:
            numeric_evidence.append(1 if value == "Returning_Visitor" else 0)

        elif i == WEEKEND_COLUMN:
            numeric_evidence.append(1 if value == "TRUE" else 0)

    return numeric_evidence


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)

    model.fit(evidence, labels)

    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificty).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positive_increase = 1 / labels.count(1)
    negative_increase = 1 / labels.count(0)

    sensitivity = 0
    specificity = 0
    for label, prediction in zip(labels, predictions):
        if label == prediction:
            if label == 1:
                sensitivity += positive_increase
            else:
                specificity += negative_increase

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
