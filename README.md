# like-py-xlsx

TL;DR: Call Python from inside Msft Beta Channel Office 365 Excel - Small Quick Xlsx Download - All Source No Binary

Contents

**1 Welcome**<br>
**2 Give short names to large values**<br>
**3 Speak code before values**<br>
**4 Name your own code**<br>
**5 As smooth as Python**<br>
**6 As light as 1 function**<br>
**7 Please help us**<br>

## 1 Welcome

Lisp in Excel is a thing

**1.1 Microsoft added a Lisp into Excel**, since late 2020 at Beta Channel Office 365 Excel

**1.2 Your Excel already has this Lisp in it**, if typing **"=LET(" or "=LAMBDA("** into a cell of your Excel triggers it to help you insert those functions, or if clicking through **the "fx" button** at the left of the Excel Formula Bar opens up the Formula Builder pane on the far right with a Search that finds the LAMBDA and LET functions explained poorly inside

**1.3 Your friends have got this Lisp bundled inside their Excel too**, if they pay often for **an Office 365 Subscription** and click through **Help > Check For Updates** to launch the Microsoft AutoUpdate app, and then switch focus to that app, and then click through **Advanced > Update Channel = Beta Channel**, and then take enough updates

**1.4 Me personally**, I launched "pelavarre/like-py-xlsx" back when they sold me Microsoft Excel for Mac, Version "16.51 (21062020)"

## 2 Give short names to large values

The "=LET(" Function in Excel lets you give your own meaningful short names to large values, not just take the A1 B2 C3 cell names that Excel shoves at you

Like you can mention a string just once, and keep working with it - You don't have to type it all out over again, as often as you need it

    =LEFT(
        "Hello Xlsx Like Py",
        FIND(" ", "Hello Xlsx Like Py")
    )
    Hello

    =LET(
        chars, "Hello Xlsx Like Py",
        LEFT(
            chars,
            FIND(" ", chars))
        )
    Hello

## 3 Speak code before values

The "=LAMBDA(" Function in Excel lets you show us your code as itself: abstract, precise, & complete

You can begin your work by writing and reading the code

You can wait to give the code concrete, specific, values to work till after you write the code

    =LAMBDA(chars,
        LEFT(
            chars,
            FIND(" ", chars))
    )("Hello Xlsx Like Py")
    Hello

## 4 Name your own code

Fair enough, if you do call out just the code without giving it specific values to work with, then even today's Excel will still rudely stop you cold, shouting a CalcError at you

    =LAMBDA(chars, index, MID(chars, LEN(chars) + 1 + index, 1))
    `  #CALC!

What's new is now Excel offers you a workaround - Excel lets you give your own meaningful short name to a large pile of code - You no longer have to type your code all out over again, as often you need your own code to come work with you again

    Excel > Tab Formulas > Define Name
    
    Enter a name for the data range:

        str.word

    Select the range of cells:

        =LAMBDA(chars,
             LEFT(chars,FIND("" "",chars))
        )

You can name it and you can call it by name

    =str.word("Hello Xlsx Like Py")
    Hello

Beware the placement of spaces - Like if you put spaces into the Range Of Cells before the "=LAMBDA" piece, then Excel will give you a vague #REF! error, which in this situation means to say please drop the leading spaces

## 5 As smooth as Python

Let's get moving?

We can crowd-source translations of the Python libraries for working with bools, chars, ints, floats, strings, lists, dicts, and so on and on

We can drop copies of these Define Name Lambda Let things into a small Xlsx, download and go (or has Microsoft even opened up web spaces somewhere, as welcoming as Google Sheets?)

You can start with a copy of our small Xlsx, add what else you please, and all along the way think in Python but write in Excel

For instance, we make it dead easy for you to split apart the Microsoft Windows path name of a file

    =list.item(str.rpartition("C:\My Documents\like-py.xlsx", "\"), -1)
    like-py.xlsx

## 6 As light as 1 function

As you glance through our Excel Lisp source here, you'll see we made a point of translating each Python function completely - We translated all the way to Excel from Python - We didn't translate from Python to just a mix of Python and Excel - You can copy out single functions when you need them - You don't have to copy all or nothing

## 7 Please help us

Got some other piece of Python you like?

Tell us about it, like come find me at https://twitter.com/pelavarre

These are our early days, not much here yet - If you look for something difficult, you won't find here - If you surprise this code with new test cases, it will betray you today

Do you love our "like-py.xlsx" like you love pie?

Please tell a friend

## 8 Contributors

Thanks to my friends for encouraging me to share our "like-py.xlsx" with you

Thanks to Charlotte Sands "Nothing's Even Wrong" 2021 for speaking the lyric line "do you love me like that", such that I misheard this line as "do you love me like Pie?", which is a line I like lots : -)
