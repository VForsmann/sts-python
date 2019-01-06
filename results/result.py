import correlations.correlation as corr
import correlations.regression as regr
import functions as fn
import statsmodels.stats.weightstats as tests
import scipy.stats as stat
import clusteranalyse.clusteranalyse as cluster_result

def do(filename):
    data = fn.load_data(filename)

    # 1. Assignment
    # regression for assingment 1
    # 16_3 und 16_8 geloescht wegen Scheinkorrelation
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 1. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    food = ['f4_13', 'f8', 'f9', 'f10_1', 'f10_2', 'f15_8', 'f18_2']
    well_being = 'f18_7'
    food_and_well_being = ['f4_13', 'f8', 'f9', 'f10_1', 'f10_2', 'f15_8', 'f18_2', 'f18_7']
    print('---- correlation ----')
    first_corr = corr.corr_for_prep_data(data[food_and_well_being], filename='first')
    print(first_corr)
    corr.corr_heatmap(first_corr, filename='first')
    print('---- well being - food regression ----')
    regr.reg_for_prep_data(food, well_being, data)
    sport = ['f3_3', 'f3_9']
    well_being = 'f3_2'
    print('---- well being - sport regression ----')
    regr.reg_for_prep_data(sport, well_being, data)

    # 2. Assignment
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 2. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(data['f4_13'][(data['f4_13'] < 8) & (data['f4_13'] > 0)].describe())
    sec_corr = corr.corr_for_prep_data(data[['f4_13', 'f5_7', 'f5_8', 'f5_10', 'f8', 'f9', 'f10_1', 'f10_2', 'f18_2', 'f18_7']], filename='second')
    print(sec_corr)
    # corr.corr_heatmap(sec_corr, filename='second')

    # 3. Assignment
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 3. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    bio_elements = ['f15_1', 'f15_2', 'f15_3', 'f15_4', 'f15_5', 'f15_6', 'f15_7', 'f15_8', 'f15_9', 'f15_10', 'f15_11', 'f15_12', 'f15_13', 'f15_14', 'f15_15', 'f15_16']
    print(data[bio_elements][(data[bio_elements] < 8) & (data[bio_elements] > 0)].describe())

    # 4. Assignment
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 4. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print('Leute, die bereit sind für Bio mehr zu zahlen, würden im Schnitt x mehr zahlen:')
    print(data['f17'][(data['f17'] > 0)].describe())
    print('Leute, die die Frage beantwortet haben:')
    prep_f17 = data['f17'][data['f17'] != 0]
    prep_f17 = prep_f17.replace(-99, 0)
    print(prep_f17.describe())

    # 5. Assignment --> cluster analysis
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 5. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    cluster_result.calculate_cluster()

    # 6. Assignment
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 6. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    bio_food = ['f16_1', 'f16_2', 'f16_3', 'f16_4', 'f16_5', 'f16_6', 'f16_7', 'f16_8', 'f16_9']
    print(data[bio_food][(data[bio_food] < 8) & (data[bio_food] > 0)].describe())

    # 7. Assignment
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - 7. Assignment - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    logos = data[['f12_1', 'f12_2', 'f12_3', 'f12_4', 'f12_5', 'f12_6', 'f12_7', 'f12_8', 'f12_9']]
    print('So oft wurden die einzelnen Bio-Siegel angekreuzt')
    print(fn.sum_characteristics(logos.values))
    print('Platz 1:')
    print(fn.count_values(data, 'f13_1'))
    print('Platz 2:')
    print(fn.count_values(data, 'f13_2'))
    print('Platz 3:')
    print(fn.count_values(data, 'f13_3'))


    # 1. Hypothesentest: Familien mit Kinder bevorzugen Bio-Nahrung ?
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - Hypothesentest 1 - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # Testen auf Normalverteilung
    print(stat.kstest(data['f9'], 'norm'))

    print('Familien mit Kinder bevorzugen Bio-Nahrung?')
    without_child = data['f9'][(data['f2'] == 1) | (data['f2'] == 2)]
    with_child = data['f9'][data['f2'] == 3]
    print(tests.ztest(without_child, with_child))
    with_child = data['f9'][(data['f23_1'] > 0) | (data['f23_2'] > 0) | (data['f23_3'] > 0) | (data['f23_4'] > 0)]
    without_child = data['f9'][(data['f23_1'] == 0) & (data['f23_2'] == 0) & (data['f23_3'] == 0) & (data['f23_4'] == 0)]
    print(tests.ztest(without_child, with_child))

    # 2. Hypothesentest:  Frauen bevorzugen Bio-Nahrung mehr als Männer ?
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - Hypothesentest 2 - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # Testen auf Normalverteilung
    print(stat.kstest(data['f9'], 'norm'))
    print('Frauen bevorzugen Bio-Nahrung mehr als Männer ?')
    male = data['f9'][(data['f21'] == 1)]
    female = data['f9'][(data['f21'] == 2)]
    print(tests.ztest(female, male))

    # 3. Hypothesentest: Familien legen mehr Wert auf touristische Qualitätssiegel
    # als Alleinreisende oder Ehepartner / Freundin ?
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - Hypothesentest 3 - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # Testen auf Normalverteilung
    print(stat.kstest(data['f18_1'], 'norm'))
    print('Familien legen mehr Wert auf touristischen Qualitätssiegel als Alleinreisende oder Ehepartner / Freundin?')
    alone_friends = data['f18_1'][(data['f2'] == 1) | (data['f2'] == 2)]
    family = data['f18_1'][(data['f2'] == 3)]
    print(tests.ztest(alone_friends, family))

    # 4. Hypothesentest:
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - Hypothesentest 4 - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # Testen auf Normalverteilung
    print(stat.kstest(data['f15_14'], 'norm'))
    biobuyer = data['f15_14'][(data['f8'] == 1) | (data['f8'] == 2) | (data['f8'] == 3)]
    nobiobuyer = data['f15_14'][(data['f8'] == 4) | (data['f8'] == 5) | (data['f8'] == 6)]
    print(tests.ztest(biobuyer, nobiobuyer))


    # 5. Hypothesentest: Testen, ob Leute die im Alltag bereits Bio kaufen, im Urlaub bereit sind dafuer mehr zu zahlen
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxx - Hypothesentest 5 - xxxxxxxxxxxxxxxxxxxxxxxxxxx')
    # Testen auf Normalverteilung
    print(stat.kstest(data['f18_2'], 'norm'))
    biobuyer = data['f18_2'][(data['f8'] == 1) | (data['f8'] == 2) | (data['f8'] == 3)]
    nobiobuyer = data['f18_2'][(data['f8'] == 4) | (data['f8'] == 5) | (data['f8'] == 6)]
    print(tests.ztest(biobuyer, nobiobuyer))
