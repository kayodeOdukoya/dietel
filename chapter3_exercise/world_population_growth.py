world_population =  8_000_000_000
growth_rate = 9

print("YEAR         ANTICIPATED-P             NUMERICAL-INCREASE")
for year in range(1,  101):
    numerical_increase = growth_rate  / 100 * world_population
    world_population = world_population  + numerical_increase
    print("{0:4d}      {1:.2f}                    {2:.2f}" .format(year, world_population, numerical_increase))