import pandas as pd

data = pd.read_csv('50_states.csv')
data_list = data.values.tolist()

class AnswerList():
    
    def __init__(self):
        
        self._list = data_list
        self._states = [x[0].lower() for x in data_list]

    def check_list(self,answer):
        return answer.lower() in self._states
    
    def give_cords(self,answer):
        index = self._states.index(answer.lower())
        x_cord = self._list[index][1]
        y_cord = self._list[index][2]
        del self._states[index]
        del self._list[index]
        return tuple([x_cord,y_cord])
            
    def generate_csv(self):
        pd.DataFrame(self._states).to_csv("Not Guessed States.csv")