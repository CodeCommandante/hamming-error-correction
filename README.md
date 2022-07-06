# Hamming Code Error Correction
***
## Description of the Program
---
For this program, we are tasked with writing a program which will perform error
correction on a transmitted (binary) message.  The basic sequence the program
follows is:
* Ask the user to enter length of the binary message (greater than length 1).
* Generate a random binary-coded message of that length.
* Create an encoded message using the Hamming method.
* Simulate sending the encoded message over a wire and generate an error in the sent message.
* Use the Hamming error-correction method to detect if the recieved message has an error and correct it.
* Decode the Hamming encoded message to the original message generated in step 2.

The Hamming method uses basic linear algebra principles to perform the encoding,
error-correction, and decoding.  At the outset, the program generates a table which
marks bit positions as either parity-bits or data-bits, and uses this table to
derive the Hamming matrices, *G*, *H*, and *R*.  From these matrices, the
various vectors *x*, and *z* can also be derived.

## Algorithms and Libraries
---
### Algorithms
To begin, we must take in user input.  The following algorithm handled the user
input:
```
def getUserInputAndValidate():
    NumBits = input("Enter number of databits:  ")
    NumBits = int(NumBits)
    if (type(NumBits) != int) or (NumBits <= 0):
        print('That is not a valid number of bits!')
        return 0
    return NumBit
```
Next, the randomly generated message of _NumBit_ length is created.
```
def genRandMessage(NumBits):
    Message = []
    for i in range(NumBits):
        Message.append(random.randint(0,1))
    return Message
```
After this, the Hamming encoding needs to take place.  This is done by
matrix-multiplying the G-Matrix by the newly generated message.  _NOTE:
See included program files for detailed
implementation on the G, H, and, R Hamming matrices.  For brevity, I will exclude listing the
code for them in this report._
```
def genXMatrix(Message):
    XMatrix = []
    GMatrix = genGMatrix(len(Message))
    for i in range(len(GMatrix)):
        Sum = 0
        for j in range(len(Message)):
            Mult = GMatrix[i][j]*Message[j]
            Sum = Sum + Mult
        Sum = Sum % 2
        XMatrix.append(Sum)    
    return XMatrix
```
The new encoded message is then "sent over a wire".  During this process, we
want to simulate the possibility of an error occurring during transmission.
This is done by "flipping" one of the bits in the encoded message at random.
For my implementation, I also leave the possibility of no error occurring at
all.

```
def genPossibleTransError(XMatrix):
    TransMessage = XMatrix.copy()
    BitFlip = random.randint(0,len(TransMessage)-1)
    TransMessage[BitFlip] = TransMessage[BitFlip] | 1
    return TransMessage
```

At this stage, we assume the message has been recieved by the reciever.  The
reciever would then multiply the Hamming matrix, *H*, by the recieved message.
This would give the reciever the _syndrome vector_, telling them if there
was indeed an error in the message.  The _syndrome vector_ is a binary
number that indicates what bit, *i, i > 0*, is incorrect.

```
def calcSyndromeVec(Recvd):
    Syndrome = []
    #Calculate the size of the original message, generate H
    NumBits = len(Recvd) - math.ceil(math.log2(len(Recvd)))
    HMatrix = genHMatrix(NumBits)
    for i in range(len(HMatrix)):
        Sum = 0
        for j in range(len(Recvd)):
            Mult = HMatrix[i][j]*Recvd[j]
            Sum = Sum + Mult
        Sum = Sum % 2
        Syndrome.append(Sum)  
    return Syndrome
```

With the _syndrome vector_ calculated, the reciever can then correct the
message.  If the _syndrome vector_ was 0, there was no error found.

```
def correctErrorInMessage(Message, ErrorBit):
    if ErrorBit == 0:
        return
    Message[ErrorBit-1] = Message[ErrorBit-1]^1
```

Finally, the encoded message would be decoded.  This is done by matrix
multiplying the recieved (error-corrected) message by the Hamming matrix, *R*.

```
def decodeOriginalMessage(Message):
    RMatrix = genRMatrix(len(Message))
    OMessage = []
    for i in range(len(RMatrix)):
        Sum = 0
        for j in range(len(Message)):
            Sum = Sum + RMatrix[i][j]*Message[j]
        OMessage.append(Sum)
    return OMessage
```

### Libraries
For this program, I was able to perform all calculations and transformations
using only the *math* and *random* libraries in Python.  My suite of unit tests
uses the *unittest* library.

## Functions and Program Structure
---
The program has three files:
* Hamming.py
* Utilities.py
* UI.py

### Hamming.py
_Hamming.py_ contains one function, _Hamming()_, which acts as a
standard _main()_ program block.  This function executes the sequence of
statements which carries out the basic input/output operations of the program.

### Utilities.py
_Utilities.py_ contains all of the heavy-lifting functions for the
program, such as constructing the Hamming matrices, and carrying out the
algorithms/functions shown in the previous section.  Below is a list of the
remaining functions in _Utilities.py_ and a brief description of what
they do.

`buildParityBitMatrix(NumBits)`

This function builds the Hamming table, which enumerates which bits are
considered the _data bits_ and which are considered the _parity
bits_.  This table (matrix) is used to construct the Hamming *G*, *H*, and *R*
matrices.

`genGMatrix(NumBits)`
`genHMatrix(NumBits)`
`genRMatrix(NumBits)`
`getHMatrixShape(PBitMatrix, DataBits)`

The first three functions here generate the *G*, *H*, and *R* Hamming matrices,
respectively.  The fourth function is merely a helper function for
_genHMatrix_.

`translateSynVec(SynVec)`

This is a helper function which translates the binary _syndrome vector_
string into it's base 10 representation.

### UI.py
_UI.py_ - short for _U_ser _I_nterface - handles all of the
input and visual output operations.  One of it's functions,
_getUserInputAndValidate()_ was already given in the previous section.
Here are the remaining functions:

`printCorrectedMessage(Message)`
`printDecodedMessage(Message)`
`printMessage(Message)`
`printParityCheck(SynVec)`
`printRecievedMessage(ZMatrix)`
`printSendVector(XMatrix)`

The names of the functions should speak for themselves, as they are merely print
functions.  Each of these correspond to the printed messages that are displayed
after the user has entered the length of the message they would like to send.
Here is how they would correspond to a typical run of the program:

```
>>> Hamming()
Enter number of databits:  8                    #getUserInputAndValidate()
Message          : [0 0 1 1 1 0 1 0]            #printMessage()
Send Vector      : [1 1 0 0 0 1 1 0 1 0 1 0]    #printSendVector()
Received Message : [1 1 0 0 0 1 1 0 1 0 0 0]    #printRecievedMessage()
Parity Check     : [1 1 0 1]                    #printParityCheck()
Corrected Message: [1 1 0 0 0 1 1 0 1 0 1 0]    #printCorrectedMessage()
Decoded Message  : [0 0 1 1 1 0 1 0]            #printDecodedMessage()
```

## Testing and Running the Program
---
### Testing
I have included a suite of unit tests, which can be run by running the file
_Unit\_Tests.py_.  There are 40 tests total that are run on the code.
This program was developed using TDD principles and should cover cases of
invalid user input and such.  If you discover bugs in the program, please let me
know right away.

To get a more descriptive enumeration of the tests, you can run the
_Unit\_Tests.py_ file with the _-v_ flag, like so:
```
>>> Unit_Tests.py -v
```

### Running the Program
The program can be run by simply executing the _Hamming.py_ file.  The
program was written using the Spyder 4 IDE, with Python 3.8, on a Linux Ubuntu
20.04 kernel.  Any machine that has Python 3.8 libraries and code-base installed
should be able to run this program (and the unit tests) with no issues.


