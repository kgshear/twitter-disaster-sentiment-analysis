import string

from DataCleaning import getDataFrame, splitFeatures, dropFeature, clean_text

if __name__ == '__main__':

    testdata = getDataFrame("../data/test.csv")
    traindata = getDataFrame("../data/train.csv")

    x_train, y_train = splitFeatures(traindata, "target")

    x_train = dropFeature(x_train, "id")
    x_train = dropFeature(x_train, "location")
    testdata = dropFeature(testdata, "id")
    testdata = dropFeature(testdata, "location")

    x_train = x_train.dropna()
    testdata = testdata.dropna()

    x_train.loc[:,'text'] = x_train.loc[:,'text'].apply(clean_text).loc[:]
    testdata.loc[:,'text'] = testdata.loc[:,'text'].apply(clean_text).loc[:]

    print(x_train.head())




