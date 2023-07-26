import copy

import MatricesFunctions


class Position:
    def __init__(self, loc=-1, flyby=True):
        self.loc = loc
        self.flyby = flyby

    def __str__(self):
        return "( "+str(self.loc)+", "+str(self.flyby)+" )"


class State:
    # Info held by every node. The info is gathered using agents actions only therefore is deterministic.
    def __init__(self):
        self.time_left = 0  # int

    def is_terminal(self):
        return self.time_left == 0


class DetState(State):
    def __init__(self, instance=None):
        super().__init__()
        self.path = {}  # a.hash(): [pos, pos, -1, ... , -1] -
        # Required to count the reward of the state. Not needed in stochastic state.
        if instance is not None:
            self.time_left = instance.horizon
            for a in instance.agents:
                self.path[a.hash()] = [None for _ in range(instance.horizon + 1)]
                self.path[a.hash()][0] = Position(a.loc.hash(), False)

    def copy(self):
        copy_state = DetState()
        copy_state.path = copy.deepcopy(self.path)
        copy_state.time_left = self.time_left
        return copy_state

    def __str__(self):
        return str((self.path, self.time_left))


class StochState(State):
    def __init__(self, instance=None):
        super().__init__()
        self.a_pos = {}
        self.matrices = {}  # a.hash(): Matrix
        self.thetas = {}  # v.hash(): probability
        self.reward = None
        if instance is not None:
            for a in instance.agents:
                self.time_left = instance.horizon
                self.a_pos[a.hash()] = Position(a.loc.hash(), True)  # a.hash(): v.hash()
                self.matrices[a.hash()] = MatricesFunctions.get_starting_matrix(a, a.loc)
            for v_hash in instance.map_map:
                self.thetas[v_hash] = 1

    def __str__(self):
        return str((self.a_pos, self.time_left))

    def copy(self):
        copy_state = StochState()
        copy_state.a_pos = copy.deepcopy(self.a_pos)
        copy_state.matrices = copy.deepcopy(self.matrices)
        copy_state.thetas = copy.deepcopy(self.thetas)
        copy_state.time_left = self.time_left
        return copy_state
