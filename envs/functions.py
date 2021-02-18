

def get_reward():
    # calculate reward for each state action pair based on the angle between
    # action vectors and DTI direction vector
    ''' fix me'''
    if 0 <=angle and angle<=pi/2:
        reward = 1
    elif pi/2 <angle and angle<=pi:
        reward = 0
    else pi <angle and angle<=2pi:
        reward = -1

    return reward

# check if episode is done
def is_done():

    if state.is_out:
        done = True
    else:
        done = False
    return done

''' TODO: transfer action to action_vector '''
def get_action_vector(action):



''' TODO: track state action pairs as streamline'''
def track_sl():

    
