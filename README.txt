This is not supposed to be an in-depth calculator, just a simple calculator.

It can run addition, subtraction, multiplication, and division.

First, it asks for which operation the user intends on performing or if the user wants to close the calculator. It takes a string as an input and accepts:

add, addition, plus
sub, substract, subtraction, minus
times, multiply, multiplication
divide, division
quit, cancel

If it does not read anyone of those inputs, then it asks for an operation again. If it gets a string that applies to any of the cateogories, then it assigns
the operation variable either "add", "subtract", "multiply", or "divide" depending on the input, and moves on. If it is told to "quit" or "cancel", it will close.

Second, it asks for the first value of the math problem. If it does not get a float value, then it asks again for the first number and reminds the user to only
use numbers and decimal points for the prompt. The calculator then asks for the second value with a similar process.

Finally, the calculator goes back to the operation variable and decides which operation needs to be done based on the string. If it, for some reason, does not recongize the
assigned string to the variable, the calculator will restart the process by asking for an operation. Otherwise, it'll take the first and second number then perform the operation. 
Afterwards, it displays the answer and starts the sequence again.