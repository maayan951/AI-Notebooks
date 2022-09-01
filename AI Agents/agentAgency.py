

from agent import Agent, AgentStrategy, pd

class AgentAgency:
    def __init__(self, agents: list[Agent], majority_needed: float|int):
        self.agents = agents
        self.majority_needed = majority_needed  # percentage of agents needed to vote for a decision
        self.__resetDealCounts()


########################################################################################################################
   
    # region Getters & Setters
    
    def __getAgents(self):
        return self.__agents
    def __getMajorityNeeded(self):
        return self.__majority_needed
    def __getInitialDealCount(self):
        return self.__initial_dealCount
    def __getConcessionDealCount(self):
        return self.__concession_dealCount
    def __getDeclinedDealCount(self):
        return self.__declined_dealCount
    
    def __setAgents(self, agents: list[Agent]):
        if not isinstance(agents, list):
            raise TypeError("agents must be a list")
        for agent in agents:
            if not isinstance(agent, Agent):
                raise TypeError("agents must be a list of Agent objects")
        self.__agents = agents
    def __setMajorityNeeded(self, majority_needed: float|int):
        if not isinstance(majority_needed, (float, int)):
            raise TypeError("majority_needed must be a float or int")
        if isinstance(majority_needed, int):
            majority_needed = float(majority_needed)
        if majority_needed < 0 or majority_needed > 100:
            raise ValueError("majority_needed must be between 0 and 100")
        if majority_needed > 1:
            majority_needed /= 100
        self.__majority_needed = majority_needed
    def __resetDealCounts(self):
        self.__initial_dealCount = 0              # flag_initial_strategy = True , flag_concession_strategy = False
        self.__concession_dealCount = 0           # flag_initial_strategy = False , flag_concession_strategy = True
        self.__declined_dealCount = 0             # flag_initial_strategy = False , flag_concession_strategy = False
    
    agents = property(__getAgents, __setAgents)
    majority_needed = property(__getMajorityNeeded, __setMajorityNeeded)
    initial_dealCount = property(__getInitialDealCount)
    concession_dealCount = property(__getConcessionDealCount)
    declined_dealCount = property(__getDeclinedDealCount)
    
    # endregion Getters & Setters

########################################################################################################################

    # region Agents List Methods
    
    def addAgent(self, agent: Agent):
        if not isinstance(agent, Agent):
            raise TypeError("agent must be a Agent object")
        if agent in self.agents:
            print(f"Agent '{agent.name}' already exists")
            return
        self.agents.append(agent)
        print(f"Agent '{agent.name}' added")
        
    def removeAgent(self, agent: Agent):
        if not isinstance(agent, Agent):
            raise TypeError("agent must be a Agent object")
        if agent not in self.agents:
            print(f"Agent '{agent.name}' not found")
            return
        self.agents.remove(agent)
        print(f"Agent '{agent.name}' removed")
    
    def removeAgentByName(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        for agent in self.agents:
            if agent.name == name:
                self.agents.remove(agent)
                print(f"Agent '{name}' removed")
                return
        print(f"Agent with name '{name}' not found")
    
    def popAgent(self, index: int):
        if not isinstance(index, int):
            raise TypeError("index must be an int")
        if index < 0 or index >= len(self.agents):
            raise IndexError("index out of range")
        return self.agents.pop(index)
    
    def popAgentByName(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        for agent in self.agents:
            if agent.name == name:
                self.agents.remove(agent)
                print(f"Agent '{name}' removed")
                return agent
        print(f"Agent with name '{name}' not found")
        return False
        
    # endregion Agents List Methods
        
########################################################################################################################

    def CheckDeal(self):
        self.__resetDealCounts()
        
        initial_strategy_list = list()
        concession_strategy_list = list()
        declined_strategy_list = list()
        
        for agent in self.agents:
            if agent.flag_initial_strategy == True:
                self.__initial_dealCount += 1
                initial_strategy_list.append(agent)
            elif agent.flag_concession_strategy == True:
                self.__concession_dealCount += 1
                concession_strategy_list.append(agent)
            else:
                self.__declined_dealCount += 1
                declined_strategy_list.append(agent)
        
        total_voted_approved = self.initial_dealCount + self.concession_dealCount
        
        if total_voted_approved >= self.majority_needed * len(self.agents):
            print(f"\nAgents accepted initial strategy: {initial_strategy_list}")
            print(f"Agents accepted concession strategy: {concession_strategy_list}")
            print(f"Agents declined both strategies: {declined_strategy_list}")
            print(f"Total accepted agents: {total_voted_approved}")
            print(f"Majority needed: {self.majority_needed * len(self.agents) :.2f}")
            print(f"Deal approved!\n")
            return initial_strategy_list + concession_strategy_list
            
        print("Deal declined! \nThere is a conflict between the agents, please resolve it manually")
        return False

########################################################################################################################

    # region Magic Methods
    
    def __str__(self):
        st = f"Majorty needed: {self.majority_needed * 100 :.2f}%\n"
        st+= f"Agents:"
        for agent in self.agents:
            st += str(agent).replace('\n','\n\t')
        return st
    
    # endregion Magic Methods

########################################################################################################################


####################    Testing the Agents class    ####################


# Creating agents with different strategies(those are loaded from the MongoDB)
column_name = ['model', 'accuracy', 'f1score', 'mapk'] 

SmithModel_data = [['SmithModel', 0.4, 0.9, 0.7]]
SmithModel_df = pd.DataFrame(SmithModel_data, columns=column_name)

DanModel_data = [['DanModel', 0.7, 0.9, 0.7]]
DanModel_df = pd.DataFrame(DanModel_data, columns=column_name)

JohnModel_data = [['JohnModel', 0.8, 0.9, 0.7]]
JohnModel_df = pd.DataFrame(JohnModel_data, columns=column_name)


# Adding all the agents to a list and creating an Agents object
agentsList = []
agentsList.append(Agent("Smith", SmithModel_df, AgentStrategy(0.3, 0.5, 0.5), AgentStrategy(0.3, 0.5, 0.5)))
agentsList.append(Agent("Dan", DanModel_df, AgentStrategy(0.8, 0.5, 0.8), AgentStrategy(0.3, 0.5, 0.7)))

cia = AgentAgency(agentsList, 0.7)
cia.addAgent(Agent("John", JohnModel_df, AgentStrategy(0.3, 0.5, 0.5), AgentStrategy(0.3, 0.5, 0.5)))

# Printing the agents
print(cia)

# Calling the CheckDeal method
print(cia.CheckDeal())
