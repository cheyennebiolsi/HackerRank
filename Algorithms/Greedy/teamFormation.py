import heapq
from heapq import heappush, heappop

class Team:
    def __init__(self, id, skillLevel):
        self.id = id
        self.size = 1
        self.minLevel = skillLevel
        self.maxLevel = skillLevel
        
    def add(self, skillLevel):
        #print("Old min and max: {} & {}".format(self.minLevel, self.maxLevel))
        self.minLevel = min(self.minLevel, skillLevel)
        self.maxLevel = max(self.maxLevel, skillLevel)
        #print("New min and max: {} & {}".format(self.minLevel, self.maxLevel))
        self.size += 1
        
    def canAdd(self, skillLevel):
        b = False
        overridden = None
        if skillLevel == self.maxLevel + 1:
            b = True
            overridden = self.maxLevel
        if skillLevel == self.minLevel - 1:
            b = True
            overridden = self.minLevel
        #print("Can add {} to ({}, {}): {}".format(skillLevel, self.minLevel, self.maxLevel, b))
        return b, overridden
    
    def __cmp__(self, other):
        return cmp(self.size, other.size)
    
    def __le__(self, other):
        return self.size <= other.size
    
    def __eq__(self, other):
        return self.size == other.size
    
    def __lt__(self, other):
        return self.size < other.size
    
    def __hash__(self):
        return int(self.id)

    def __repr__(self):
        return "Team {}: ({},{}), size: {}".format(self.id, self.minLevel, self.maxLevel, self.size)
    
def splitTeams(skillLevels):
    
    teams = []
    maxLevel = {}
    minLevel = {}
    id = 0
    for skill in skillLevels:
        #print(skill)
        possibleTeams = []
        if skill - 1 in maxLevel:
            possibleTeams += maxLevel[skill - 1]
        if  skill + 1 in minLevel:
            possibleTeams += minLevel[skill - 1]
        
        heapq.heapify(possibleTeams)
        #print(possibleTeams)
        if len(possibleTeams) == 0:
            newTeam = Team(id, skill)
            id += 1
            teams.append(newTeam)
            if skill in minLevel:
                heappush(minLevel[skill], (newTeam))
            else:
                lst = [(1, newTeam)]
                heapq.heapify(lst)
                minLevel[skill] = [(newTeam)]
            if skill in maxLevel:
                heappush(maxLevel[skill], (newTeam))
            else:
                lst = [(newTeam)]
                heapq.heapify(lst)
                maxLevel[skill] = [(newTeam)]
            #print(teams)
            #print(maxLevel)
            #print(minLevel)
            continue
            
        smallestTeam = heappop(possibleTeams)
        canAdd, overridden = smallestTeam.canAdd(skill)
        while not canAdd:
            if len(possibleTeams) == 0:
                #print("Ran out")
                newTeam = Team(id, skill)
                id += 1
                teams.append(newTeam)
                if skill in minLevel:
                    heappush(minLevel[skill], (newTeam))
                else:
                    lst = [(1, newTeam)]
                    heapq.heapify(lst)
                    minLevel[skill] = [(newTeam)]
                if skill in maxLevel:
                    heappush(maxLevel[skill], (newTeam))
                else:
                    lst = [(newTeam)]
                    heapq.heapify(lst)
                    maxLevel[skill] = [(newTeam)]
                break
            smallestTeam = heappop(possibleTeams)
            canAdd, overridden = smallestTeam.canAdd(skill)
        
        
        if not canAdd:
            #print(teams)
            #print(maxLevel)
            #print(minLevel)
            continue
        smallestTeam.add(skill)
        if overridden < skill:
            #print("Removing {} from maxLevel {}".format(smallestTeam, skill - 1))
            #maxLevel[skill - 1].remove(smallestTeam)
            if skill in maxLevel:
                heappush(maxLevel[skill], (smallestTeam))
            else:
                lst = [(smallestTeam)]
                heapq.heapify(lst)
                maxLevel[skill] = [(smallestTeam)]
        else:
            #print("Removing {} from minLevel {}".format(smallestTeam, skill + 1))
            #minLevel[skill + 1].remove(smallestTeam)
            if skill in minLevel:
                heappush(minLevel[skill], (smallestTeam))
            else:
                lst = [(smallestTeam)]
                heapq.heapify(lst)
                minLevel[skill] = [(smallestTeam)]
        #print(teams)
        #print(maxLevel)
        #print(minLevel)
    return min(teams, key = lambda team: team.size).size
    

testCases = int(input().strip())
for test in range(testCases):
    values = list(map(int, input().strip().split(' ')))
    if values[0] == 0:
        print(0)
        continue
    skillLevels = sorted(values[1:])
    #if test != 15:
    #    continue
    #print(skillLevels)
    print(splitTeams(skillLevels))