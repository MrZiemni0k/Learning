#https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring/#34445090
def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)
        
with open("./Input/Letters/starting_letter.txt") as file:
    l_templ = file.read()
    start_index = [(i, l_templ[i:i+6]) for i in findall('[name]', l_templ)]
    print(start_index)

with open ("./Input/Names/invited_names.txt") as file_name:
    name_list = file_name.read().split("\n")

for name in name_list:
    with open(f"./Output/ReadyToSend/Letter_{name}.txt", mode='w') as file:
        for change in start_index:
            temp_templ = l_templ
            temp_templ = (temp_templ[:change[0]] + 
                          name + 
                          temp_templ[change[0]+6:])
            file.write(temp_templ)
        
        



#TODO: Create  a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp