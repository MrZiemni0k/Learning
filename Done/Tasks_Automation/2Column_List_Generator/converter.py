class MakeList():
    
    def __init__(self):
        pass
        
    def make_list1(self,text):
        
        
        first_column = text.splitlines()
        if first_column[0][0:8] == 'KOLUMNA ':
            del first_column[0]
        if first_column[0][0] == '‾':
            del first_column[0]
        column_length = len(max(first_column,key=len))
        output_str = 'KOLUMNA'+ ' '*(column_length-7) + '| OPIS\n' + '‾'*50+'\n'
        
        for x in first_column:
            dots = column_length - len(x)
            output_str += x + dots*"." + "⭕\n"
        return output_str
    
    def unmake_list1(self,text):
        
        first_column = text.splitlines()
        if first_column[0][0:8] == 'KOLUMNA ':
            del first_column[0]
        if first_column[0][0] == '‾':
            del first_column[0]
        output_str = ''
        for x in first_column:
            x =  x.partition('.')[0]
            output_str += x + "\n"
        return output_str
        
