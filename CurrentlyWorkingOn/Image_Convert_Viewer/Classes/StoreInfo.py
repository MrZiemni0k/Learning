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
            Where [0] = Amount, [1] = Total size in MB (Round/2), [2] = Avarage size in KB (Round/2)
        _path(str):
            Path with images to count.
        '''
        self._dictionary = _dictionary
        self._path = _path

    def count_imgs(self):
        
        try:
            dictkeylist = self._dictionary.keys()

            for imfile in os.listdir(self._path):
                imfile = imfile.lower()
                _location, _extension = os.path.splitext(imfile)

                if _extension in dictkeylist:
                    self._dictionary[_extension][0] += 1
                    imgsize = os.path.getsize(self._path+'/'+imfile)/1024/1024
                    self._dictionary[_extension][1] += round(imgsize,2)
            
            for _type in dictkeylist:
                if self._dictionary[_type][0] != 0:
                    avgsize = self._dictionary[_type][1]/self._dictionary[_type][0]*1024
                    self._dictionary[_type][2] = round(avgsize,2)    
        
        except:
            print("Cannot count images with empty dictionary -> No keys forwarded.")
            


    

