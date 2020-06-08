from flask import Flask, render_template, request

from flaskr.db_connection import DBConnection
from flaskr.query import Query


def create_app():
    app = Flask(__name__)
    db_connection = DBConnection("root", "0", "127.0.0.1", "giardino_botanico")
    db_connection.connect()

    @app.route("/")
    def home():
        data: list = Query(db_connection).get_all_plants()
        json: dict = {}
        for plant in data:
            json[plant.nome_pianta] = data.index(plant)
        args: list = {
            "data": data,
            "json": json,
        }
        return render_template("pages/home_page.html", **args)

    @app.route("/search")
    def search():
        search: str = request.args.get("search")
        data: list = Query(db_connection).get_specific_plant(search)
        return render_template("pages/search_page.html", data=data)

    @app.route("/detail/<plant_name>")
    def detail(plant_name: str):
        data: list = Query(db_connection).get_specific_plant_complete_details(
            plant_name
        )
        return render_template("pages/detail_page.html", data=data)

    return app
