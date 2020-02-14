import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Parser_GUI

string_t_value=''

string_t_type=''
bool_colon_found =0
j=0
token_len = 0

#token_value, token_type = Parser_GUI.UI.Read()

#
#
#
#
################## drawing rectangle ######################
#
#
#
#
def draw_Rectangle(x,y,string1,string2,image,flag):
    x1 = x + 80
    y1 = y + 50
    image = cv.rectangle(image, (x, y), (x1, y1), (255, 255, 0), 1)
    center_x = int(((x1+x)/2))-20
    center_y = int(((y1+y)/2))
    center = (center_x,center_y)
    cv.putText(image,string1,center,cv.FONT_HERSHEY_SIMPLEX,.5,(127,255,127),1)
    if flag == 1:                               # depending on the type of the rectangle I'll add the second string or not
        center = (center_x+7,center_y+15)
        cv.putText(image,string2,center,cv.FONT_HERSHEY_SIMPLEX,.5,(127,255,127),1)
    Bottom_y = y1
    return x1, center_x, center_y, y, Bottom_y

#
#
#
#
#################### drawing Line ####################3
#
#
#
#
def draw_line(x,x1,y,y1,image):
    #x1 = x + (140-20)
    cv.line(image, (x, y), (x1, y1), (127, 255, 127), 2)
    return x1,y1

#
#
#
#
################## drawing Circle ##################
#
#
#
#
def draw_circle(x,y,string1,string2,image,flag):
    radius = 30
    center = (x,y)
    cv.circle(image,center,radius,(127,255,127),1)
    center = (x-17,y)
    cv.putText(image,string1,center,cv.FONT_HERSHEY_SIMPLEX,.35,(127,255,127),1)
    if flag == 1:
        center = (x-20,y+15)
        cv.putText(image,string2,center,cv.FONT_HERSHEY_SIMPLEX,.5,(127,255,127),1)
    return x,x+50, y-radius, y+radius

#
#
#
#
#################### general Checking shape #######################
#
#
#
#
def IF_Check_condition(x_axis,y_axis,image,string1,string2,string3,string4,string5,string6,flag):
    x_axis, y_axis = draw_line(x_axis, x_axis - 40, y_axis, y_axis + 40, image)
    top_y = y_axis
    x_axis, y_axis = x_axis, y_axis + 30
    new_x_axis,_, _, new_y_axis = draw_circle(x_axis, y_axis,  string2, string1,image, flag)
    x_axis, y_axis = draw_line(new_x_axis, new_x_axis - 40, new_y_axis, new_y_axis + 40, image)
    x_axis, y_axis = x_axis, y_axis + 30
    x_axis,_, _, y_axis = draw_circle(x_axis, y_axis, string4, string3, image, 1)
    x_axis, y_axis = draw_line(new_x_axis, new_x_axis + 40, new_y_axis, new_y_axis + 40, image)
    x_axis, y_axis = x_axis, y_axis + 30
    _,Last_x_axis, y_minus , y_Plus = draw_circle(x_axis, y_axis,  string6,string5, image, 1)
    return Last_x_axis, y_minus , y_Plus, top_y
#
#
#
#
####################### it only draws a line and circle to it ###############
#
#
#
#
def Assignment(x_axis,y_axis,image,string1,string2):
    x_axis, y_axis = draw_line(x_axis, x_axis, y_axis, y_axis + 40, image)
    x_axis, y_axis = x_axis, y_axis + 30
    x_axis,_, y_minus, y_Plus = draw_circle(x_axis, y_axis, string1, string2, image, 1)
    return x_axis, y_minus, y_Plus
#
#
#
#
######################### assignment expression  ############################
#
#
#
#
def assign_Expression(x,y,image,operation_type,operator,Left_type,Left_Value,Right_Type,Right_Value,Assignee_Name,flag):
    output_x, x_axis, Center_y, _, y_axis = draw_Rectangle(x,y-20,"assign",Assignee_Name,image,1)
    if flag == 1:
        Assignment(x_axis,y_axis,image,Left_Value,Left_type)
    else:
        IF_Check_condition(x_axis+50,y_axis,image,operation_type,operator,Left_type,Left_Value,Right_Type,Right_Value,1)
    return output_x,Center_y
#
#
#
#
######################## Write expression ############
#
#
#
#
def write_Function(x,y,image,string1,string2): #,flag):
#    if flag == 0:
    output_x, x_axis, Center_y, _, y_axis = draw_Rectangle(x,y-20,"write","no",image,0)
    Assignment(x_axis,y_axis,image,string1,string2)
#    else:
#        output_x, x_axis, Center_y, _, y_axis = draw_Rectangle(x+80, y-25, "write", "no", image, 0)
#        draw_line(output_x-160,output_x-80,Center_y,Center_y,image)
#        Assignment(x_axis, y_axis, image, string1, string2)
    return output_x,Center_y

#
#
#
#
##################### read Function ########################
#
#
#
#
def read_Function(x,y,string,image):
    output_x, _, Center_y, _, _ = draw_Rectangle(x,y-20,"read",string,image,1)
    return output_x, Center_y
#
#
#
#
#################### If Functions ################
#
#
#
#
def IF_Function_part1(image,x,y,string1,string2,string3,string4,string5,string6):
    Bottom_x,x_axis,_,Center_y,y_axis = draw_Rectangle(x,y-20,"IF",0,image,0)
    Last_x_axis,_,_,top_y = IF_Check_condition(x_axis,y_axis,image,string1,string2,string3,string4,string5,string6,1)
    return Bottom_x,Last_x_axis,Center_y, top_y, y_axis

def IF_Function_else_part(image,Line_start_x,Line_start_y,Line_end_x,Line_end_y,Rec_start_x,Rec_Start_y):
    draw_line(Line_start_x,Line_start_y,Line_end_x,Line_end_y,image)
    _,Center_x,_,_,Bottom_y = draw_Rectangle(Rec_start_x,Rec_Start_y,"else","Null",image,0)
    return Center_x, Bottom_y
#
#
#
#
################### repeat Function ######################
#
#
#
#
def repeat(image,x,y):
    x,Center_x,_,center_y,Bottom_y = draw_Rectangle(x,y-20,"repeat","null",image,0)
    return x,Center_x,center_y,Bottom_y

#
#
#
#
################################## line + circle Right #########################
#
#
#
#

def LinePlusCircleRight(x_axis, y_axis, image, string1, string2, flag):
    x_axis, y_axis = draw_line(x_axis, x_axis + 40, y_axis, y_axis + 40, image)
    x_axis, y_axis = x_axis, y_axis +30
    new_x_axis, _, _, new_y_axis = draw_circle(x_axis, y_axis, string1, string2,image, flag)
    return new_x_axis, new_y_axis

#
#
#
#
################################## line + circle left #########################
#
#
#
#

def LinePlusCircleLeft(x_axis, y_axis, image, string1, string2,flag):
    x_axis, y_axis = draw_line(x_axis, x_axis - 40, y_axis, y_axis + 40, image)
    x_axis, y_axis = x_axis, y_axis + 30
    new_x_axis, _, _, new_y_axis = draw_circle(x_axis, y_axis,  string1, string2,image, flag)
    return new_x_axis, new_y_axis

#
#
#
#
######################## Start Of the code #################
#
#
#
#

############### taking input #######################

############### end of imputs ######################


def process(token_value, token_type):
    #################### image Size ###############
    black_rec = np.zeros((500, 1300, 3), np.uint8)

    i = 0
    check = 0
    x, y = 0, 0
    read_flag = 0
    repeat_flag = 0
    IF_OR_Repeat_Bottom_x = 0
    Center_Y_OF_Previous_Position = 0
    Last_X = 0
    until_x = 0
    until_flag = 0
    end_flag = 0

#    if "(" in token_value:
#        token_value.remove("(")

#    if ")" in token_value:
#        token_value.remove(")")

#    if "OPENBRACKET" in token_type:
#        token_type.remove("OPENBRACKET")

#    if "CLOSEDBRACKET" in token_type:
#        token_type.remove("CLOSEDBRACKET")

    While_loop_Check_condition = len(token_value)
    while i < While_loop_Check_condition:
        if check == 0:
            x, y = 20, 20

        if token_value[i] == "read":
            if check == 1 and (read_flag == 0 and repeat_flag == 0):
                if until_flag == 1 or end_flag == 1:
                    x, _ = draw_line(x, x + Last_X, y, y, black_rec)
                    until_flag = 0
                    end_flag = 0
                else:
                    x, _ = draw_line(x, x + 40, y, y, black_rec)
            elif check == 0:
                print(1)
            else:
                x, _ = draw_line(IF_OR_Repeat_Bottom_x, x, y, y + 20, black_rec)
                read_flag = 0
                repeat_flag = 0

            x, y = read_Function(x, y, "(" + token_value[i + 1] + ")", black_rec)
            Last_X = x
            check = 1

        elif token_value[i] == "write":
            if check == 1 and (read_flag == 0 and repeat_flag == 0):
                if until_flag == 1 or end_flag == 1:
                    x, _ = draw_line(x, x + Last_X, y, y, black_rec)
                    until_flag = 0
                    end_flag = 0
                else:
                    x, _ = draw_line(x, x + 40, y, y, black_rec)

            elif check == 0:
                print(1)
            else:
                x, _ = draw_line(IF_OR_Repeat_Bottom_x, x, y, y + 20, black_rec)
                read_flag = 0
                repeat_flag = 0

            x, y = write_Function(x, y, black_rec, token_type[i + 1], token_value[i + 1])
            Last_X = x
            check = 1

        elif token_value[i] == "if":
            if check == 1 and (read_flag == 0 and repeat_flag == 0):
                if until_flag == 1 or end_flag == 1:
                    x, _ = draw_line(x, x + Last_X, y, y, black_rec)
                    until_flag = 0
                    end_flag = 0
                else:
                    x, _ = draw_line(x, x + 40, y, y, black_rec)
            elif check == 0:
                x = x + 80
                print(1)
            else:
                x, _ = draw_line(IF_OR_Repeat_Bottom_x, x, y, y + 20, black_rec)
                read_flag = 0
                repeat_flag = 0

            IF_OR_Repeat_Bottom_x, x, Center_Y_OF_Previous_Position, y, _ = IF_Function_part1(black_rec, x, y,
                                                                                              token_value[i + 2],
                                                                                              token_type[i + 2],
                                                                                              token_value[i + 1],
                                                                                              token_type[i + 1],
                                                                                              token_value[i + 3],
                                                                                              token_type[i + 3])
            i = i + 4
            check = 1
            read_flag = 1

        elif token_value[i] == ":=":
            if check == 1 and (read_flag == 0 and repeat_flag == 0):
                print("NoOOOOOOOOOOO")
                print(check)
                if until_flag == 1 or end_flag == 1:
                    x, _ = draw_line(x, x + Last_X, y, y, black_rec)
                    until_flag = 0
                    end_flag = 0
                else:
                    x, _ = draw_line(x, x + 40, y, y, black_rec)
            elif check == 0:
                x = x + 80
                print(1)
            else:
                print("WHhhhhaaaaaaaaaaaaaaaaaaay")
                x, _ = draw_line(IF_OR_Repeat_Bottom_x, x, y, y - 40, black_rec)
                y = y + 25
                read_flag = 0
                repeat_flag = 0

            if i+2 == While_loop_Check_condition or i+2 > While_loop_Check_condition:
                x, y = assign_Expression(x, y, black_rec, "null", "null", token_value[i + 1], token_type[i + 1], "null",
                                         "null", token_value[i - 1], 1)

            else:

                if token_value[i + 2] == "+" or token_value[i + 2] == "-" or token_value[i + 2] == "*" or token_value[i + 2] == "/":

                    if token_value[i+3] == "(":
                        token_value.remove("(")
                        token_value.remove(")")
                        token_type.remove("OPENBRACKET")
                        token_type.remove("CLOSEDBRACKET")
                        While_loop_Check_condition = len(token_value)
                        if token_value[i + 2] == "+" or token_value[i + 2] == "-" or token_value[i + 2] == "*" or token_value[i + 2] == "/":

                            x, _, _, y2 = draw_circle(100, 100, token_type[i + 2], token_value[i + 2], black_rec, 1)
                            LinePlusCircleLeft(x, y2, black_rec, token_type[i + 1], token_value[i + 1], 1)

                            if (i + 4 == While_loop_Check_condition) or (i + 4 > While_loop_Check_condition):
                                LinePlusCircleRight(x, y2, black_rec, token_type[i + 3], token_value[i + 3], 1)
                                # if token_value[i+2] == "+" or token_value[i+2] == "-" or token_value[i+2] == "*" or token_value[i+2] == "/":


                            else:
                                i += 2
                                while token_value[i + 2] == "+" or token_value[i + 2] == "-" or token_value[i + 2] == "*" or token_value[
                                    i + 2] == "/":
                                    print(token_value[i + 2])
                                    #                    print(token_type[i+2])
                                    x, y2 = LinePlusCircleRight(x, y2, black_rec, token_type[i + 2], token_value[i + 2], 1)
                                    LinePlusCircleLeft(x, y2, black_rec, token_type[i + 1], token_value[i + 1], 1)

                                    if i + 4 == While_loop_Check_condition or i + 4 > While_loop_Check_condition:
                                        print(token_value[i + 3])
                                        x, y2 = LinePlusCircleRight(x, y2, black_rec, token_type[i + 3], token_value[i + 3], 1)
                                        break
                                    else:
                                        i += 2
                    else:
                        x, y = assign_Expression(x, y, black_rec, token_value[i + 2], token_type[i + 2], token_value[i + 1],
                                         token_type[i + 1], token_value[i + 3], token_type[i + 3], token_value[i - 1],
                                         0)  ##### not completed yet

                else:
                    x, y = assign_Expression(x, y, black_rec, "null", "null", token_value[i + 1], token_type[i + 1], "null",
                                         "null", token_value[i - 1], 1)
            Last_X = x
            check = 1

        elif token_value[i] == "Repeat":
            if check == 1 and (read_flag == 0 and repeat_flag == 0):
                if until_flag == 1 or end_flag == 1:
                    x, _ = draw_line(x, x + Last_X, y, y, black_rec)
                    until_flag = 0
                    end_flag = 0
                else:
                    x, _ = draw_line(x, x + 40, y, y, black_rec)
            elif check == 0:
                x = x + 80
                print(1)
            else:
                x, _ = draw_line(IF_OR_Repeat_Bottom_x, x, y, y + 20, black_rec)
                read_flag = 0
                repeat_flag = 0

            until_x, x, Center_Y_OF_Previous_Position, y = repeat(black_rec, x, y)
            y = y + 40
            IF_OR_Repeat_Bottom_x = x
            check = 1
            repeat_flag = 1

        elif token_value[i] == "else":
            x, y = IF_Function_else_part(black_rec, IF_OR_Repeat_Bottom_x, x, y, y + 20, x, y + 20)
            check = 1

        elif token_value[i] == "Until":
            x, y = draw_line(IF_OR_Repeat_Bottom_x, Last_X + 100, Center_Y_OF_Previous_Position + 50,
                             Center_Y_OF_Previous_Position + 90, black_rec)
            x, _, _, _ = IF_Check_condition(x, y, black_rec, token_value[i+2],token_type[i+2],
                                            token_value[i + 1],  token_type[i + 1], token_value[i + 3],token_type[i + 3],  1)
            y = Center_Y_OF_Previous_Position + 20
            x = IF_OR_Repeat_Bottom_x + 60
            Last_X = x
            until_flag = 1

        elif token_value[i] == "end":
            y = Center_Y_OF_Previous_Position
            x = Last_X
            end_flag = 1

        i += 1
    cv.imshow("window", black_rec)
    cv.waitKey()