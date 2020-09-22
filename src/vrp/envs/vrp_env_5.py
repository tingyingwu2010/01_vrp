import numpy as np # type: ignore
import gym # type: ignore

class VRPEnv5(gym.Env):
    """This class replicates the CVRP Environment from (Nazari et. al 2018).
        https://arxiv.org/abs/1802.04240
    
    Trying desperately to fix code cov
        
    Attributes:
        n_destinations (int): An integer indicating number of destinations
    """

    def __init__(self):
        """Inits VRPEnv with n_destinations"""
        super(VRPEnv5, self).__init__()
        self.n_destinations = 5
        self.n_vehicles = 1
        self.homogeneous = True # Trucks are all homogeneous i.e. the same.
        self.capacity = 10 # Set arbitrarily high for now.

    def step(self, action: int) -> int:
        """Takes a step using `action`."""
        raise NotImplementedError

    def reset(self):
        """Performs operation blah."""
        raise NotImplementedError
    
    def render(self):
        """Performs operation blah."""
        raise NotImplementedError
    
    def close(self):
        """Performs operation blah."""
        raise NotImplementedError
