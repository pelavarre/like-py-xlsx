# xlsx-like-py

TL;DR => To Speak Python Inside Msft Beta Channel Office 365 Excel - Small Quick Xlsx Download - All Source No Binary

## Lisp in Excel is a thing

**1 ) Microsoft added a Lisp into Excel**, since late 2020 at Beta Channel Office 365 Excel

**2 ) Your Excel already has this Lisp in it**, if typing "=LET(" or "=LAMBDA(" into a cell of your Excel triggers it to prompt you to type out more of those functional calls, or if clicking through the (fx) button at the left of the Formula Bar opens up the Formula Builder pane on the far right with a Search that finds LAMBDA or LET inside

**3 ) Your friends get this Lisp bundled inside their Excel too if** they pay for an Office 365 Subscription and click through Help > Check For Updates to launch the Microsoft AutoUpdate app, and then switch focus to that app, and then click through Advanced > Update Channel = Beta Channel and so on - I launched this GitHub Repo when they sold me Microsoft Excel for Mac, Version 16.51 (21062020)

## Lisp in Excel lets you give short names to large values

The "=LET(" stuff lets you give your own meaningful short names to large values, not just take the A1 B2 C3 cell names Excel coins for you

Like you can mention a string just once, and keep working with it, you don't have to type it all out over again, as often as you need it

    =MID("Hello Xlsx Like Py", LEN("Hello Xlsx Like Py") + 1 +  -2,   1)
    P

    =LET( chars,"Hello Xlsx Like Py", index,-2, MID(chars,LEN(chars)+1+index,1) )
    P

## Lisp in Excel lets you speak code before values

The "=LAMBDA(" stuff lets you show us code as it exists - abstract, precise, and complete - all without demanding you begin by giving it concrete, specific, values to work with

    =LAMBDA( chars, index, MID(chars, LEN(chars) + 1 + index, 1) )( "Hello Xlsx Like Py", -2 )
    P

## Lisp in Excel lets you name the code

Admittedly, if you do call out just the code without choosing values for it work with, Excel even today will still rudely stop you cold, with a CalcError

    =LAMBDA( chars, index, MID(chars, LEN(chars) + 1 + index, 1) )
    `  #CALC!

But now Excel has a workaround:  Excel lets you give your own meaningful short name to a large pile of code, now you don't have to type the code all out over again, as often you need the code to come work with you

    Excel > Tab Formulas > Define Name
    
    Enter a name for the data range:  str.char
    Select the range of cells:
        =LAMBDA(chars, index,
            IF(index < 0,
                MID(chars, LEN(chars) + 1 + index, 1),
                MID(chars, index, 1)))

    =str.char("Hello Xlsx Like Py", -2)
    P

## Lisp in Excel lets us give you the Python libraries

Ta da, yes we can crowd-source translations of the Python libraries for working with characters (chars), ints, floats, strings, and so on and on

Drop these Define Name Lambda Let things into a small Xlsx, download and go

So long as you start work inside a copy of our small Xlsx, you can add what else you please, and all along the way think in Python but write in Excel

For example

    =list.item(str.rpartition("C:\My Documents\like-py.xlsx", "\"), -1)
    like-py.xlsx
    
## Love this like Pie

Love this like pie?

Tell a friend
