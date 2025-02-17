from search import *


class MissCannibalsVariant(Problem):


    def __init__(self, N1=4, N2=4, goal=(3, 3, True)):
        """ Define goal state and initialize a problem """
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)

    def result(self, state, action):
        """ Return the state that results from executing the action in the state """
        return state   

    def actions(self, state):
        """ Return the actions that can be executed in thes state """
        return state

    

if __name__ == '__main__':
    mc = MissCannibalsVariant(4,4)
    print(mc.actions((3, 3, True)))  # Test case

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)