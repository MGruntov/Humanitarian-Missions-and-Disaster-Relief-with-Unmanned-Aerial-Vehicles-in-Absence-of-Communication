import Instance 
import Vertex
import Agent
vertex0 = Vertex.Vertex(0)
vertex0.distribution = {0: 1}
vertex1 = Vertex.Vertex(1)
vertex1.distribution = {1: 1}
vertex2 = Vertex.Vertex(2)
vertex2.distribution = {0: 1}
vertex3 = Vertex.Vertex(3)
vertex3.distribution = {0: 1}
vertex4 = Vertex.Vertex(4)
vertex4.distribution = {0: 1}
vertex5 = Vertex.Vertex(5)
vertex5.distribution = {0: 1}
vertex6 = Vertex.Vertex(6)
vertex6.distribution = {0: 1}
vertex7 = Vertex.Vertex(7)
vertex7.distribution = {0: 1}
vertex8 = Vertex.Vertex(8)
vertex8.distribution = {0: 1}
vertex9 = Vertex.Vertex(9)
vertex9.distribution = {0: 1}
vertex10 = Vertex.Vertex(10)
vertex10.distribution = {0: 1}
vertex11 = Vertex.Vertex(11)
vertex11.distribution = {0: 1}
vertex12 = Vertex.Vertex(12)
vertex12.distribution = {0: 1}
vertex13 = Vertex.Vertex(13)
vertex13.distribution = {0: 1}
vertex14 = Vertex.Vertex(14)
vertex14.distribution = {0: 1}
vertex15 = Vertex.Vertex(15)
vertex15.distribution = {0: 1}
vertex16 = Vertex.Vertex(16)
vertex16.distribution = {0: 1}
vertex17 = Vertex.Vertex(17)
vertex17.distribution = {0: 1}
vertex18 = Vertex.Vertex(18)
vertex18.distribution = {0: 1}
vertex19 = Vertex.Vertex(19)
vertex19.distribution = {0: 1}
vertex20 = Vertex.Vertex(20)
vertex20.distribution = {0: 1}
vertex21 = Vertex.Vertex(21)
vertex21.distribution = {0: 1}
vertex22 = Vertex.Vertex(22)
vertex22.distribution = {0: 1}
vertex23 = Vertex.Vertex(23)
vertex23.distribution = {0: 1}
vertex24 = Vertex.Vertex(24)
vertex24.distribution = {0:1}
vertex25 = Vertex.Vertex(25)
vertex25.distribution = {0:1}
vertex26 = Vertex.Vertex(26)
vertex26.distribution = {0: 1}
vertex27 = Vertex.Vertex(27)
vertex27.distribution = {0: 1}
vertex28 = Vertex.Vertex(28)
vertex28.distribution = {0: 1}
vertex29 = Vertex.Vertex(29)
vertex29.distribution = {0: 1}
vertex30 = Vertex.Vertex(30)
vertex30.distribution = {10000: 0.0005}
vertex31 = Vertex.Vertex(31)
vertex31.distribution = {0: 1}
vertex32 = Vertex.Vertex(32)
vertex32.distribution = {0: 1}
vertex33 = Vertex.Vertex(33)
vertex33.distribution = {0: 1}
vertex34 = Vertex.Vertex(34)
vertex34.distribution = {0: 1}
vertex35 = Vertex.Vertex(35)
vertex35.distribution = {0: 1}
vertex0.neighbours = [vertex6, vertex1]
vertex1.neighbours = [vertex0, vertex7, vertex2]
vertex2.neighbours = [vertex1, vertex8, vertex3]
vertex3.neighbours = [vertex2, vertex9, vertex4]
vertex4.neighbours = [vertex3, vertex10, vertex5]
vertex5.neighbours = [vertex4, vertex11]
vertex6.neighbours = [vertex0, vertex12, vertex7]
vertex7.neighbours = [vertex1, vertex6, vertex13, vertex8]
vertex8.neighbours = [vertex2, vertex7, vertex14, vertex9]
vertex9.neighbours = [vertex3, vertex8, vertex15, vertex10]
vertex10.neighbours = [vertex4, vertex9, vertex16, vertex11]
vertex11.neighbours = [vertex5, vertex10, vertex17]
vertex12.neighbours = [vertex6, vertex18, vertex13]
vertex13.neighbours = [vertex7, vertex12, vertex19, vertex14]
vertex14.neighbours = [vertex8, vertex13, vertex20, vertex15]
vertex15.neighbours = [vertex9, vertex14, vertex21, vertex16]
vertex16.neighbours = [vertex10, vertex15, vertex22, vertex17]
vertex17.neighbours = [vertex11, vertex16, vertex23]
vertex18.neighbours = [vertex12, vertex24, vertex19]
vertex19.neighbours = [vertex13, vertex18, vertex25, vertex20]
vertex20.neighbours = [vertex14, vertex19, vertex26, vertex21]
vertex21.neighbours = [vertex15, vertex20, vertex27, vertex22]
vertex22.neighbours = [vertex16, vertex21, vertex28, vertex23]
vertex23.neighbours = [vertex17, vertex22, vertex29]
vertex24.neighbours = [vertex18, vertex30, vertex25]
vertex25.neighbours = [vertex19, vertex24, vertex31, vertex26]
vertex26.neighbours = [vertex20, vertex25, vertex32, vertex27]
vertex27.neighbours = [vertex21, vertex26, vertex33, vertex28]
vertex28.neighbours = [vertex22, vertex27, vertex34, vertex29]
vertex29.neighbours = [vertex23, vertex28, vertex35]
vertex30.neighbours = [vertex24, vertex31]
vertex31.neighbours = [vertex25, vertex30, vertex32]
vertex32.neighbours = [vertex26, vertex31, vertex33]
vertex33.neighbours = [vertex27, vertex32, vertex34]
vertex34.neighbours = [vertex28, vertex33, vertex35]
vertex35.neighbours = [vertex29, vertex34]
agent0 = Agent.Agent(0, vertex0, 6, 1)
map1 = [vertex0, vertex1, vertex2, vertex3, vertex4, vertex5, 
        vertex6, vertex7, vertex8, vertex9, vertex10, vertex11, 
        vertex12, vertex13, vertex14, vertex15, vertex16, vertex17, 
        vertex18, vertex19, vertex20, vertex21, vertex22, vertex23, 
        vertex24, vertex25, vertex26, vertex27, vertex28, vertex29, 
        vertex30, vertex31, vertex32, vertex33, vertex34, vertex35]
agents = [agent0]
instance1 = Instance.Instance(map1, agents, 6)