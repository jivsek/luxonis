import json
import psycopg2
from requests_html import HTMLSession
from itertools import groupby

url = 'https://www.sreality.cz/en/search/for-sale/apartments'

f = open("flats.json", "x")
f = open("images.json", "x")
f = open("data.json", "x")

images_dict = {}
titles_dict = {}
result = {}

for j in range(25):
    page_url = f"{url}url?page={j+1}"

    s = HTMLSession()
    r = s.get(page_url)
    r.html.render(sleep=2)

    flat_ads = r.html.xpath('//*[@id="page-layout"]/div[2]/div[3]/div[3]/div/div/div/div/div[3]/div', first=True)

    titles = flat_ads.find('div.text-wrap')

    property_lists = r.html.find('div.dir-property-list')

    # Extract the 'src' attribute for all <img> tags in each property list
    img_srcs = []
    for prop_list in property_lists:
        imgs = prop_list.find('img')
        for img in imgs:
            if "ffffff" not in img.attrs['src']:
                img_srcs.append(img.attrs['src'])

    # Split the image urls into seperate list
    apartments_images = [list(group) for key, group in groupby(img_srcs, lambda x: x == '/img/camera.svg') if not key]

    # Create a dictionary with apartment images 
    for i, images in enumerate(apartments_images):
        url_json = json.dumps(images)
        images_dict[(j*20)+i] = url_json
    
    # Create a dictionary with apartment titles
    for i, title in enumerate(titles):
        titles_dict[(j*20)+i] = title.text
        
# Write the images dictionary to a JSON file
with open('images.json', 'a') as f:
    json.dump(images_dict, f, indent=4)

# Write the dictionary to a JSON file
with open('flats.json', 'a') as f:
    json.dump(titles_dict, f, indent=4)


# Insert the data into the database
with open('flats.json', 'r') as f:
    flat_titles = json.load(f)

with open('images.json', 'r') as f:
    flat_images = json.load(f)

# combine the two JSON files
for key in flat_titles:
    try:
        result[flat_titles[key]] = flat_images[key]
    except:
        result[flat_titles[key]] = []
        

# write out the combined JSON to a new file
with open('data.json', 'a') as f:
    json.dump(result, f)

# Connect to database
conn = psycopg2.connect(
    dbname="sreality",
    user="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create a new table if it doesn't exist to store the JSON data
cur.execute("""
    CREATE TABLE IF NOT EXISTS apartments (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        images JSONB
    );
""")

# Load the JSON data from file
with open("data.json", "r") as f:
    data = json.load(f)


for title, images in data.items():    
    cur.execute("""
        INSERT INTO apartments (title, images)
        VALUES (%s, %s);
    """, (title, images))

# Commit the changes to the database and close the cursor and connection
conn.commit()
cur.close()
conn.close()

    

