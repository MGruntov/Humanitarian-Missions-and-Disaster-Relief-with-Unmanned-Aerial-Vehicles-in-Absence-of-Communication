import Instance 
import Vertex
import Agent
vertex0 = Vertex.Vertex(0)
vertex0.distribution = {2: 0.1, 0: 0.9}
vertex1 = Vertex.Vertex(1)
vertex1.distribution = {10: 1}
vertex2 = Vertex.Vertex(2)
vertex2.distribution = {10: 1}
vertex3 = Vertex.Vertex(3)
vertex3.distribution = {10: 1}
vertex0.neighbours = [vertex2, vertex1]
vertex1.neighbours = [vertex0, vertex3]
vertex2.neighbours = [vertex0, vertex3]
vertex3.neighbours = [vertex1, vertex2]
agent0 = Agent.Agent(0, vertex0, 2, 4)
map1 = [vertex0, vertex1, 
        vertex2, vertex3]
agents = [agent0]
instance1 = Instance.Instance(map1, agents, 4)
