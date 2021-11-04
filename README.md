# Calculator App

## Description

A calculator program designed to accept two numerical inputs and perform basic mathematical operations, namely addition, subtraction, multiplication and division in the command-line interface. It also allows the user the option to change their inputs before or after performing any mathematical operations. 

## Getting started

### Prerequisites

Please ensure you have Git and Python installed in your local machine before running the program.

### Running the Program

To run the program, open your command line and please run the following command: 

```
git clone https://github.com/maziasy/calculator.git 
```

Check out to the 'calculator' directory, and then run the following command to get the program running: 
```
python main.py
```

### Running Unit Tests

While staying in the calculator directory, please run the following command to execute unit tests: 

```
python calculator_tests.py
```

### Possible Improvements 

I had some ideas for improvements and additional toughts as I tested the program that I thought were worth mentioning and, if I had spent more than 2 hours on this program, I may have implemented.

- Firstly, I would write the driver function and helper functions as methods for a class, so the overall program is more aligned with object-oriented programming. This would be a quick change, and really a matter of preference as well.  
- Secondly, there is definitely room to write more unit tests for the helper functions in main.py that verified their outputs for given inputs, which I would have definitely written with more time. 
- Thirdly, at this time I only handled the possibility where the input is too large a number. I could potentially also handle the possibility that the resulting number is too large as well, but I think that depends on how we want the calculator to operate. It currently simply returns inf (i.e. infinity) and not necessarily an error. 
