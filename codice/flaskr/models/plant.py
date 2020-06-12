import datetime


class Plant:
    id: int
    nome_pianta: str
    nome_pianta_latino: str
    specie: str
    visitabile: bool
    zona_giardino: int
    inizio_fioritura: str
    fine_fioritura: str
    giorno_piantumazione: str
    acqua_necessaria: str
    mauntenzione_necessaria: str
    viva: bool
    immagine: str

    def __init__(
        self,
        id: int,
        nome_pianta: str,
        nome_pianta_latino: str,
        specie: str,
        visitabile: bool,
        zona_giardino: int,
        inizio_fioritura: str,
        fine_fioritura: str,
        giorno_piantumazione: str,
        acqua_necessaria: str,
        manutenzione_necessaria: str,
        viva: bool,
        immagine: str,
    ):
        self.id = id
        self.nome_pianta = nome_pianta
        self.nome_pianta_latino = nome_pianta_latino
        self.specie = specie
        self.visitabile = visitabile
        self.zona_giardino = zona_giardino
        self.inizio_fioritura = inizio_fioritura
        self.fine_fioritura = fine_fioritura
        self.giorno_piantumazione = self._format_date(giorno_piantumazione)
        self.acqua_necessaria = acqua_necessaria
        self.manutenzione_necessaria = manutenzione_necessaria
        self.viva = viva
        self.immagine = immagine

    @staticmethod
    def _format_date(date_no_formatted) -> str:
        formatted_datetime = date_no_formatted.strftime("%d %m %Y")
        return formatted_datetime
