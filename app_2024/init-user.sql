ALTER USER 'adminnet'@'%' IDENTIFIED WITH mysql_native_password BY 'Cuador.0730';

USE epolaris;
CREATE TABLE users (
  email VARCHAR(255) NOT NULL,
  name VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL,
  is_default_password TINYINT(1) NOT NULL DEFAULT 1,
  privilege VARCHAR(20) NOT NULL DEFAULT 'user',
  username VARCHAR(255),
  PRIMARY KEY (email),
  UNIQUE (username)
);
INSERT INTO users (email, name, password, privilege, is_default_password, username)
VALUES ('admin@example.com', 'Admin User', '\$2b\$10\$dA.jNSzAuUD74oC.4aGIeuPfQUZbBxCp7Ksmx/kAXjC3XDkZTdQrC', 'admin', TRUE, 'admin');
