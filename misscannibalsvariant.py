from search import *


class MissCannibalsVariant(Problem):


    def __init__(self, N1=4, N2=4, goal=(3, 3, True)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)


    def actions(self, state):
        """Return the actions that can be executed in the given state.
        State is a tuple (m, c, onLeft) representing number of missionaries and
        cannibals on left bank and whether boat is on left bank."""
        m, c, onLeft = state
        actions = []
        if onLeft:
            for i in range(m + 1):
                for j in range(c + 1):
                    if 1 <= i + j <= 2:
                        actions.append(('MC', i, j))
        else:
            for i in range(self.N1 - m + 1):
                for j in range(self.N2 - c + 1):
                    if 1 <= i + j <= 2:
                        actions.append(('MMM', i, j))
        return actions

    def result(self, state, action):
        """Return the state that results from executing the given action in the given state.
        Action is assumed to be a valid action in the state."""
        m, c, onLeft = state
        if onLeft:
            return (m - action[1], c - action[2], False) if action[0] == 'MC' else (m - action[1], c - action[2], False)
        else:
            return (m + action[1], c + action[2], True) if action[0] == 'MC' else (m + action[1], c + action[2], True)


if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    print(mc.actions((3, 3, True)))  # Test case
    # ['MC', 'MMM']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)