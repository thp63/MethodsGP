CREATE TABLE "Cart" (
           	"userID"           	TEXT,
           	"ISBN"   INTEGER,
           	"Quantity"       	INTEGER,
           	FOREIGN KEY("ISBN") REFERENCES "Inventory"("ISBN"),
           	FOREIGN KEY("userID") REFERENCES "User"("userID")
);
CREATE TABLE "Inventory" (
           	"ISBN"   INTEGER,
           	"title"	TEXT,
           	"author"           	TEXT,
           	"genre" TEXT,
           	"pages" INTEGER,
           	"releaseDate" 	TEXT,
           	"stock"  INTEGER,
           	PRIMARY KEY("ISBN")
);
CREATE TABLE "User" (
           	"userID"           	TEXT,
           	"email"  TEXT,
           	"password"     	TEXT,
           	"firstName"    	TEXT,
           	"lastName"     	TEXT,
           	"address"         	TEXT,
           	"city" 	TEXT,
           	"state"   TEXT,
           	"zip"   	INTEGER,
           	"payment"       	TEXT,
           	PRIMARY KEY("userID")
);
