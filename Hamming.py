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
Created on Sun Jan 31 15:36:48 2021

@author: Jim Leon

@description: Error detection and correction simulator.  Used to demonstrate
the Hamming parity check method.
"""
import Utilities as utils
import UI as ui

def Hamming():
    """The main method called to run the program."""
    NumBits = ui.getUserInputAndValidate()
    if NumBits == 0:
        return -1
    
    Message = utils.genRandMessage(NumBits)
    ui.printMessage(Message)
    SendMessage = utils.genXMatrix(Message)
    ui.printSendVector(SendMessage)
    SendVec = utils.genPossibleTransError(SendMessage)
    ui.printRecievedMessage(SendVec)
    SynVec = utils.calcSyndromeVec(SendVec)
    ui.printParityCheck(SynVec)
    ErrorBit = utils.translateSynVec(SynVec)
    utils.correctErrorInMessage(SendVec,ErrorBit)
    ui.printCorrectedMessage(SendVec)
    Decoded = utils.decodeOriginalMessage(SendVec)
    ui.printDecodedMessage(Decoded)
    
    return 0

Hamming()