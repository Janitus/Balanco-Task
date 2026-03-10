import os
import requests
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE", "credentials.json")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def fetch_sweden_top10():
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {
        "api_key": TMDB_API_KEY,
        "region": "SE",
        "language": "fi-FI",
        "page": 1,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    movies = response.json()["results"][:10]
    return movies


def write_to_sheet(movies):
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)

    spreadsheet = client.open_by_key(GOOGLE_SHEET_ID)
    sheet = spreadsheet.sheet1

    headers = ["#", "Elokuva", "Julkaisupäivä", "Suosio", "Arvosana", "Äänimäärä"]
    rows = [headers]

    for i, movie in enumerate(movies, start=1):
        rows.append([
            i,
            movie.get("title", ""),
            movie.get("release_date", ""),
            round(movie.get("popularity", 0), 2),
            movie.get("vote_average", 0),
            movie.get("vote_count", 0),
        ])

    # Time tracking section
    rows.append([])
    rows.append(["Ajankäyttö"])
    rows.append(["Vaihe", "Aika (min)"])
    rows.append(["TMDB API-tunnusten luonti", ""])
    rows.append(["Google Credentials luonti", ""])
    rows.append(["Koodaus ja toteutus", ""])
    rows.append(["Yhteensä", ""])

    sheet.update("A1", rows)

    # Bold headers
    sheet.format("A1:F1", {"textFormat": {"bold": True}})
    sheet.format("A13:B13", {"textFormat": {"bold": True}})
    sheet.format("A14:B14", {"textFormat": {"bold": True}})
    sheet.format("A17:B17", {"textFormat": {"bold": True}})

    print(f"Taulukko päivitetty: {spreadsheet.url}")
    return spreadsheet.url


def main():
    print("Haetaan Ruotsin top 10 elokuvat TMDB:stä...")
    movies = fetch_sweden_top10()
    print(f"Löytyi {len(movies)} elokuvaa.")

    print("Kirjoitetaan Google Sheetsiin...")
    url = write_to_sheet(movies)

    print(f"\nValmis! Avaa taulukko: {url}")


if __name__ == "__main__":
    main()
