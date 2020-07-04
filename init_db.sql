--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: project; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.project (
    id integer NOT NULL,
    name character varying,
    description character varying,
    start_date timestamp without time zone,
    end_date timestamp without time zone,
    user_id character varying NOT NULL
);


ALTER TABLE public.project OWNER TO postgres;

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_id_seq OWNER TO postgres;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.project_id_seq OWNED BY public.project.id;


--
-- Name: test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public.test OWNER TO postgres;

--
-- Name: test_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.test_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_id_seq OWNER TO postgres;

--
-- Name: test_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.test_id_seq OWNED BY public.test.id;


--
-- Name: workitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workitem (
    id integer NOT NULL,
    name character varying,
    description character varying,
    duration double precision,
    workspace_id integer NOT NULL
);


ALTER TABLE public.workitem OWNER TO postgres;

--
-- Name: workitem_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workitem_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workitem_id_seq OWNER TO postgres;

--
-- Name: workitem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workitem_id_seq OWNED BY public.workitem.id;


--
-- Name: workspace; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.workspace (
    id integer NOT NULL,
    name character varying,
    description character varying,
    price double precision,
    project_id integer NOT NULL
);


ALTER TABLE public.workspace OWNER TO postgres;

--
-- Name: workspace_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.workspace_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.workspace_id_seq OWNER TO postgres;

--
-- Name: workspace_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.workspace_id_seq OWNED BY public.workspace.id;


--
-- Name: project id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);


--
-- Name: test id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test ALTER COLUMN id SET DEFAULT nextval('public.test_id_seq'::regclass);


--
-- Name: workitem id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workitem ALTER COLUMN id SET DEFAULT nextval('public.workitem_id_seq'::regclass);


--
-- Name: workspace id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workspace ALTER COLUMN id SET DEFAULT nextval('public.workspace_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
270587040265
\.


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.project (id, name, description, start_date, end_date, user_id) FROM stdin;
20	Client #17	dev and design stuff	2020-06-27 10:08:14.784384	2020-07-11 10:08:14.784384	5ee344e01fb8c3001471413c
21	Client #17	dev and design stuff	2020-06-27 10:10:51.761391	2020-07-11 10:10:51.761391	5ee344e01fb8c3001471413c
22	Client #17	dev and design stuff	2020-06-27 10:11:11.248085	2020-07-11 10:11:11.248085	5ee344e01fb8c3001471413c
23	Client #18	dev and design stuff	2020-06-27 00:00:00	2020-07-11 00:00:00	5ee344e01fb8c3001471413c
24	Client #18	dev and design stuff	2020-06-27 00:00:00	2020-07-11 00:00:00	5efedcaca9ced90019caef18
25	Client #18	dev and design stuff	2020-06-27 00:00:00	2020-06-27 00:00:00	5ee344e01fb8c3001471413c
26	Client #18	dev and design stuff	2020-06-27 00:00:00	2020-07-11 00:00:00	5ee344e01fb8c3001471413c
27	Client #19	dev and design stuff	2020-06-27 00:00:00	2020-07-11 00:00:00	5ee344e01fb8c3001471413c
28	Client #28	dev and design stuff	2020-06-29 00:00:00	2020-07-13 00:00:00	5ee344e01fb8c3001471413c
29	Client #29	dev and design stuff	2020-06-29 00:00:00	2020-07-13 00:00:00	5ee344e01fb8c3001471413c
30	Client #29	dev and design stuff	2020-06-29 00:00:00	2020-07-13 00:00:00	5e90eff575ad040c19a6e4ca
31	Client #1	business & marketing stuff	2020-06-29 00:00:00	2020-07-13 00:00:00	5e90eff575ad040c19a6e4ca
\.


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test (id, name) FROM stdin;
\.


--
-- Data for Name: workitem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workitem (id, name, description, duration, workspace_id) FROM stdin;
17	task #1	initial implementation	2	35
18	task #2	initial implementation	1	35
20	task #4	initial implementation	5	35
21	task #1	initial design	5	41
22	task #2	initial design	15	41
23	task #3	initial design	25	41
24	task #5	initial design	12	35
25	task #5	initial design	12	35
26	task #6	initial design	9	35
27	task #6	initial design	9	41
28	task #8	initial design	9	35
29	task #9	initial design	9	35
30	task #10	initial design	9	41
31	task #10	initial design	9	40
32	task #10	initial design	9	35
33	task #11	initial design	91	35
19	update UX	different flow	13.5	35
\.


--
-- Data for Name: workspace; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.workspace (id, name, description, price, project_id) FROM stdin;
30	biz #1	biz and marketing stuff	2100	31
31	biz #2	biz and marketing stuff	2100	31
32	biz #3	biz and marketing stuff	2100	31
33	biz #4	biz and marketing stuff	21000	31
34	marketing #1	biz and marketing stuff	100	29
35	marketing #2	biz and marketing stuff	100	29
36	marketing #3	biz and marketing stuff	100	29
37	marketing #4	biz and marketing stuff	100	29
38	marketing #5	biz and marketing stuff	100	29
39	marketing #6	biz and marketing stuff	100	29
40	marketing #7	biz and marketing stuff	100	29
41	marketing #7	biz and marketing stuff	100	31
42	marketing #7	biz and marketing stuff	100	31
43	marketing #8	biz and marketing stuff	100	31
44	marketing #8	biz and marketing stuff	100	29
\.


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.project_id_seq', 31, true);


--
-- Name: test_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_id_seq', 1, false);


--
-- Name: workitem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workitem_id_seq', 33, true);


--
-- Name: workspace_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.workspace_id_seq', 44, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: project project_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- Name: test test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_pkey PRIMARY KEY (id);


--
-- Name: workitem workitem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workitem
    ADD CONSTRAINT workitem_pkey PRIMARY KEY (id);


--
-- Name: workspace workspace_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workspace
    ADD CONSTRAINT workspace_pkey PRIMARY KEY (id);


--
-- Name: workitem workitem_workspace_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workitem
    ADD CONSTRAINT workitem_workspace_id_fkey FOREIGN KEY (workspace_id) REFERENCES public.workspace(id) ON DELETE CASCADE;


--
-- Name: workspace workspace_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.workspace
    ADD CONSTRAINT workspace_project_id_fkey FOREIGN KEY (project_id) REFERENCES public.project(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

