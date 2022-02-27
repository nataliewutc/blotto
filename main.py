import random
import time

'''class BlottoStrat(Strategy):
  def __init__(self, distribution):
    if len(distribution) < 10:
      print("error")
    super.create_offspring(self)'''

class Strategy():
  def __init__(self, distribution):
    self.distribution = distribution
    self.len = len(distribution)

  def __getitem__(self, key):
    return self.distribution[key]

  def create_offspring(self, num_offspring):
    offspring = []
    for off in range(num_offspring):
      gen_method = random.randint(1, 3)
      if gen_method == 1:
        offspring.append(self.offspring_generation1())
      elif gen_method == 2:
        offspring.append(self.offspring_generation2())
      else:
        offspring.append(self.offspring_generation3())
    return offspring

  # move some soldiers between two adjacent castles
  def offspring_generation1(self):
    len_distribution = len(self.distribution)
    offspring = self.distribution.copy()
    random_castle = random.randint(0, len_distribution - 2)
    castle1_migration = random.randint(0, offspring[random_castle])
    castle2_migration = random.randint(0, offspring[random_castle + 1])
    offspring[random_castle] = offspring[random_castle] - castle1_migration + castle2_migration
    offspring[random_castle + 1] = offspring[random_castle + 1] - castle2_migration + castle1_migration
    return Strategy(offspring)

  # swap two adjacent castles
  def offspring_generation2(self):
    len_distribution = len(self.distribution)
    offspring = self.distribution.copy()
    random_castle = random.randint(0, len_distribution - 2)
    temp = offspring[random_castle]
    offspring[random_castle] = offspring[random_castle + 1]
    offspring[random_castle + 1] = temp
    return Strategy(offspring)
    
    

  # subtract 1 soldier from all and add to one random column
  def offspring_generation3(self):
    len_distribution = len(self.distribution)
    offspring = self.distribution.copy()
    migration = 0
    for i in range(len_distribution):
      if offspring[i] > 0:
        offspring[i] -= 1
        migration += 1
    random_castle = random.randint(0, len_distribution - 1)
    offspring[random_castle] += migration
    return Strategy(offspring)

def compare_strat(strat1, strat2):
  if strat1.len != strat2.len:
    raise Exception("")
  streak1 = 0
  streak2 = 0
  score1 = 0
  score2 = 0
  for i in range(strat1.len):
    if strat1[i] > strat2[i]:
      score1 += i + 1
      streak1 += 1
      streak2 = 0
      if streak1 == 3:
        remaining = sum(list(range(i + 2,strat1.len + 1)))
        score1 = score1 + remaining
        break
    elif strat2[i] > strat1[i]:
      score2 += i + 1
      streak1 = 0
      streak2 += 1
      if streak2 == 3:
        remaining = sum(list(range(i + 2,strat2.len + 1)))
        score2 = score2 + remaining
        break
    else:
      streak1 = 0
      streak2 = 0

#   if score1 <= score2:
#     score1 = 0
#   if score2 <= score1:
#     score2 = 0  
    
  return score1, score2

strat1 = Strategy([10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
strat2 = Strategy([12, 18, 0, 10, 5, 15, 7, 11, 11, 11])

def score_strats(strategies):
  num_strats = len(strategies)
  scores = [0] * num_strats
  for strat1_index in range(0, num_strats):
    for strat2_index in range(strat1_index + 1, num_strats):
      strat1 = strategies[strat1_index]
      strat2 = strategies[strat2_index]
      score1, score2 = compare_strat(strat1, strat2)
      scores[strat1_index] = score1
      scores[strat2_index] = score2
  return scores

def get_top_strats(strategies, number_of_winners):
  scores = score_strats(strategies)
  score_strat = list(zip(strategies, scores))
  score_strat.sort(key=lambda x: x[1], reverse=True)
  top_n_score_strats = score_strat[0:number_of_winners]
  return [ss[0] for ss in top_n_score_strats]

def flatten(list_of_lists):
  acc = []
  for l in list_of_lists:
    acc.extend(l)
  return acc

def optimise_single_species(generations=50, offspring=10, num_survivors=50, strats=[]):
  start_time = time.time()
  for x in range(0, generations):
    print(x, time.time() - start_time)
    strats = flatten([s.create_offspring(offspring) for s in strats])
    strats = get_top_strats(strats, num_survivors)
  return strats


strat1 = Strategy([0, 0, 20, 35, 35, 0, 5, 5, 0, 0])
strats1 = strat1.create_offspring(50)
strat2 = Strategy([10, 10, 0, 15, 12, 8, 5, 5, 20, 15])
strats2 = strat2.create_offspring(50)
strat3 = Strategy([10, 0, 20, 0, 30, 0, 20, 0, 10, 10])
strats3 = strat3.create_offspring(50)
strat4 = Strategy([5, 10, 20, 40, 0, 5, 20, 0, 0, 0])
strats4 = strat4.create_offspring(50)

# lets rinse species
species1 = optimise_single_species(strats=strats1)
species2 = optimise_single_species(strats=strats2)
species3 = optimise_single_species(strats=strats3)
species4 = optimise_single_species(strats=strats4)

strats=species1[0:20] + species2[0:10] + species3[0:10] + species4[0:10]
alpha_species = optimise_single_species(generations=80, offspring=7, num_survivors=70,strats=strats)

alpha_species[0].distribution
