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
Created on Mon Feb  1 21:40:30 2021

@author: Jim Leon

@description: Unit test suite for the Hamming.py program.
"""
import unittest
import numpy as np
import Utilities as utils

class TestParityBitMatrixMethod(unittest.TestCase):
    
    def test_buildParityBitMatrix_neg(self):
        PBitM_neg = []
        PBitMatrix = utils.buildParityBitMatrix(-7)
        self.assertTrue(np.array_equal(PBitM_neg,PBitMatrix))
    
    def test_buildParityBitMatrix_0(self):
        PBitM_0 = []
        PBitMatrix = utils.buildParityBitMatrix(0)
        self.assertTrue(np.array_equal(PBitM_0,PBitMatrix))
        
    def test_buildParityBitMatrix_4(self):
        PBitM_4 =   [(0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0),
                     (0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1),
                     (0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1),
                     (0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1),
                     (0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1)]
        PBitMatrix = utils.buildParityBitMatrix(4)
        self.assertTrue(np.array_equal(PBitM_4,PBitMatrix))
        
    def test_buildParityBitMatrix_1(self):
        PBitM_1 = [(0,1,1,0,1,0),
                   (0,1,0,1,0,1),
                   (0,0,1,1,0,0)]
        PBitMatrix = utils.buildParityBitMatrix(1)
        self.assertTrue(np.array_equal(PBitM_1,PBitMatrix))
    
class TestGMatrixMethod(unittest.TestCase):
    def test_genGMatrix_neg(self):
        GMat_neg = []
        GMatrix = utils.genGMatrix(-7)
        self.assertTrue(np.array_equal(GMatrix,GMat_neg))
        
    def test_genGMatrix_0(self):
        GMat_0 = []
        GMatrix = utils.genGMatrix(0)
        self.assertTrue(np.array_equal(GMatrix,GMat_0)) 
    
    def test_genGMatrix_4(self):
        GMat_4 = [(1,1,0,1),
                  (1,0,1,1),
                  (1,0,0,0),
                  (0,1,1,1),
                  (0,1,0,0),
                  (0,0,1,0),
                  (0,0,0,1)]
        GMatrix = utils.genGMatrix(4)
        self.assertTrue(np.array_equal(GMatrix,GMat_4))
    
    def test_genGMatrix_1(self):
        GMat_1 = [[1],
                  [1],
                  [1]]
        GMatrix = utils.genGMatrix(1)
        self.assertTrue(np.array_equal(GMatrix,GMat_1))
        
    def test_genGMatrix_7(self):
        GMat_7 = [(1,1,0,1,1,0,1),
                  (1,0,1,1,0,1,1),
                  (1,0,0,0,0,0,0),
                  (0,1,1,1,0,0,0),
                  (0,1,0,0,0,0,0),
                  (0,0,1,0,0,0,0),
                  (0,0,0,1,0,0,0),
                  (0,0,0,0,1,1,1),
                  (0,0,0,0,1,0,0),
                  (0,0,0,0,0,1,0),
                  (0,0,0,0,0,0,1)]
        GMatrix = utils.genGMatrix(7)
        self.assertTrue(np.array_equal(GMatrix,GMat_7))
    
class TestHMatrixMethod(unittest.TestCase):
    
    def test_genHMatrix_4(self):                           
        HMat_4 = [(1,0,1,0,1,0,1),
                  (0,1,1,0,0,1,1),
                  (0,0,0,1,1,1,1)]
        HMatrix = utils.genHMatrix(4)                  
        self.assertTrue(np.array_equal(HMatrix,HMat_4))
        
    def test_genHMatrix_1(self):
        HMat_1 = [(1,0,1),
                  (0,1,1)]
        HMatrix = utils.genHMatrix(1)
        self.assertTrue(np.array_equal(HMatrix,HMat_1))
        
    def test_genHMatrix_5(self):
        HMat_5 = [(1,0,1,0,1,0,1,0,1),
                  (0,1,1,0,0,1,1,0,0),
                  (0,0,0,1,1,1,1,0,0),
                  (0,0,0,0,0,0,0,1,1)]
        HMatrix = utils.genHMatrix(5)
        self.assertTrue(np.array_equal(HMatrix,HMat_5))
        
    def test_genHMatrix_7(self):
        HMat_7 = [(1,0,1,0,1,0,1,0,1,0,1),
                  (0,1,1,0,0,1,1,0,0,1,1),
                  (0,0,0,1,1,1,1,0,0,0,0),
                  (0,0,0,0,0,0,0,1,1,1,1)]
        HMatrix = utils.genHMatrix(7)
        self.assertTrue(np.array_equal(HMatrix,HMat_7))
        
class TestGenRandomMessageMethod(unittest.TestCase): 
    def test_genRandMessage_neg(self):
        Message = utils.genRandMessage(-7)
        self.assertEqual(0,len(Message))
        
    def test_genRandMessage_0(self):
        Message = utils.genRandMessage(0)
        self.assertEqual(0,len(Message))
        
    def test_genRandMessage_1(self):
        Message = utils.genRandMessage(1)
        self.assertEqual(1,len(Message))
        
    def test_genRandMessage_10(self):
        Message = utils.genRandMessage(10)
        self.assertEqual(10,len(Message))
    
    def test_genRandMessage_20(self):
        Message = utils.genRandMessage(20)
        self.assertEqual(20,len(Message))
        
class TestGenXMethod(unittest.TestCase):
    def test_genX_4(self):
        Message = [1,0,1,1]
        XMat_4 = [0,1,1,0,0,1,1]
        XMatrix = utils.genXMatrix(Message)
        self.assertTrue(np.array_equal(XMatrix,XMat_4))
        
class TestCalcSyndromeVec(unittest.TestCase):
    def test_calcSyndromeVec(self):
        RMessage = [0,1,1,0,0,1,1]
        Act_Syn = [0,0,0]
        Syndrome = utils.calcSyndromeVec(RMessage)
        self.assertTrue(np.array_equal(Syndrome,Act_Syn))
        
class TestGetHMatrixShape(unittest.TestCase):
    def test_getHMatrixShape_1(self):
        PBitMat = utils.buildParityBitMatrix(1)
        Width, Height = utils.getHMatrixShape(PBitMat, 1)
        self.assertEqual(Width,3)
        self.assertEqual(Height,2)
        
    def test_getHMatrixShape_2(self):
        PBitMat = utils.buildParityBitMatrix(2)
        Width, Height = utils.getHMatrixShape(PBitMat, 2)
        self.assertEqual(Width,5)
        self.assertEqual(Height,3)
        
    def test_getHMatrixShape_4(self):
        PBitMat = utils.buildParityBitMatrix(4)
        Width, Height = utils.getHMatrixShape(PBitMat, 4)
        self.assertEqual(Width,7)
        self.assertEqual(Height,3)
    
    def test_getHMatrixShape_7(self):
        PBitMat = utils.buildParityBitMatrix(7)
        Width, Height = utils.getHMatrixShape(PBitMat, 7)
        self.assertEqual(Width,11)
        self.assertEqual(Height,4)
        
    def test_getHMatrixShape_11(self):
        PBitMat = utils.buildParityBitMatrix(11)
        Width, Height = utils.getHMatrixShape(PBitMat,11)
        self.assertEqual(Width,15)
        self.assertEqual(Height,4)

class TestTranslateSynVec(unittest.TestCase):
    def test_translateSynVec_0(self):
        SynVec_0 = [0,0,0,0,0]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,0)
        
    def test_translateSynVec_1(self):
        SynVec_0 = [1,0,0,0,0]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,1)
        
    def test_translateSynVec_2(self):
        SynVec_0 = [0,1,0,0,0]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,2)
        
    def test_translateSynVec_3(self):
        SynVec_0 = [1,1,0,0,0]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,3)
        
    def test_translateSynVec_5(self):
        SynVec_0 = [1,0,1,0,0]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,5)
        
    def test_translateSynVec_12(self):
        SynVec_0 = [0,0,1,1,0]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,12)
        
    def test_translateSynVec_25(self):
        SynVec_0 = [1,0,0,1,1]
        ErrorBit = utils.translateSynVec(SynVec_0)
        self.assertEqual(ErrorBit,25)
        
class TestCorrectErrorInMessage(unittest.TestCase):
    def test_correctErrorInMess(self):
        SendMssg = [1,0,1,0,1]
        ErrorBit = 3
        CorrMssg = [1,0,0,0,1]
        utils.correctErrorInMessage(SendMssg,ErrorBit)
        self.assertTrue(np.array_equal(CorrMssg,SendMssg))
        
class TestGenRMatrix(unittest.TestCase):
    def test_genRMatrix_3(self):
        RMat_3 = [(0,0,1)]
        RMatrix = utils.genRMatrix(3)
        self.assertTrue(np.array_equal(RMat_3,RMatrix))
        
    def test_genRMatrix_5(self):
        RMat_5 = [(0,0,1,0,0),
                  (0,0,0,0,1)]
        RMatrix = utils.genRMatrix(5)
        self.assertTrue(np.array_equal(RMat_5,RMatrix))
        
    def test_genRMatrix_7(self):
        RMat_7 = [(0,0,1,0,0,0,0),
                  (0,0,0,0,1,0,0),
                  (0,0,0,0,0,1,0),
                  (0,0,0,0,0,0,1)]
        RMatrix = utils.genRMatrix(7)
        self.assertTrue(np.array_equal(RMat_7,RMatrix))
        
    def test_genRMatrix_11(self):
        RMat_11 = [(0,0,1,0,0,0,0,0,0,0,0),
                  (0,0,0,0,1,0,0,0,0,0,0),
                  (0,0,0,0,0,1,0,0,0,0,0),
                  (0,0,0,0,0,0,1,0,0,0,0),
                  (0,0,0,0,0,0,0,0,1,0,0),
                  (0,0,0,0,0,0,0,0,0,1,0),
                  (0,0,0,0,0,0,0,0,0,0,1)]
        RMatrix = utils.genRMatrix(11)
        self.assertTrue(np.array_equal(RMat_11,RMatrix))
        
class TestDecodeOriginalMessage(unittest.TestCase):
    def test_decodeOriginalMessage_1(self):
        OMessage = [1]
        SendMessage = utils.genXMatrix(OMessage)
        SendVec = utils.genPossibleTransError(SendMessage)
        SynVec = utils.calcSyndromeVec(SendVec)
        ErrorBit = utils.translateSynVec(SynVec)
        utils.correctErrorInMessage(SendVec,ErrorBit)
        RMessage = utils.decodeOriginalMessage(SendVec)
        self.assertTrue(np.array_equal(OMessage,RMessage))
        
    def test_decodeOriginalMessage_3(self):
        OMessage = [1,0,0,1,1,0]
        SendMessage = utils.genXMatrix(OMessage)
        SendVec = utils.genPossibleTransError(SendMessage)
        SynVec = utils.calcSyndromeVec(SendVec)
        ErrorBit = utils.translateSynVec(SynVec)
        utils.correctErrorInMessage(SendVec,ErrorBit)
        RMessage = utils.decodeOriginalMessage(SendVec)
        self.assertTrue(np.array_equal(OMessage,RMessage))
        
    def test_decodeOriginalMessage_7(self):
        OMessage = [1,0,0,1,0,1,1,1,0,0,0]
        SendMessage = utils.genXMatrix(OMessage)
        SendVec = utils.genPossibleTransError(SendMessage)
        SynVec = utils.calcSyndromeVec(SendVec)
        ErrorBit = utils.translateSynVec(SynVec)
        utils.correctErrorInMessage(SendVec,ErrorBit)
        RMessage = utils.decodeOriginalMessage(SendVec)
        self.assertTrue(np.array_equal(OMessage,RMessage))
        
        
if __name__ == '__main__':
    unittest.main()