import pandas as pd

import functions as fn

data = fn.load_data('../data_preparation/data_preparation.csv')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

x = pd.crosstab(data['f3_2'], data['f3_1'], rownames=['f2'], colnames=['f1'])
corr = data.corr(method="spearman")
corr = corr[(corr[:] > 0.5) & (corr[:] < 1)].dropna(how='all').dropna(axis='columns', how='all')
print(corr)


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

