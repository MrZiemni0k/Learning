class AppDictionary():
    '''
    Class to create and modify dictionaries in APP efficiently.
    ........

    Methods
    ----------
    create_dic()
        Creates a dictionary based on list and its values.
    '''
    def __init__(self,typelist,values):
        '''
        Parameters:
        ------------
        typelist(str/list)
            Preferable list of dictionary Key names.
        values(str/list)
            Preferable list of dictionary Keys' values.
        '''
        self.typelist = typelist
        self.listvalues = values
    
    def create_dic(self):
        '''
        create_dic()
            Creates a dictionary based on list and its values.
        '''
        
        self.typedic = {}
        
        for _type in self.typelist:
            self.typedic[_type] = self.values
