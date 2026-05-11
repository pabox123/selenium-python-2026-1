Feature: Buscar un artista en last.fm y validar su ultima fecha de lanzamiento
    Scenario: Validar la fecha del ultimo lanzamiento de Bruno Mars
        Given el usuario se encuentra en last.fm
        When el usuario busca al artista "Bruno Mars"
        And navega al tab de artistas y selecciona el primer resultado
        Then la fecha de su ultimo lanzamiento debe ser "8 May 2026"