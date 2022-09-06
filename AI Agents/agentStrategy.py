

class AgentStrategy:
    def __init__(self, accuracy: float, f1score: float, mapk: float):
        self.accuracy = accuracy
        self.f1score = f1score
        self.mapk = mapk

########################################################################################################################

    # region Getters & Setters
    
    def __getAccuracy(self):
        return self.__accuracy
    def __getF1score(self):
        return self.__f1score
    def __getMapk(self):
        return self.__mapk
    
    def __setAccuracy(self, accuracy: float):
        if not isinstance(accuracy, float):
            raise TypeError("accuracy must be a float")
        self.__accuracy = accuracy
    def __setF1score(self, f1score: float):
        if not isinstance(f1score, float):
            raise TypeError("f1score must be a float")
        self.__f1score = f1score
    def __setMapk(self, mapk: float):
        if not isinstance(mapk, float):
            raise TypeError("mapk must be a float")
        self.__mapk = mapk
        
    accuracy = property(__getAccuracy, __setAccuracy)
    f1score = property(__getF1score, __setF1score)
    mapk = property(__getMapk, __setMapk)
    
    # endregion Getters & Setters

########################################################################################################################

    # region Magic Methods
    
    # these methods are used to compare the objects and can be configured in different ways (depending on the needs)
    
    # lt = less than (<)
    def __lt__(self, other):
        return self.accuracy < other.accuracy and self.f1score < other.f1score and self.mapk < other.mapk
    
    # gr = greater than (>)
    def __gt__(self, other):
        return self.accuracy > other.accuracy and self.f1score > other.f1score and self.mapk > other.mapk
    
    # le = less than or equal to (<=)
    def __le__(self, other):
        return self.accuracy <= other.accuracy and self.f1score <= other.f1score and self.mapk <= other.mapk
    
    # ge = greater than or equal to (>=)
    def __ge__(self, other):
        return self.accuracy >= other.accuracy and self.f1score >= other.f1score and self.mapk >= other.mapk
    
    # eq = equal to (==)
    def __eq__(self, other):
        return self.accuracy == other.accuracy and self.f1score == other.f1score and self.mapk == other.mapk
    
    # ne = not equal to (!=)
    def __ne__(self, other):
        return self.accuracy != other.accuracy or self.f1score != other.f1score or self.mapk != other.mapk
    
    # str = string representation
    def __str__(self):
        st = f'\n\tAccuracy: {self.accuracy:.3f} \n\tF1-score: {self.f1score:.3f} \n\tMAPK: \t  {self.mapk:.3f}'
        return st
    
    # endregion Magic Methods

########################################################################################################################


####################    Testing the AgentStrategy class    ####################


# strat = AgentStrategy(0.5, 0.5, 0.5)
# print(strat)
