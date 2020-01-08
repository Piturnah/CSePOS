"""
Multiline string formatting
Author: Pit
Acknowledgements: Thanks to Will for highlighting the importance
of automated boxes! You are my inspiration.
Copyright (c) 2019 Peter Hebden under MIT License
"""



#BOX: (generates a box around a string)
#takes string to add box around, and parameters for width, justification, border, and padding
#returns formatted string
def box(toFormat, boxChar = '|',width = 0, justify = "c", isPadded = True):
    try:
        width = _Check_Width(width, toFormat, isPadded)

        #Format the box
        #Add the top border (with padding if applicable)
        formattedStr = boxChar * width
        if isPadded:
            formattedStr += "\n" + boxChar + " ".center(width - 2) + boxChar

        #Format each line individually
        for line in toFormat.splitlines():
            formattedStr += "\n" + boxChar

            funcDict = {
                "c" : line.center,
                "l" : line.ljust,
                "r" : line.rjust
            }
            if isPadded:
                formattedStr += " " + funcDict[justify](width - 4) + " "
            else:
                formattedStr += funcDict[justify](width - 2)
            
            formattedStr += boxChar

        #Add bottom border (with padding if applicable)
        if isPadded:
            formattedStr += "\n" + boxChar + " ".center(width - 2) + boxChar
        formattedStr += "\n" + boxChar * width

        return formattedStr
    except:
        print(error_message + "\n> Error with box()")

#COLUMN: Formats mutliline string into columns.
def col(toFormat, colChar = "|", colWidth = "auto", just = "c", delimiter = " "):
    try:
        #Check for widest cell to set column width
        try:
            maxWidth = int(colWidth)
        except:
            maxWidth = 0
            
        if colWidth == "auto":
            
            #Check length of each cell againt maxWidth
            for cell in toFormat.split(delimiter):
                if len(cell) > maxWidth:
                    maxWidth = len(cell)

        #Format the columns
        formattedStr = ""
        for line in toFormat.splitlines():
            
            for cell in line.split(delimiter):
                funcDict = {
                    "c" : cell.center,
                    "l" : cell.ljust,
                    "r" : cell.rjust
                }

                #Determine whether cell contains integer value
                isInt = False
                try:
                    cell = int(cell)
                    isInt = True
                except:
                    pass
                cell = str(cell)

                #Justify the current cell
                if not isInt:    
                    formattedStr += colChar + funcDict[just](maxWidth)
                else:
                    formattedStr += colChar + cell.rjust(maxWidth)
                    
            formattedStr += colChar
            formattedStr += "\n"

        return(formattedStr)
    except:
        print(error_message + "\n> Error with col()")

#FLAIR: Bring some life
def flair(toFormat, flairChar = "~", width = "auto", just = "c"):
    try:
        #Determine the length of the longest line
        maxLineWidth = _Check_Width(0, toFormat, False)
        #If no total width provided, allocate 5 spaces outside longest line
        try:
            width = int(width)
        except:
            width = maxLineWidth + 10
            

        formattedStr = ""
        for line in toFormat.splitlines():
            
            funcDict = {
                "c" : line.center,
                "l" : line.ljust,
                "r" : line.rjust
            }
            formattedStr+= funcDict[just](width, flairChar) 

            formattedStr+="\n"

        return formattedStr
    except:
        print(error_message + "\n> Error with flair()")

    
#Check each line to see if it has a greater width than the user defined width
#If it does, update the width    
def _Check_Width(testWidth, toTest, isPadded):
    for line in toTest.splitlines():
        if isPadded:
            if len(line) + 4 > testWidth:
                testWidth = len(line) + 4
        elif len(line) + 2 > testWidth:
            testWidth = len(line) + 2
            
    return testWidth

error_message = flair("\nSomething went wrong. Try multilines.help()",".",50, "r")
    
def help():
    print(box(flair(" MULTILINES USAGE ", "=", 63) + "\n Info:\n\n" + col("""Version:0.1.1
Author:Peter "Pit" Hebden""", " ", 30, "l", ":") + "\n Usage:\n\n" +
          flair(box("""Welcome to my multiline formatting tool.
Here are the currently available functions:
box - returns the string, in a box.
col - returns the string, in columns.
flair - adds flair to the string.
The parameters for each function are largely
the same:
toFormat*, char, width, just
toFormat - string, the string you want
    formatted.
char - string, the character used (e.g for
    border, flair).
width - int, the width of the formatting.
    For col, this is the width of each column.
    If arg is 0, width is automatically
    determined.
just - "l"/"r"/"c", the justification.
    left/right/center. Center by default.
Some functions have extra unique parameters
box - isPadded, bool, True by default: whether
    the box has padding
col - delimiter, string, the delimiter for each
    column. Space by default.""", ":", 50, "l")), "|", 0, "l"))
