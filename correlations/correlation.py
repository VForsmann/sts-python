import matplotlib.pyplot as plt
import pandas as pd

import functions as fn

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

pd.crosstab(data['f3_2'], data['f3_1'], rownames=['f2'], colnames=['f1'])
# filtered_data = data[[
#     'f1',
#     'f3_2', 'f3_5', 'f3_6', 'f3_8', 'f3_11',
#     'f4_11', 'f4_12', 'f4_13',
#     'f5_1', 'f5_2', 'f5_3', 'f5_4', 'f5_5', 'f5_6', 'f5_7', 'f5_8', 'f5_9',
#     'f6_1', 'f6_2', 'f6_3', 'f6_4', 'f6_5', 'f6_6', 'f6_7', 'f6_8', 'f6_9',
#     'f8',
#     'f9',
#     'f10_1', 'f10_2',
#     'f15_1', 'f15_2', 'f15_3', 'f15_4', 'f15_5', 'f15_6', 'f15_7', 'f15_8', 'f15_9', 'f15_10', 'f15_11', 'f15_12',
#     'f15_13', 'f15_14',
#     'f16_1', 'f16_2', 'f16_3', 'f16_4', 'f16_5', 'f16_6', 'f16_7', 'f16_8', 'f16_9',
#     'f18_2', 'f18_3', 'f18_7', 'f18_8', 'f18_9',
#     'f19_1', 'f19_3', 'f19_10'
# ]]
filtered_data = data
corr = filtered_data.corr(method='spearman')
corr = corr[((corr[:] > 0.4) & (corr[:] < 1)) | ((corr[:] < -0.5) & (corr[:] >= -1))].dropna(how='all').dropna(axis='columns', how='all')
print(corr)
# table = go.Table(
#     header=dict(values=corr.columns,
#                 line=dict(color='#7D7F80'),
#                 fill=dict(color='#a1c3d1'),
#                 align=['left'] * 5),
#     columnwidth=50,
#     cells=dict(values=corr.values,
#                line=dict(color='#7D7F80'),
#                fill=dict(color='#EDFAFF'),
#                align=['left'] * 5))
# table = [table]
plt.matshow(corr)
plt.show()
corr.to_html('pandas_table.html')
html = open('pandas_table.html', 'a')
html.write("""<script>
let tds = document.getElementsByTagName("td");

for (td of tds) {
td.onclick = (event) => {
alert("Spalte: " + getNameOfIndex(event.srcElement.cellIndex) + " Zeile: " + getNameOfIndex(event.srcElement.parentElement.rowIndex));
}
}
function getNameOfIndex(index) {
let ths = document.getElementsByTagName("th")
return (ths[index].innerText);
}
</script>""")

