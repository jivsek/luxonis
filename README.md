# Luxonis: sreality scraper

This project scrapes the first 500 flats from https://www.sreality.cz/ and saves them to a Postgresql database. It then displays them on a simple website.

## Note

When you run the code outside of docker it works fine, the flats are saved to a db and displayed on localhost:8080. When building a docker image I ran into a problem when creating a webpage request which I wasn't able to resolve https://github.com/psf/requests-html/issues/52.

## Run the code without docker

1. Create a venv and run `pip install -r requirements.txt`
2. Run the bash script to create the database with `./create_database.sh`
3. Run the scraping script with `python app/r_html.py`
4. Run the app with `python app/app.py` or `flask run -h localhost -p 8080` inside the /app folder

You can view the scraped items on `localhost:8080`
