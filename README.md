# Slides

En aquest repositori recollirem slides i presentacions fetes en públic que vinguin en markdown renderitzat.

## Marp

[Marp](https://marp.app/) és un framework en javascript que renderitza presentacions en markdown a HTML o PDF.
Pot incloure LaTeX.

### Maneres de treballar-hi

* VS Code: té una extensió que facilita molt la vida, ja que mostra el preview i permet exportar

* CLI: cal construir la imatge indicada al `docker-compose.yaml`. Per defecte serveix el directori arrel, però es pot modificar el command per a exportar un deckset a HTML.

Amb l'execució de:
```bash
docker-compose up -d
```
se serveix marp amb aquest directori arrel a `localhost:8080`.

## Pandoc

[Pandoc](https://pandoc.org/) és el convertidor universal de documents per excel·lència.


# Deployment instructions

Cal copiar el fitxer exportat a un repositori github pages públic
