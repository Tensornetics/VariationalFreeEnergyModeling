import unittest
import FokkerPlanck
import numpy as np

class TestFokkerPlanck(unittest.TestCase):
    def test_solver(self):
        # Test inputs
        initial_probability_density = np.array([0.1, 0.2, 0.3, 0.4])
        time_step = 0.1
        expected_result = np.array([0.11, 0.22, 0.33, 0.44])

        # Call the solver function
        result = FokkerPlanck.solver(initial_probability_density, time_step)

        # Assert that the result is as expected
        np.testing.assert_array_almost_equal(result, expected_result)
        
    def test_nonlinearity(self):
        # Test inputs
        initial_probability_density = np.array([0.1, 0.2, 0.3, 0.4])
        time_step = 0.1
        nonlinear_coefficient = 0.5
        expected_result = np.array([0.12, 0.24, 0.36, 0.48])

        # Call the solver function with nonlinearity
        result = FokkerPlanck.solver(initial_probability_density, time_step, nonlinear_coefficient)

        # Assert that the result is as expected
        np.testing.assert_array_almost_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()
