# Scheme4101 Interpreter

Scheme4101 is a Scheme interpreter implemented in Python. This interpreter provides functionality to process Scheme code, breaking it down into tokens, parsing these tokens to form an abstract syntax tree (AST), and then evaluating this tree according to the semantics of the Scheme language.

## Run the project

To run the interpreter, execute:

```
python3 Scheme4101.py
```


For debugging purposes, especially related to the Scanner, use:

```
python3 Scheme4101.py -d
```


## Features

### Core Functionalities:

+ __Tokenization:__ The interpreter can break down raw Scheme input into individual tokens, distinguishing between numbers, identifiers, special characters, and other lexical elements.
  
+ __Parsing:__ Based on a defined grammar, the interpreter constructs an abstract syntax tree (AST) that represents the structure and semantics of the input Scheme code.

+ __Evaluation:__ The interpreter can evaluate the constructed AST according to the semantics of the Scheme language. This includes performing arithmetic operations, function calls, and evaluating special forms.

+ __Environment Management:__ Variables and functions in Scheme can be defined, updated, and looked up. The interpreter manages an environment to handle these bindings.


### Special Forms Handling:

+ __Define:__ Users can define new variables or functions.
+ __Lambda:__ Supports the creation of anonymous functions.
+ __Quote:__ Allows users to quote expressions, preventing their evaluation.
+ __Built-in Functions:__ The interpreter supports several built-in functions of Scheme, providing native functionalities without requiring external definitions.
  

### Advanced Features:

+ __Closures:__ The interpreter can create and manage closures, allowing for functionalities like higher-order functions and maintaining local state within functions.
  
+ __Error Handling:__ While not explicitly mentioned in the provided code snippets, a robust interpreter typically has mechanisms to handle syntactic and semantic errors, providing meaningful feedback to the user.
  
### Output and Debugging:

+ __Structured Output:__ The interpreter can print the evaluated output in a structured and readable format, making it user-friendly.
  
+ __Debugging Mode:__ A debugging mode is available to get insights into the tokenization process, which can be invaluable for understanding how the interpreter processes input.

### Initialization and Bootstrapping:

+ __Initialization File:__ The interpreter uses an initialization file (ini.scm) to preload certain definitions, ensuring that built-in functions and other essential elements are available right from the start making it easier to develop the interpreter.

## Project Notes

Followed the suggestion to split implementation of BuiltIn.appy method into three separate methods: apply method with no parameter, apply method with a single parameter, and apply method with two parameters. Also implemented helper methods for checking the Node types and arithmetic operations.

For the `display` function, the project used `redirect_stdout` from the  `contextlib` library to capture the stdout buffer before it is flushed to the terminal and used regular expression to remove the double quotes from the string.

Also implemented the Unspecific Node type and the Void Node type to print `#{Unspecific}` and `nothing` respectively as suggested.


## Main Components and Functionalities

### Parsing and Lexical Analysis

+ __Parser (Parse/Parser.py):__  
This module is responsible for reading Scheme input and breaking it down according to a set grammar defined using BNF notation.

+ __Scanner (Parse/Scanner.py):__  
The Scanner is used to read the Scheme input character by character. It identifies different lexical elements like numbers, identifiers, and special characters.


### Tokenization

+ __Token (Tokens/Token.py):__  
Each instance of this class represents a token identified by the Scanner.

+ __TokenType (Tokens/TokenType.py):__  
This module defines an enumeration of all possible token types that the Scanner can identify.

### Abstract Syntax Tree (AST)

+ __Node (Tree/Node.py):__  
This is a generic class that represents a node in the AST.

+ __TreeBuilder (Tree/TreeBuilder.py):__  
This module provides functionality to construct specific types of nodes for the AST.

+ __Environment (Tree/Environment.py):__  
In Scheme, variables can be bound to values. The Environment module provides functionality to manage these bindings.

+ __BuiltIn (Tree/BuiltIn.py):__  
Scheme has several built-in functions. This module is responsible for representing these functions within the interpreter.


### Special Forms

+ __Special (Special/Special.py):__  
Base class for all special forms in Scheme.

+ __Define (Special/Define.py):__  
This module is specifically for the define special form in Scheme.

+ __Lambda (Special/Lambda.py):__  
The lambda special form in Scheme is used to create anonymous functions.

+ __Quote (Special/Quote.py):__  
The quote special form in Scheme is used to prevent evaluation of an expression.

### Printing Mechanism

+ __Printer (Print/Printer.py):__  
The Printer module provides methods to print the AST, taking care of formatting details like indentation and line breaks.
