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
Created on Mon Feb  1 21:38:55 2021

@author: Jim Leon

@description:  Utilities for the Hamming.py program.  All of the underlying 
methods and business logic used in Hamming.py are defined in this file.
"""
import random
import math

def buildParityBitMatrix(NumBits):
    """
    Constructs the parity and data bit matrix based on the number of bits requested
    by the user.  This matrix is used throughout by other methods to construct 
    the other matrices used for error detection and correction.

    Parameters
    ----------
    NumBits : integer
        The number of data bits being transmitted in the message.

    Returns
    -------
    ParityBitMatrix : 2D array
        The parity/data bit matrix.

    """
    #First row of Matrix defines parity bits as 1, all else as 0
    #This row will be unused, except as a 
    #reference to which bits are parity bits and which not.
    ParityBitMatrix = []
    if NumBits <= 0:
        return ParityBitMatrix
    #Make the matrix roughly twice the size it needs to be, to handle potential
    #overflow/overrun.
    NumCols = 2*(math.floor(math.log2(NumBits)) + 2 + NumBits)
    NumRows = math.floor(math.log2(NumBits)) + 3
    p = 0
    Row = []
    for ColIndex in range(NumCols):
        if 2**p == ColIndex:
            Row.append(1)
            p = p + 1
        else:
            Row.append(0)
    ParityBitMatrix.append(Row)
    #Build remainder of Matrix.  Index 0 will always be 0 and is, again,
    #unused by future constructions.
    RowIndex = 1
    while RowIndex < NumRows:
        CurrRow = []
        Ticker = 2**(RowIndex-1)
        TickerLimit = -(2**(RowIndex-1))
        j = 0
        while j < NumCols:
            if j < Ticker:
                CurrRow.append(0)
            elif Ticker > 0:
                CurrRow.append(1)
                Ticker = Ticker - 1
            else:
                CurrRow.append(0)
                Ticker = Ticker - 1      
            if Ticker == TickerLimit:
                Ticker = 2**(RowIndex-1)
            j = j + 1
        ParityBitMatrix.append(CurrRow)
        RowIndex = RowIndex + 1
    return ParityBitMatrix

def calcSyndromeVec(Recvd):
    """
    Calculates the Syndrome vector - the vector that determines which bit in 
    the sent message has an error.

    Parameters
    ----------
    Recvd : 1D array (vector)
        The received message, as a string of 1s and 0s.

    Returns
    -------
    Syndrome : 1D array (vector)
        A vector describing the bit number that has an error.

    """
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

def correctErrorInMessage(Message, ErrorBit):
    """
    Given the bit number that is in error and the recieved message, correct (bit-flip) 
    the bit in error.

    Parameters
    ----------
    Message : 1D array (vector)
        The recieved message.
    ErrorBit : integer
        The bit number that is in error, starting at position 1.

    Returns
    -------
    None.

    """
    if ErrorBit == 0:
        return
    Message[ErrorBit-1] = Message[ErrorBit-1]^1
    
def decodeOriginalMessage(Message):
    """
    After error correction, decode the recieved Hamming 
    code to the original message.

    Parameters
    ----------
    Message : 1D array (vector)
        The error-corrected code.

    Returns
    -------
    OMessage : 1D array (vector)
        The decoded original message.

    """
    RMatrix = genRMatrix(len(Message))
    OMessage = []
    for i in range(len(RMatrix)):
        Sum = 0
        for j in range(len(Message)):
            Sum = Sum + RMatrix[i][j]*Message[j]
        OMessage.append(Sum)
    return OMessage

def genGMatrix(NumBits):
    """
    Generates the G-matrix used to construct the Hamming code from the original 
    message.

    Parameters
    ----------
    NumBits : integer
        The size (in number of bits) of the original message.

    Returns
    -------
    GMatrix : 2D array
        The G-matrix

    """
    PBitMatrix = buildParityBitMatrix(NumBits)
    GMatrix = []
    if len(PBitMatrix) == 0:
        return GMatrix
    PRow = 1
    Bit = 1
    IdMatrixCol = 0
    while IdMatrixCol < NumBits:
        PCol = 1
        Row = []
        if PBitMatrix[0][Bit] == 1:
            DataBitCount = 0
            while DataBitCount < NumBits:
                if PBitMatrix[0][PCol] == 1:
                    PCol = PCol + 1
                else:
                    Row.append(PBitMatrix[PRow][PCol])
                    DataBitCount = DataBitCount + 1
                    PCol = PCol + 1
            PRow = PRow + 1
        else:
            DataBitCount = 0
            while DataBitCount < NumBits:
                if IdMatrixCol == DataBitCount:
                    Row.append(1)
                else:
                    Row.append(0)
                DataBitCount = DataBitCount + 1
            
            IdMatrixCol = IdMatrixCol + 1
        
        Bit = Bit + 1
        GMatrix.append(Row)
    
    return GMatrix

def genHMatrix(NumBits):
    """
    Generates the H-matrix; also called the parity-check matrix.

    Parameters
    ----------
    NumBits : integer
        The size (in number of bits) of the original message.

    Returns
    -------
    HMatrix : 2D array
        The (parity-bit) H-matrix

    """
    PBitMatrix = buildParityBitMatrix(NumBits)
    HMatrix = []
    
    #Special case...
    if len(PBitMatrix) == 0:
        return HMatrix
    
    NumCols, NumRows = getHMatrixShape(PBitMatrix,NumBits)
    PRow = 1
    while PRow < (NumRows + 1):
        HRow = []
        PCol = 1
        while PCol < (NumCols + 1):
            HRow.append(PBitMatrix[PRow][PCol])
            PCol = PCol + 1 
        HMatrix.append(HRow)
        PRow = PRow + 1
    return HMatrix

def getHMatrixShape(PBitMatrix, DataBits):
    """
    Helper function that describes the shape (width and height) of the H-matrix, 
    based on the number of databits in the original message.

    Parameters
    ----------
    PBitMatrix : TYPE 2D array
        DESCRIPTION.  The table generated at the beginning of the program.
    DataBits : TYPE integer
        DESCRIPTION.  The number of data bits in the original message.

    Returns
    -------
    Width : integer
        The width of the new H-matrix.
    Height : integer
        The height of the new H-matrix.

    """
    Width = 0
    Height = 0
    Num = 0
    while( Num < DataBits):
        if(PBitMatrix[0][Width+1] == 0):
            Num = Num + 1
        else:
            Height = Height + 1
        Width = Width + 1
    return Width, Height

def genPossibleTransError(XMatrix):
    """
    Randomly generates an error in the sent (coded) message.  Its also possible 
    that it will NOT generate an error at all.

    Parameters
    ----------
    XMatrix : 2D array
        Technically just a vector, which represents the sent coded 
        message.

    Returns
    -------
    TransMessage : TYPE 2D array
        DESCRIPTION. The coded message with a (possible) error.

    """
    TransMessage = XMatrix.copy()
    BitFlip = random.randint(0,len(TransMessage)-1)
    TransMessage[BitFlip] = TransMessage[BitFlip] | 1
    return TransMessage

def genRandMessage(NumBits):
    """
    Based on user requested size, generates a random message - made up of 1s and 
    0s.

    Parameters
    ----------
    NumBits : integer
        The number of data bits in the message.

    Returns
    -------
    Message : 1D array (vector)
        The random message.

    """
    Message = []
    for i in range(NumBits):
        Message.append(random.randint(0,1))
    return Message

def genRMatrix(MessLength):
    """
    Generates the r-matrix (vector), which is the received message in the 
    transmission.

    Parameters
    ----------
    MessLength : integer
        The length of the recieved message.

    Returns
    -------
    RMatrix : 2D array
        The r-matrix (vector).

    """
    NumRows = MessLength - math.ceil(math.log2(MessLength))
    PBitMatrix = buildParityBitMatrix(NumRows)
    RMatrix = []
    IdBit = 1
    for i in range(NumRows):
        Row = []
        Bit = 1
        for j in range(MessLength):
            if PBitMatrix[0][j+1] == 1:
                Row.append(0)
            elif IdBit == Bit:
                Row.append(1)
                Bit = Bit + 1
            else:
                Row.append(0)
                Bit = Bit + 1
        IdBit = IdBit + 1
        RMatrix.append(Row)
    return RMatrix

def genXMatrix(Message):
    """
    The X-matrix, which results from multiplying the G-matrix and the original 
    message, p.

    Parameters
    ----------
    Message : 1D array (vector)
        The original message.

    Returns
    -------
    XMatrix : 2D array (vector)
        The X-matrix.

    """
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

def translateSynVec(SynVec):
    """
    Translates the syndrome vector into an index, representing the position 
    in the transmitted message where the bit error occurred.

    Parameters
    ----------
    SynVec : 1D array (vector)
        The syndrome vector.

    Returns
    -------
    ErrorBit : integer
        The position in the tranmistted message where the bit error occurred.

    """
    ErrorBit = 0
    for i in range(len(SynVec)):
        ErrorBit = ErrorBit + SynVec[i]*(2**i)
    return ErrorBit
    
    