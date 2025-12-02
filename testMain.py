import unittest
import mainToTest # Module to test

import ctypes

cLibrary = ctypes.CDLL("./PointerExercise.dll")

#cLibrary = ctypes.CDLL("./PointerExercise.a") - Error  [WinError 193] %1 is not a valid Win32 application

class TESTMAIN(unittest.TestCase):  # class which calls module functions with different inputs
    def setUp(self): # Test related init functions like constructor.
        test_main_start  = False
        test_main_second = False
        
    
    def test_mainToTest_fgetVar(self):
       '''TEST VALUE NEGATIVE'''
       test_main_start = True
       test_input = -160
       result = mainToTest.mainToTest_fgetVar(test_input)
       #print("Result of 1st Test {0}",result)
       self.assertEqual(result,-10.0)

    def test_mainToTest_fgetSecond(self):
        '''TEST VALUE POSITIVE'''
        test_input = 16        
        test_main_second = True
        result = mainToTest.mainToTest_fgetVar(test_input)
        #print("Result of 2nd Test {0}",result)
        self.assertEqual(result,1)

    def test_mainToTest_fgetThird(self):
        '''TEST VALUE None '''
        test_input = None
        result = mainToTest.mainToTest_fgetVar(test_input)
        #print("Result of 3rd Test {0}",result)
        self.assertEqual(result,"WrongType")

    def tearDown(self):  # method to reset the test vars at the end
        test_main_start  = False
        test_main_second = False



if __name__ == '__main__':
    unittest.main()
    #print(cLibrary.main())