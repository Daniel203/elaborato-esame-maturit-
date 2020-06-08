class Plant:
    nome_pianta: str
    nome_pianta_latino: str
    specie: str
    visitabile: bool
    zona_giardino: int

    def __init__(
        self,
        nome_pianta: str,
        nome_pianta_latino: str,
        specie: str,
        visitabile: bool,
        zona_giardino: int,
    ):
        self.nome_pianta = nome_pianta
        self.nome_pianta_latino = nome_pianta_latino
        self.specie = specie
        self.visitabile = visitabile
        self.zona_giardino = zona_giardino
