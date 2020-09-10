# Function Plotter
This project intends to plot any function user enters.
this project is separated into multiple parts, the first two parts behaves as a compiler,
it  1- checks the syntax provided by the user, saves it,
    2- checks the grammar provided.
third part is GUI which consists of:
    1- labels           2- text editor           3- button
    4- plot
fourth and final part is the part where it calculates the function and plot it.

## Table Of Contents
* [Application](#system-layout).  
* [Handled cases](#handled-cases).  
* [Features](#features).  
* [Limitations](#limitations).  
* [Future thoughts](#future-thoughts).  
## Application
system design  
![sys](https://user-images.githubusercontent.com/31229408/92669529-15dd3180-f312-11ea-94a2-878a1141cce5.PNG)  

plot  
![plot](https://user-images.githubusercontent.com/31229408/92669564-373e1d80-f312-11ea-8776-282a277f5ddb.PNG)  

error  
![error](https://user-images.githubusercontent.com/31229408/92669583-44f3a300-f312-11ea-8172-7ac70de54e48.PNG)  

## Handled cases:
    1-  +x        => Expected a digit or a variable.  
    2-  +         => Expected a variable.  
    3-  10        => Expected a variable.  
    4-  x+1+      => Expected a digit or a variable.  
    5-  x++1      => Expected a digit or a variable.  
    6-  x**1      => Expected a digit or a variable.  
    7-  x+10%     => unsupported operator, please recheck the function.  
    8-  10+15+20  => variable error, please enter exactly one variable.  
    9-  in Min/Max: character => Make sure that Min/Max is a valid integer number.  
    10- in Min/Max: character+digit (x10) => Make sure that Min/Max is a valid integer number.  
    11- in Min/Max: Min = Max => Please recheck Max/Min values.  
    12- in Min/Max: Min > Max => Please recheck Max/Min values.  
    
## Features:
    1- checks syntax entered by the user.  
    2- displays error messages if any.  
    3- takes min, max range for the function.  
    4- checks on the input range.  
    5- plot entered equation using matplotlib, which is embedded in PySide2 GUI.  
    6- simple design.  

## Limitations:
    1- it can draw equations which has only one variable.  
    2- as this application is still under development, so it supports only (+, -, *, ^, /), for now.  
    3- it can't handle (,{,[, which will be considered during future thoughts.  
    
## Future thoughts:
    1- support more operations.
    2- improve code.
