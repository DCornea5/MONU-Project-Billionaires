-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "Billionaires" (
    "ID" varchar   NOT NULL,
    "Name" varchar   NOT NULL,
    "Country" varchar   NOT NULL,
    "geometry" varchar   NOT NULL,
    "NetWorth" numeric   NOT NULL,
    "Age" numeric   NOT NULL,
    "Source" varchar   NOT NULL,
    "Rank" numeric   NOT NULL,
    "longitude" numeric   NOT NULL,
    "latitude" numeric   NOT NULL,
    "Counts" numeric   NOT NULL
);

CREATE TABLE "Rank" (
    "Rank" numeric   NOT NULL,
    "NetWorth" numeric   NOT NULL
);

CREATE TABLE "Countries" (
    "Country" varchar   NOT NULL,
    "geometry" numeric   NOT NULL,
    "longitude" numeric   NOT NULL,
    "latitude" numeric   NOT NULL
);

CREATE TABLE "Details" (
    "ID" varchar   NOT NULL,
    "Name" varchar   NOT NULL,
    "Age" numeric   NOT NULL,
    "Source" varchar   NOT NULL,
    "Country" varchar   NOT NULL
);

CREATE TABLE "AnnualData" (
    "ID" varchar   NOT NULL,
    "Name" varchar   NOT NULL,
    "NetWorth" numeric   NOT NULL,
    "Rank" numeric   NOT NULL,
    "Year" date   NOT NULL
);

ALTER TABLE "Rank" ADD CONSTRAINT "fk_Rank_Rank" FOREIGN KEY("Rank")
REFERENCES "AnnualData" ("Rank");

ALTER TABLE "Countries" ADD CONSTRAINT "fk_Countries_Country" FOREIGN KEY("Country")
REFERENCES "Details" ("Country");

ALTER TABLE "Details" ADD CONSTRAINT "fk_Details_ID" FOREIGN KEY("ID")
REFERENCES "AnnualData" ("ID");

