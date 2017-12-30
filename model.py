# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:30:06 2017

@author: user1
"""
#imports necessary
import random
import operator
import csv
import matplotlib
import matplotlib.pyplot
import agentframework

#make a rowlist list
rowlist = []

#assign values
num_of_agents = 10
num_of_iterations = 100 
neighbourhood = 20

#open the csv file
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

#make an environment list and for loop
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist) 	

#define distance between argument
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

#make a list of agents
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
     
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

#plot the agents
'''
#scatter plot
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()
'''

#plot the agents ant the csv
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show() 

#calculate distance between agents
for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)
     
#a = agentframework.Agent()
#print(a.y, a.x)
#a.move()
#print(a.y, a.x)