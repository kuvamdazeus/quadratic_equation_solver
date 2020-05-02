from equation import extract_coef
import unittest
sample_equations = ["+1*x^2+0*x+36", "+34*x^2-67*x+0", "+1*x^-65*x-76"]

class Test(unittest.TestCase):
    def test_coef(self):
        self.assertEqual(extract_coef(sample_equations[0]), ['+1', '+0', '+36'])
        self.assertEqual(extract_coef(sample_equations[1]), ['+34', '-67', '+0'])
        self.assertEqual(extract_coef(sample_equations[2]), ['+1', '-65', '-76'])

if __name__ == "__main__":
    unittest.main()