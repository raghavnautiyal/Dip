# Dip

Dip is a dynamically typed interpreted programming language written in Python, which gives
emphasis to readability and ease of use, while also providing the power of all of python’s
libraries. Dip is aimed at beginners, looking to start with programming.

# Working with Dip

Dip gives you access to a development environment which comes bundled with Dip - The DDE,
short for Dip Development Environment. It gathers inspiration from Python’s IDLE, and has a
text editor for you to edit and create dip programs, and an interactive shell, where you can
execute and see the output of your programs.

You can evaluate expressions by writing them after ​<code>Dip></code>

<code>Dip> 1 + 2
3
Dip> 1 - 3
-2
Dip> 3 + 9
12
</code>



# Evaluating external files

It's possible to load external files written in Dip by calling the ‘run’ function inside the DDE
interface by executing the run function followed by the relative path of the files that you want to
be evaluated.

<code>Dip Beta (Version 0.1)
Type in 'exit' to exit the shell</code>
<code>Dip> run("/Users/raghav/Desktop/hello_dip.dip")
Hello, Dip
0 </code>


# Dip basics

Most of Dip’s functions are either reminiscent of Python, or build off them, so people getting
started with programming (or even Python programmers for that matter) won’t have any trouble
understanding them. These basics are divided into three different categories, data types, builtin
functions and the standard library.

## Dip’s Data Types

Dip contains 5 data types which you will generally interact with. These are Numbers, Strings,
Lists, Functions and Errors.

**Numbers**

Dip supports integers and decimals, called ints and floats in python. Note that anything following
a ‘#’ on the same line is interpreted as a comment and not evaluated.

<code>Dip Beta (Version 0.1)
Type in 'exit' to exit the shell

Dip> 10 / 2
5.0
Dip> 1 + 3
4
Dip> 34 * 34
1156</code>


Note that in case of recurring decimals, they are left at 15 decimal places

<code>Dip> 100 / 6
16.666666666666668</code>

Some functions you can perform on numbers are sin, cos, tan and pi.

<code>Dip> sin(45)
0.8509035245341184
Dip> cos(45)
0.5253219888177297
Dip> tan(45)
1.6197751905438615
Dip> pi
3.141592653589793</code>



**Strings**

A string is a combination of zero or more characters contains inside double-quotes.

<code>Dip> "Hello, Dip!"
Hello, Dip!
</code>

There are many things that you can do with strings, including adding them, iterating through
them, and joining them.

<code>Dip> join("Hello ", "Dip!")
Hello Dip!
Dip> print("I am dip, an interpreted programming language")
I am dip, an interpreted programming language
Dip> variable str = "string!"
string!
Dip> for i = 0 to length(str) then print(str / i)
s
t
r
i
n
g
!</code>


**Lists**

A list is a combination of values inside square braces, separated by commas.
<code>Dip> ["l", "i", "s", "t"]
l, i, s, t</code>

Lists can contain integers, strings, functions and even other lists.

<code>Dip> [[1, 2], [3, 4], [5, 6]]
1, 2, 3, 4, 5, 6
Dip> </code>

There are many things that you can do with lists, including ‘join’, which joins two lists, ‘add’,
which adds an element to a list, ‘remove’, which removes an element at an index from a list.

<code>Dip> variable new_list = join([1, 2, 3], [4, 5, 6])
1, 2, 3, 4, 5, 6
Dip> new_list
1, 2, 3, 4, 5, 6
Dip> add(new_list, 7)
1, 2, 3, 4, 5, 6, 7
Dip> new_list
1, 2, 3, 4, 5, 6, 7
Dip> remove(new_list, 4)
5
Dip> new_list
1, 2, 3, 4, 6, 7
Dip> </code>


Note that the ‘remove’ function removes the element from the 4th index in this case, which is 5.

**Functions**

Functions can be defined using the 'function' keyword, followed by the name of the function, and then its arguments in parenthesis. For a single line function, you can use '->' and then type what you want it to do. For a multi-line function, enter a new line and end the function with an end statement

<code>Dip> function add(a, b) -> print(a + b)
<function add>
Dip> add(4, 5)
9
Dip> </code>

<code>
function odd_or_even(number)
    if number % 2 == 0 then print("even") else print("odd")
end
</code>

Read more about functions in the builtin functions section!

**Errors**

Errors are generated automatically when the user tries to evaluate invalid code. Dip contains 5
different error types, Illegal Character Error, Expected Character Error, Runtime Errors, Invalid
Syntax Errors and Custom Errors. Custom errors can also be generated using the ‘error’
function followed by a string inside parenthesis. The string will be the message of the error.
Errors in the interpreter can help the user by providing insightful commentary.

**Illegal Character Errors - Called when an illegal character is found**
<code>Dip> @
Illegal Character: '@'
File Dip Shell, line 1
@
^
</code>

**Expected Character Errors - Called when a character is not found**

<code>Invalid Syntax / Character Not Found: Expected 'end'
File <Dip Shell>, line 1
function add(a, b); return a + b^
</code>
**Runtime Errors - A range of errors that might rise at runtime**

<code>Runtime Error: Illegal operation - check you are comparing two different data types (eg. integer and string)
File <Dip Shell>, line 1

1 - "1"
^^^^^^^
</code>


**Invalid Syntax Errors - Called when the syntax is invalid**
<code>Invalid Syntax / Character Not Found: Expected int, float, identifier, '+', '-', '(', '[', if, for, while or function
File <Dip Shell>, line 1

5 === 5
       ^
 </code>

**Custom Errors - User Defined errors that can be called any time**

 <code>
Dip> error("test error")
Custom Error: test error
 </code>
These errors can then be used like the built-in errors.

## Dip’s Built-in Functions

**What is a Builtin Function**

How do these functions actually work under the hood? In reality, they are nothing more than a function written in Python, that the interpreter calls when evaluating the symbol associated to it. That's how I inserted basic functionalities into the language like arithmetic operations and list manipulation, but it doesn't stop here, from very simple builtin operations you can write complex functions like the ones in the std library and expand the functionalities of the language without writing a single line of Python.


**Print**

Prints text to the screen

<code>Dip> print("I am dip, an interpreted programming language")
I am dip, an interpreted programming language</code>

**Say**

Uses the Operating System’s ‘say’ command and says whatever is passed into it. Returns nothing.

<code>
Dip> say("hi!")
0
Dip>
</code>

**Random Int**

Selects a random integer from the range given to it

<code>Dip> random_int(0, 10)
10
Dip> random_int(0, 10)
9
Dip> random_int(0, 10)
0</code>

**Root**

Gets the square root of the number given to it

<code>Dip> root(4)
2.0</code>

**Sin*

Calculates the sin value of a given number

<code>Dip> sin(45)
0.8509035245341184</code>

**Cos**

Calculates the cos value of a given number

<code>Dip> cos(45)
0.5253219888177297</code>

**Tan**

Calculates the tan value of a given number

<code>Dip> tan(45)
1.6197751905438615</code>

**Input**

Gets User Input

<code>Dip> input("User Input...")
ok</code>

**Input_Integer**

Gets User Input and ensures it is an integer

<code>Dip> input_integer("User Input...")
23</code>

<code>Dip> input_integer("User Input...")
Must be an integer, try again
Dip>input_integer("User Input...")</code>

**is_number()**

Checks if the argument passed is a number

<code>
Dip> is_number(34)
1
Dip> is_number("F")
0</code>

**is_string()**

Checks if the argument passed is a string

<code>
Dip> is_string("string")
1
Dip> is_string(34)
0</code>

**is_list()**

Checks if the argument passed is a list

<code>
Dip> is_list([3, 4, 5])
1
Dip> is_list(34)
0</code>


**is_function()**

Checks if the argument passed is a function

<code>Dip> variable x = function add(a, b) -> a + b
<function add>
Dip> x
<function add>
Dip> is_function(x)
1
Dip> is_function("F")
0
Dip></code>

**add()**

Adds an element to a list

<code>Dip> variable lst = [0]
0
Dip> add(lst, 1)
0, 1
Dip> lst
0, 1
Dip></code>

**remove()**

Removes the element at index in a list

<code>Dip> remove(lst, 0)
0
Dip> lst
1
Dip></code>

**join()**

Joins two lists or strings

<code>Dip> join(lst, [2, 3])
1, 2, 3
Dip> join("hi", " there")
hi there
Dip></code>

**integer()**

Converts argument to an integer

<code>Dip> integer("4")
4
Dip> integer("definitely not an integer")

Runtime Error: ValueError: Invalid literal for integer() with base 10: 'definitely not an integer'
File <Dip Shell>, line 1

integer("definitely not an integer")</code>

**decimal()**

Converts argument to a decimal

<code>Dip> decimal("34.3434")
34.3434
Dip> decimal("definitely not an decimal")

Runtime Error: ValueError: Could not convert string to decimal: 'definitely not an decimal'
File <Dip Shell>, line 1

decimal("definitely not an decimal")</code>

**string()**

Converts argument to a string

<code>Dip> string(3434343)
3434343</code>

**wait()**

Freezes the program for the number of seconds provided in the argument

<code>Dip> wait(3)
</code>

**open()**

Opens the website name given in the argument

<code>Dip> open("google.com")</code>

## Dip’s Standard Library

The standard library is a collection of custom functions written in Dip that gets automatically
loaded when you run the Dip interface.

**Loops in Dip**

There are two major types of loops in Dip, for loops and while loops.

**For Loops**

Each for loop begins with the word ‘for’ and then defines its range. This is done like this:

<code>Dip> for i = 0 to 5</code>

After this, using the then keyword, users can specify what needs to be done for each of these
values.

<code>Dip>  for i = 0 to 5 then print(i)</br>
0</br>
1</br>
2</br>
3</br>
45</code>


Note that only ‘i’ can be used as an iterable in for loops in Dip.

**While Loops**
<code>Dip>  variable x = 0</br>
0</br>
Dip>  while x < 5 then; print(x); variable x = x + 1 end</br>
0</br>
1</br>
2</br>
3</br>
4</code>


Note that a ‘;’ defines a new line
Note that while loops can use any variable as an iterable

**Recursion in Dip**

Here is an example of a recursive program in Dip - A function to calculate the factorial of a number

<code>
# factorial function

function factorial(term)

    variable fact = 1
    if term >= 1 then
        for i = 1 to term + 1 then
            variable fact = fact * i
        end
    end
    say(fact)
end
</code>

Another function in Dip - the famous Fibonacci function

<code>
# Fibonnaci Function

function fib(nterms)

    variable n1 = 0
    variable n2 = 1
    variable count = 0

    if nterms <= 0 then print("Input a positive integer")
    if nterms == 1 then
        print("Fibonnaci sequence upto" + " 1" + ":")
        print(n1)
    else
        print("Fibonacci sequence:")
        while count < nterms then
            print(n1)
            variable nth = n1 + n2
            variable n1 = n2
            variable n2 = nth
            variable count = count + 1
        end
    end
end
</code>

# Installation

Install Dip at dip-lang.org/install

