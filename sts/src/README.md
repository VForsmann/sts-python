# Interna

## Visualisierung

### Graphen

Ein Graph kann mit der `<graph-component>` Komponente dargestellt werden.

`<graph-component [data]="Name.html [height]="'500px'" [widht]="'500px'"></graph-component>`

Die Name.html muss ein durch Python generierter HTML Graph im Verzeichnis: `sts_fallstudie__python/graphs/html/htmlGraphs` sein
`height` und `width` sind normale im String gehaltene CSS Propertys, welche für korrekte Darstellung übergeben werden sollten.
### Sidebar und Navigation

Die Sidebar agiert komplett automatisch.
Wenn ein Element Teil der Sidebar werden soll (Hierzu am besten Textelemente wie `h1` verwenden), dann kann dem Element die Klasse `navPoint-l` oder `navPoint-sm` gegeben werden. Welche Klasse bestimmt ob "Überpunkt" oder "Unterpunkt".

`<h1 class="navPoint-l">Einführung</h1>`

sorgt für einen automatischen Eintrag in der Sidebar.

Ein Eintrag in der Sidebar ist ebenfalls `smooth-scrollable`