from io import StringIO
import unittest
import sys
sys.path.insert(0, '../')

from LogoManager import LogoManager as lm

class TestLogoManager(unittest.TestCase):

  def test_version(self):
      x = "VERSION NONE"
      capturedOutput = StringIO()
      sys.stdout = capturedOutput
      lm.printVersion(x)           
      sys.stdout = sys.__stdout__        
      self.assertEqual(capturedOutput.getvalue().rstrip(), x)

if __name__ == '__main__':
    unittest.main()