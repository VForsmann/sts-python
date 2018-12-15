import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm as cm

import functions as fn

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

pd.crosstab(data['f3_2'], data['f3_1'], rownames=['f2'], colnames=['f1'])

filtered_data = data[['f4_13', 'f5_7', 'f5_8', 'f5_10', 'f8', 'f9', 'f10_1', 'f10_2', 'f17', 'f18_2', 'f18_3', 'f18_7', 'f18_9', 'f26']]
corr = filtered_data.corr(method='spearman')
filtered_corr = corr[((corr[:] > 0.4) & (corr[:] < 1)) | ((corr[:] < -0.5) & (corr[:] >= -1))].dropna(how='all').dropna(axis='columns', how='all')
plt.matshow(corr)
plt.show()
filtered_corr.to_html('pandas_table.html')
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

# TODO variabel machen und labels anpassen, sodass alle angezeigt werden
fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax1.imshow(corr, interpolation="nearest", cmap=cmap)
ax1.grid(True)
plt.title('Corr')
labels = ['f4_13', 'f5_7', 'f5_8', 'f5_10', 'f8', 'f9', 'f10_1', 'f10_2', 'f18_2', 'f18_7']
ax1.set_xticklabels(labels, fontsize=8)
ax1.set_yticklabels(labels, fontsize=8)
fig.colorbar(cax)
plt.show()

