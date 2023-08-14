import Instance 
import Vertex
import Agent
vertex1 = Vertex.Vertex(1)
vertex1.distribution = {0: 1}
vertex2 = Vertex.Vertex(2)
vertex2.distribution = {1: 1}
vertex3 = Vertex.Vertex(3)
vertex3.distribution = {1: 1}
vertex4 = Vertex.Vertex(4)
vertex4.distribution = {1: 1}
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
vertex10.distribution = {1: 1}
vertex11 = Vertex.Vertex(11)
vertex11.distribution = {1: 1}
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
vertex17.distribution = {1: 1}
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
vertex24.distribution = {0: 1}
vertex25 = Vertex.Vertex(25)
vertex25.distribution = {0: 1}
vertex26 = Vertex.Vertex(26)
vertex26.distribution = {0: 1}
vertex27 = Vertex.Vertex(27)
vertex27.distribution = {0: 1}
vertex28 = Vertex.Vertex(28)
vertex28.distribution = {0: 1}
vertex29 = Vertex.Vertex(29)
vertex29.distribution = {0: 1}
vertex30 = Vertex.Vertex(30)
vertex30.distribution = {0: 1}
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
vertex36 = Vertex.Vertex(36)
vertex36.distribution = {0: 1}
vertex37 = Vertex.Vertex(37)
vertex37.distribution = {0: 1}
vertex38 = Vertex.Vertex(38)
vertex38.distribution = {0: 1}
vertex39 = Vertex.Vertex(39)
vertex39.distribution = {0: 1}
vertex40 = Vertex.Vertex(40)
vertex40.distribution = {7: 1}
vertex1.neighbours = [vertex2, vertex9]
vertex2.neighbours = [vertex3, vertex1, vertex10]
vertex3.neighbours = [vertex4, vertex2, vertex11]
vertex4.neighbours = [vertex5, vertex3, vertex12]
vertex5.neighbours = [vertex6, vertex4, vertex13]
vertex6.neighbours = [vertex7, vertex5, vertex14]
vertex7.neighbours = [vertex8, vertex6, vertex15]
vertex8.neighbours = [vertex7, vertex16]
vertex9.neighbours = [vertex10, vertex17, vertex1]
vertex10.neighbours = [vertex11, vertex9, vertex18, vertex2]
vertex11.neighbours = [vertex12, vertex10, vertex19, vertex3]
vertex12.neighbours = [vertex13, vertex11, vertex20, vertex4]
vertex13.neighbours = [vertex14, vertex12, vertex21, vertex5]
vertex14.neighbours = [vertex15, vertex13, vertex22, vertex6]
vertex15.neighbours = [vertex16, vertex14, vertex23, vertex7]
vertex16.neighbours = [vertex15, vertex24, vertex8]
vertex17.neighbours = [vertex18, vertex25, vertex9]
vertex18.neighbours = [vertex19, vertex17, vertex26, vertex10]
vertex19.neighbours = [vertex20, vertex18, vertex27, vertex11]
vertex20.neighbours = [vertex21, vertex19, vertex28, vertex12]
vertex21.neighbours = [vertex22, vertex20, vertex29, vertex13]
vertex22.neighbours = [vertex23, vertex21, vertex30, vertex14]
vertex23.neighbours = [vertex24, vertex22, vertex31, vertex15]
vertex24.neighbours = [vertex23, vertex32, vertex16]
vertex25.neighbours = [vertex26, vertex33, vertex17]
vertex26.neighbours = [vertex27, vertex25, vertex34, vertex18]
vertex27.neighbours = [vertex28, vertex26, vertex35, vertex19]
vertex28.neighbours = [vertex29, vertex27, vertex36, vertex20]
vertex29.neighbours = [vertex30, vertex28, vertex37, vertex21]
vertex30.neighbours = [vertex31, vertex29, vertex38, vertex22]
vertex31.neighbours = [vertex32, vertex30, vertex39, vertex23]
vertex32.neighbours = [vertex31, vertex40, vertex24]
vertex33.neighbours = [vertex34, vertex25]
vertex34.neighbours = [vertex35, vertex33, vertex26]
vertex35.neighbours = [vertex36, vertex34, vertex27]
vertex36.neighbours = [vertex37, vertex35, vertex28]
vertex37.neighbours = [vertex38, vertex36, vertex29]
vertex38.neighbours = [vertex39, vertex37, vertex30]
vertex39.neighbours = [vertex40, vertex38, vertex31]
vertex40.neighbours = [vertex39, vertex32]
agent0 = Agent.Agent(0, vertex1, 7, 2)
agent1 = Agent.Agent(1, vertex1, 11, 2)
map1 = [
        vertex1 , vertex2 , vertex3 , vertex4 , vertex5 , vertex6 , vertex7 , vertex8 , 
        vertex9 , vertex10, vertex11, vertex12, vertex13, vertex14, vertex15, vertex16, 
        vertex17, vertex18, vertex19, vertex20, vertex21, vertex22, vertex23, vertex24, 
        vertex25, vertex26, vertex27, vertex28, vertex29, vertex30, vertex31, vertex32, 
        vertex33, vertex34, vertex35, vertex36, vertex37, vertex38, vertex39, vertex40, ]
agents = [agent0, agent1]
instance1 = Instance.Instance("grid6AG", map1, agents, 11)
