from abc import ABC

import State
import Instance
import Vertex
import Agent
import Instance
import copy
import MatricesFunctions


class GenStochInstance(Instance.Instance):
    def __init__(self, instance):
        super().__init__(instance.map, instance.agents, instance.horizon)
        self.map, self.map_map = instance.make_special_map_and_map_map(Vertex.Stoch_Vertex)
        self.agents, self.agents_map = instance.make_agents_and_agents_map(self.map_map, Agent.StochAgent)
        self.horizon = instance.horizon
        default_state = self.get_default_state(instance)
        self.initial_state = self.make_action(self.action_zero(default_state), default_state)
        self.initial_state.time_left = self.horizon
        self.flybys = instance.flybys

    def actions(self, state):
        agent_actions = {}
        if self.flybys:
            fly_by_options = [True, False]
        else:
            fly_by_options = [False]
        for a_hash in state.a_pos:

            a_loc = self.map_map[state.a_pos[a_hash].loc]
            agent_actions[a_hash] = [State.Position(a_loc.hash(), b) for b in fly_by_options] +\
                                    [State.Position(n.hash(), b) for n in a_loc.neighbours for b in fly_by_options]

        actions = [a for a in Instance.product_dict(agent_actions)]
        return actions

    def get_default_state(self, instance):
        return State.StochState(instance)

    def action_zero(self, zero_state):
        action_zero = {}
        for a_hash in zero_state.a_pos:
            action_zero[a_hash] = State.Position(zero_state.a_pos[a_hash].loc, False)
        return action_zero

    def make_action(self, action, state):
        raise NotImplementedError

    def reward(self, state):
        raise NotImplementedError


class U1StochInstance(GenStochInstance):
    def __init__(self, instance):
        super().__init__(instance)



    def make_action(self, action, state):
        new_state = state.copy()
        new_state.time_left -= 1
        new_state.a_pos = copy.deepcopy(action)

        for a_hash in self.agents_map:
            if action[a_hash] is None or action[a_hash].flyby or \
                    self.agents_map[a_hash].movement_budget < self.horizon - new_state.time_left:
                continue
            vertex_hash = action[a_hash].loc
            new_matrix = MatricesFunctions.new_matrix(state.matrices[a_hash], self.map_map[vertex_hash].distribution,
                                                      new_state.distr[vertex_hash])
            new_theta = MatricesFunctions.update_distr_u1(state.matrices[a_hash], new_state.distr[vertex_hash])
            new_state.matrices[a_hash] = new_matrix
            new_state.distr[vertex_hash] = new_theta
        return new_state

    def reward(self, state):
        if state.reward is not None:
            return state.reward
        state.reward = MatricesFunctions.get_tot_reward(state.matrices)
        return state.reward


class UisRStochInstance(GenStochInstance):
    def __init__(self, i):
        super().__init__(i)

    def get_default_state(self, instance):
        return State.StochUisRState(instance)

    def make_action(self, action, state):
        new_state = state.copy()
        new_state.time_left -= 1
        new_state.a_pos = copy.deepcopy(action)

        for a_hash in self.agents_map:
            if action[a_hash] is None or action[a_hash].flyby or \
                    self.agents_map[a_hash].movement_budget < self.horizon - new_state.time_left:
                continue
            vertex_hash = action[a_hash].loc
            new_matrix = MatricesFunctions.stoch_subtract(state.matrices[a_hash], new_state.distr[vertex_hash])
            new_distr = MatricesFunctions.stoch_subtract(new_state.distr[vertex_hash], state.matrices[a_hash])
            new_state.matrices[a_hash] = new_matrix
            new_state.distr[vertex_hash] = new_distr
        return new_state

    def reward(self, state):
        if state.reward is not None:
            return state.reward
        state.reward = MatricesFunctions.get_vectors_reward(state.matrices)
        return state.reward