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

### Backup-links

Ein Backup link ist ein Element was ins Backup verweist.
Per click-event wird ein scrolling an die Stelle ins Backup betrieben. Um wieder zurück zu navigieren kann auf das Element im Backup geklickt werden - dies führt zu automatischem "zurückscrollen".

Vorgehen dafür:

`<p scrollTo="backupinfo">Test</p>`
scrollt zum Element mit der id `backupinfo`: `<h1 class="navPoint-l" id="backupinfo">Backup-Info</h1>`

Das automatische zurückscrollen ist immer aktiviert, d.h. nach dem klick auf das `p` wird auf dem `h1` ebenfalls ein click-event registriert.
Es ist egal wo diese Elemente stehen, es funktionieren auch scrollings außerhalb des Backups - es ist aber ursprünglich dazu gedacht.

Das automatische zurückscrollen entfällt nach einmaligem klicken.