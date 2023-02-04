import numpy as np
import scipy.integrate as spi

class FokkerPlanck:
    def __init__(self, drift, diffusion, initial_condition, t_grid):
        self.drift = drift
        self.diffusion = diffusion
        self.initial_condition = initial_condition
        self.t_grid = t_grid
        
    def solve(self):
        t = self.t_grid
        y0 = self.initial_condition
        
        def f_drift(y, t, params):
            return self.drift(y, t, params)
        
        def f_diffusion(y, t, params):
            return np.dot(self.diffusion(y, t, params), y)
        
        solution = spi.solve_ivp(fun=lambda t, y: f_drift(y, t, None) + f_diffusion(y, t, None), t_span=(t[0], t[-1]), y0=y0, t_eval=t)
        return solution.y
