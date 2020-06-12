from flask import Flask, redirect, render_template, request, url_for

from flaskr.db_connection import DBConnection
from flaskr.query import Query


def create_app():
    app = Flask(__name__)
    db_connection = DBConnection("root", "0", "127.0.0.1", "giardino_botanico")
    db_connection.connect()

    @app.route("/")
    def home():
        data: list = Query(db_connection).get_all_plants_type()
        json: dict = {}
        for plant in data:
            json[plant.nome_pianta] = data.index(plant)
        args: dict = {
            "data": data,
            "json": json,
        }
        return render_template("pages/home_page.html", **args)

    @app.route("/search")
    def search():
        search: str = request.args.get("search")
        data: list = Query(db_connection).get_plants_from_name(search)
        return render_template("pages/search_page.html", data=data)

    @app.route("/detail/id_pianta=<plant_id>")
    def detail(plant_id: str):
        data: list = Query(db_connection).get_specific_plant_from_id(plant_id)
        return render_template("pages/detail_page.html", data=data)

    @app.route("/admin/login")
    def admin_login():
        pass

    @app.route("/admin")
    def admin():
        return render_template("pages/admin_page.html")

    @app.route("/admin/add_plant")
    def add_plant():
        plant_types: list = Query(db_connection).get_all_plant_types()
        garden_zones: list = Query(db_connection).get_garden_zones()
        args: dict = {
            "plant_types": plant_types,
            "garden_zones": garden_zones,
        }
        return render_template("pages/admin_add_plant_page.html", **args)

    @app.route("/admin/added_plant", methods=["GET", "POST"])
    def added_plant():
        if request.method == "POST":
            result = request.form
            Query(db_connection).add_plant(result)
            return render_template("pages/success_form_page.html")

    return app
