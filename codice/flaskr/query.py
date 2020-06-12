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
                id_pianta,
                nome_pianta,
                nome_pianta_latino,
                nome_specie,
                visitabile,
                numero_zona,
                inizio_fioritura,
                fine_fioritura,
                giorno_piantumazione,
                acqua_necessaria,
                manutenzione_necessaria,
                viva,
                immagine,
            ) in self.db_cursor:
                plants.append(
                    Plant(
                        id_pianta,
                        nome_pianta,
                        nome_pianta_latino,
                        nome_specie,
                        visitabile,
                        numero_zona,
                        inizio_fioritura,
                        fine_fioritura,
                        giorno_piantumazione,
                        acqua_necessaria,
                        manutenzione_necessaria,
                        viva,
                        immagine,
                    )
                )

            return plants
        return []

    def get_all_plants_type(self) -> list:
        QUERY: str = """
SELECT p.id_pianta, tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie,
zg.visitabile, zg.numero_zona, tp.inizio_fioritura, tp.fine_fioritura,
p.giorno_piantumazione, tp.acqua_necessaria, tp.manutenzione_necessaria,
p.viva, p.immagine
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
GROUP BY tp.nome_pianta
ORDER BY tp.nome_pianta
        """
        self._execute_query(QUERY)
        data: list = self._parse_data()
        return data

    def get_plants_from_name(self, plant_name: str) -> list:
        QUERY: str = f"""
SELECT p.id_pianta, tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie,
zg.visitabile, zg.numero_zona, tp.inizio_fioritura, tp.fine_fioritura,
p.giorno_piantumazione, tp.acqua_necessaria, tp.manutenzione_necessaria,
p.viva, p.immagine
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
WHERE tp.nome_pianta = "{plant_name}"
ORDER BY tp.nome_pianta
        """
        self._execute_query(QUERY)
        data: list = self._parse_data()
        return data

    def get_specific_plant_from_id(self, plant_id: str) -> list:
        QUERY: str = f"""
SELECT p.id_pianta, tp.nome_pianta, tp.nome_pianta_latino, tp.nome_specie,
zg.visitabile, zg.numero_zona, tp.inizio_fioritura, tp.fine_fioritura,
p.giorno_piantumazione, tp.acqua_necessaria, tp.manutenzione_necessaria,
p.viva, p.immagine
FROM TipologiaPianta AS tp
INNER JOIN Pianta AS p ON p.tipologia_pianta = tp.id_tipo_pianta
INNER JOIN ZonaGiardino as zg ON p.zona_giardino = zg.id_zona
WHERE p.id_pianta = "{plant_id}"
        """
        self._execute_query(QUERY)
        data: list = self._parse_data()
        return data
