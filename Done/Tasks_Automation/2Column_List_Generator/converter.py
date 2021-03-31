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
        output_str = 'KOLUMNA'+ ' '*(column_length-7) + '| OPIS\n' + '‾'*72+'\n'
        
        for x in first_column:
            dots = column_length - len(x)
            output_str += x + dots*"." + "⭕"+"˯"*(70-len(x)-(column_length-len(x))-1)+'\n'
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
    
    def create_dbtable(self,_list):
        
        separator = '/'*50+'\n'+f'//*{_list[-1]}*\n'+'/'*50+'\n'
        make_str = (f'Table {_list[-1]} [\n'
                     'headercolor: #14274e,\n'
                     'note:\n'
                     '\'\n'
                     '\n'
                     '\']{\n')
        return separator+make_str
                     
    def create_dbcolumns(self,_list,column_list):
        print(_list)
        count = 0
        column_str = ''
        for x in _list:
            if count != len(_list)-1:
                if count == 0:
                    column_str += f'    "🔑{x}" TO_DO [\nnote:\n\'\n\']\n' 
                else:
                    column_str += (f'    "{x}" TO_DO [\n'
                                    'note:\n'
                                    '\'⚿  - Identyfikator\n'
                                    '\n'
                                   f' 1️⃣ ---> ♾️ {_list[-1]}\n'
                                    '(🔑ID_)\n'
                                    '\']\n')
            count += 1
        column_str += ('    "📝INNE'+'⠀'*50+'" list [\n'
                       'note:\n'
                       '\'')
        
        inne_str = ''       
        for x in column_list:
            inne_str += f'{x}\n'            

        column_str += self.make_list1(inne_str) + '\']\n' 
        
        column_str += ('    "📝INNE2'+'⠀'*49+'" list [\n'
                       'note:\n'
                       '\'\n'
                       '\n'
                       '\']\n')
        return column_str 
            
        
    def make_table_list(self,text):
        
        filtered_text = text[text.find("SELECT"):text.find("FROM")]
        filtered_text = filtered_text[filtered_text.find("["):]
        columns = filtered_text.split(",")
        filtered_columns = []
        for x in columns:
            filtered_c = x[1:x.index("]")]
            filtered_columns.append(filtered_c)
        count = 0
        key_list = []
        for x in filtered_columns:
            if x[0:3] == 'ID_' or x[0:4] == 'SYM_' or x[0:4] == 'KOD_' or x[0:4] == 'VAT_':
                key_list.append(filtered_columns.pop(count))
            count += 1
            
        filtered_text = text[text.find("[dbo]."):]
        filtered_text = filtered_text[:filtered_text.find("]\n")]
        key_list.append(filtered_text[7:])
        print(key_list)
        return self.create_dbtable(key_list) + self.create_dbcolumns(key_list,filtered_columns) + '}'
        
    
