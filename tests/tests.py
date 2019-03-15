import pandas as pd

def displayAllTests():

    max_values = {'carbs': 49.2, 'protein': 9.6, 'fat': 24.48}
    NUM_DIVISIONS = 4
    order_no = 0
    d = []

    for i_p in range(NUM_DIVISIONS+1):
        for i_f in range(NUM_DIVISIONS+1):
            for i_c in range(NUM_DIVISIONS+1):
                order_no += 1
                protein = i_p * max_values['protein'] / NUM_DIVISIONS
                fat = i_f * max_values['fat'] / NUM_DIVISIONS
                carbs = i_c * max_values['carbs'] / NUM_DIVISIONS

                granola, seeds, crans = getRecipe(protein, fat, carbs)

                actual_protein = 2.745 * granola + 4.8 * seeds
                actual_fat = 2.2875 * granola + 12.24 * seeds
                actual_carbs = 14.86875 * granola + 5.52 * seeds + 24.6 * crans
                d.append({"Protein(Order)": protein,
                         "Fat(Order)": fat,
                         "Carbs(Order)": carbs,
                         "Protein(Actual)": actual_protein,
                         "Fat(Actual)": actual_fat,
                         "Carbs(Actual)": actual_carbs,
                         "Granola": granola,
                         "Seeds": seeds,
                         "Cranberries": crans,
                         "Total dispenses": granola + seeds + crans})
    columns = ["Protein(Order)",
               "Fat(Order)",
               "Carbs(Order)",
               "Protein(Actual)",
               "Fat(Actual)",
               "Carbs(Actual)",
               "Granola",
               "Seeds",
               "Cranberries",
               "Total dispenses"]

    df = pd.DataFrame(d, columns=columns)
    df['Protein(error)'] = df["Protein(Order)"] - df["Protein(Actual)"]
    df['Fat(error)'] = df["Fat(Order)"] - df["Fat(Actual)"]
    df['Carbs(error)'] = df["Carbs(Order)"] - df["Carbs(Actual)"]


    df.to_csv("combinations.csv")
if __name__ == '__main__':
    displayAllTests()