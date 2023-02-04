import unittest
import InformationBottleneck

class TestInformationBottleneck(unittest.TestCase):
    
    def setUp(self):
        # set up input data
        self.input_data = [1, 2, 3, 4, 5]

    def test_information_flow_limitation(self):
        # initialize InformationBottleneck object
        ib = InformationBottleneck()

        # run information bottleneck method on input data
        internal_states = ib.run(self.input_data)

        # check that information flow is limited
        self.assertLess(len(internal_states), len(self.input_data))
        
    def test_information_capture(self):
        # initialize InformationBottleneck object
        ib = InformationBottleneck()

        # run information bottleneck method on input data
        internal_states = ib.run(self.input_data)

        # check that relevant information from input data is captured in internal states
        for state in internal_states:
            self.assertIn(state, self.input_data)

if __name__ == '__main__':
    unittest.main()
