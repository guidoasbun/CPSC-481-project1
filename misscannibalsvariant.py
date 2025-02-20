from search import *


class MissCannibalsVariant(Problem):


    def __init__(self, N1=4, N2=4, goal=None):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        if goal is None:
            goal = (0, 0, False)
        super().__init__(initial, goal)


    def actions(self, state):
        """Return the actions that can be executed in the given state.
        State is a tuple (m, c, onLeft) representing number of missionaries and
        cannibals on left bank and whether boat is on left bank."""
        m, c, onLeft = state
        valid_actions = []
        
        possible_actions = ['M', 'C', 'MM', 'MC', 'CC', 'MMM', 'MMC', 'MCC', 'CCC']
        
        if onLeft:  # Boat on left bank, moving people from left to right
            for action in possible_actions:
                m_count = action.count('M')
                c_count = action.count('C')
                
                # Check if we have enough people on the left bank
                if m_count <= m and c_count <= c:
                    # Check if move is safe on both banks
                    new_left_m = m - m_count
                    new_left_c = c - c_count
                    new_right_m = self.N1 - new_left_m
                    new_right_c = self.N2 - new_left_c
                    
                    # Safety check: missionaries not outnumbered on either bank
                    if ((new_left_m == 0 or new_left_m >= new_left_c) and 
                        (new_right_m == 0 or new_right_m >= new_right_c)):
                        valid_actions.append(action)
        
        else:  # Boat on right bank, moving people from right to left
            right_m = self.N1 - m
            right_c = self.N2 - c
            
            for action in possible_actions:
                m_count = action.count('M')
                c_count = action.count('C')
                
                # Check if we have enough people on the right bank
                if m_count <= right_m and c_count <= right_c:
                    # Check if move is safe on both banks
                    new_left_m = m + m_count
                    new_left_c = c + c_count
                    new_right_m = self.N1 - new_left_m
                    new_right_c = self.N2 - new_left_c
                    
                    # Safety check: missionaries not outnumbered on either bank
                    if ((new_left_m == 0 or new_left_m >= new_left_c) and 
                        (new_right_m == 0 or new_right_m >= new_right_c)):
                        valid_actions.append(action)
        
        return valid_actions

    def result(self, state, action):
        """Return the state that results from executing the given action in the given state.
        Action is assumed to be a valid action in the state."""
        m, c, onLeft = state
        m_count = action.count('M')
        c_count = action.count('C')
        
        if onLeft:  # Moving from left to right
            return (m - m_count, c - c_count, False)
        else:  # Moving from right to left
            return (m + m_count, c + c_count, True)


if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    print(mc.actions((3, 3, True)))  # Test case
    # ['MC', 'MMM']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)