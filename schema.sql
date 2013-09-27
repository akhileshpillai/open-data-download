CREATE TYPE "software" AS ENUM ('ckan', 'socrata', 'opendatasoft', 'junar', 'bespoke');

CREATE TABLE "dataset" (
  "uri" text not null,
  "portal_software" software not null,

  "name" text not null,
  "description" text not null,
  "keywords" text not null,

  "columns" integer[] not null,
  -- http://www.postgresql.org/docs/9.1/static/arrays.html

  "raw_metadata" json not null,
  -- http://www.postgresql.org/docs/9.3/static/functions-json.html
  -- http://michael.otacoo.com/postgresql-2/postgres-9-3-feature-highlight-json-operators/
);
