# Titanic: Machine Learning from Disaster

This repository contains code for the Titanic Kaggle competition, where the goal is to predict survival on the Titanic.

## Dataset Description

The dataset consists of two CSV files:
- `train.csv`: Contains training data with features and target labels.
- `test.csv`: Contains test data with features (without target labels).

### Features

- **PassengerId**: Unique identifier for each passenger.
- **Survived**: Target variable indicating survival (0 = No, 1 = Yes).
- **Pclass**: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd).
- **Name**: Passenger's name.
- **Sex**: Passenger's sex.
- **Age**: Passenger's age in years.
- **SibSp**: Number of siblings/spouses aboard the Titanic.
- **Parch**: Number of parents/children aboard the Titanic.
- **Ticket**: Ticket number.
- **Fare**: Passenger fare.
- **Cabin**: Cabin number.
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

## Approach

In this repository, we use a Random Forest Classifier to predict survival on the Titanic. Random Forest is an ensemble learning method that constructs a multitude of decision trees during training and outputs the mode of the classes (classification) of the individual trees.

## Instructions

1. Clone this repository:

```bash
git clone https://github.com/Agnidipto/titanic-kaggle
