to use this tool run Main.py either in an IDE or a terminal, you will also need the 3 other .py files that accompany
Main.py you will need a python interpreter to run this code.

to revise all the questions and suggestions you may use the function verifyQuestions()
that is commented out on line 8 of Main.py

This tool gives personalized suggestions depending on how well each question is answered (suggestions 
are given if the user marks 0, 1, or 2) and also depending on how well they perform on 
each section. if they recieve any individual score that is less than 75 percent they
will be shown a specific suggestion related to that section. if you would like to see all of the
suggestions pertaining to their score of each section use the function seeScoreSuggestions() commented
out on line 9 of Main.py

In a few of the suggestions it will mention looking for the security best practices file. the file that it is referencing
is named "Security Best Practices.docx" it is located in the directory that contains this file.

To run on windows (unless you have python interpretor on your system Path variables):
winpty python.exe Main.py

(with path variables set up):
python Main.py