from os import system
from dataclasses import dataclass
from typing import List
from time import sleep
from random import randint

static = staticmethod

@dataclass
class Stats:
    health: List[float]
    attack: int
    defense: int
@dataclass
class Agent:
    identifier: int
    name: str
    level: int
    stats: Stats

class Combat:

    @static
    def entry(A:int,B:int):
        print("\n ~ Teste combate\n")
        logs: List[str] = []
        rounds = 1
        agentA = "?"
        agentB = "?"
        for agent in GameAgents.register:
            if agent.identifier == A:
                agentA = agent
            if agent.identifier == B:
                agentB = agent
        while True:
            system("cls || clear")
            GameAgents.inspectByID(1)
            GameAgents.inspectByID(2)
            for msg in logs:
                print(msg)
            if rounds % 2 == 0:
                print("Vez de {}".format(agentA.name))
                sleep(1.5)
                multiplier = randint(1,3)
                trueDamage = agentA.stats.attack * multiplier - agentB.stats.defense
                trueDamage += 10
                [targetHealthMax,targetHealthCurrent] = agentB.stats.health
                targetHealthCurrent = targetHealthCurrent - trueDamage
                agentB.stats.health = [targetHealthMax, targetHealthCurrent]
                logs.append("{} causou {} de dano em {}".format(agentA.name,trueDamage,agentB.name))
                if(targetHealthCurrent <= 0):
                    logs.append("{} morreu".format(agentB.name))
                    break
            else:
                print("Vez de {}".format(agentB.name))
                sleep(1.5)
                multiplier = randint(1,3)
                trueDamage = agentB.stats.attack * multiplier - agentA.stats.defense
                trueDamage += 10
                [targetHealthMax,targetHealthCurrent] = agentA.stats.health
                targetHealthCurrent = targetHealthCurrent - trueDamage
                agentA.stats.health = [targetHealthMax, targetHealthCurrent]
                logs.append("{} causou {} de dano em {}".format(agentB.name,trueDamage,agentA.name))
                if(targetHealthCurrent <= 0):
                    logs.append("{} morreu".format(agentA.name))
                    break
            rounds+=1
        system("cls || clear")
        GameAgents.inspectByID(1)
        GameAgents.inspectByID(2)
        for msg in logs:
            print(msg)



class GameAgents:
    idCounter = 1
    register:List[Agent] = []
    def new(name:str, level:int, stats:Stats):
        (_hp,_atk,_defs) = stats
        _stats = Stats([_hp,_hp],_atk,_defs)
        _agent = Agent(GameAgents.idCounter,name,level,_stats)
        GameAgents.register.append(_agent)
        GameAgents.idCounter += 1
    def inspectByID(target: id):
        for agent in GameAgents.register:
            if agent.identifier == target:
                print("_______________________")
                print("Name: {}".format(agent.name))
                print("Level: {}".format(agent.level))
                print("Health: {}".format(agent.stats.health))
                print("Attack: {}".format(agent.stats.attack))
                print("Defense: {}".format(agent.stats.defense))
                print("_______________________")

def testing():
    GameAgents.new("Jogador",1,(100,30,30))
    GameAgents.new("Rato",1,(70,20,20))
    GameAgents.inspectByID(1)
    GameAgents.inspectByID(2)
    Combat.entry(1,2)

def main():
    system("cls || clear")
    testing()

if __name__ == "__main__":
    main()
