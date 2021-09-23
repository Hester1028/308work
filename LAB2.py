# Transform the arr into [0, 0, 1, 2, 0, 2, 2, 1, 1, 0, 1]
def create_put_transform_arr(list1, puts):
    for word in list1:
        if len(list1) > 1:
            if list1[0] == "else" and list1[1] == "if":
                puts.append(2)
                return
        if word == "else":
            puts.append(1)
        if word == "if":
            puts.append(0)
    return

# Fifth grade
def get_if_elseif_else_num(puts):
    num=0
    flag=1
    for i in puts:
        if i == 2 and flag ==1 :
            num+=1
            flag=0
        else:
            flag=1
    return num

# Forth grade
def get_if_else_num(puts):
    num1=0
    for i in range(len(puts)):
        if puts[i] == 0 and i+1 < len(puts):
            if puts[i] == 0 and puts[i+1]==1:
                num1+=1
    return num1

# Third grade
def get_case_num(put,length):
    arr = [0 for i in range(length)]
    i = -1
    print("case num: ", end=" ")
    for num in put:
        if num == 1:
            i += 1
        if num == 0:
            arr[i] += 1

    for i in arr:
        print(i,end=" ")
    return

# Second grade
def get_switch_num(put):
    num=0
    for i in put:
        if i==1:
            num+=1
    return num

# get the switch case array  as [1, 0, 0, 0, 1, 0, 0]
def get_switchcase_arr(list1,put):
    for word in list1:
        if word == "switch":
            put.append(1)
        if word == "case":
            put.append(0)
    return

# First grade
def get_keyword_num():
    num = 0
    key_word = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'if', 'while', 'static',
                'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'int', 'long', 'register', 'return',
                'short', 'signed', 'sizeof', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile']
    while True:
        line = file.readlines()
        for word in line:
            word = word.replace(",", "").replace(".", "").replace("{", " ").replace("}", " ").replace(":", "").replace(";", "").\
                replace("?", "").replace("(", " ").replace(")", " ")
            list1 = word.split()
            for word in list1:
                if word in key_word:
                   num=num+1

            # get the switch case array  as [1, 0, 0, 0, 1, 0, 0]
            get_switchcase_arr(list1, put)

            # Transform the arr into [0, 0, 1, 2, 0, 2, 2, 1, 1, 0, 1]
            create_put_transform_arr(list1, puts)

        if not line:
            break
    return num

# main method
file_path=input("input the file path : ")
# file_path=C:\Users\hua\Desktop\code.txt
grade=eval(input("input the grade :"))
file = open(file_path, "r", encoding='utf-8')
grade=5
put=[]
puts=[]
if grade>=1:
    print("total num: ", get_keyword_num())
    if grade>=2:
        print("switch num: ", get_switch_num(put))
        if grade >= 3:
            get_case_num(put,get_switch_num(put) )
            print()
            if grade >= 4:
                print("if-else num: ", get_if_else_num(puts))
                if grade >= 5:
                    print("if-elseif-else num: ", get_if_elseif_else_num(puts))
file.close()

