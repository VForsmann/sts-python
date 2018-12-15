import matplotlib.pyplot as plt
import pandas as pd

import functions as fn

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

pd.crosstab(data['f3_2'], data['f3_1'], rownames=['f2'], colnames=['f1'])

filtered_data = data[['f4_13', 'f5_7', 'f5_8', 'f5_10', 'f8', 'f9', 'f10_1', 'f10_2', 'f17', 'f18_2', 'f18_3', 'f18_7', 'f18_9', 'f26']]
corr = filtered_data.corr(method='spearman')
corr = corr[((corr[:] > 0.4) & (corr[:] < 1)) | ((corr[:] < -0.5) & (corr[:] >= -1))].dropna(how='all').dropna(axis='columns', how='all')
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

