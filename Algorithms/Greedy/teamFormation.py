import heapq
from heapq import heappush, heappop, heapify

class Team:
    def __init__(self, skillLevel, id):
        self.id = id
        self.size = 1
        self.minLevel = skillLevel
        self.maxLevel = skillLevel

    def add(self, skillLevel):
        self.minLevel = min(self.minLevel, skillLevel)
        self.maxLevel = max(self.maxLevel, skillLevel)
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

class BoundaryDictionary:
    def __init__(self):
        self.allTeams = []
        self.maxLevel = {}
        self.minLevel = {}

    def getTeamsThatCanAddSkillLevel(self, skillLevel):
        teamSet = self.getTeamsWithMaxSkillBoundary(skillLevel - 1).union(self.getTeamsWithMinSkillBoundary(skillLevel + 1))
        teamHeap = list(teamSet)
        heapify(teamHeap)
        return teamHeap

    def getTeamsWithMaxSkillBoundary(self, boundary):
        if boundary in self.maxLevel:
            return self.maxLevel[boundary]
        return set()

    def getTeamsWithMinSkillBoundary(self, boundary):
        if boundary in self.minLevel:
            return self.minLevel[boundary]
        return set()

    def addTeamWithSkillLevel(self, skillLevel):
        newTeam = Team(skillLevel, len(self.allTeams))
        self.allTeams.append(newTeam)
        self.addToInnerDictionary(newTeam, skillLevel, self.minLevel)
        self.addToInnerDictionary(newTeam, skillLevel, self.maxLevel)

    def updateMaxSkillBoundary(self, team):
        previousBoundaryList = self.maxLevel[team.maxLevel - 1]
        previousBoundaryList.remove(team)
        self.addToInnerDictionary(team, team.maxLevel, self.maxLevel)

    def updateMinSkillBoundary(self, team):
        previousBoundaryList = self.minLevel[team.minLevel + 1]
        previousBoundaryList.remove(team)
        self.addToInnerDictionary(team, team.minLevel, self.minLevel)

    def addToInnerDictionary(self, team, skillLevel, innerDictionary):
        if skillLevel in innerDictionary:
            self.minLevel[skillLevel].add(team)
        else:
            innerDictionary[skillLevel] = set({team})

def splitTeams(skillLevels):
    boundaryDictionary = BoundaryDictionary()
    for skillLevel in skillLevels:
        teamsThatCanAddSkillLevel = boundaryDictionary.getTeamsThatCanAddSkillLevel(skillLevel)
        if len(teamsThatCanAddSkillLevel) == 0:
            boundaryDictionary.addTeamWithSkillLevel(skillLevel)
            continue

        smallestTeam = heappop(teamsThatCanAddSkillLevel)
        smallestTeam.add(skillLevel)
        if smallestTeam.maxLevel == skillLevel:
            boundaryDictionary.updateMaxSkillBoundary(smallestTeam)
        else:
            boundaryDictionary.updateMinSkillBoundary(smallestTeam)
    return min(boundaryDictionary.allTeams, key = lambda team: team.size).size






def splitTeams2(skillLevels):
    teams = []
    maxLevel = {}
    minLevel = {}
    for skill in skillLevels:
        possibleTeams = []
        if skill - 1 in maxLevel:
            possibleTeams += maxLevel[skill - 1]
        if  skill + 1 in minLevel:
            possibleTeams += minLevel[skill - 1]

        # heapq.heapify(possibleTeams)
        # if len(possibleTeams) == 0:
        #     newTeam = Team(id, skill)
        #     id += 1
        #     teams.append(newTeam)
        #     if skill in minLevel:
        #         heappush(minLevel[skill], (newTeam))
        #     else:
        #         lst = [(1, newTeam)]
        #         heapq.heapify(lst)
        #         minLevel[skill] = [(newTeam)]
        #     if skill in maxLevel:
        #         heappush(maxLevel[skill], (newTeam))
        #     else:
        #         lst = [(newTeam)]
        #         heapq.heapify(lst)
        #         maxLevel[skill] = [(newTeam)]
        #     continue

        smallestTeam = heappop(possibleTeams)
        canAdd, overridden = smallestTeam.canAdd(skill)
        while not canAdd:
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
                break
            smallestTeam = heappop(possibleTeams)
            canAdd, overridden = smallestTeam.canAdd(skill)

        if not canAdd:
            continue
        smallestTeam.add(skill)
        if overridden < skill:
            if skill in maxLevel:
                heappush(maxLevel[skill], (smallestTeam))
            else:
                lst = [(smallestTeam)]
                heapq.heapify(lst)
                maxLevel[skill] = [(smallestTeam)]
        else:
            if skill in minLevel:
                heappush(minLevel[skill], (smallestTeam))
            else:
                lst = [(smallestTeam)]
                heapq.heapify(lst)
                minLevel[skill] = [(smallestTeam)]
    return min(teams, key = lambda team: team.size).size


testCases = int(input().strip())
for test in range(testCases):
    #values = list(map(int, input().strip().split(' ')))
    values = [1, 1, 2, 3, 1, 2, 3, 2, 3]
    if values[0] == 0:
        print(0)
        continue
    skillLevels = sorted(values[1:])
    #if test != 15:
    #    continue
    #print(skillLevels)
    print(splitTeams(skillLevels))
