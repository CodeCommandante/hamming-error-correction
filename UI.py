"""    
    Program simulating Hamming Error Code detection.
    Copyright (C) 2021  Jim Leon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:21:58 2021

@author: Jim Leon

@description: Contains all of the methods that handle user input and validation.
Also handles any output and print functionality for the program.
"""
def getUserInputAndValidate():
    """
    Gets user input, validates the input, and returns valid output.  If input is 
    invalid, will return 0.

    Returns
    -------
    NumBits: integer
        The size of the message to generate and send.

    """
    NumBits = input("Enter number of databits:  ")
    NumBits = int(NumBits)
    if (type(NumBits) != int) or (NumBits <= 0):
        print('That is not a valid number of bits!')
        return 0
    return NumBits

def printCorrectedMessage(Message):
    """
    Prints out the (error) corrected message.

    Parameters
    ----------
    Message : 1D array (vector)
        The message.

    Returns
    -------
    None.

    """
    PrintMessage = "["
    for i in range(len(Message)-1):
        PrintMessage = PrintMessage + str(Message[i]) + " "
    PrintMessage = PrintMessage + str(Message[len(Message)-1]) + "]"
    print("Corrected Message: ",PrintMessage)
    
def printDecodedMessage(Message):
    """
    Prints out the decoded message.

    Parameters
    ----------
    Message : 1D array (vector)
        The message.

    Returns
    -------
    None.

    """
    PrintMessage = "["
    for i in range(len(Message)-1):
        PrintMessage = PrintMessage + str(Message[i]) + " "
    PrintMessage = PrintMessage + str(Message[len(Message)-1]) + "]"
    print("Decoded Message  : ",PrintMessage)    

def printMessage(Message):
    """
    Prints the original message generated from the user input.

    Parameters
    ----------
    Message : 1D array (vector)
        The message.

    Returns
    -------
    None.

    """
    PrintMessage = "["
    for i in range(len(Message)-1):
        PrintMessage = PrintMessage + str(Message[i]) + " "
    PrintMessage = PrintMessage + str(Message[len(Message)-1]) + "]"
    print("Message          : ",PrintMessage)

def printParityCheck(SynVec):
    """
    Prints out the syndrome vector.

    Parameters
    ----------
    SynVec : 1D array (vector)
        The syndrome vector.

    Returns
    -------
    None.

    """
    PrintMessage = "["
    for i in range(len(SynVec)-1):
        PrintMessage = PrintMessage + str(SynVec[i]) + " "
    PrintMessage = PrintMessage + str(SynVec[len(SynVec)-1]) + "]"
    print("Parity Check     : ",PrintMessage)

def printRecievedMessage(ZMatrix):
    """
    Prints out the message recieved on the other side of the process.

    Parameters
    ----------
    ZMatrix : 1D array (vector)
        The z-matrix (recieved message)

    Returns
    -------
    None.

    """
    PrintMessage = "["
    for i in range(len(ZMatrix)-1):
        PrintMessage = PrintMessage + str(ZMatrix[i]) + " "
    PrintMessage = PrintMessage + str(ZMatrix[len(ZMatrix)-1]) + "]"
    print("Recieved Message : ",PrintMessage)

def printSendVector(XMatrix):
    """
    Prints out the coded message to send.

    Parameters
    ----------
    XMatrix : 1D array (vector)
        The x-matrix.

    Returns
    -------
    None.

    """
    PrintMessage = "["
    for i in range(len(XMatrix)-1):
        PrintMessage = PrintMessage + str(XMatrix[i]) + " "
    PrintMessage = PrintMessage + str(XMatrix[len(XMatrix)-1]) + "]"
    print("Send Vector      : ",PrintMessage)