#/'/
def clamp(x, minimum, maximum):
    return max(minimum, min(x, maximum))

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

    NOTE: This function doesn't work very well since lots of solutions to the system equation involve negative numbers.
          Better solutions do exist that account for this, but ran out of time.

          Don't let user order 0    0   0 or 0   0   12.3
    """

    # Number of total dispenses for the cup
    NUM_DISPENSES = 2


    # See https://docs.google.com/spreadsheets/d/1G05H-1YGS_nNvjeI72Ml56ZUtodRG3egraHT0ixtrEo/edit#gid=0
    # for calculation of these values
    recipe = {'granola': 0       * carbs + 0.54114 * protein - 0.21221 * fat,
              'seeds'  : 0       * carbs - 0.10113 * protein + 0.12136 * fat,
              'crans'  : 0.04065 * carbs - 0.30438 * protein + 0.10103 * fat}

    # Round the value to nearest integer and clamp it to 0 and 2
    recipe_ints   = {x:clamp(int(round(recipe[x])), 0, 2) for x in recipe.keys()}

    # Find the error created by the round and clamp
    recipe_errors = {x:abs(recipe_ints[x] - recipe[x]) for x in recipe.keys()}

    # Sort the errors for each ingredient
    sorted_errors_keys = sorted(recipe_errors, key=recipe_errors.__getitem__)

    # Initialize dispense values
    dispenses = 0
    granola = 0
    seeds = 0
    crans = 0

    # Set the count values to be returns
    for error_key in sorted_errors_keys:
        ing_dispenses = recipe_ints[error_key]

        for i in range(ing_dispenses):
            if error_key == 'granola':
                granola += 1
            elif error_key == 'seeds':
                seeds += 1
            elif error_key == 'crans':
                crans += 1

            dispenses += 1
            if dispenses >= NUM_DISPENSES:
                return (granola, seeds, crans)

    return (granola, seeds, crans)

