# Dip

Dip is a dynamically typed interpreted programming language written in Python, which gives emphasis to readability and ease of use, while also providing the power of all of python’s libraries. Dip is aimed at beginners, looking to start with programming.

# Working with Dip

Dip gives you access to a development environment which comes bundled with Dip - The DDE, short for Dip Development Environment. It gathers inspiration from Python’s IDLE, and has a text editor for you to edit and create dip programs, and an interactive shell, where you can execute and see the output of your programs.

You can evaluate expressions by writing them after `Dip>`.

```dip
Dip> 1 + 2
3
Dip> 1 - 3
-2
Dip> 3 + 9
12
```

# Evaluating external files

It's possible to load external files written in Dip by calling the ‘run’ function inside the DDE interface by executing the run function followed by the relative path of the files that you want to be evaluated.

```dip
Dip Beta (Version 0.1)
Type in 'exit' to exit the shell
Dip> run("/Users/raghav/Desktop/hello_dip.dip")
Hello, Dip
0
```

# Dip basics

Most of Dip’s functions are either reminiscent of Python, or build off them, so people getting started with programming (or even Python programmers for that matter) won’t have any trouble understanding them. These basics are divided into three different categories, data types, builtin functions and the standard library.

## Dip’s Data Types

Dip contains 5 data types which you will generally interact with. These are Numbers, Strings, Lists, Functions and Errors.

### Numbers

Dip supports integers and decimals, called ints and floats in python. Note that anything following a ‘#’ on the same line is interpreted as a comment and not evaluated.

```dip
Dip Beta (Version 0.1)
Type in 'exit' to exit the shell

Dip> 10 / 2
5.0
Dip> 1 + 3
4
Dip> 34 * 34
1156
```

Note that in case of recurring decimals, they are left at 15 decimal places.

```dip
Dip> 100 / 6
16.666666666666668
```

Some functions you can perform on numbers are sin, cos, and tan. The pi constant is available.

```dip
Dip> sin(45)
0.8509035245341184
Dip> cos(45)
0.5253219888177297
Dip> tan(45)
1.6197751905438615
Dip> pi
3.141592653589793
```

### Strings

A string is a combination of zero or more characters contains inside double-quotes.

```dip
Dip> "Hello, Dip!"
Hello, Dip!
```

There are many things that you can do with strings, including adding them, iterating through them, and joining them.

```dip
Dip> join("Hello ", "Dip!")
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
!
```

### Lists

A list is a combination of values inside square braces, separated by commas.

```dip
Dip> ["l", "i", "s", "t"]
l, i, s, t
```

Lists can contain integers, strings, functions and even other lists.

```dip
Dip> [[1, 2], [3, 4], [5, 6]]
1, 2, 3, 4, 5, 6
```

There are many things that you can do with lists, including `join`, which joins two lists, `add`, which adds an element to a list, `remove`, which removes an element at an index from a list.

```dip
Dip> variable new_list = join([1, 2, 3], [4, 5, 6])
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
```

Note that the ‘remove’ function removes the element from the 4th index in this case, which is 5.

### Functions

Functions can be defined using the 'function' keyword, followed by the name of the function, and then its arguments in parenthesis. For a single line function, you can use `->` and then type what you want it to do. For a multi-line function, enter a new line and end the function with an end statement.

```dip
Dip> function add(a, b) -> print(a + b)
<function add>
Dip> add(4, 5)
9
```

```dip
function odd_or_even(number)
    if number % 2 == 0 then print("even") else print("odd")
end
```

Read more about functions in the builtin functions section!

### Errors

Errors are generated automatically when the user tries to evaluate invalid code. Dip contains 5 different error types, Illegal Character Error, Expected Character Error, Runtime Errors, Invalid Syntax Errors and Custom Errors. Custom errors can also be generated using the `error` function followed by a string inside parenthesis. The string will be the message of the error. Errors in the interpreter can help the user by providing insightful commentary.

#### Illegal Character Errors - Called when an illegal character is found

```dip
Dip> @
Illegal Character: '@'
File Dip Shell, line 1
@
^
```

#### Expected Character Errors - Called when a character is not found

```dip
Invalid Syntax / Character Not Found: Expected 'end'
File <Dip Shell>, line 1
function add(a, b); return a + b^
```

#### Runtime Errors - A range of errors that might be raised at runtime

```dip
Runtime Error: Illegal operation - check you are comparing two different data types (eg. integer and string)
File <Dip Shell>, line 1

1 - "1"
^^^^^^^
```

#### Invalid Syntax Errors - Called when the syntax is invalid

```dip
Invalid Syntax / Character Not Found: Expected int, float, identifier, '+', '-', '(', '[', if, for, while or function
File <Dip Shell>, line 1

5 === 5
       ^
```

#### Custom Errors - User Defined errors that can be called any time

```dip
Dip> error("test error")
Custom Error: test error
```

These errors can then be used like the built-in errors.

## Dip’s Built-in Functions

### What is a Builtin Function?

How do these functions actually work under the hood? In reality, they are nothing more than a function written in Python, that the interpreter calls when evaluating the symbol associated to it. That's how I inserted basic functionalities into the language like arithmetic operations and list manipulation, but it doesn't stop here, from very simple builtin operations you can write complex functions like the ones in the std library and expand the functionalities of the language without writing a single line of Python.

### Print

Prints text to the screen.

```dip
Dip> print("I am dip, an interpreted programming language")
I am dip, an interpreted programming language
```

### Say

Uses the Operating System’s ‘say’ command and says whatever is passed into it. Returns nothing.

```dip
Dip> say("hi!")
0
```

### Random Int

Selects a random integer from the range given to it.

```dip
Dip> random_int(0, 10)
10
Dip> random_int(0, 10)
9
Dip> random_int(0, 10)
0
```

### Root

Gets the square root of the number given to it.

```dip
Dip> root(4)
2.0
```

### Sin

Calculates the sine of a given number.

```dip
Dip> sin(45)
0.8509035245341184
```

### Cos

Calculates the cosine of a given number.

```dip
Dip> cos(45)
0.5253219888177297
```

### Tan

Calculates the tangent of a given number.

```dip
Dip> tan(45)
1.6197751905438615
```

### Input

Gets User Input.

```dip
Dip> input("User Input...")
ok
```

### Input_Integer

Gets User Input and ensures it is an integer.

```dip
Dip> input_integer("User Input...")
23
```

```dip
Dip> input_integer("User Input...")
Must be an integer, try again
Dip> input_integer("User Input...")
```

### is_number

Checks if the argument passed is a number.

```dip
Dip> is_number(34)
1
Dip> is_number("F")
0
```

### is_string

Checks if the argument passed is a string.

```dip
Dip> is_string("string")
1
Dip> is_string(34)
0
```

### is_list

Checks if the argument passed is a list.

```dip
Dip> is_list([3, 4, 5])
1
Dip> is_list(34)
0
```


### is_function

Checks if the argument passed is a function.

```dip
Dip> variable x = function add(a, b) -> a + b
<function add>
Dip> x
<function add>
Dip> is_function(x)
1
Dip> is_function("F")
0
Dip>
```

### add

Adds an element to a list.

```dip
Dip> variable lst = [0]
0
Dip> add(lst, 1)
0, 1
Dip> lst
0, 1
Dip>
```

### remove

Removes the element at index in a list.

```dip
Dip> remove(lst, 0)
0
Dip> lst
1
Dip>
```

### join

Joins two lists or strings.

```dip
Dip> join(lst, [2, 3])
1, 2, 3
Dip> join("hi", " there")
hi there
Dip>
```

### integer

Converts argument to an integer.

```dip
Dip> integer("4")
4
Dip> integer("definitely not an integer")

Runtime Error: ValueError: Invalid literal for integer() with base 10: 'definitely not an integer'
File <Dip Shell>, line 1

integer("definitely not an integer")
```

### decimal

Converts argument to a decimal.

```dip
Dip> decimal("34.3434")
34.3434
Dip> decimal("definitely not an decimal")

Runtime Error: ValueError: Could not convert string to decimal: 'definitely not an decimal'
File <Dip Shell>, line 1

decimal("definitely not an decimal")
```

### string

Converts argument to a string.

```dip
Dip> string(3434343)
3434343
```

### wait

Freezes the program for the number of seconds provided in the argument.

```dip
Dip> wait(3)
```

### open

Opens the website name given in the argument.

```dip
Dip> open("google.com")
```

## Dip’s Standard Library

The standard library is a collection of custom functions written in Dip that gets automatically loaded when you run the Dip interface.

### Loops in Dip

There are two major types of loops in Dip, for loops and while loops.

#### For Loops

Each for loop begins with the word ‘for’ and then defines its range. This is done like this:

```dip
Dip> for i = 0 to 5
```

After this, using the then keyword, users can specify what needs to be done for each of these values.

```dip
Dip>  for i = 0 to 5 then print(i)
0
1
2
3
45
```

Note that only ‘i’ can be used as an iterable in for loops in Dip.

#### While Loops

```dip
Dip>  variable x = 0
0
Dip>  while x < 5 then; print(x); variable x = x + 1 end
0
1
2
3
4
```

Note that a ‘;’ defines a new line. Note that while loops can use any variable as an iterable.

#### Recursion in Dip

Here is an example of a recursive program in Dip - A function to calculate the factorial of a number.

```dip
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
```

Another function in Dip - the famous Fibonacci function.

```dip
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
```

# Installation

Install Dip at <http://dip-lang.org/install>.

# Thanks!

Thanks to Robert Nystrom for his great book [Crafting Interpreters](https://craftinginterpreters.com/), [CodePulse](https://www.youtube.com/channel/UCUVahoidFA7F3Asfvamrm7w) for his video tutorials, and Daniel Holden for his book [Build your own lisp](http://www.buildyourownlisp.com/), all of which helped a lot in the making of Dip!
