import mysql.connector

from flaskr.models.plant import Plant


class Query:

    db_cursor: mysql.connector.cursor.MySQLCursor

    def __init__(self, db_connection):
        self.db_cursor = db_connection.get_cursor()

    def _execute_query(self, query: str) -> mysql.connector.cursor.MySQLCursor:
        if self.db_cursor is not None:
            try:
                self.db_cursor.execute(query)

            except mysql.connector.Error as err:
                print(f"Errore {err}")

    def _parse_data(self) -> list:
        if self.db_cursor is not None:
            plants: list = []
            for (
                nome_pianta,
                nome_pianta_latino,
                nome_specie,
                visitabile,
                numero_zona,
            ) in self.db_cursor:
                plants.append(
                    Plant(
                        nome_pianta,
                        nome_pianta_latino,
                        nome_specie,
                        visitabile,
                        numero_zona,
                    )
                )

            return plants
        return []

    def get_all_plants(self) -> list:
        QUERY: str = """
SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie,
zg.visitabile, zg.numero_zona
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
ORDER BY tp.nome_pianta
        """
        self._execute_query(QUERY)
        data: list = self._parse_data()
        return data

    def get_specific_plant(self, plant_name: str) -> list:
        QUERY: str = f"""
SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie,
zg.visitabile, zg.numero_zona
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
WHERE tp.nome_pianta = "{plant_name}"
ORDER BY tp.nome_pianta
        """
        self._execute_query(QUERY)
        data: list = self._parse_data()
        return data

    def get_specific_plant_complete_details(self, plant_name: str) -> list:
        QUERY: str = f"""
SELECT tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie,
zg.visitabile, zg.numero_zona, p.giorno_piantumazione, p.viva
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
WHERE tp.nome_pianta = "{plant_name}"
ORDER BY tp.nome_pianta
        """
        self._execute_query(QUERY)
        data: list = self._parse_data()
        return data
