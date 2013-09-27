CREATE TYPE "software" AS ENUM ('ckan', 'socrata', 'opendatasoft', 'junar', 'bespoke');

CREATE TABLE "dataset" (
  "uri" text not null,
  "portal_software" software not null,
  "portal" text not null, -- like data.gov.uk
  "dataset_id" text not null, -- within the portal

  "name" text not null,
  "description" text not null,
  "keywords" text not null,

  "publishing_organization" text not null, -- the department
  "source_url" text not null, -- site whence the data came, if available

  "columns" integer[] not null,
  -- http://www.postgresql.org/docs/9.1/static/arrays.html

  "raw_metadata" json not null,
  -- http://www.postgresql.org/docs/9.3/static/functions-json.html
  -- http://michael.otacoo.com/postgresql-2/postgres-9-3-feature-highlight-json-operators/
);
