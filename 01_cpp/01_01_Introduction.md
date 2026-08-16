# Modern C++ and the C++ Standard

- Early 1970s
    
    - C Programming Language
        
    - Dennis Ritchie
        
- 1979
    
    - Bjarne Stroustrup
        
    - C with Classes
        
- 1983
    
    - Name changed to C++
        
- 1989
    
    - First commercial release
        
- 1998
    
    - C++98 Standard
        
- 2003
    
    - C++03 Standard
        
- **2011**
    
    - **C++11 Standard**
        
- **2014**
    
    - **C++14 Standard**
        
- **2017**
    
    - **C++17 Standard**

# Modern C++ and the C++ Standard

- Classical C++
    
    - Pre C++11 Standard
        
- Modern C++
    
    - C++11
        
        - Lots of new features
            
    - C++14
        
        - Smaller changes
            
    - C++17
        
        - Simplification
            
    - Best practices
        
    - Core Guidelines

# How does it all work?

- You must tell the computer EXACTLY what to do
  - Program - like a recipe

- Programming language
  - source code
  - high-level
  - for humans

- Editor - used to enter program text
  - .cpp and .h files

- Binary or other low-level representation
  - object code
  - for computers

- Compiler - translates from high-level to low-level

- Linker - links together our code with other libraries
  - Creates executable program

- Testing and Debugging - finding and fixing program errors
![[Pasted image 20260816233346.png]]

# Integrated Development Environments (IDEs)
- Editor
- Compiler
- Linker
- Debugger
- Keep everything in sync
- CodeLite
- Code::Blocks
- NetBeans
- Eclipse
- CLion
- Dev-C++
- KDevelop
- Visual Studio
- Xcode

# Using the command-line interface
- A text editor (not a Word Processor)
- A command-prompt or terminal window
- An installed C++ compiler
- No need for an IDE
- Simple, efficient workflow
- Better as you gain experience
- Can be used if you are overwhelmed by IDEs
- Useful if hardware resources are limited

# Curriculum Overview
- Getting Started
- Structure of a C++ Program
- Variables and Constants
- Arrays and Vectors
- Strings in C++
- Expressions, Statements and Operators
- Statements and Operators
- Determining Control Flow
- Functions
- Pointers and References
- OOP – Classes and Objects
- Operator Overloading
- Inheritance
- Polymorphism
- Smart Pointers
- The Standard Template Library (STL)
- I/O Streams
- Exception Handling

# Curriculum Overview
## Challenge Exercises
- At the end of most course sections
- Develop real C++ programs using what we discussed in the section
- Section challenges
  - Description
  - Starting project
  - Completed solution
- Have fun and keep coding!
# Section Overview
## The Structure of a C++ Program
- Basic Components
- Preprocessor Directives
- The main function
- Namespaces
- Comments
- Basic I/O

## Preprocessor Directives
- What is a preprocessor?
- What does it do?
- Directives start with ‘#’
- Commands to the preprocessor
```cpp
#include <iostream>
#include “myfile.h”

#if
#elif
#else
#endif

#ifdef
#ifndef
#define
#undef

#line
#error
#pragma
```

## Namespaces
- Why `std::cout` and not just `cout`?
- What is a naming conflict?
- Names given to parts of code to help reduce naming conflicts
- `std` is the name for the C++ ‘standard’ namespace
- Third-party frameworks will have their own namespaces
- Scope resolution operator `::`
- How can we use these namespaces?
