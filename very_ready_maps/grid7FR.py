import Instance 
import Vertex
import Agent
vertex1 = Vertex.Vertex(1)
vertex1.distribution = {0: 1}
vertex2 = Vertex.Vertex(2)
vertex2.distribution = {1: 0.1285, 0: 0.8715}
vertex3 = Vertex.Vertex(3)
vertex3.distribution = {0: 1}
vertex4 = Vertex.Vertex(4)
vertex4.distribution = {0: 1}
vertex5 = Vertex.Vertex(5)
vertex5.distribution = {2: 0.908, 0: 0.092}
vertex6 = Vertex.Vertex(6)
vertex6.distribution = {2: 0.4248, 0: 0.5752}
vertex7 = Vertex.Vertex(7)
vertex7.distribution = {0: 1}
vertex8 = Vertex.Vertex(8)
vertex8.distribution = {2: 0.3679, 0: 0.6321}
vertex9 = Vertex.Vertex(9)
vertex9.distribution = {2: 0.8935, 0: 0.1065}
vertex10 = Vertex.Vertex(10)
vertex10.distribution = {0: 1}
vertex11 = Vertex.Vertex(11)
vertex11.distribution = {1: 0.034, 0: 0.966}
vertex12 = Vertex.Vertex(12)
vertex12.distribution = {0: 1}
vertex13 = Vertex.Vertex(13)
vertex13.distribution = {2: 0.6358, 0: 0.3642}
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
vertex19.distribution = {2: 0.3917, 0: 0.6083}
vertex20 = Vertex.Vertex(20)
vertex20.distribution = {0: 1}
vertex21 = Vertex.Vertex(21)
vertex21.distribution = {0: 1}
vertex22 = Vertex.Vertex(22)
vertex22.distribution = {1: 0.7804, 0: 0.2196}
vertex23 = Vertex.Vertex(23)
vertex23.distribution = {0: 1}
vertex24 = Vertex.Vertex(24)
vertex24.distribution = {1: 0.3389, 0: 0.6611}
vertex25 = Vertex.Vertex(25)
vertex25.distribution = {0: 1}
vertex26 = Vertex.Vertex(26)
vertex26.distribution = {0: 1}
vertex27 = Vertex.Vertex(27)
vertex27.distribution = {1: 0.4475, 0: 0.5525}
vertex28 = Vertex.Vertex(28)
vertex28.distribution = {0: 1}
vertex29 = Vertex.Vertex(29)
vertex29.distribution = {0: 1}
vertex30 = Vertex.Vertex(30)
vertex30.distribution = {1: 0.8927, 0: 0.1073}
vertex31 = Vertex.Vertex(31)
vertex31.distribution = {0: 1}
vertex32 = Vertex.Vertex(32)
vertex32.distribution = {1: 0.1295, 0: 0.8705}
vertex33 = Vertex.Vertex(33)
vertex33.distribution = {0: 1}
vertex34 = Vertex.Vertex(34)
vertex34.distribution = {0: 1}
vertex35 = Vertex.Vertex(35)
vertex35.distribution = {1: 0.255, 0: 0.745}
vertex36 = Vertex.Vertex(36)
vertex36.distribution = {2: 0.8826, 0: 0.1174}
vertex37 = Vertex.Vertex(37)
vertex37.distribution = {2: 0.0157, 0: 0.9843}
vertex38 = Vertex.Vertex(38)
vertex38.distribution = {1: 0.462, 0: 0.538}
vertex39 = Vertex.Vertex(39)
vertex39.distribution = {1: 0.1735, 0: 0.8265}
vertex40 = Vertex.Vertex(40)
vertex40.distribution = {2: 0.8886, 0: 0.1114}
vertex1.neighbours = [vertex2, vertex6]
vertex2.neighbours = [vertex3, vertex1, vertex7]
vertex3.neighbours = [vertex4, vertex2, vertex8]
vertex4.neighbours = [vertex5, vertex3, vertex9]
vertex5.neighbours = [vertex4, vertex10]
vertex6.neighbours = [vertex7, vertex11, vertex1]
vertex7.neighbours = [vertex8, vertex6, vertex12, vertex2]
vertex8.neighbours = [vertex9, vertex7, vertex13, vertex3]
vertex9.neighbours = [vertex10, vertex8, vertex14, vertex4]
vertex10.neighbours = [vertex9, vertex15, vertex5]
vertex11.neighbours = [vertex12, vertex16, vertex6]
vertex12.neighbours = [vertex13, vertex11, vertex17, vertex7]
vertex13.neighbours = [vertex14, vertex12, vertex18, vertex8]
vertex14.neighbours = [vertex15, vertex13, vertex19, vertex9]
vertex15.neighbours = [vertex14, vertex20, vertex10]
vertex16.neighbours = [vertex17, vertex21, vertex11]
vertex17.neighbours = [vertex18, vertex16, vertex22, vertex12]
vertex18.neighbours = [vertex19, vertex17, vertex23, vertex13]
vertex19.neighbours = [vertex20, vertex18, vertex24, vertex14]
vertex20.neighbours = [vertex19, vertex25, vertex15]
vertex21.neighbours = [vertex22, vertex26, vertex16]
vertex22.neighbours = [vertex23, vertex21, vertex27, vertex17]
vertex23.neighbours = [vertex24, vertex22, vertex28, vertex18]
vertex24.neighbours = [vertex25, vertex23, vertex29, vertex19]
vertex25.neighbours = [vertex24, vertex30, vertex20]
vertex26.neighbours = [vertex27, vertex31, vertex21]
vertex27.neighbours = [vertex28, vertex26, vertex32, vertex22]
vertex28.neighbours = [vertex29, vertex27, vertex33, vertex23]
vertex29.neighbours = [vertex30, vertex28, vertex34, vertex24]
vertex30.neighbours = [vertex29, vertex35, vertex25]
vertex31.neighbours = [vertex32, vertex36, vertex26]
vertex32.neighbours = [vertex33, vertex31, vertex37, vertex27]
vertex33.neighbours = [vertex34, vertex32, vertex38, vertex28]
vertex34.neighbours = [vertex35, vertex33, vertex39, vertex29]
vertex35.neighbours = [vertex34, vertex40, vertex30]
vertex36.neighbours = [vertex37, vertex31]
vertex37.neighbours = [vertex38, vertex36, vertex32]
vertex38.neighbours = [vertex39, vertex37, vertex33]
vertex39.neighbours = [vertex40, vertex38, vertex34]
vertex40.neighbours = [vertex39, vertex35]
agent0 = Agent.Agent(0, vertex1, 4, 2)
agent1 = Agent.Agent(1, vertex1, 8, 5)
map1 = [
        vertex1 , vertex2 , vertex3 , vertex4 , vertex5 , 
        vertex6 , vertex7 , vertex8 , vertex9 , vertex10, 
        vertex11, vertex12, vertex13, vertex14, vertex15, 
        vertex16, vertex17, vertex18, vertex19, vertex20, 
        vertex21, vertex22, vertex23, vertex24, vertex25, 
        vertex26, vertex27, vertex28, vertex29, vertex30, 
        vertex31, vertex32, vertex33, vertex34, vertex35, 
        vertex36, vertex37, vertex38, vertex39, vertex40, ]
agents = [agent0, agent1]
instance1 = Instance.Instance("grid7FR", map1, agents, 8)
