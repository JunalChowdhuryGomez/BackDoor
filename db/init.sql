-- creacion de la tabla
CREATE TABLE IF NOT EXISTS stions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    option_1 TEXT NOT NULL,
    option_2 TEXT NOT NULL,
    option_3 TEXT NOT NULL,
    option_4 TEXT NOT NULL,
    correct_option_index INT NOT NULL CHECK (correct_option_index BETWEEN 0 AND 3),
    difficulty INT NOT NULL CHECK (difficulty BETWEEN 1 AND 3)
);

--  preguntas de prueba
-- preguntas nivel 1
INSERT INTO stions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('En  año se proclamo la Independencia del Peru', '1810', '1821', '1835', '1840', 1, 1),
('Quien fue el primer presidente del Peru', 'Simon Bolivar', 'Jose de San Martin', 'Jose de la Riva-Agüero', 'Ramon Castilla', 2, 1),
(' civilizacion antigua construyo Machu Picchu', 'Chavin', 'Moche', 'Inca', 'Nazca', 2, 1),
('Cuál fue la capital del Imperio Inca', 'Lima', 'Cusco', 'Arequipa', 'Trujillo', 1, 1),
(' conquistador lidero la caida del Imperio Inca', 'Hernán Cortes', 'Francisco Pizarro', 'Diego de Almagro', 'Pedro de Valdivia', 1, 1),
(' batalla sello la independencia del Peru', 'Ayacucho', 'Junin', 'Tarapacá', 'Angamos', 0, 1),
(' presidente peruano abolio la esclavitud', 'Ramon Castilla', 'Andres Avelino Cáceres', 'Nicolás de Pierola', 'Augusto B. Leguia', 0, 1),
(' recurso fue clave en la economia del Virreinato del Peru', 'Oro', 'Plata', 'Petroleo', 'Cobre', 1, 1),
(' pais invadio las Islas Chincha en 1864', 'Chile', 'España', 'Ecuador', 'Gran Bretaña', 1, 1),
(' tratado puso fin a la Guerra del Pacifico', 'Tratado de Ancon', 'Tratado de Lima', 'Tratado de Paz con Chile', 'Tratado de Guayaquil', 0, 1);

-- preguntas nivel 2
INSERT INTO stions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
(' rebelion indigena fue liderada por Tupac Amaru II', 'Rebelion de Huánuco', 'Gran Rebelion de 1780', 'Revolucion de Tacna', 'Sublevacion de Huaraz', 1, 2),
(' presidente implemento el "Oncenio" en el Peru', 'oscar R. Benavides', 'Augusto B. Leguia', 'Manuel Prado', 'Fernando Belaunde', 1, 2),
(' conflicto armado enfrento a Peru y Ecuador en 1941', 'Guerra del Cenepa', 'Guerra del Pacifico', 'Guerra de Zarumilla', 'Guerra del 41', 3, 2),
(' heroe naval peruano murio en el Combate de Angamos', 'Miguel Grau', 'Francisco Bolognesi', 'Alfonso Ugarte', 'Andres Avelino Cáceres', 0, 2),
(' cultura preinca construyo las Lineas de Nazca', 'Paracas', 'Nazca', 'Moche', 'Chimu', 1, 2),
(' virrey del Peru fue el más destacado', 'Virrey Toledo', 'Virrey Pezuela', 'Virrey La Serna', 'Virrey Abascal', 0, 2),
('En  año se dio el "Baguazo"', '2007', '2009', '2011', '2013', 1, 2),
(' grupo terrorista fue liderado por Abimael Guzmán', 'MRTA', 'Sendero Luminoso', 'Movimiento Revolucionario', 'Vanguardia Revolucionaria', 1, 2),
(' batalla fue clave en la Guerra del Pacifico', 'Batalla de Arica', 'Batalla de Huamachuco', 'Batalla de Miraflores', 'Batalla de Tarapacá', 2, 2),
(' presidente peruano fue derrocado por Fujimori en 1992', 'Alan Garcia', 'Valentin Paniagua', 'Alberto Fujimori', 'Fernando Belaunde', 0, 2);

-- preguntas nivel 3
INSERT INTO stions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
(' lider indigena resistio en la "Breña" durante la Guerra del Pacifico', 'Miguel Iglesias', 'Lizardo Montero', 'Andres A. Cáceres', 'Francisco Garcia Calderon', 2, 3),
(' tratado cedio Tarapacá a Chile despues de la Guerra del Pacifico', 'Tratado de Lima', 'Tratado de Ancon', 'Tratado de Valparaiso', 'Tratado de Paz y Amistad', 1, 3),
(' presidente peruano nacionalizo el petroleo en 1968', 'Fernando Belaunde', 'Juan Velasco Alvarado', 'Francisco Morales Bermudez', 'Manuel Prado', 1, 3),
(' cultura preinca es conocida por sus "huacos retratos"', 'Chavin', 'Moche', 'Chimu', 'Paracas', 1, 3),
(' batalla marco el fin de la Confederacion Peru-Boliviana', 'Yungay', 'Ingavi', 'Ayacucho', 'Junin', 0, 3),
(' lider del MRTA murio en la toma de la residencia del embajador de Japon', 'Nestor Cerpa Cartolini', 'Victor Polay Campos', 'Oscar Ramirez Durand', 'Abimael Guzmán', 0, 3),
(' virrey intento sofocar la Rebelion de Tupac Amaru II', 'Virrey Amat', 'Virrey Jáuregui', 'Virrey Abascal', 'Virrey Pezuela', 1, 3),
(' heroe civil peruano murio defendiendo el Morro de Arica', 'Alfonso Ugarte', 'Francisco Bolognesi', 'Miguel Grau', 'Andres A. Cáceres', 1, 3),
('En  gobierno se creo el Sol (nuevo sol) como moneda oficial', 'Alan Garcia (1985)', 'Alberto Fujimori (1991)', 'Alejandro Toledo (2001)', 'Fernando Belaunde (1980)', 1, 3),
(' arologo descubrio la ciudadela de Caral', 'Julio C. Tello', 'Ruth Shady', 'Walter Alva', 'Luis Lumbreras', 1, 3);
