class AppDictionary():
    '''
    Class to create and modify dictionaries in APP efficiently.
    ........

    Methods
    ----------
    add_to_dict()
        Add keys and its values to dictionary.
    '''
    def __init__(self,typelist,values,typedic={}):
        '''
        Parameters:
        ------------
        typelist(str/list)
            Preferable list of dictionary Key names.
        values(str/list)
            Preferable list of dictionary Keys' values.
        typedic(dict)
            Dictionary to work with.
        '''
        self.typelist = typelist
        self.values = values
        self.typedic = typedic
    
    def add_to_dict(self):
        '''
        Add keys and its values to dictionary.
        '''
        
        for _type in self.typelist:
            self.typedic[_type] = self.values
