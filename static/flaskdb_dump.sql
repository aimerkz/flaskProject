--
-- PostgreSQL database dump
--

-- Dumped from database version 13.9
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: file; Type: TABLE; Schema: public; Owner: flaskuser
--

CREATE TABLE public.file (
    file_id integer NOT NULL,
    name text NOT NULL,
    extension character varying(10) NOT NULL,
    size integer NOT NULL,
    path character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone,
    comment text
);


ALTER TABLE public.file OWNER TO flaskuser;

--
-- Name: file_file_id_seq; Type: SEQUENCE; Schema: public; Owner: flaskuser
--

CREATE SEQUENCE public.file_file_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.file_file_id_seq OWNER TO flaskuser;

--
-- Name: file_file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flaskuser
--

ALTER SEQUENCE public.file_file_id_seq OWNED BY public.file.file_id;


--
-- Name: file file_id; Type: DEFAULT; Schema: public; Owner: flaskuser
--

ALTER TABLE ONLY public.file ALTER COLUMN file_id SET DEFAULT nextval('public.file_file_id_seq'::regclass);


--
-- Data for Name: file; Type: TABLE DATA; Schema: public; Owner: flaskuser
--

COPY public.file (file_id, name, extension, size, path, created_at, updated_at, comment) FROM stdin;
1	doc	.txt	1265353	/home/documents/	2022-09-22 16:43:46.789777	\N	comment
2	file	.odt	1265363	/home/documents/others/	2022-09-22 16:45:46.789777	\N	commentcomm
3	file2	.pdf	3473993	/home/documents/	2022-09-22 16:55:46.789777	2022-09-22 17:55:46.789777	commentcommcomcomcom
\.


--
-- Name: file_file_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flaskuser
--

SELECT pg_catalog.setval('public.file_file_id_seq', 3, true);


--
-- Name: file file_pkey; Type: CONSTRAINT; Schema: public; Owner: flaskuser
--

ALTER TABLE ONLY public.file
    ADD CONSTRAINT file_pkey PRIMARY KEY (file_id);


--
-- PostgreSQL database dump complete
--

