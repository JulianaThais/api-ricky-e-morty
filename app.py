from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)
@app.route("/")
def get_list_characters_page():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict= json.loads(data)

    return render_template("characters.html", characters=dict["results"])

@app.route("/profile/<id>")
def get_profile(id):

    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict= json.loads(data)

    return render_template("profile.html", profile=dict)


@app.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "Nome": character["name"],
            "status": character ["status"]
        }

        characters.append(character)

    return{"characters": characters}
#fim 

@app.route("/listaEpisodios")
def get_list_episodes_page():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episodes.html", episodes=dict["results"])

@app.route("/episode/<id>")
def get_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("episode.html", episode=dict)

@app.route("/episode")
def get_list_episodes():

    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes = []

    for episode in dict["results"]:
        episode = {
            "Nome do episódio: " : episode["name"],
            "Data de lançamento: ": episode["air_date"],
            "Código: " : episode["id"]
        }

        episodes.append(episode)

    return{"episodes" : episodes}

#fim 


@app.route("/listaLocalizacao")
def get_list_location_page():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("locations.html", locations=dict["results"])

@app.route("/location/<id>")
def get_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("location.html", location=dict)

@app.route("/location")
def get_list_locations():

    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dict = json.loads(locations)

    locations = []

    for location in dict["results"]:
        location = {
            "Nome : " : location["name"],
            "Tipo: ": location["type"],
            "dimensão: " : location["dimension"]
        }

        locations.append(location)

    return{"locations" : location}