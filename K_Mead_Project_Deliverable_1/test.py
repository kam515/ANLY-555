#=====================================================================
# Testing script for Deliverable 1: Source Code Framework
#=====================================================================

#=====================================================================
# Testing DataSet Class 
# (Not meant to be called, but will show instantiation, attributes,
# and member methods)
#=====================================================================
from Project_Deliverable_1 import (DataSet, QuantDataSet, QualDataSet,
                                        TextDataSet, TimeSeriesDataSet)

def test_DataSet():
    filename = "testing_the_data_set_class"
    print("DataSet Instantiation....")
    dataset_for_testing = DataSet(filename)
    print("===========================================================")
    print("Check member methods...")
    print("===========================================================")
    #print("Now call DataSet.__readFromCSV()...")
    #dataset_for_testing.__readFromCSV()
    #print("===========================================================")
    #print("Now call DataSet.__load()...")
    #dataset_for_testing.__load()
    #print("===========================================================")
    print("Now call DataSet.clean()...")
    dataset_for_testing.clean()
    print("===========================================================")
    print("Now call DataSet.explore()...")
    dataset_for_testing.explore()
    print("\n\n")


def test_QuantDataSet():
    filename = "testing_the_quant_data_set_class"
    print("QuantDataSet Instantiation....")
    dataset_for_testing = QuantDataSet(filename)
    print("===========================================================")
    print("Check member methods...")
    print("===========================================================")
    #print("Now call QuantDataSet.__readFromCSV()...")
    #dataset_for_testing.__readFromCSV()
    #print("===========================================================")
    #print("Now call QuantDataSet.__load()...")
    #dataset_for_testing.__load()
    #print("===========================================================")
    print("Now call QuantDataSet.clean()...")
    dataset_for_testing.clean()
    print("===========================================================")
    print("Now call QuantDataSet.explore()...")
    dataset_for_testing.explore()
    print("\n\n")

def test_QualDataSet():
    filename = "testing_the_qual_data_set_class"
    print("QualDataSet Instantiation....")
    dataset_for_testing = QualDataSet(filename)
    print("===========================================================")
    print("Check member methods...")
    print("===========================================================")
    #print("Now call QualDataSet.__readFromCSV()...")
    #dataset_for_testing.__readFromCSV()
    #print("===========================================================")
    #print("Now call QualDataSet.__load()...")
    #dataset_for_testing.__load()
    #print("===========================================================")
    print("Now call QualDataSet.clean()...")
    dataset_for_testing.clean()
    print("===========================================================")
    print("Now call QualDataSet.explore()...")
    dataset_for_testing.explore()
    print("\n\n")

def test_TextDataSet():
    filename = "testing_the_text_data_set_class"
    print("TextDataSet Instantiation....")
    dataset_for_testing = TextDataSet(filename)
    print("===========================================================")
    print("Check member methods...")
    print("===========================================================")
    #print("Now call TextDataSet.__readFromCSV()...")
    #dataset_for_testing.__readFromCSV()
    #print("===========================================================")
    #print("Now call TextDataSet.__load()...")
    #dataset_for_testing.__load()
    #print("===========================================================")
    print("Now call TextDataSet.clean()...")
    dataset_for_testing.clean()
    print("===========================================================")
    print("Now call TextDataSet.explore()...")
    dataset_for_testing.explore()
    print("\n\n")

def test_TimeSeriesDataSet():
    filename = "testing_the_time_series_data_set_class"
    print("TimeSeriesDataSet Instantiation....")
    dataset_for_testing = TimeSeriesDataSet(filename,"weekly")
    print("===========================================================")
    print("Check member methods...")
    print("===========================================================")
    #print("Now call TimeSeriesDataSet.__readFromCSV()...")
    #dataset_for_testing.__readFromCSV()
    #print("===========================================================")
    #print("Now call TimeSeriesDataSet.__load()...")
    #dataset_for_testing.__load()
    #print("===========================================================")
    print("Now call TimeSeriesDataSet.clean()...")
    dataset_for_testing.clean()
    print("===========================================================")
    print("Now call TimeSeriesDataSet.explore()...")
    dataset_for_testing.explore()
    print("\n\n")

#=====================================================================
# Testing Classifier Class 
# (Not meant to be called, but will show instantiation, attributes,
# and member methods)
#=====================================================================
from Project_Deliverable_1 import (ClassifierAlgorithm,
                                simpleKNNClassifier,kdTreeKNNClassifier)
                                        
def test_ClassifierAlgorithm():
    print("ClassifierAlgorithm Instantiation....")
    classifier = ClassifierAlgorithm("response")
    print("==============================================================")
    print("Check class member methods...\n")
    x = "data"
    print("==============================================================")
    print("ClassifierAlgorithm.train(data):")
    print(classifier.train(x))
    print("==============================================================")
    print("ClassifierAlgorithm.test(data):")
    print(classifier.test(x))
    print("===========================================================\n\n")

def test_simpleKNNClassifier():
    print("simpleKNNClassifier Instantiation....")
    classifier = simpleKNNClassifier("response")
    print("==============================================================")
    print("Check class member methods...\n")
    x = "data"
    print("==============================================================")
    print("simpleKNNClassifier.train(data):")
    print(classifier.train(x))
    print("==============================================================")
    print("simpleKNNClassifier.test(data):")
    print(classifier.test(x))
    print("===========================================================\n\n")

def test_kdTreeKNNClassifier():
    print("kdTreeKNNClassifier Instantiation....")
    classifier = kdTreeKNNClassifier("response")
    print("==============================================================")
    print("Check class member methods...\n")
    x = "data"
    print("==============================================================")
    print("kdTreeKNNClassifier.train(data):")
    print(classifier.train(x))
    print("==============================================================")
    print("kdTreeKNNClassifier.test(data):")
    print(classifier.test(x))
    print("===========================================================\n\n")

#=====================================================================
# Testing Classifier Class 
# (Not meant to be called, but will show instantiation, attributes,
# and member methods)
#=====================================================================
from Project_Deliverable_1 import Experiment

def test_Experiment():
    print("Experiment Instantiation....")
    experiment = Experiment()
    print("==============================================================")
    print("Check class member methods...\n")
    print("Experiment.runCrossVal(numFolds,statistic):")
    experiment.runCrossVal("data")
    print("==============================================================")
    print("Experiment.score():")
    experiment.score()
    print("===========================================================")
    #print("Experiment.__confusionMatrix():")
    #experiment.__confusionMatrix()
    #print("===========================================================\n\n")
    
    
def main():
    test_DataSet()
    test_QualDataSet()
    test_TextDataSet()
    test_TimeSeriesDataSet()
    test_ClassifierAlgorithm()
    test_simpleKNNClassifier()
    test_kdTreeKNNClassifier()
    test_Experiment()
    
if __name__=="__main__":
    main()