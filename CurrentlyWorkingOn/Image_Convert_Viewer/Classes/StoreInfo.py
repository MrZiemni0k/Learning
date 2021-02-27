import os

class StoreInfo():
    '''
    Class to get and store info about files in directories based on dictionary.
    Dictionary should have form '.type':[int,int,int]
    ........

    Methods
    ----------
    count_imgs()
        Count images, its sizes and avg.
    '''
       
    def __init__(self,_dictionary,_path=os.getcwd()):
        '''
        Parameters
        ------------
        _dictionary(dict):
            Dictionary with form '.type':[int,int,int] 
            Where [0] = Amount, [1] = Total size in MB (:.3f), [2] = Avarage size in MB (:.3f)
        _path(str):
            Path with images to count.
        '''
        self._dictionary = _dictionary
        self._path = _path

    def count_imgs(self):
        '''
        Count images by keys in dictionary and path to directory.
        It counts Amount ,Total Size(MB)(:.3f) and AVG Size(MB)(:.3f). 
        '''

        if len(self._dictionary):
            dictkeylist = self._dictionary.keys()   #Get Keys from Dictionary

            #For everyfile in path
            for imfile in os.listdir(self._path):
                imfile = imfile.lower()
                _location, _extension = os.path.splitext(imfile)    #Grab extension

                #Count Amount and Total Size(MB)
                if _extension in dictkeylist:
                    self._dictionary[_extension][0] += 1
                    imgsize = os.path.getsize(self._path+'/'+imfile)/1024/1024
                    self._dictionary[_extension][1] += imgsize

            #Count AVG(MB)
            for _extension in dictkeylist:
                if self._dictionary[_extension][0] != 0:
                    avgsize = self._dictionary[_extension][1]/self._dictionary[_extension][0] 
                    self._dictionary[_extension][2] = avgsize

            #Round() was not consistent - Change values into strings .3f
            try:
                for _extension in dictkeylist:
                    self._dictionary[_extension][1] = f"{self._dictionary[_extension][1]:.3f}" 
                    self._dictionary[_extension][2] = f"{self._dictionary[_extension][2]:.3f}" 
            except ValueError as e:
                print(f'{e}')
        
        else:
            print("StoreInfo.count_imgs():")
            print("Dictionary is empty. Cannot count images")



    

