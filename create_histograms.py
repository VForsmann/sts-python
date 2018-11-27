# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Assign filename to variable: file
file = 'daten_robinson.csv'

data = pd.read_csv(file, sep=';', na_values=('Nothing'), error_bad_lines=False)
# not working questions for graph
forbiddenQuestions = [0]
# fragwuerdig 23, 24, 25
for val in list(data):
    isValid = False
    isValid2 = False
    for forb in forbiddenQuestions:
        try:
            val.split('_')[0].index(forb)
            isValid = False
            break
        except:
            isValid = True
            pass
        try:
            val.split('_')[1].index('txt')
            isValid2 = False
            break
        except:
            isValid2 = True
            pass

    if val != 'Ort' and val != 'ID' and isValid and isValid2:
        # range as bins
        upper = pd.DataFrame.max(data[[val]])
        lower = pd.DataFrame.min(data[[val]])
        print(upper)
        try:
            pd.DataFrame.hist(data[[val]], bins=np.arange(int(upper) + 2) - 0.25, width=0.5)
        except:
            print('doesnt work now')
            continue
        plt.xticks(range(int(upper) + 1))

        if int(upper-lower) > 9:
            plt.xticks(rotation=90)

        plt.ylabel('Anzahl')
        plt.xlabel("Auspraegung")
        # plt.show()
        plt.savefig('./graphs/histograms/' + val + '.png')
        print('Image created')
