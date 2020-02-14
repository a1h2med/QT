from os import stat
token_value=[]
string_t_value=''
error_type = ""
token_type=[]
string_t_type=''
bool_colon_found =0
j=0
token_len = 0
turn_on = True
#************************************************************************************#
def match():
    global j
    if j+1 < token_len:
        j += 1
def error(error_type):
    print("ERROOOOOR")
    print(error_type)
#*************************************************************************************#
def factor():
    global error_type
    if (token_type[j]=='OPENBRACKET'):
        match()
        exp()
        if(token_type[j]=='CLOSEDBRACKET'):
            match()
        else:
            error_type = "expected ["
            error(error_type)
            # exit()
    elif(token_type[j]=='NUMBER'):
        match()
    elif(token_type[j]=='IDENTIFIER'):
        match()
    else:
        error_type = "Expected Variable or Number"
        error(error_type)
        # exit()

#*************************************************************************************#
def term():
    global error_type
    factor()
    # if (token_type[j] != 'MULT' and token_type[j] != 'DIV'):
    #     error()
    # else:
    while (token_type[j] == 'MULT' or token_type[j] == 'DIV'):
        match()
        factor()

#*************************************************************************************#
def simple_exp():
    global error_type
    term()
    # if(token_type[j]!='PLUS' and  token_type[j]!='MINUS'):
    #     error()
    # else:
    while(token_type[j]=='PLUS' or  token_type[j]=='MINUS'):
            match()
            term()
#*************************************************************************************#
def exp():
    global error_type
    simple_exp()
    if(token_type[j]=='LESSTHAN'or token_type[j]=='EQUAL'):
        match()
        simple_exp()
#*************************************************************************************#
def write_stmt():
    global error_type
    if(token_type[j]=='WRITE'):
        match()
        exp()
    else:
        error_type = "expected write"
        error(error_type)
        # exit()
#*************************************************************************************#
def read_stmt():
    global error_type
    if(token_type[j]=='READ'):
        match()
        if(token_type[j]=='IDENTIFIER'):
           match()
        else:
            error_type = "Expected Variable or Number"
            error(error_type)
            # exit()
    else:
        error_type = "expected read"
        error(error_type)
        # exit()

#************************************************************************************#
def assign_stmt():
    global error_type
    if(token_type[j]=='IDENTIFIER'):
        match()
        if(token_type[j]=='ASSIGN'):
            match()
            exp()
        else:
            error_type = "expected :="
            error(error_type)
            # exit()
    else:
        error_type = "Expected Variable or Number"
        error(error_type)
        # exit()
#*************************************************************************************#
def repeat_stmt():
    global error_type
    if(token_type[j]=='REPEAT'):
        match()
        stmt_sequence()
        if(token_type[j]=='UNTIL'):
            match()
            exp()
        else:
            error_type = "expected untill"
            error(error_type)
            # exit()
    else:
        error_type = "expected repeat"
        error(error_type)
        # exit()

#*************************************************************************************#
def if_stmt():
    global error_type
    if(token_type[j]=='IF'):
        match()
        exp()

        if(token_type[j]=='THEN'):
            match()
            stmt_sequence()
            if(token_type[j]=='ELSE'):
                match()
                stmt_sequence()

            elif(token_type[j]=='END'):
                match()
            else:
                error_type = "expected end"
                error(error_type)
                # exit()

        else:
            error_type = "expected then"
            error(error_type)
            # exit()

    else:
        error_type = "expected if"
        error(error_type)
        # exit()

#*************************************************************************************#
def statement():
    global error_type
    if j < token_len:
        if(token_type[j]=='IF'):
            if_stmt()
        elif(token_type[j]=='REPEAT'):
            repeat_stmt()
        elif (j+1 < token_len) and (token_type[j+1]=='ASSIGN'):
            assign_stmt()
        elif (token_type[j] == 'READ'):
            read_stmt()
        elif (token_type[j] == 'WRITE'):
            write_stmt()
        else:
            error_type = "expected valid statement"
            error(error_type)
            # # exit()

#*************************************************************************************#
def stmt_sequence():
    global error_type
    statement()
    # if(token_type[j]!='SEMICOLON'):
    #     error()
    # else:
    # print(j)
    while(token_type[j]=='SEMICOLON' and j != token_len-1):
          match()
          statement()

#************************************************************************************#
def program():
    # global turn_on
    global j
    global error_type
    error_type = ""
    j = 0
    stmt_sequence()

    # else:
    #     error_type = "file is empty"

#********************************************start**************************************#

# filepath = 'C:/Users/Mariam/PycharmProjects/parser_project/input to parser .txt '
# set = stat('test.txt').st_size == 0
# # print(set)
# if set != True:
#     with open('test.txt') as fp:
#        for cnt, line in enumerate(fp):
#         # print(line)
#
#         for i in line:
#             if i ==' ':
#                 pass;
#             elif i == ',':
#                 bool_colon_found=1
#
#             elif bool_colon_found==0:
#                string_t_value+=i
#             elif (bool_colon_found==1) and (i!='\n'):
#                 string_t_type+=i
#         token_value.append(string_t_value)
#         token_type.append(string_t_type)
#         token_len = len(token_type)
#         bool_colon_found = 0
#         string_t_value=''
#         string_t_type=''
# else:
#     # global error_type
#     turn_on = False
#     error_type = "the file is empty"
#     error(error_type)
    # # exit()

# print("token_value", token_value)
# print("token_type", token_type)

# program()
# def start(x):
#     if x == 0:
#         program()

# start(0)