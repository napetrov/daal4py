import daal4py as d4p
import numpy as np

# let's try to use pandas' fast csv reader
try:
    import pandas
    read_csv = lambda f, c: pandas.read_csv(f, usecols=c, delimiter=',').values
except:
    # fall back to numpy loadtxt
    read_csv = lambda f, c: np.loadtxt(f, usecols=c, delimiter=',')

nFeatures = 20
nClasses = 2


def main():
    # read training data from file
    trainfile = "./data/batch/binary_cls_train.csv"
    train_data = read_csv(trainfile, range(nFeatures))
    train_dep_data = read_csv(trainfile, range(nFeatures, nFeatures + 1))
    nVectors = train_data.shape[0]
    train_dep_data.shape = (nVectors, 1)  # must be a 2d array

    # set parameters and train
    train_alg = d4p.logistic_regression_training(nClasses=nClasses)
    train_result = train_alg.compute(train_data, train_dep_data)

    # read testing data from file
    testfile = "./data/batch/binary_cls_test.csv"
    predict_data = read_csv(testfile, range(nFeatures))

    # set parameters and compute predictions
    predict_alg = d4p.logistic_regression_prediction(nClasses=nClasses)
    predict_result = predict_alg.compute(predict_data, train_result.model)

    # check that results are present
    assert predict_result.prediction.shape == (predict_data.shape[0], train_dep_data.shape[1])


if __name__ == "__main__":
    main()
    print('All looks good!')
