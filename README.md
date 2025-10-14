# Who Wants to be a Millionaire? 
## Description
A console app version of the TV game-show "Who Wants To Be a Millionaire" using Python and the Open Trivia DB Api.


## Issues Faced During Development
### 10/4/2025
- Had to learn how to properly parse data from an API. 
- Determining how to output the questions, answers and how to accept input for said answers, checking said answers.
### 10/6/2025
- I'm still getting used to using Python instead of C#, so I'm used to just clicking run in Visual Studio and it running. Thats not the case in Pycharm, as I need to actually have main chosen to run it. Because of this, I have no idea for how long my questions object, has been working as I was just running the api-handler file.
- Generally just fell behind in terms of how much I should have done by not, especially in keeping record of issues.
- I may have fleshed things out more than necessary into different files instead of condensing it down to less files. Need to work on making code concise and not making 10 different files for one small program.
- Worked in conjunction with a classmate to resolve issues regarding the question and answer portion. The issue was primarily that while I was able to convert the answer to a number to fit the necessary requirements to pull from an array, I was struggling to be able to use said question to check the inputted answer, receiving a nonetype error or out of index error.

### 10/7/2025 - 10/14/2025
- This whole period was spent trying to figure out why the question and answer portion of the game wasnt functioning as needed, specifically when a question was answered incorrectly. The issue was the recursive call in qna, which was unnecessary as the gameplay was already contained in a loop that ended when a question was answered incorrectly. This caused the question to be asked again after the game had been lost and an option had been selected from the question for whether or not to play again.

### 10/14/2025
- Despite this project being for a class lab, I wanted it to be something I could add to a portfolio and have available, so I went back and tried to add comments where there were none and statements at the top explaining what the file does. I learned about """ comments because I had a comment using triple single quotes at the beginning of one of the files and Pycharm made a correction to align with the commenting standards 
- In the last point, I mentioned I was using Pycharm. While the lab instructions directed us to use visual studio, Pycharm honestly feels very good to use, so I have been using that for most labs and assignments. 
- At some point, I was having issues calling variables within different methods. It would not let me call the external variables, but would rather say the name of a variable was the same as that of a variable from the outer scope. Since the variables were needed in several functions across the program, I ended up researching to figure out how to solve this and the answer I came up with was declaring the values as global in the functions. While I'm unsure if this is the best way to resolve this in Python, it got the job done.

## Credits
Program made by Steven Mullins

## LEGAL DISCLAIMER & ATTRIBUTION

This console application is a fan-made tribute to the popular game show "Who Wants to Be a Millionaire?", originally created by David Briggs, Mike Whitehill, and Steven Knight.

All rights, trademarks, and copyrights for "Who Wants to Be a Millionaire?", including its format, name, and associated imagery, are the property of Sony Pictures Television.

This project is unofficial, non-commercial, and created for educational and entertainment purposes only. It is not endorsed by or affiliated with the official rights holders.

-------------------------------------------------------------------------------------
API Provided by the fine folks at PixelTail Games under the Creative Commons license.

https://creativecommons.org/licenses/by-sa/4.0/
https://opentdb.com/
https://www.pixeltailgames.com/   
