# the framework to follow
import gym
from gym import spaces
from gym.spaces import Discrete, Box
import numpy as np
from RL_FiberTracking.envs.functions import get_reward, is_done, get_action_vector
from RL_FiberTracking.envs.agent import Agent
from src.data import HCPDataContainer, ISMRMDataContainer

hcp_data = HCPDataContainer(100307)
ismrm_data = ISMRMDataContainer()


class RLenv(gym.Env):
    # justifying action and observation space
    def __init__(self, device):
        self.device = device
        self.agent = Agent()
        # 30 directions we can take
        self.action_space = spaces.Discrete(30)
        self.observation_space = spaces.Box(np.array([0,0,0]), np.array([x,y,z]))
        self.done = Flase

    # tranform the cartesian coordinate state to the interpolated_dwi as the input of network
    def get_input_state(self.state):
        ras_points = hcp_data.to_ras(self.state) # Transform state to World RAS+ coordinate system
        interpolated_dwi = hcp_data.get_interpolated_dwi(ras_points, ignore_outside_points=False)# numpy arrary convert it to tensor
        input_state = interpolated_dwi

        return input_state

    # calculate the angle between action vector and DTI_direction_vector
    ### TODO: load the DTI_direction_vector ###
    def Angle_calculator(action_vector, DTI_direction_vector):
        m=get_action_vector(action)
        n=DTI_direction_vector
        l_m=np.sqrt(m.dot(m))
        l_n=np.sqrt(n.dot(n))
        dot_product=x.dot(y)
        cos_=dot_product/(l_m*l_n)
        angle=np.arccos(cos_)
        return angle

    # action will be performed and returns calculated state and reward
    def step(self, action):
        # apply action
        self.agent.action = Agent.select_action()
        action_vector = get_action_vector(action)
        next_state = state + step_width * norm(action_vector)

        # calculate reward
        reward = get_reward()
        done = is_done()
        state = next_state

        # return step information
        return state, reward, done

    # reset the game and returns the observed data from the last episode
    def reset(self):
        del self.agent
        # reset state
        self.agent = Agent()
        return self.state

    def close(self):
        self.env.close()

    ### TODO: render the process ###
    def render(self, mode="human")
