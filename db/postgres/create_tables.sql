CREATE TABLE users(
  username VARCHAR PRIMARY KEY,
  password VARCHAR
);

CREATE TABLE vehicles(
  id VARCHAR PRIMARY KEY,
  distance VARCHAR,
  owner VARCHAR REFERENCES users(username)
);
