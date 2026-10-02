import numpy as np
import matplotlib.pyplot as plt

from decision_tree import DecisionTree


def accuracy_score(Y_true, Y_predict):
    # TODO: return accuracy of the data.
    return


def evaluate_performance():
    '''
    Evaluate the performance of decision trees and logistic regression,
    average over 1,000 trials of 10-fold cross validation

    Return:
      a matrix giving the performance that will contain the following entries:
      stats[0,0] = mean accuracy of decision tree
      stats[0,1] = std deviation of decision tree accuracy
      stats[1,0] = mean accuracy of logistic regression
      stats[1,1] = std deviation of logistic regression accuracy

    ** Note that your implementation must follow this API**
    '''

    # Load Data
    filename = 'data/SPECTF.dat'
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    y = np.array([data[:, 0]]).T
    n, d = X.shape

    for trial in range(1000):
        # TODO: shuffle for each of the trials.
        # the following code is for reference only.
        idx = np.arange(n)
        np.random.seed(13)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # TODO: write your own code to split data (for cross validation)
        # the code here is for your reference.
        Xtrain = X[1:101, :]  # train on first 100 instances
        Xtest = X[101:, :]
        ytrain = y[1:101, :]  # test on remaining instances
        ytest = y[101:, :]

        # train the decision tree
        classifier = DecisionTree(100)
        classifier.fit(Xtrain, ytrain)

        # output predictions on the remaining data
        y_pred = classifier.predict(Xtest)
        accuracy = accuracy_score(ytest, y_pred)
        break

    # compute the training accuracy of the model
    meanDecisionTreeAccuracy = np.mean(all_accuracies)

    # TODO: update these statistics based on the results of your experiment
    stddevDecisionTreeAccuracy = 0
    meanLogisticRegressionAccuracy = 0
    stddevLogisticRegressionAccuracy = 0
    meanRandomForestAccuracy = 0
    stddevRandomForestAccuracy = 0

    # make certain that the return value matches the API specification
    stats = np.zeros((2, 2))
    stats[0, 0] = meanDecisionTreeAccuracy
    stats[0, 1] = stddevDecisionTreeAccuracy
    stats[1, 0] = meanRandomForestAccuracy
    stats[1, 1] = stddevRandomForestAccuracy
    stats[2, 0] = meanLogisticRegressionAccuracy
    stats[2, 1] = stddevLogisticRegressionAccuracy
    return stats


# Do not modify from HERE...
if __name__ == "__main__":
    stats = evaluate_performance()
    print "Decision Tree Accuracy = ", stats[0, 0], " (", stats[0, 1], ")"
    print "Random Forest Tree Accuracy = ", stats[1, 0], " (", stats[1, 1], ")"
    print "Logistic Reg. Accuracy = ", stats[2, 0], " (", stats[2, 1], ")"
# ...to HERE.
