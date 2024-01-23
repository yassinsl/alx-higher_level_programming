# Import & Modules

This project contains some tasks for learning about imports and modules in **Python**.

## Tasks To Complete

+ [x] 0\. Import a simple function from a simple file <br/>_**[0-add.py](0-add.py)**_  imports the function `def add(a, b):` from the file [add_0.py](add_0.py) and prints the result of the addition `1 + 2 = 3`.
+ [x] 1\. My first toolbox! <br/>_**[1-calculation.py](1-calculation.py)**_ imports functions from the file [calculator_1.py](calculator_1.py), does some Maths, and prints the result.
+ [x] 2\. How to make a script dynamic! <br/>_**[2-args.py](2-args.py)**_ prints the number of and the list of its arguments.
+ [x] 3\. Infinite addition <br/>_**[3-infinite_add.py](3-infinite_add.py)**_ prints the result of the addition of all arguments.
+ [x] 4\. Who are you? <br/>_**[4-hidden_discovery.py](4-hidden_discovery.py)**_ prints all the names defined by the compiled module [hidden_4.pyc](hidden_4.pyc) (compatible with Python 3.8.x).
+ [x] 5\. Everything can be imported <br/>_**[5-variable_load.py](5-variable_load.py)**_ imports the variable `a` from the file [variable_load_5.py](variable_load_5.py) and prints its value.
+ [x] 6\. Build my own calculator! <br/>_**[100-my_calculator.py](100-my_calculator.py)**_ imports all functions from the file [calculator_1.py](calculator_1.py) and handles basic operations.
+ [x] 7\. Easy print <br/>_**[101-easy_print.py](101-easy_print.py)**_ prints `#pythoniscool`, followed by a new line, in the standard output.
+ [x] 8\. ByteCode -> Python #3 <br/>_**[102-magic_calculation.py](102-magic_calculation.py)**_ contains a Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
  ```c
    3           0 LOAD_CONST               1 (0)
                3 LOAD_CONST               2 (('add', 'sub'))
                6 IMPORT_NAME              0 (magic_calculation_102)
                9 IMPORT_FROM              1 (add)
               12 STORE_FAST               2 (add)
               15 IMPORT_FROM              2 (sub)
               18 STORE_FAST               3 (sub)
               21 POP_TOP

    4          22 LOAD_FAST                0 (a)
               25 LOAD_FAST                1 (b)
               28 COMPARE_OP               0 (<)
               31 POP_JUMP_IF_FALSE       94

    5          34 LOAD_FAST                2 (add)
               37 LOAD_FAST                0 (a)
               40 LOAD_FAST                1 (b)
               43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               46 STORE_FAST               4 (c)

    6          49 SETUP_LOOP              38 (to 90)
               52 LOAD_GLOBAL              3 (range)
               55 LOAD_CONST               3 (4)
               58 LOAD_CONST               4 (6)
               61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               64 GET_ITER
          >>   65 FOR_ITER                21 (to 89)
               68 STORE_FAST               5 (i)

    7          71 LOAD_FAST                2 (add)
               74 LOAD_FAST                4 (c)
               77 LOAD_FAST                5 (i)
               80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
               83 STORE_FAST               4 (c)
               86 JUMP_ABSOLUTE           65
          >>   89 POP_BLOCK

    8     >>   90 LOAD_FAST                4 (c)
               93 RETURN_VALUE

   10     >>   94 LOAD_FAST                3 (sub)
               97 LOAD_FAST                0 (a)
              100 LOAD_FAST                1 (b)
              103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
              106 RETURN_VALUE
              107 LOAD_CONST               0 (None)
              110 RETURN_VALUE
  ```
+ [x] 9\. Fast alphabet <br/>_**[103-fast_alphabet.py](103-fast_alphabet.py)**_ prints the alphabet in uppercase, followed by a new line.
