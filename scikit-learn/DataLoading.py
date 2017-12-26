import numpy as np
import urllib.request as ur

def load_data():
    # url of dataset
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"

    # download the file
    raw_data = ur.urlopen(url)

    # load the CSV file as a numpy matrix
    dataset = np.loadtxt(raw_data, delimiter=",")

    # separate data
    X = dataset[:,0:8]
    y = dataset[:,8]
    
    return (X,y)

if __name__ == "__main__":
    (X,y) = load_data()
    print(np.shape(X))
    print(y)