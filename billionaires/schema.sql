CREATE TABLE "rank" (
	"rankid" numeric,
    "rank" numeric PRIMARY KEY,
    "networth" numeric   NOT NULL
);


CREATE TABLE "countries" (
	"countryid" varchar   NOT NULL,
    "country" varchar   PRIMARY KEY NOT NULL,
    "geometry" varchar   NOT NULL,
    "longitude" numeric   NOT NULL,
    "latitude" numeric   NOT NULL
);

CREATE TABLE "details" (
    "bid" varchar   NOT NULL,
    "name" varchar   NOT NULL,
    "age" numeric   NOT NULL,
    "source" varchar   NOT NULL,
    "country" varchar   NOT NULL
);

CREATE TABLE "annualdata" (
    "yid" varchar   NOT NULL,
    "name" varchar   NOT NULL,
    "networth" numeric   NOT NULL,
    "rank" numeric   NOT NULL,
    "year" numeric   NOT NULL
);








 
