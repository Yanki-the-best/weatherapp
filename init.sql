CREATE TABLE IF NOT EXISTS weather (
    "id" SERIAL PRIMARY KEY,
    "city" VARCHAR(255) NOT NULL UNIQUE,
    "temperature" INT NOT NULL,
    "condition" VARCHAR(255)
);

INSERT INTO weather (city, temperature, condition) VALUES ('vienna', 25, 'sunny');
INSERT INTO weather (city, temperature, condition) VALUES ('jerusalem', 29, 'sunny');
INSERT INTO weather (city, temperature, condition) VALUES ('negrostein', 67, 'freezing');
INSERT INTO weather (city, temperature, condition) VALUES ('bomboclatia', 10, 'boiling');
INSERT INTO weather (city, temperature, condition) VALUES ('casastarik', 99, 'chilly');