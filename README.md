# Snake-Xenzia
Classic Snake Game Using Turtle and Screen Classes of turtle 

# TO RUN THIS PROJECT
Download and Save all Files in the same Folder

# main.py

 This file contains the main code and is explained using comments.
 
# Classes Used :

I have created seperate classes with distinct functionalities: 

## Snake Class 
Creates Snake Body and has methods to define movement of Snake , Increase Size of Snake , Detect Collisions with itself or Wall <br />
Snake Body is Square in Shape. This is done using turtle class

## Food Class 
Creates a Circular Food item  within the Boundary Walls using turtle class and places it in random locations within the Boundary. <br />
The size of food turtle is half of that of the Snake's turtle object done using shapesize() method

## Score Class

This Class reads High Score from a File HighScore.txt and displays current Score as well as High Score on the Top of the Screen <br />
It has methods to update Score as well as High Score <br />
If New High Score is achieved by Player, it writes the new score in HighScore.txt <br />

# HighScore.txt

A Text File that Saves the High Scores.
