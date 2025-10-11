population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

possible = True

while True:
    below_min = [i for i, x in enumerate(population) if x < minimum_wealth]
    if not below_min:  # everyone has at least minimum
        break

    richest_index = population.index(max(population))
    poorest_index = below_min[0]  # fix the first below minimum

    needed = minimum_wealth - population[poorest_index]

    if population[richest_index] - needed >= minimum_wealth:
        population[richest_index] -= needed
        population[poorest_index] += needed
    else:
        possible = False
        break

if possible:
    print(population)
else:
    print("No equal distribution possible")