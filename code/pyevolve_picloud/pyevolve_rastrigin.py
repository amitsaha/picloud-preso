# Rastrigin function example from PyEvolve framework
# Slight changes to include the CSV DB Adapter

from pyevolve import GSimpleGA
from pyevolve import G1DList
from pyevolve import Mutators, Initializators
from pyevolve import Selectors
from pyevolve import Consts
from pyevolve import DBAdapters
import math

# This is the Rastrigin Function, a deception function
def rastrigin(genome):
   n = len(genome)
   total = 0
   for i in xrange(n):
      total += genome[i]**2 - 10*math.cos(2*math.pi*genome[i])
   return (10*n) + total

def run_ga(seed, runid):
   # Genome instance
   genome = G1DList.G1DList(20)
   genome.setParams(rangemin=-5.2, rangemax=5.30, bestrawscore=0.00, rounddecimal=2)
   genome.initializator.set(Initializators.G1DListInitializatorReal)
   genome.mutator.set(Mutators.G1DListMutatorRealGaussian)

   genome.evaluator.set(rastrigin)

   # Genetic Algorithm Instance

   ga = GSimpleGA.GSimpleGA(genome,seed) #initialize with seed 'seed'
   ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
   ga.setMinimax(Consts.minimaxType["minimize"])
   ga.setGenerations(3000)
   ga.setCrossoverRate(0.8)
   ga.setPopulationSize(20)
   ga.setMutationRate(0.06)
   
   # set elitism
   ga.setElitism(True)
   ga.setElitismReplacement(1)
   

   # CSV Adapater
   csv_adapter = DBAdapters.DBFileCSV(identify=str(runid), filename="stats_" + str(runid) +".csv")
   ga.setDBAdapter(csv_adapter)

   # evolve
   ga.evolve(freq_stats=50)
