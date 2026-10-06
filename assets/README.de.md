# Medien

Öffentliche Markenmedien, Diagramme und Präsentationsgrafiken der UNITERA-Dokumentation.
Architekturdiagramme bleiben vorzugsweise Mermaid in Markdown.

## Aktuelle Markenmedien — 6. Oktober 2026

Die Markenmedien stammen aus dem vom Owner bereitgestellten Asset-Paket.
Importierte SVG-Originale sind unveränderte Kopien. Abgeleitete Varianten sind
unten gesondert beschrieben. Die Einbindung ist eine visuelle Aktualisierung;
sie erzeugt keine fachliche Adoption, Berechtigung oder Produktreife.

| Medium | Verwendung |
|---|---|
| [UNITERA OS Wortmarke](identity/os/svg/unitera_os_wordmark_light.svg) | Produktname auf den Einstiegsseiten. |
| [Kranich Hero](identity/os/masters/svg/unitera-crane-hero-graphite.svg) | Großes Emblem auf der Repository-Startseite und in beiden Sprachausgaben. |
| [Kranich Glyph](identity/os/masters/svg/unitera-crane-glyph-graphite.svg) | Kompaktes Emblem für mittlere Darstellungsgrößen. |
| [Kranich Micro](identity/os/masters/svg/unitera-crane-micro-graphite.svg) | Vereinfachtes Emblem für Favicons und kleinste Darstellungen. |
| UNITERA Systems Wortmarke und Zeichen | Firmenidentität; bleibt von Produktwortmarke und Kranich getrennt. |

Die Einstiegsseiten verwenden SVG statt der bisherigen großen PNG-Medien.
Die Farbschema-Auswahl verwendet Graphite auf hellem und Ivory auf dunklem
Hintergrund. Alle gelieferten Hero-, Glyph- und Micro-Varianten liegen unter
`identity/os/masters/svg/`, einschließlich der neutralen `currentColor`-Quellen.
Ein separat eingebundenes SVG erbt die Textfarbe seiner umgebenden Seite nicht;
deshalb verwenden die Einstiegsseiten die fest eingefärbten Varianten.

## Abgeleitete Varianten

- Die dunkle OS-Wortmarke ist aus der gelieferten hellen Wortmarke abgeleitet:
  ausschließlich die UNITERA-Textfarbe wechselt von Graphite zu Ivory;
  Geometrie, Typografie und OS-Akzent bleiben gleich.
- Die Favicons verwenden die gelieferte Micro-Silhouette. PNG und ICO zeigen
  Graphite auf einer Ivory-Fläche. Das zusätzliche SVG-Favicon passt seine
  Farbe dem Farbschema an; das Safari-Zeichen ist monochrom.
- Die ICO-Datei enthält Größen von 16, 32 und 48 Pixeln; die PNG-Dateien liegen
  in denselben Größen vor.

## GitBook-Medien

Beide Sprachausgaben enthalten identische Kopien unter
`docs/<lang>/.gitbook/assets/brand/`: OS-Wortmarken, Hero/Glyph/Micro in Graphite
und Ivory, Systems-Medien und `platform-icons/favicon/`.

Die im Paket enthaltenen Systems-Dateien sind übernommen. Das helle
Systems-Zeichen und das helle Systems-Lockup sind im Paket nicht enthalten;
ihre bereits vorhandenen Fassungen bleiben gebunden. Die Medienablage ersetzt
keine separat konfigurierte GitBook-Oberflächeneinstellung.

## Iconset

`iconography/20/` enthält 18 Objekt-Icons. `iconography/modifiers/20/` enthält
11 Modifikatoren. Beide Gruppen sind unveränderte SVG-Originale aus dem Paket;
ihre eingebetteten Statuskennzeichnungen bleiben erhalten.

Person, Rolle, Entscheidung, Grant, Receipt und Verification bleiben getrennte
Zeichen. Ein Freigabe-Modifikator bezeichnet keinen Grant; ein Receipt-Icon
beweist kein verifiziertes Ergebnis. Ein Icon erzeugt keine Authority.

Die [Markenhinweise](../legal/TRADEMARKS.md) gelten weiterhin.
