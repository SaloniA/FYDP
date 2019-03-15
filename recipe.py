#/'/

def getRecipe(protein, fat, carbs):
    """
    Returns the recipe for the GranolaPod machine.

    Params:
    protein: Amount of Protein in grams
    fat: Amount of fat in grams
    carbs: Amount of Carbs in grams

    Max:
    Protein: 9.6
    Fat: 24.48
    Carbs: 49.2

    Returns: (granola, seeds, crans)
    granola: Amount of dispenses (Paddlewheel divisions) for granola
    seeds:   Amount of dispenses for seeds
    crans:   Amount of dispenses for cranberries
    """

    # See https://docs.google.com/spreadsheets/d/1G05H-1YGS_nNvjeI72Ml56ZUtodRG3egraHT0ixtrEo/edit#gid=0
    # for calculation of these values
    recipe = {'granola': 0       * carbs + 0.54114 * protein - 0.21221 * fat,
              'seeds'  : 0       * carbs - 0.10113 * protein + 0.12136 * fat,
              'crans'  : 0.04065 * carbs - 0.30438 * protein + 0.10103 * fat}

    recipe_ints   = {x:round(recipe[x]) for x in recipe.keys()}
    recipe_errors = {x:abs(round(recipe[x]) - recipe[x]) for x in recipe.keys()}
    recipe_errors['granola'] = 5

    sorted_errors = sorted(recipe_errors, key=recipe_errors.__getitem__)

    return (granola, seeds, crans)

def main():
    carbs = 49.2
    protein = 9.6
    fat = 24.48

    order = getRecipe(protein, fat, carbs)
    print(order)

if __name__ == '__main__':
    main()