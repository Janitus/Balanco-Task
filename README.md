# Balanco-Task

Hakee Ruotsin 10 suosituinta elokuvaa TMDB API:n kautta ja kirjoittaa ne Google Sheetsiin.

## Asennus

```bash
pip install -r requirements.txt
```

## Konfigurointi

1. Kopioi `.env.example` → `.env` ja täytä arvot:
   - `TMDB_API_KEY` — Luo API-avain osoitteessa https://www.themoviedb.org/settings/api
   - `GOOGLE_SHEET_EMAIL` — Sähköpostiosoite, jolle Google Sheet jaetaan
   - `GOOGLE_CREDENTIALS_FILE` — Google Service Account JSON-tiedoston polku (oletus: `credentials.json`)

2. Luo Google Service Account:
   - Avaa [Google Cloud Console](https://console.cloud.google.com/)
   - Luo uusi projekti
   - Ota käyttöön **Google Sheets API** ja **Google Drive API**
   - Luo **Service Account** ja lataa JSON-avaintiedosto nimellä `credentials.json` projektin juureen

## Käyttö

```bash
python main.py
```

Skripti tulostaa Google Sheet -linkin, johon tulokset on kirjoitettu.

## Taulukkorakenne

| # | Elokuva | Julkaisupäivä | Suosio | Arvosana | Äänimäärä |
|---|---------|---------------|--------|----------|-----------|
| 1 | ...     | ...           | ...    | ...      | ...       |

Taulukon lopussa on myös ajankäyttöosio, johon merkitään aika minuutteina.
