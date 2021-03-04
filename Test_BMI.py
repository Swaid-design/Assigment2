import unittest

from BMICalc import BMI_Calculator

class BMICalcTest(unittest.TestCase):
    
    def test_create_BMICalc(self):
        person = BMI_Calculator()
        self.assertEqual(person.get_height(), 0)
        self.assertEqual(person.get_weight(), 0)

    def test_set_weight_error(self):  #bad values
        person = BMI_Calculator()
        with self.assertRaises(KeyError):
            person.set_weight(-1)
        with self.assertRaises(KeyError):
            person.set_weight(0)
        with self.assertRaises(KeyError):
            person.set_weight(601)

    def test_set_weight_no_error(self):  #good values
        person = BMI_Calculator()
        self.assertAlmostEqual(person.set_weight(150), 68.0385)


if __name__ == '__main__':
    unittest.main()