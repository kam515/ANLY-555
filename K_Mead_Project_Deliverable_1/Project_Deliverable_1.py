#* Project_Deliverable_1.py
#*
#* ANLY 555 2023 Spring
#* Project Deliverable 1
#*
#* Due on: 2/12/23
#* Author(s): Katie Mead
#*
#*
#* In accordance with the class policies and Georgetown's
#* Honor Code, I certify that, with the exception of the
#* class resources and those items noted below, I have neither
#* given nor received any assistance on this project other than
#* the TAs, professor, textbook and teammates.
#*

# ------------------------------------------------------------------------------------------------------------------------------------------------------#
# DataSet Class and subclasses
# ------------------------------------------------------------------------------------------------------------------------------------------------------#

class DataSet:
    """DataSet class for defining the type of dataset to be used on subclasses."""
    def __init__(self, filename):
        """Initializes the DataSet class."""
        print("DataSet.__init__() invoked")
    def __readFromCSV(self):
        """Reads the dataset from a CSV file."""
        print("DataSet.__readFromCSV() invoked")
    def __load(self):
        """Loads the dataset into memory."""
        print("DataSet.__load() invoked")
    def clean(self):
        """Cleans the dataset."""
        print("DataSet.clean() invoked")
    def explore(self):
        """Explores the dataset."""
        print("DataSet.explore() invoked")

class QuantDataSet(DataSet):
    """QuantDataSet for reading, loading, cleaning, and exploring quantitative datasets."""
    def __init__(self, filename):
        """Initializes the QuantDataSet class, but inherits from the DataSet class."""
        super().__init__(filename)
        print("QuantDataSet.__init__() invoked")
    def __readFromCSV(self):
        """Reads the QuantDataSet from a CSV file."""
        print("QuantDataSet.__readFromCSV() invoked")
    def __load(self):
        """Loads the QuantDataSet into memory."""
        print("QuantDataSet.__load() invoked")
    def clean(self):
        """Cleans the QuantDataSet."""
        print("QuantDataSet.clean() invoked")
    def explore(self):
        """Explores the QuantDataSet."""
        print("QuantDataSet.explore() invoked")

class QualDataSet(DataSet):
    """QualDataSet for reading, loading, cleaning, and exploring qualitative datasets."""
    def __init__(self, filename):
        """Initializes the QualDataSet class, but inherits from the DataSet class."""
        super().__init__(filename)
        print("QualDataSet.__init__() invoked")
    def __readFromCSV(self):
        """Reads the QualDataSet from a CSV file."""
        print("QualDataSet.__readFromCSV() invoked")
    def __load(self):
        """Loads the QualDataSet into memory."""
        print("QualDataSet.__load() invoked")
    def clean(self):
        """Cleans the QualDataSet."""
        print("QualDataSet.clean() invoked")
    def explore(self):
        """Explores the QualDataSet."""
        print("QualDataSet.explore() invoked")

class TextDataSet(DataSet):
    """TextDataSet for reading, loading, cleaning, and exploring text datasets."""
    def __init__(self, filename):
        """Initializes the TextDataSet class, but inherits from the DataSet class."""
        super().__init__(filename)
        print("TextDataSet.__init__() invoked")
    def __readFromCSV(self):
        """Reads the TextDataSet from a CSV file."""
        print("TextDataSet.__readFromCSV() invoked")
    def __load(self):
        """Loads the TextDataSet into memory."""
        print("TextDataSet.__load() invoked")
    def clean(self):
        """Cleans the TextDataSet."""
        print("TextDataSet.clean() invoked")
    def explore(self):
        """Explores the TextDataSet."""
        print("TextDataSet.explore() invoked")

class TimeSeriesDataSet(DataSet):
    """TimeSeriesDataSet for reading, loading, cleaning, and exploring time series datasets."""
    def __init__(self, filename, timeDelta):
        """Initializes the TimeSeriesDataSet class, but inherits from the DataSet class."""
        super().__init__(filename)
        print("TimeSeriesDataSet.__init__() invoked")
    def __readFromCSV(self):
        """Reads the TimeSeriesDataSet from a CSV file."""
        print("TimeSeriesDataSet.__readFromCSV() invoked")
    def __load(self):
        """Loads the TimeSeriesDataSet into memory."""
        print("TimeSeriesDataSet.__load() invoked")
    def clean(self):
        """Cleans the TimeSeriesDataSet."""
        print("TimeSeriesDataSet.clean() invoked")
    def explore(self):
        """Explores the TimeSeriesDataSet."""
        print("TimeSeriesDataSet.explore() invoked")

# ------------------------------------------------------------------------------------------------------------------------------------------------------#
# ClassifierAlgorithm Class and subclasses
# ------------------------------------------------------------------------------------------------------------------------------------------------------#

class ClassifierAlgorithm:
    """ClassifierAlgorithm class for defining the type of classifier algorithm to be used on subclasses."""
    def __init__(self, response):
        """Initializes the ClassifierAlgorithm class."""
        print("ClassifierAlgorithm.__init__() invoked")
    def train(self, data):
        """Trains the ClassifierAlgorithm class."""
        print("ClassifierAlgorithm.train() invoked")
    def test(self, data):
        """Tests the ClassifierAlgorithm class."""
        print("ClassifierAlgorithm.test() invoked")

class simpleKNNClassifier(ClassifierAlgorithm):
    """simpleKNNClassifier class for k-nearest neighbor classification using a simple data structure."""
    def __init__(self, response):
        """Initializes the simpleKNNClassifier class, but inherits from the Classifier Algorithm class."""
        super().__init__(response)
        print("simpleKNNClassifier.__init__() invoked")
    def train(self, data):
        """Trains the simpleKNNClassifier class."""
        print("simpleKNNClassifier.train() invoked")
    def test(self, data):
        """Tests the simpleKNNClassifier class."""
        print("simpleKNNClassifier.test() invoked")

class kdTreeKNNClassifier(ClassifierAlgorithm):
    """kdTreeKNNClassifier class for k-nearest neighbor classification using a kd-tree data structure."""
    def __init__(self, response):
        """Initializes the kdTreeKNNClassifier class, but inherits from the Classifier Algorithm class."""
        super().__init__(response)
        print("kdTreeKNNClassifier.__init__() invoked")
    def train(self, data):
        """Trains the kdTreeKNNClassifier class."""
        print("kdTreeKNNClassifier.train() invoked")
    def test(self, data):
        """Tests the kdTreeKNNClassifier class."""
        print("kdTreeKNNClassifier.test() invoked")

# ------------------------------------------------------------------------------------------------------------------------------------------------------#
# Experiment Class
# ------------------------------------------------------------------------------------------------------------------------------------------------------#


class Experiment:
    """Experiment class for running cross-validation, scoring, and confusion matrices on datasets."""
    def runCrossVal(self, k):
        """Runs k-fold cross-validation on the dataset."""
        print("Experiment.runCrossVal() invoked")
    def score(self):
        """Scores the results of the experiment."""
        print("Experiment.score() invoked")
    def __confusionMatrix(self):
        """Generates a confusion matrix for the experiment."""
        print("Experiment.__confusionMatrix() invoked")
