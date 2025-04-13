-- creacion de la tabla
CREATE TABLE IF NOT EXISTS questions (
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
INSERT INTO questions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('En que año se proclamó la Independencia del Perú', '1810', '1821', '1835', '1840', 1, 1),
('Quien fue el primer presidente del Perú', 'Simón Bolívar', 'Jose de San Martín', 'Jose de la Riva-Agüero', 'Ramón Castilla', 2, 1),
('Que civilización antigua construyó Machu Picchu', 'Chavín', 'Moche', 'Inca', 'Nazca', 2, 1),
('Cuál fue la capital del Imperio Inca', 'Lima', 'Cusco', 'Arequipa', 'Trujillo', 1, 1),
('Que conquistador lideró la caída del Imperio Inca', 'Hernán Cortes', 'Francisco Pizarro', 'Diego de Almagro', 'Pedro de Valdivia', 1, 1),
('Que batalla selló la independencia del Perú', 'Ayacucho', 'Junín', 'Tarapacá', 'Angamos', 0, 1),
('Que presidente peruano abolió la esclavitud', 'Ramón Castilla', 'Andres Avelino Cáceres', 'Nicolás de Pierola', 'Augusto B. Leguía', 0, 1),
('Que recurso fue clave en la economía del Virreinato del Perú', 'Oro', 'Plata', 'Petróleo', 'Cobre', 1, 1),
('Que país invadió las Islas Chincha en 1864', 'Chile', 'España', 'Ecuador', 'Gran Bretaña', 1, 1),
('Que tratado puso fin a la Guerra del Pacífico', 'Tratado de Ancón', 'Tratado de Lima', 'Tratado de Paz con Chile', 'Tratado de Guayaquil', 0, 1);

-- preguntas nivel 2
INSERT INTO questions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('Que rebelión indígena fue liderada por Túpac Amaru II', 'Rebelión de Huánuco', 'Gran Rebelión de 1780', 'Revolución de Tacna', 'Sublevación de Huaraz', 1, 2),
('Que presidente implementó el "Oncenio" en el Perú', 'Óscar R. Benavides', 'Augusto B. Leguía', 'Manuel Prado', 'Fernando Belaúnde', 1, 2),
('Que conflicto armado enfrentó a Perú y Ecuador en 1941', 'Guerra del Cenepa', 'Guerra del Pacífico', 'Guerra de Zarumilla', 'Guerra del 41', 3, 2),
('Que heroe naval peruano murió en el Combate de Angamos', 'Miguel Grau', 'Francisco Bolognesi', 'Alfonso Ugarte', 'Andres Avelino Cáceres', 0, 2),
('Que cultura preinca construyó las Líneas de Nazca', 'Paracas', 'Nazca', 'Moche', 'Chimú', 1, 2),
('Que virrey del Perú fue el más destacado', 'Virrey Toledo', 'Virrey Pezuela', 'Virrey La Serna', 'Virrey Abascal', 0, 2),
('En que año se dio el "Baguazo"', '2007', '2009', '2011', '2013', 1, 2),
('Que grupo terrorista fue liderado por Abimael Guzmán', 'MRTA', 'Sendero Luminoso', 'Movimiento Revolucionario', 'Vanguardia Revolucionaria', 1, 2),
('Que batalla fue clave en la Guerra del Pacífico', 'Batalla de Arica', 'Batalla de Huamachuco', 'Batalla de Miraflores', 'Batalla de Tarapacá', 2, 2),
('Que presidente peruano fue derrocado por Fujimori en 1992', 'Alan García', 'Valentín Paniagua', 'Alberto Fujimori', 'Fernando Belaúnde', 0, 2);

-- preguntas nivel 3
INSERT INTO questions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('Que líder indígena resistió en la "Breña" durante la Guerra del Pacífico', 'Miguel Iglesias', 'Lizardo Montero', 'Andres A. Cáceres', 'Francisco García Calderón', 2, 3),
('Que tratado cedió Tarapacá a Chile despues de la Guerra del Pacífico', 'Tratado de Lima', 'Tratado de Ancón', 'Tratado de Valparaíso', 'Tratado de Paz y Amistad', 1, 3),
('Que presidente peruano nacionalizó el petróleo en 1968', 'Fernando Belaúnde', 'Juan Velasco Alvarado', 'Francisco Morales Bermúdez', 'Manuel Prado', 1, 3),
('Que cultura preinca es conocida por sus "huacos retratos"', 'Chavín', 'Moche', 'Chimú', 'Paracas', 1, 3),
('Que batalla marcó el fin de la Confederación Perú-Boliviana', 'Yungay', 'Ingavi', 'Ayacucho', 'Junín', 0, 3),
('Que líder del MRTA murió en la toma de la residencia del embajador de Japón', 'Nestor Cerpa Cartolini', 'Víctor Polay Campos', 'Oscar Ramírez Durand', 'Abimael Guzmán', 0, 3),
('Que virrey intentó sofocar la Rebelión de Túpac Amaru II', 'Virrey Amat', 'Virrey Jáuregui', 'Virrey Abascal', 'Virrey Pezuela', 1, 3),
('Que heroe civil peruano murió defendiendo el Morro de Arica', 'Alfonso Ugarte', 'Francisco Bolognesi', 'Miguel Grau', 'Andres A. Cáceres', 1, 3),
('En que gobierno se creó el Sol (nuevo sol) como moneda oficial', 'Alan García (1985)', 'Alberto Fujimori (1991)', 'Alejandro Toledo (2001)', 'Fernando Belaúnde (1980)', 1, 3),
('Que arqueólogo descubrió la ciudadela de Caral', 'Julio C. Tello', 'Ruth Shady', 'Walter Alva', 'Luis Lumbreras', 1, 3);