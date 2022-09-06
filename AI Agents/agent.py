
from agentStrategy import AgentStrategy
import pandas as pd

class Agent:
    def __init__(self, model_df, initial_strategy: AgentStrategy, concession_strategy: AgentStrategy):
        self.__setName(model_df.model_type[0])
        self.__setModel(model_df.model[0])
        self.__setModelStrategy(AgentStrategy(model_df.accuracy[0], model_df.f1score[0], model_df.mapk[0]))
        self.initial_strategy = initial_strategy
        self.concession_strategy = concession_strategy

########################################################################################################################

    # region Getters & Setters
    
    def __getName(self):
        return self.__name
    def __getModel(self):
        return self.__model
    def __getModelStrategy(self):
        return self.__model_strategy
    def __getInitialStrategy(self):
        return self.__initial_strategy
    def __getConcessionStrategy(self):
        return self.__concession_strategy
    def __getFlagInitialStrategy(self):
        return self.__flag_initial_strategy
    def __getFlagConcessionStrategy(self):
        return self.__flag_concession_strategy
    
    def __setName(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.__name = name
    def __setModel(self, model: any):
        self.__model = model
    def __setModelStrategy(self, strategy: AgentStrategy):
        if not isinstance(strategy, AgentStrategy):
            raise TypeError("strategy must be a Strategy")
        self.__model_strategy = strategy
        
    def __setInitialStrategy(self, strategy: AgentStrategy):
        if not isinstance(strategy, AgentStrategy):
            raise TypeError("strategy must be a Strategy")
        self.__initial_strategy = strategy
        
        # if the initial strategy is less than the model strategy, set the flag to true otherwise false
        if self.__initial_strategy <= self.__model_strategy:
            self.__flag_initial_strategy = True
        else:
            self.__flag_initial_strategy = False
         
    def __setConcessionStrategy(self, strategy: AgentStrategy):
        if not isinstance(strategy, AgentStrategy):
            raise TypeError("strategy must be a Strategy")
        self.__concession_strategy = strategy
        
        # if the initial strategy flag is true set the concession strategy flag to false
        if self.__flag_initial_strategy == True:
            self.__flag_concession_strategy = False
            return
        # if the concession strategy is less than the model strategy, set the flag to true otherwise false
        if self.__concession_strategy <= self.__model_strategy:
            self.__flag_concession_strategy = True
        else:
            self.__flag_concession_strategy = False


    name = property(__getName)
    model = property(__getModel)
    model_strategy = property(__getModelStrategy)
    initial_strategy = property(__getInitialStrategy, __setInitialStrategy)
    concession_strategy = property(__getConcessionStrategy, __setConcessionStrategy)
    # flags are initialized automatically depending on the initial strategy and concession strategy
    flag_initial_strategy = property(__getFlagInitialStrategy)
    flag_concession_strategy = property(__getFlagConcessionStrategy)
    
    # endregion Getters & Setters

########################################################################################################################

    # region Magic Methods

    def __str__(self):
        st = f"\nAgent {self.name}:"
        st += f"\n\tModel: {self.model}"                                          # Model type
        st += "\n\tModel Strategy: " + str(self.model_strategy).replace('\n','\n\t')
        st += "\n\tInitial Strategy: " + str(self.initial_strategy).replace('\n','\n\t')
        st += "\n\tConcession Strategy: " + str(self.concession_strategy).replace('\n','\n\t')
        st += f"\n\tFlag Initial Strategy: {self.flag_initial_strategy}"
        st += f"\n\tFlag Concession Strategy: {self.flag_concession_strategy}"
        return st
    
    # endregion Magic Methods
    
########################################################################################################################


####################    Testing the Agent class    ####################


# data = [['SmithModel', 'Smith', 0.7, 0.9, 0.4]]
# column_name = ['model','model_type', 'mapk', 'f1score', 'accuracy'] 
# df = pd.DataFrame(data, columns=column_name)

# agent = Agent(df, AgentStrategy(0.3, 0.5, 0.5), AgentStrategy(0.3, 0.5, 0.5))

# print(agent)