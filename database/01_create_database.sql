CREATE DATABASE fastapi_simple_project;

\c fastapi_simple_project

CREATE SCHEMA IF NOT EXISTS "public";

CREATE TABLE IF NOT EXISTS "public"."livro" (
        "id" serial NOT NULL,
        "titulo" character varying(100) NOT NULL,
        "autor" character varying(100) NOT NULL,
        "ano" integer NOT NULL,
        CONSTRAINT "livro_pkey" PRIMARY KEY ("id")
);

