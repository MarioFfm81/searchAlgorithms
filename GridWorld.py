from tkinter import *
import time
from queue import PriorityQueue

class GridWorld:
    def __init__(self):
        self.pos = (None, None)
        self.goal = (None, None)
        self.loadGrid()
        self.padding = 10
        self.size = 20

        self.root = Tk()
        self.root.title("A.I with Mario - Search Algorithms")
        height = max(self.size*len(self.world)+2*self.padding, 400)
        if len(self.world)>0:
            width = max(self.size*len(self.world[0])+2*self.padding, 400)
        else:
            width = 400
        self.c = Canvas(self.root, height=height, width=width, bg="black")
        self.c.pack()

        self.visited = set()
        self.queue = []
        self.prioQueue = PriorityQueue()
        self.fringe = {}
        
        

    def getPos(self):
        return self.pos

    def loadGrid(self):
        self.world =   [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','S','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','G','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

        self.world =   [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','S','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','G','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

        self.world =   [['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','S','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','G','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','#'],
                        ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    def getPossibleActions(self, pos):
        x, y = pos  # expects a (x, y) tuple
        if self.world[y][x] == '#' or self.world[y][x]=='G':
            return []
        actions = []
        
        #check if going left is possible
        if x>0 and self.world[y][x-1] != '#':
            actions.append((-1,0))
        #check if going right is possible
        if x<len(self.world[y])-1 and self.world[y][x+1] != '#':
            actions.append((1,0))
        #check if going up is possible
        if y>0 and self.world[y-1][x] != '#':
            actions.append((0,-1))
        #check if going right is possible
        if y<len(self.world)-1 and self.world[y+1][x] != '#':
            actions.append((0,1))
        
        return actions

    def isGoalState(self, pos):
        x, y = pos
        return self.world[y][x]=='G'


    def drawGrid(self):
        x=self.padding
        y=self.padding
        
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                if self.world[i][j]=='#':
                    self.c.create_rectangle(x+j*self.size,y+i*self.size, x+(j+1)*self.size, y+(i+1)*self.size, fill="brown", outline="brown")
                elif self.world[i][j]=='S':
                    self.c.create_rectangle(x+j*self.size,y+i*self.size, x+(j+1)*self.size, y+(i+1)*self.size, fill="blue")
                    self.player = self.c.create_oval((x+j*self.size)+2,(y+i*self.size)+2, (x+(j+1)*self.size)-2, (y+(i+1)*self.size)-2, fill="yellow", outline=None)
                    self.pos = (j, i) # i is rows, ergo y, j is columns, ergo x and we return the position as (x, y)
                elif self.world[i][j]=='G':
                    self.c.create_rectangle(x+j*self.size,y+i*self.size, x+(j+1)*self.size, y+(i+1)*self.size, fill="green")
                    self.goal = (j, i)
                else: 
                    self.c.create_rectangle(x+j*self.size,y+i*self.size, x+(j+1)*self.size, y+(i+1)*self.size, fill="blue")
        self.c.tag_raise(self.player) # to have the player-circle in the top layer

        self.visited.add(self.pos)
        self.queue.append((self.pos, []))
        self.prioQueue.put((self.AStarHeuristic(self.pos), 0, self.pos, []))
        self.fringe[self.pos] = (self.AStarHeuristic(self.pos), 0, [])
        '''
        self.c.bind_all("<Key>", self.move_player)
        '''

    def setMarker(self, pos):
        x, y = pos
        self.c.create_oval((self.padding+x*self.size)+2,(self.padding+y*self.size)+2, (self.padding+(x+1)*self.size)-2, (self.padding+(y+1)*self.size)-2, outline="orange", fill=None)
    
    def setStepMarker(self, pos):
        x, y = pos
        self.c.create_oval((self.padding+x*self.size)+2,(self.padding+y*self.size)+2, (self.padding+(x+1)*self.size)-2, (self.padding+(y+1)*self.size)-2, outline=None, fill="red")

    def runBFS(self):
        if self.queue:
            pos, route = self.queue.pop(0)
            self.setMarker(pos)
            #time.sleep(0.1)
            
            route.append(pos)
            if self.isGoalState(pos):
                self.queue = []
                for step in route[1:]:
                    self.setStepMarker(step)
                return route
            
            for action in self.getPossibleActions(pos):
                actionPos = (pos[0]+action[0], pos[1]+action[1])
                if not actionPos in self.visited:
                    self.visited.add(actionPos)
                    self.queue.append((actionPos,route[:]))
            #print(queue)
            self.root.after(50, self.runBFS)

    def runDFS(self):
        if self.queue:
            pos, route = self.queue.pop()
            self.visited.add(pos)
            self.setMarker(pos)
            
            route.append(pos)
            if self.isGoalState(pos):
                self.queue = []
                for step in route[1:]:
                    self.setStepMarker(step)
                return route
            
            for action in self.getPossibleActions(pos):
                actionPos = (pos[0]+action[0], pos[1]+action[1])
                if not actionPos in self.visited:
                    self.queue.append((actionPos,route[:]))
            #print(queue)
            self.root.after(50, self.runDFS)

    def AStarHeuristic(self, pos):
        return abs(self.goal[0]-pos[0]) + abs(self.goal[1]-pos[1])

    def helper_fringeHasElements(self):
        for i_element in self.fringe:
            if self.fringe[i_element] != None:
                return True
        return False

    def helper_getBestElement(self):
        bestElement = None
        bestH = 9999999
        for element in self.fringe:
            if self.fringe[element]:
                h, c, route = self.fringe[element]
                if (h+c) < bestH:
                    bestElement = element
                    bestH = h + c
        return bestElement

    def runAStar(self):
        print(self.fringe)
        if self.helper_fringeHasElements():
            el = self.helper_getBestElement()
            print(el)
            self.setMarker(el)
            h, c, route = self.fringe[el]
            self.fringe[el] = None

            c += 1
            route.append(el)
            if self.isGoalState(el):
                self.fringe = {}
                for step in route[1:]:
                    self.setStepMarker(step)
                return route
            for action in self.getPossibleActions(el):
                actionPos = (el[0]+action[0], el[1]+action[1])
                if actionPos not in self.fringe:
                    self.fringe[actionPos] = (self.AStarHeuristic(actionPos), c, route[:])
                elif self.fringe[actionPos]:
                    h_fringe, c_fringe, _ = self.fringe[actionPos]
                    if (h+c) < (h_fringe + c_fringe):
                        self.fringe[actionPos] = (self.AStarHeuristic(actionPos), c, route[:])
            self.root.after(50, self.runAStar)

        '''
        if self.prioQueue.qsize()>0:
            cost, steps, pos, route = self.prioQueue.get()
            self.setMarker(pos)
            print(cost, steps, pos, route)
            steps += 1
            route.append(pos)
            if self.isGoalState(pos):
                self.queue = []
                for step in route[1:]:
                    self.setStepMarker(step)
                return route
            for action in self.getPossibleActions(pos):
                actionPos = (pos[0]+action[0], pos[1]+action[1])
                self.prioQueue.put((steps+self.AStarHeuristic(actionPos), steps, actionPos, route[:]))
            exit(0)
        '''
            


    '''
    def move_player(self, event):
        if event.keysym=="Up":
            self.c.move(self.player, 0,-5)
        if event.keysym=="Down":
            self.c.move(self.player, 0,5)
        if event.keysym=="Left":
            self.c.move(self.player, -5,0)
        if event.keysym=="Right":
            self.c.move(self.player, 5,0)
    '''


    def show(self):
        self.drawGrid()

        #self.root.after(200, self.runBFS)    
        self.root.after(200, self.runAStar)    
        self.root.mainloop()
        

gw = GridWorld()
print(gw.show())