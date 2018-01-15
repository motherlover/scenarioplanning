--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.9
-- Dumped by pg_dump version 9.5.9

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: con_of_znw_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE con_of_znw_table (
    con_id numeric,
    znw_id numeric,
    con_of_znw_id bigint NOT NULL
);


ALTER TABLE con_of_znw_table OWNER TO postgres;

--
-- Name: con_of_znw_table_con_of_znw_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE con_of_znw_table_con_of_znw_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE con_of_znw_table_con_of_znw_id_seq OWNER TO postgres;

--
-- Name: con_of_znw_table_con_of_znw_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE con_of_znw_table_con_of_znw_id_seq OWNED BY con_of_znw_table.con_of_znw_id;


--
-- Name: con_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE con_table (
    con text,
    con_id bigint NOT NULL
);


ALTER TABLE con_table OWNER TO postgres;

--
-- Name: con_table_con_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE con_table_con_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE con_table_con_id_seq OWNER TO postgres;

--
-- Name: con_table_con_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE con_table_con_id_seq OWNED BY con_table.con_id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE django_session OWNER TO postgres;

--
-- Name: generic_words; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE generic_words (
    generic_word text,
    generic_word_id bigint NOT NULL
);


ALTER TABLE generic_words OWNER TO postgres;

--
-- Name: generic_words_generic_word_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE generic_words_generic_word_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE generic_words_generic_word_id_seq OWNER TO postgres;

--
-- Name: generic_words_generic_word_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE generic_words_generic_word_id_seq OWNED BY generic_words.generic_word_id;


--
-- Name: info_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE info_table (
    sector text,
    branche text,
    type text,
    body text,
    info_id bigint NOT NULL
);


ALTER TABLE info_table OWNER TO postgres;

--
-- Name: info_table_info_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE info_table_info_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE info_table_info_id_seq OWNER TO postgres;

--
-- Name: info_table_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE info_table_info_id_seq OWNED BY info_table.info_id;


--
-- Name: prog_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE prog_table (
    sector text,
    branche text,
    type text,
    head text,
    body text,
    prog_id bigint NOT NULL
);


ALTER TABLE prog_table OWNER TO postgres;

--
-- Name: prog_table_prog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE prog_table_prog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE prog_table_prog_id_seq OWNER TO postgres;

--
-- Name: prog_table_prog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE prog_table_prog_id_seq OWNED BY prog_table.prog_id;


--
-- Name: trend_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE trend_table (
    sector text,
    branche text,
    type text,
    head text,
    body text,
    trend_id bigint NOT NULL
);


ALTER TABLE trend_table OWNER TO postgres;

--
-- Name: trend_table_trend_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE trend_table_trend_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE trend_table_trend_id_seq OWNER TO postgres;

--
-- Name: trend_table_trend_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE trend_table_trend_id_seq OWNED BY trend_table.trend_id;


--
-- Name: znw_in_prog_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE znw_in_prog_table (
    znw_prog_id bigint NOT NULL
);


ALTER TABLE znw_in_prog_table OWNER TO postgres;

--
-- Name: znw_in_prog_table_znw_prog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE znw_in_prog_table_znw_prog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE znw_in_prog_table_znw_prog_id_seq OWNER TO postgres;

--
-- Name: znw_in_prog_table_znw_prog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE znw_in_prog_table_znw_prog_id_seq OWNED BY znw_in_prog_table.znw_prog_id;


--
-- Name: znw_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE znw_table (
    znw text,
    znw_id bigint NOT NULL
);


ALTER TABLE znw_table OWNER TO postgres;

--
-- Name: znw_table_znw_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE znw_table_znw_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE znw_table_znw_id_seq OWNER TO postgres;

--
-- Name: znw_table_znw_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE znw_table_znw_id_seq OWNED BY znw_table.znw_id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: con_of_znw_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY con_of_znw_table ALTER COLUMN con_of_znw_id SET DEFAULT nextval('con_of_znw_table_con_of_znw_id_seq'::regclass);


--
-- Name: con_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY con_table ALTER COLUMN con_id SET DEFAULT nextval('con_table_con_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: generic_word_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY generic_words ALTER COLUMN generic_word_id SET DEFAULT nextval('generic_words_generic_word_id_seq'::regclass);


--
-- Name: info_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY info_table ALTER COLUMN info_id SET DEFAULT nextval('info_table_info_id_seq'::regclass);


--
-- Name: prog_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY prog_table ALTER COLUMN prog_id SET DEFAULT nextval('prog_table_prog_id_seq'::regclass);


--
-- Name: trend_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY trend_table ALTER COLUMN trend_id SET DEFAULT nextval('trend_table_trend_id_seq'::regclass);


--
-- Name: znw_prog_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY znw_in_prog_table ALTER COLUMN znw_prog_id SET DEFAULT nextval('znw_in_prog_table_znw_prog_id_seq'::regclass);


--
-- Name: znw_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY znw_table ALTER COLUMN znw_id SET DEFAULT nextval('znw_table_znw_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add permission	3	add_permission
8	Can change permission	3	change_permission
9	Can delete permission	3	delete_permission
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add trend	7	add_trend
20	Can change trend	7	change_trend
21	Can delete trend	7	delete_trend
22	Can add info	8	add_info
23	Can change info	8	change_info
24	Can delete info	8	delete_info
25	Can add movies	9	add_movies
26	Can change movies	9	change_movies
27	Can delete movies	9	delete_movies
28	Can add genres	10	add_genres
29	Can change genres	10	change_genres
30	Can delete genres	10	delete_genres
31	Can add prognose	11	add_prognose
32	Can change prognose	11	change_prognose
33	Can delete prognose	11	delete_prognose
34	Can add acted in	12	add_actedin
35	Can change acted in	12	change_actedin
36	Can delete acted in	12	delete_actedin
37	Can add actors	13	add_actors
38	Can change actors	13	change_actors
39	Can delete actors	13	delete_actors
40	Can add movies genres	14	add_moviesgenres
41	Can change movies genres	14	change_moviesgenres
42	Can delete movies genres	14	delete_moviesgenres
43	Can add post	15	add_post
44	Can change post	15	change_post
45	Can delete post	15	delete_post
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 1, false);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, false);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: con_of_znw_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY con_of_znw_table (con_id, znw_id, con_of_znw_id) FROM stdin;
\.


--
-- Name: con_of_znw_table_con_of_znw_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('con_of_znw_table_con_of_znw_id_seq', 1, false);


--
-- Data for Name: con_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY con_table (con, con_id) FROM stdin;
\.


--
-- Name: con_table_con_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('con_table_con_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	api	trend
8	api	info
9	api	movies
10	api	genres
11	api	prognose
12	api	actedin
13	api	actors
14	api	moviesgenres
15	api	post
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 1, false);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2017-10-09 11:24:13.516988+02
2	auth	0001_initial	2017-10-09 11:24:13.579475+02
3	admin	0001_initial	2017-10-09 11:24:13.600918+02
4	admin	0002_logentry_remove_auto_add	2017-10-09 11:24:13.613516+02
5	api	0001_initial	2017-10-09 11:24:13.622014+02
6	api	0002_info_prognose_trend	2017-10-09 11:24:13.628166+02
7	contenttypes	0002_remove_content_type_name	2017-10-09 11:24:13.651906+02
8	auth	0002_alter_permission_name_max_length	2017-10-09 11:24:13.662015+02
9	auth	0003_alter_user_email_max_length	2017-10-09 11:24:13.677963+02
10	auth	0004_alter_user_username_opts	2017-10-09 11:24:13.692007+02
11	auth	0005_alter_user_last_login_null	2017-10-09 11:24:13.708198+02
12	auth	0006_require_contenttypes_0002	2017-10-09 11:24:13.709908+02
13	auth	0007_alter_validators_add_error_messages	2017-10-09 11:24:13.720301+02
14	auth	0008_alter_user_username_max_length	2017-10-09 11:24:13.734369+02
15	sessions	0001_initial	2017-10-09 11:24:13.744244+02
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 15, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
giq8h86ipla12kleqsw6kvt6a3lr572m	NGFjMjRkNzZhNmY4MjE1M2MwMWZhMjMxN2FhODI2ZTk1YzI2NzRlYjp7InNjZW5hcmlvX25yIjoyLCIyIjp7ImVmZmVjdF9saXN0IjpbWzUsMSw3LDNdLFs0LDgsNiwyXV0sInByb2dfaWRfbGlzdCI6WyIxNzIiLCIxNjgiLCIxNzEiXSwidHJlbmRfaWRfbGlzdCI6WyIxODIiXSwibnJfb2ZfcHJvZ190cmVuZCI6NCwidHJlbmRfc3RyaW5nX2xpc3QiOlsiVGVjaG5vbG9naWUgZW4gZGF0YSBsZWlkZW4gdXcgaW5ub3ZhdGllOiBzdGFiaWVsIl0sInByb2dfc3RyaW5nX2xpc3QiOlsiR3JvbmRzdG9mcHJpanplbiBcdTIwMTMgTm9nIHZlZWwgb3BzbGFnLCBvbmRhbmtzIHN0aWpnZW5kZVxucHJpanplbjogbmVlbXQgYWYvIHN0YWduZWVydC8ga3JpbXB0IiwiRS1jb21tZXJjZSBcdTIwMTMgSG9nZSBpbmdlYnJ1aWtuYW1lIHZhbiBsb2dpc3RpZWsgdmFzdGdvZWQ6IG5lZW10IHRvZSAvIG9udHdpa2tlbHQgLyBncm9laXQiLCJCb3V3IFx1MjAxMyBBYW5nZXRyb2trZW4gYm91d3Byb2R1Y3RpZSBndW5zdGlnIHZvb3JcbndlZ3RyYW5zcG9ydDogbmVlbXQgYWYvIHN0YWduZWVydC8ga3JpbXB0Il19LCJ0cmVuZF9zdHJpbmdfbGlzdCI6WyJLYW5zZW4gZG9vciBcdTIwMThob3RlbGlzZXJpbmdcdTIwMTk6IG5lZW10IHRvZSAvIG9udHdpa2tlbHQgLyBncm9laXQiXSwicHJvZ19pZF9saXN0IjpbIjk4IiwiOTciLCI5OSJdLCIxIjp7ImVmZmVjdF9saXN0IjpbWzQsNiw4LDJdLFs5LDMsNSw3XV0sInByb2dfaWRfbGlzdCI6WyIxNzIiLCIxNjgiLCIxNzMiXSwidHJlbmRfaWRfbGlzdCI6WyIxODAiXSwibnJfb2ZfcHJvZ190cmVuZCI6NCwidHJlbmRfc3RyaW5nX2xpc3QiOlsiVmVyc3RlcmtlbiB2YW4gZGUgcG9zaXRpZSBvcCBkZSBhcmJlaWRzbWFya3Q6IG5lZW10IGFmLyBzdGFnbmVlcnQvIGtyaW1wdCJdLCJwcm9nX3N0cmluZ19saXN0IjpbIkUtY29tbWVyY2UgXHUyMDEzIEhvZ2UgaW5nZWJydWlrbmFtZSB2YW4gbG9naXN0aWVrIHZhc3Rnb2VkOiBzdGFiaWVsIiwiRHV1cnphYW0gXHUyMDEzIExvZ2lzdGllayB2YXN0Z29lZCBzdGVlZHMgZWZmaWNpXHUwMGVibnRlciBlblxuZHV1cnphbWVyOiBuZWVtdCB0b2UgLyBvbnR3aWtrZWx0IC8gZ3JvZWl0IiwiQm91dyBcdTIwMTMgQWFuZ2V0cm9ra2VuIGJvdXdwcm9kdWN0aWUgZ3Vuc3RpZyB2b29yXG53ZWd0cmFuc3BvcnQ6IG5lZW10IGFmLyBzdGFnbmVlcnQvIGtyaW1wdCJdfSwidHJlbmRfaWRfbGlzdCI6WyIxMDMiXSwiYnJhbmNoZV9saXN0IjpbImdvZWRlcmVud2VndmVydm9lciIsIm9wc2xhZyJdLCJlZmZlY3RfbGlzdCI6W1szLDUsMSw3XSxbOCw0LDIsNl1dLCJicmFuY2hlX3Jlc19saXN0IjpbXSwibnJfb2ZfcHJvZ190cmVuZCI6NCwicHJvZ19zdHJpbmdfbGlzdCI6WyJDb25zdW1lbnQgaGVlZnQgdmVydHJvdXdlbjogc3RhYmllbCIsIlRvZW5hbWUgdG9lcmlzbWUgdmVyd2FjaHQ6IG5lZW10IGFmLyBzdGFnbmVlcnQvIGtyaW1wdCIsIkNvbnN1bWVudCBraWVzdCB2b29yIHZha2FudGllaHVpc2plOiBuZWVtdCBhZi8gc3RhZ25lZXJ0LyBrcmltcHQiXX0=	2017-11-15 13:28:50.639975+01
\.


--
-- Data for Name: generic_words; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY generic_words (generic_word, generic_word_id) FROM stdin;
\.


--
-- Name: generic_words_generic_word_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('generic_words_generic_word_id_seq', 1, false);


--
-- Data for Name: info_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY info_table (sector, branche, type, body, info_id) FROM stdin;
Agrarisch	akkerbouw	prognose	Opbrengstprijzen in de akkerbouwbranche zijn voor een deel\n afhankelijk van ontwikkelingen op de mondiale markt (suiker\nen tarwe). Gunstige productieomstandigheden hebben geleid tot forse\nvoorraadopbouw voor granen (tarwe en soja). Voor 2016 verwachten\nwij een volumegroei van 3% in 2017 en in 2018.	1
Agrarisch	kalverhouderij	prognose	De consumptie van vlees staat onder druk en kalfsvlees is daar\ngeen uitzondering in. Voor 2017 verwachten we dat net als in 2016\nde productie stabiel zal zijn en verwachten we geen grote\nprijsveranderingen.	2
Agrarisch	melkveehouderij	prognose	Melkveehouders hebben een slecht  jaar achter de rug. De\nmelkprijs lag voor het tweede jaar op rij onder de kostprijs, als\ngevolg van onbalans tussen vraag en aanbod. Voor 2017 verwachten\nwij een flinke daling van de productie, maar ook een flink herstel\nvan de prijs.	3
Agrarisch	pluimveehouderij	prognose	Wereldwijd gaat kip naar verwachting binnen 10 jaar het meest\ngegeten vlees van alle soorten worden. Dit heeft te maken met de\nrelatief lage prijs van dit efficiënt geproduceerde vlees, maar ook\nmet het feit dat er wereldwijd minder religieuze bezwaren zijn\ntegen het eten van pluimvee. In Nederland is met name duurzaamheid\neen belangrijk thema, dit zorgt voor druk op de productie.	4
Agrarisch	sierteelt	prognose	De sierteelt is een competitieve branche. De concurrentie komt\nmet name uit het buitenland. Maar ook Nederlandse producten\nstrijden voor een plek in het boeket. 2016 was een positief jaar:\nhet  economisch herstel zorgde voor positieve resultaten voor\nde sierteelt. Voor 2017 verwachten wij dat dit resultaat wordt\ndoorgezet.	5
Agrarisch	varkenshouderij	prognose	De hogere prijzen zorgden voor een opleving in de\nvarkenshouderij. De rendementen namen toe in 2016. Voor 2017\nverwacht ABN AMRO een verdere toename van de prijzen, maar de kans\nbestaat dat door deze hogere prijzen de varkensstapel in Europa\n toeneemt met een stagnatie van de prijzen in 2018 tot\ngevolg.	6
Agrarisch	visserij	prognose	De visserijbranche is voor inkomsten sterk afhankelijk van de\nhoeveelheid vis die men mag vangen en de brandstofkosten voor\nhet schip. Economisch herstel leidt tot meer vraag naar vis, maar\neen Brexit kan mogelijk roet in het eten gooien. Voor 2017\nverwachten we een volumegroei van 4%.	7
Agrarisch	voedingstuinbouw	prognose	De teelt van glasgroenten  laat zich redelijk voorspellen\nqua afzetvolumes. Voor onbedekte teelten is dit vaak lastiger,\ndoordat de impact van weersomstandigheden vaak groter is. Voor 2017\nverwacht ABN AMRO een volumegroei van 2%.	8
Bouw	architectenbureaus	prognose	De omzet van architecten steeg in 2016 met 7,3 procent en hun\nomzet zal in 2017 naar verwachting met 5% groeien en in 2018 met 3\nprocent. Daarmee zijn de architecten er nog lang niet. Hun omzet\nligt nog 43 procent onder het niveau van 2008. Architecten blijven\nprofiteren van het herstel van de woningmarkt en zien hun tarieven\nlangzaam stijgen.	9
Bouw	grond--weg-waterbouw	prognose	De beperkte investeringen van de overheid in de infrastructuur\nde afgelopen jaren raken de gww. Circa 75 procent van de gww is\nafhankelijk van overheidsprojecten. In 2017 wordt EUR 6,8 miljard\ngeïnvesteerd in de infrastructuur. Vanaf 2018 nemen de\noverheidsinvesteringen weer toe. Voor 2017 verwachten wij een groei\nvan 3 procent en voor 2018 een groei van 3,5 procent. Lees ook onze\n\nBrancheupdate over de gww, 2 augustus 2016	10
Bouw	groothandel-hout-bouwmaterialen	prognose	De groothandel heeft in 2016 sterk geprofiteerd van de groei in\nde bouwproductie en de woningmarkt. Consumenten huurden vaker een\naannemer in voor de renovatie van hun woning. De omzet zal naar\nverwachting in 2017 en 2018 minder hard groeien. De omzet van de\ngroothandel groeit in zowel 2017 als 2018 met 5 procent.	11
Bouw	hout-bouwmaterialenindustrie	prognose	De hout- en bouwmaterialenindustrie profiteert van de toenemende\nbouwproductie. De houtindustrie groeide in 2016 harder dan de\nbouwmaterialenindustrie. Wel steeg de omzet van bedrijven actief in\nde bouwmaterialenindustrie harder dan van bedrijven actief in de\nhoutindustrie. De hout- en bouwmaterialenindustrie groeit naar\nverwachting in 2017 met 4,5 procent en in 2018 met 4 procent.	12
Bouw	ingenieursbureaus	prognose	Ingenieurs hebben relatief weinig last gehad van de crisis in de\nbouwsector en hun omzet lag in 2016 alweer boven het niveau van\n2008. Internationale onzekerheden, zoals de verkiezing van Trump en\nhet Brexit referendum, zijn een risico voor de grote\ningenieursbureaus. Wij verwachten dat de omzet van ingenieurs zowel\nin 2017 als in 2018 met 2 procent groeit.	13
Bouw	installatiebedrijven	prognose	De installateurs profiteren van het groei van de bouw en\nindustrie. Naar verwachting zal hun omzet in zowel 2017 als 2018\nmet 5 procent groeien. Installateurs kunnen bij trends zoals\nvergrijzing en verduurzaming het voortouw nemen. Doordat deze\ntrends de komende jaren belangrijker worden, neemt het belang van\ninstallateurs toe.	14
Bouw	utiliteitsbouw	prognose	De utiliteitsbouw heeft het moeilijk gehad. Door veranderende\nbehoeftes en krimpende organisaties staan veel gebouwen nu (deels)\nleeg. Wij verwachten dat de utiliteitsbouw voorbij het dieptepunt\nis. Naar verwachting groeit de utiliteitsbouw in 2017 met 3 procent\nen in 2018 met 3,5 procent. Er worden vooral meer nieuwe kantoren,\ncombinatie bedrijfshallen en kassen gebouwd.	15
Bouw	woningbouw	prognose	De woningbouw is niet alleen de grootste, maar ook de sterkst\ngroeiende branche van de bouw. Nieuwbouw trekt de kar. Er worden\nvooral nieuwe koopwoningen gebouwd, maar commerciële marktpartijen\nbouwen ook steeds meer nieuwe huurwoningen in de grote steden.\nWoningcorporaties bouwen nog maar nauwelijks. De woningbouw groeit\nnaar verwachting in 2017 met 7 procent en in 2018 met 5,5\nprocent.	16
Food	agf-industrie	prognose	De\nAGF-industrie is voor een belangrijk deel afhankelijk van de export\nbinnen Europa, met name richting Duitsland, Frankrijk en het\nVerenigd Koninkrijk. Maar ook de vraag van de Nederlandse consument\nheeft veel invloed op de omzet. Deze vraag hangt deels af van de\neconomische groei, en daarmee lijkt het in 2017 wel goed te\nzitten.	17
Food	brood-deegwarenindustrie	prognose	Deze branche is sterk afhankelijk van ontwikkelingen op de\nNederlandse markt. De groei van de Nederlandse economie is dan ook\neen stimulans voor deze industrie.	18
Food	drankenindustrie	prognose	De drankenindustrie kenmerkt zich door een lage volatiliteit en\neen groot exportbelang. In 2016 stegen de productie en omzet licht,\nvooral door een toenemende export. En in weerwil van wet- en\nregelgeving rond de consumptie van alcohol en suiker, die de sector\nzowel in Nederland als daarbuiten onder druk zet.	19
Food	groothandel-in-voedingsmiddelen	prognose	De groeiende Europese economie stimuleert de\nvoedingsmiddelenindustrie in haar totaliteit: een grotere vraag\nnaar producten leidt tot meer handelsvolume. De omzet zal in 2017\ndan ook groeien, met zo’n 2 procent.	20
Food	visindustrie	prognose	Vis heeft een positief imago. De industrie profiteert hiervan,\nnet als van de aantrekkende economie in de EU. Beide zorgen ervoor\ndat er meer vis wordt gegeten, zowel in Nederland als in de rest\nvan Europa. We zien de export dan ook groeien.	21
Food	vleesindustrie	prognose	De vleesindustrie richt zich op twee afzetgebieden. De\nontwikkelde consumentenmarkt, waar kwaliteit en duurzaamheid steeds\nbelangrijker worden. En de bulkmarkt, veelal buiten Nederland.\nGroei komt vooral uit de export. Doordat het welvaartsniveau ook in\nandere delen van de wereld stijgt, wordt vlees daar voor grotere\nbevolkingsgroepen bereikbaar.	22
Food	zuivelindustrie	prognose	Doordat de welvaart wereldwijd toeneemt, is de vraag naar zuivel\nde afgelopen jaren fors gestegen. De zuivelindustrie heeft hierop\ningespeeld door meer te produceren. Deels doordat de melkquotering\nvoor melkveehouders is weggevallen, kwam er meer aanvoer en daalde\nde melkprijs. Naar verwachting zal deze in de tweede helft van 2017\ngaan stijgen.	23
Industrie	basismetaalindustrie	prognose	De metaalbewerkingsindustrie, automotive, transport- en\nenergiesector en de bouwsector zijn grote afnemers. Daar trekt de\nactiviteit aan. Maar de impact van trends in industriële\nmetaalmarkten (zie onder) is zeer hoog voor deze branche. Voor 2016\nverwachten wij een lichte krimp van de productie van 0,2, terwijl\nde productie in 2017 weer kan aantrekken naar een groei van\n2,2 procent.	24
Industrie	chemische-industrie	prognose	Voor de chemische industrie verwachten wij een productiegroei\nvan 3,2 prodent in 2016 en 3,1 procent in 2017. De branche kampt\nnog met een relatief zwakke vraag en hevige concurrentie in de\neurozone. De branche zal in 2017 nog enig profijt hebben van de\nrelatief lage olieprijs, maar de olieprijs zal ook in 2017 verder\nstijgen. De groei van de vraag van buiten de eurozone kan een\nimpuls krijgen, aangezien de euro dit jaar zal verzwakken en dat is\ngunstig voor de export.	25
Industrie	elektro-en-technische-apparatenindustrie	prognose	Bij een groot deel van de eindgebruikers zijn de vooruitzichten\nrelatief gunstig en dit komt terug in onze productieverwachtingen\nvoor 2016 en 2017. De groei in de industriële branches en in de\nbouw gerelateerde sectoren zal een positieve uitwerking hebben op\nde productiegroei. Wij denken dat in 2016 de productie met\ngemiddeld 6,1 procent zal groeien. De groei zal in 2017 aanhouden,\nmaar zal gemiddeld lager uitkomen op 3,3 procent.	26
Industrie	machine-industrie	prognose	De productie van machines zal in 2016 is met 1,1 procent\nkrimpen. Deels ligt hier de vertragingen in de groei van de vraag\nvanuit opkomende landen aan ten grondslag, maar de afname van de\norders vanuit Duitsland begin 2016 spelen ook een rol. Voor 2017\ndenken wij dat de groei weer zal aantrekken, mede gezien de\ngroeitrends in export (de zwakkere euro) en de groei van de\nmondiale economie.	27
Industrie	metaalproductenindustrie	prognose	Naast de machine-industrie is de bouwsector een belangrijke\nafnemersgroep. De gunstige verwachtingen voor de bouwproductie\nspelen de branche in de kaart, maar de productiegroei in de\nmachinebouw schatten wij gematigd in. Wij verwachten dat in 2016 en\n2017 de productie van metaalproducten verder zal groeien met\nrespectievelijk 1,5 en 2,5 procent.	28
Industrie	meubelindustrie	prognose	Door de toenemende verkopen van woningen heeft de vraag naar\nnieuwe meubelen een impuls gekregen. Daar profiteert de\nmeubelindustrie van. De vooruitzichten voor woningmarkt blijven\ngunstig, alhoewel het groeitempo in transacties zal afnemen.\nDaardoor zal de productiegroei in 2016 ook een vertraging laten\nzien. Wij gaan uit van 1,5 procent in 2016 en dit groeitempo neemt\nin 2017 af naar 0,8%.	29
Industrie	rubber-kunststofproductenindustrie	prognose	Een belangrijke afnemer van rubber- en kunststofproducten is de\nbouw. De prognoses voor de bouwproductie in 2016 en 2017 zijn\ngunstig en dat is goed nieuws voor de afzet van deze branche. Voor\n2016 gaan wij uit van een productiegroei van 2,7 procent. Voor 2017\ngaan wij ervan uit dat de groei aantrekt tot 2,9 procent. De\nrisico’s komen uit het buitenland, want de druk van internationaal\nopererende bedrijven neemt jaarlijks toe.	30
Industrie	transportmiddelenindustrie	prognose	Wij gaan uit van een sterke productiegroei van 12,4 procent\nin 2016. In 2017 neemt het groeitempo af naar gemiddeld 4,3\nprocent. De verkopen van vervoermaterieel is van zowel de\nbinnenlandse als de buitenlandse markt afhankelijk. De\nmarktomstandigheden in beide afzetgebieden zijn positief, maar de\nrisico’s blijven nog relatief hoog. Dat geeft de branche zijn\ngrilligheid. De verwachtingen wat betreft de bestedingen van\nconsumenten aan duurzame goederen blijven gunstig.	31
Leisure	attractieparken-dierentuinen	prognose	Wij verwachten dat het bezoek aan attractieparken in 2017 met 3\nprocent toeneemt. Investeringen in bijvoorbeeld slaapplaatsen,\nnieuwe attracties en VIP-ervaringen resulteren in extra bezoek.\nVoor 2018 gaan we uit van een stijging van het bezoek met 2,5\nprocent.	32
Leisure	campings-vakantieparken	prognose	Het aantal overnachtingen in de verblijfsrecreatie nam in\n2016 met 0,3 procent toe naar 62 miljoen. Daarbij daalde het\naantal overnachtingen door Nederlandse bezoekers met 1,8%. Het\naantal overnachtingen door buitenlandse bezoekers steeg met 6,5%.\nVoor zowel huisjesparken als voor campings kwam de totale groei\nvoort uit de toename van het buitenlands bezoek. In de laatste\njaren steeg het buitenlandse bezoek sowieso veel harder dan het\nbinnenlandse bezoek. Nog altijd komt echter wel 73 procent van\novernachtingen in verblijfsrecreatie van bezoekers uit eigen land.\nWij verwachten dat het totaal aantal overnachtingen in de\nverblijfsrecreatie in 2017 met 2 procent toeneemt, geholpen door de\npositieve economische omstandigheden. Vakantieparken en\nkustcampings profiteren daarvan. De camping met luxe onderkomens\n(in de branche gedoopt tot ‘glamping’) is daarbij een kansrijk\nconcept.	33
Leisure	foodservice	prognose	Na een groei voor de foodservice van 2,7 procent in 2016 gaan\nwij uit van een groei van 2,3 procent in 2017 en 2 procent in 2018.\nGroothandels in foodservice profiteren van de toegenomen behoefte\nvan de consument om buitenshuis te eten en te drinken. Daarvan\nprofiteert de horeca direct, en de foodservice-groothandels\nindirect. Het is belangrijk voor foodservice-groothandels om in te\nspelen op de trends in de eindmarkten. Zo zijn bijvoorbeeld\nduurzaamheid en gezondheid belangrijker geworden.	34
Leisure	hotels	prognose	De hotelmarkt zit in de lift. Na een omzetgroei van 5 procent in\n2016, gaan wij voor 2017 en 2018 uit van een omzetgroei van 3\nprocent. Daarbij spelen de economische omstandigheden (in\nbelangrijke herkomstlanden) een belangrijke rol. Dankzij de\naanhoudende groei van het toerisme zijn de bezettingsgraden van\nhotels in de afgelopen jaren gestegen. Echter is niet alles goud\nwat er blinkt voor hotels. De concurrentie is groot. Voor hoteliers\ndie nu niet onderscheidend genoeg zijn is het belangrijk keuzes te\nmaken. Daarmee voorkomen deze hoteliers dat zij niet bestendig\nzijn tegen een onverhoopte dip in het toerisme en/of in de\neconomie. Dat geldt zeker voor hotelvestigingen op minder\ntoeristische plekken. Hoteliers proberen via verbeteringen op\nde website en loyaliteitsprogramma’s meer directe boekingen te\nscoren; nu gaat ongeveer een derde via online travel\nagencies. Over die boekingen draag een hotel circa 18 procent\naf.	35
Leisure	kunst-cultuur	prognose	Voor de branche ‘kunst en cultuur’ verwachten wij in 2017 en\n2018 een volumestijging van 1,5 procent per jaar. In de afgelopen\njaren was er ook al groei te zien, waarbij wel verschillen binnen\nde branche zijn te zien. Musea realiseerden tussen 2011 en 2015 een\ntoename van liefst 47% van het bezoek. Sinds 2009 verdubbelde zelfs\nhet aantal Museumkaarthouders in ons land. Ook bioscopen zitten in\nde lift. Theaters zagen sinds 2012 het bezoek wel afnemen, en\nvoelde daarbij ook de afname aan subsidies.	36
Leisure	restaurants	prognose	Nadat de verkoopvolumes van restaurants 4,7 procent\nstegen in 2016, verwachten wij een stijging van 4,5 procent in\n2017. De positieve economische omstandigheden spelen deze branche\nin de kaart. Dankzij een stijging van de volumes met bijna 24\nprocent in de laatste zeven jaar liggen de verkoopvolumes van\nrestaurant weer boven précrisisniveaus. Daarbij profiteren\nrestaurants op dit moment nadrukkelijk van het\nconsumentenvertrouwen. In de beginmaanden van 2017 stond het\nconsumentenvertrouwen op het hoogste punt sinds de zomer van 2007.\nDaarbij geven consumenten aan de huidige periode als ‘gunstig’ voor\ngrote aankopen te zien.	37
Leisure	travel	prognose	De laatste jaren liet de reisbranche flinke groei zien, geholpen\ndoor de positieve economische omstandigheden. De volumes stegen in\n2016 met 7,9 procent. Die groei lijkt met name te zitten bij\nde reisbemiddelaars en partijen die toeristische informatie\nverschaffen. Touroperators hebben het veel lastiger; hun omzet\ndaalde in 2016 met 1,2 procent. Een belangrijk issues voor\nreisbureaus is de concurrentie van internet, die de consument\nfrequent gebruikt om reizen te boeken en samen te spelen. Een goede\nvindbaarheid en profilering online (ook mobiel) is voor de\nreisbranche dan ook essenieel. Voor 2017 verwachten wij – dankzij\nde groei van het toerisme – een volumegroei van 3,5 procent,\ngedragen door de reisbemiddelaars. De marges in de branches blijven\nrelatief laag binnen de branche, ook door de concurrentie van\nonline travel agencies als Booking.com.	38
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	prognose	Door lage olie- en gasprijzen zijn investeringen in de sector\nflink afgenomen. Onderhoud, internationale oriëntatie, innovatie en\nhet inzetten van branchekennis bij de ontwikkeling van windenergie\nop zee bieden kansen voor de branche. Overnames en\nindustrie-consolidatie kan een belangrijke strategie zijn om\ngedurende deze downcycle posities verder te versterken en\nconsolideren.	39
Retail	autoretail	prognose	De autoretail realiseerde in 2016 een stijging van de omzet van\n1,3%, onder meer dankzij de verkoop van occassions. Deze verkoop\nsteeg in 2016 met 4,5%, terwijl de nieuwverkopen onder druk stonden\nen zelfs met 15% daalden. Mede dankzij de betere economische\nomstandigheden verwachten wij dat de autoretail in 2017 een\nomzetstijging van 2% realiseert. De branche heeft wel een aantal\nflinke uitdagingen.	40
Retail	bouwmarkten	prognose	In 2016 slaagden bouwmarkten erin om uit het dal te klimmen. De\nverkoopvolumes stegen liefst met 6%. De branche kon dat goed\ngebruiken, na de daling in 2015. De verkoopvolumes bevinden zich\nnog wel een kwart onder de niveaus van voor de crisis. De\nvooruitzichten wijzen op groei, maar er zijn diverse uitdagingen in\nde branche. Voor 2017 gaan we uit van een volumegroei van 1,7%.	41
Retail	drogisterijen	prognose	Drogisterijen wisten in 2016 met 2% te groeien in\nverkoopvolumes, en wij verwachten opnieuw groei in 2017 en 2018.\nDrogisterijen hielden zowel de volumes als de omzet op peil tijdens\nde crisis. De aanhoudende vraag naar verzorgingsproducten is\ngunstig voor de branche, en samenwerking is binnen deze branche een\naantrekkelijke optie.	42
Retail	groothandel-non-food	prognose	Voor groothandels verwachten wij een flinke groei in 2017 en\n2018. De betere economische omstandigheden en de groei van de\nexport zijn gunstige factoren en stuwen de verkopen van\ngroothandels non-food. De branche kent echter ook uitdagingen,\nonder meer in de concurrentie met internetinitiatieven en\nhandhaving van de rol in de keten.	43
Retail	kledingwinkels	prognose	Dankzij een eindspurt in het vierde kwartaal wisten\nkledingwinkels in 2016 de verkoopvolumes met 3% te verhogen.\nKledingwinkels zitten nog wel 11% onder precrisisniveaus in hun\nverkoopvolumes. Kledingzaken wisten vorig jaar eindelijk de prijzen\nte verhogen, na de daling in 2014 en 2015. De concurrentie blijft\nechter groot en de gemiddelde marges zijn laag.	44
Retail	supermarkten	prognose	Supermarkten wisten de verkoopvolumes vorig jaar met 1% te\nverhogen, terwijl de omzet met 2% steeg. Daarmee zitten de supers\ngezamenlijk al 7% boven de niveaus van voor de crisis. Ook voor\n2017 en 2018 verwachten we groei. Toch staat ook deze branche voor\nuitdagingen: met name in het middensegment. Partijen die inzetten\nop beleving, concurrentie vanuit de non-food-sector en internet\nmaken de concurrentie voor hen groter.	45
Retail	winkels-in-consumentenelektronica	prognose	2016 was een zwaar jaar voor winkels in consumentelektronica,\nmet een daling van 3,5% van de verkoopvolumes en van 4,4% van de\nomzet. Mede door de grote prijsdruk daalde het aantal (vestigingen\nvan) winkels in elektronica in de afgelopen zeven jaar met 556, het\naantal computerwinkels met 454 en aantal verkopers van radio’s en\ntelevisies met 159. Mede dankzij de betere economische\nomstandigheden verwachten wij voor 2017 een beter jaar, waarin\nde verkoopvolumes richting stabilisatie gaan.	46
Retail	woonwinkels	prognose	Woonwinkels profiteren van de fikse groei van het aantal\ntransacties op de wingmarkt. Na de zware jaren stegen de\nverkopen van woonwinkels in 2014 en 2015 weer. In 2016 groeiden de\nverkoopvolumes met 2,1%, voor 2017 gaan we uit van 1,3%\nvolumegroei. De volumes liggen wel nog altijd ruim 27 procent\nonder précrisisniveaus.	47
Technologie-Media-Telecom	drukkerijen	prognose	Drukkerijen hebben bijzonder zwaar te lijden onder\ndigitalisering van de samenleving. De vraag naar drukwerk viel\ndaardoor structureel terug. Negen opeenvolgende jaren daalde de\nomzet totdat in 2016 eindelijk weer eens een bescheiden omzetgroei\nvan 1,3% werd geboekt. Voor 2017 verwachten wij een lichte\nomzetkrimp van 0,5%. In 2018 zal de branche met 1% krimpen.	48
Technologie-Media-Telecom	ict-hardware	prognose	Voor ICT Hardware verwachten wij groei in 2017,  in\nnavolging van de goede ontwikkeling in 2015 en 2016. De aanhoudende\nvraag naar telecomapparatuur speelt de sector in de kaart, maar de\nsector heeft ook uitdagingen. Denk daarbij bijvoorbeeld aan de\nprijsdruk op consumentenelektronica en online concurrentie.	49
Technologie-Media-Telecom	it-software-services	prognose	De IT-branche trekt de kar binnen de TMT-sector, maar de omzet\nis op een lager groeipad beland. Na een omzetgroei van 9,5 procent\nin 2015 was er een groei van ‘slechts’ 2,9% in 2016.  Voor\n2017 verwachten wij een groei van 4,5%. IT-bedrijven profiteren van\nde aantrekkende economie en van de digitale transformatie die in\ndiverse sectoren plaatsvindt. IT wordt belangrijker binnen\nbedrijfsprocessen. De groeivertraging heeft dan ook niet te maken\nmet de vraag naar IT-producten en diensten, maar veeleer met\nproductiebelemmeringen zoals een tekort aan goed opgeleid\npersoneel.	50
Technologie-Media-Telecom	reclamebureaus	prognose	De crisis heeft de reclamebranche geraakt. Bedrijven bezuinigden\nop advertenties en de omzet binnen de branche daalde na 2008 met\neen kwart. Er lijkt echter een kentering te zijn. Inmiddels groeit\nde omzet al 3 jaar op rij.  Wij verwachten echter dat het\nherstel van de laatste jaren doorzet in 2017, geholpen door online\nadvertentiebestedingen en de betere economie.	51
Technologie-Media-Telecom	telecom	prognose	De telecombranche verkeert nog steeds in transitie. De consument\nis telecommunicatie anders gaan gebruiken en de sector past zich\ndaarop aan. Wij voorzien een omzetdaling van 1,5 procent in 2017 en\n2% in 2018. De omzet in deze branche is sinds de crisis met 18\nprocent gedaald.	52
Technologie-Media-Telecom	televisie-omroepen	prognose	Wij verwachten een positief jaar voor de televisie-branche,\ngeholpen door een verbetering van het economisch klimaat. Een\ngroeimarkt hierbinnen zijn de producenten van tv-content, die\nprofiteren van de strijd om de aandacht voor de consument. Wij\nverwachten voor hen omzetgroei van 4,5 procent in 2017 en 3,5% in\n2018.	53
Technologie-Media-Telecom	uitgeverijen	prognose	Voor uitgeverijen verwachten wij een krimp van 1,5 procent in\n2017 en 2% in 2018. Sinds het uitbreken van de crisis daalde de\nomzet van de branche met 27%; voor een belangrijk deel omdat de\nconsument minder printmedia consumeerde. De transitie naar digitaal\nkost tijd. Het tempo van de omzetdalingen blijft stabiel.	54
Transport-en-Logistiek	binnenvaart	prognose	In 2016 namen de vrachtvolumes in de binnenvaart met 3,2 procent\ntoe, terwijl de omzet met 5,9 procent daalde. Deze omzetdaling werd\ndeels vertekend doordat 2015 een goed jaar was voor de binnenvaart\nvanwege laagwater. Daardoor kon in 2015 minder vervoerd worden,\nmaar voor hogere tarieven. In 2016 is hier verandering in gekomen.\nDit zorgt ervoor dat het rendement van binnenvaartschippers in 2016\nweer onder druk kwam te staan. Voor 2017 en 2018 verwachten wij\ngroei van het vervoerde volume door de binnenvaart, van 3\nrespectievelijk 2,5 procent.	55
Transport-en-Logistiek	expediteurs	prognose	De economische groei in Nederland en de eurozone zal voor meer\nvrachtvolumes zorgen, maar de expediteurs bevinden zich in een\nsterk veranderend speelveld. Gewijzigde regelgeving, strengere\ngrenscontroles, digitalisering en geopolitieke ontwikkelingen\nzorgen voor uitdagingen.	56
Transport-en-Logistiek	goederenvervoer-over-spoor	prognose	De volumes over het spoor zijn in 2016 met 0,8 procent gestegen.\nIn het eerste halfjaar van 2016 profiteerden de spoorvervoerders\nnog van het laagwater in 2015. Daardoor kon de binnenvaart minder\ngoederen vervoeren en kwam het vervoer via het spoor in beeld als\nalternatief. Naar verwachting groeien de vervoerde volumes in zowel\n2017 als 2018 met 1,5 procent.	57
Transport-en-Logistiek	goederenwegvervoer	prognose	Nu de Nederlandse economie het beter doet dan de economie in de\neurozone als geheel, profiteert het wegtransport meer van de\neconomische groei dan de kustvaart, binnenvaart en spoor:\nmodaliteiten die vooral op het buitenland gericht zijn. Naar\nverwachting groeit het wegvervoer in 2017 met 2,5 procent en in\n2018 met 2 procent.	58
Transport-en-Logistiek	opslag	prognose	De omzet van de opslagbranche is volgens de statistieken van het\nCBS in 2016 stabiel gebleven, terwijl de tarieven met 1,4 procent\nstegen. Opslagbedrijven profiteren van de toename in onder andere\nonline verkopen.	59
Transport-en-Logistiek	short-sea-shipping	prognose	Vooral de economische groei in de eurozone bepaalt de\nvolumeontwikkeling van short sea shipping. In 2016 was de\neconomische groei van de eurozone positief (1,7 procent), maar de\neconomie van de eurozone komt uit een dal en daar heeft short sea\nshipping de gevolgen van ondervonden. Naar verwachting groeit het\nvervoerde volume in zowel 2017 als 2018 met 1 procent.	60
Utilities	wind-solar	prognose	In de afgelopen jaren zijn investeringen in wind- en\nzonne-energie enorm toegenomen in Europa en Nederland. Daarmee zijn\ndeze vormen van energie de snelst stijgende vormen van energie. De\nkomende jaren zal deze trend doorzetten, met name in offshore wind,\nals gevolg van de uitvoering van het COP21 Klimaatakkoord en het\nNationale Energie Akkoord.	61
Zakelijke-dienstverlening	accountantskantoren	prognose	Vanaf 2010 heeft de branche 5 jaar omzetkrimp meegemaakt. . In\n2015 en 2016 liet de sector weer een gezonde groei zien.  Wij\nverwachten een verdere toename van de omzet in 2017, en wel\nmet 4,5 procent. In 2018 neemt de groei wat af tot 3,5%.	62
Zakelijke-dienstverlening	advocatenkantoren	prognose	De vraag naar advocaatdiensten stijgt door onder meer de\naanhoudende juridisering van de samenleving. Wel neemt de\nconcurrentie toe, ook van branchevreemde partijen. Samen met de\ntariefdruk dempt dit de omzetgroei. Voor 2017 gaan wij uit van een\ngroei van de omzet met 2,5 procent.	63
Zakelijke-dienstverlening	beveiligingsbedrijven	prognose	De verdere groei van de bedrijvigheid is gunstig voor de\nbeveiligingsmarkt. Door structurele verzadiging van de markt kan de\nsector echter weinig omzetgroei realiseren. Per saldo\ngaan wij uit van een toename van de omzet van 0,5% in 2017. In 2018\nzal de branche geen omzetgroei laten zien.	64
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	prognose	De teruggang van het aantal ambtshandelingen en geldvorderingen\nwordt deels goedgemaakt door de omzet uit het voorkomen van\ngeldvorderingen en nieuwe diensten. Ondanks de tariefdruk gaan we\nwel uit van enige tariefverhoging.	65
Zakelijke-dienstverlening	notariskantoren	prognose	Na jaren van omzetdaling is de brancheomzet de afgelopen twee\njaar weer toegenomen. Vooral het herstel van de verkoop van\nwoningen heeft hieraan bijgedragen. De woningmarkt blijft op de\nkorte termijn groeien, maar de tariefdruk blijft.	66
Zakelijke-dienstverlening	schoonmaakbedrijven	prognose	De groei van de bedrijvigheid in Nederland stimuleert de\nschoonmaakmarkt. De druk op het aantal m2 bedrijfsruimte en een\ninbestedende overheid beperken echter de volumegroei. Door zich\nmeer in te leven in de klant wordt de prijsdruk afgezwakt. Voor\n2017 verwachten wij een omzetgroei van 4,5 procent.	67
Zakelijke-dienstverlening	uitzendbureaus	prognose	Als zeer cyclische branche hebben uitzendbureaus de economische\nwind stevig in de rug. Het aantal uitzenduren is de laatste jaren\ndan ook fors toegenomen. Met de verwachte verdere stijging van de\neconomie en toenemende flexibilisering verwachten wij voor 2017 een\ngroei van de omzet van 6,5 procent.	68
\.


--
-- Name: info_table_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('info_table_info_id_seq', 204, true);


--
-- Data for Name: prog_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY prog_table (sector, branche, type, head, body, prog_id) FROM stdin;
Agrarisch	akkerbouw	prognose	Areaal voor tarwe flink afgenomen	 Het aantal akkerbouwbedrijven is in 2016\nverder gedaald. Al jaren is het aantal bedrijven in deze branche\naan het dalen. Door schaalvergroting neemt het gemiddelde areaal\nper bedrijf nog wel toe, maar het totale areaal voor akkerbouw\nneemt duidelijk af. Wel was er in 2016 een verschil te zien tussen\nde verschillende gewassen. Het areaal waar tarwe op wordt verbouwd\nnam in 2016 met 10% af, de lage prijs van tarwe zal hier een\nbelangrijke reden voor zijn. Daar stond tegenover dat het areaal\nvoor suikerbieten na een scherpe daling in 2015, in 2016 met meer\ndan 20% steeg. Het areaal voor suikerbieten zal dit jaar verder\nstijgen, met name ten koste van tarwe.	1
Agrarisch	akkerbouw	prognose	Afschaffen suikerbietenquotum zorgt voor\nprijsdaling	 In 2016 daalde het rendement van de\nakkerbouwers. Dit had met name te maken lagere volumes voor granen,\nvoedergewassen en aardappelen. De prijs van aardappelen steeg\nweliswaar flink met bijna 15%, maar dat kon er niet voor zorgen dat\nhet rendement voor de akkerbouwers steeg. Interessant  is wat\ner met suikerbieten gebeurde in 2016: daar steeg de productie\nbehoorlijk, maar nam de prijs ook af. Een voorbode van wat de\nondernemers in 2017 te wachten staat. Door het afschaffen van het\nsuikerbietenquotum wordt er in Europa dit jaar meer suikerbieten\nverbouwd.	2
Agrarisch	akkerbouw	prognose	Nederland heeft goede positie in aardappelen en\nuien	 Nederland heeft internationaal een goede\npositie op het gebied van aardappelen en uien. Er is veel kennis en\nde uitstekende infrastructuur in Nederland in combinatie met de\nlage vrachtkosten hebben voor een groei van de export gezorgd. De\nuitvoerwaarde nam toe met 17% in 2016. Voor de gehele akkerbouw\ngeldt dat de prijzen in 2017 nog onder druk blijven staan. \nEchter, door een hogere suikerbietenproductie en de goede\nconcurrentiepositie op het gebied van aardappelen en uien, zullen\nde volumes toenemen.	3
Agrarisch	kalverhouderij	prognose	Minder kalveren, maar meer rosévlees	 Het aantal vleeskalveren in Nederland is\nin 2016 met 6% toegenomen. De stijging was met name te danken aan\neen stijging van het aantal vleeskalveren voor witvlees. De\nafgelopen jaren nam met name het aantal kalveren voor rosé vlees\nflink toe. In tien jaar tijd steeg deze soort met 78%, terwijl de\nvleeskalveren voor witvlees in de zelfde periode met 5% afnam. Toch\nblijft deze laatste nog wel het grootste deel van de\nvleeskalverenstapel. Hoewel het aantal kalveren toenam, daalde het\naantal bedrijven. In 2016 waren er 1860 kalverhouderijbedrijven: 3%\nminder dan in 2015. Dit duidt op schaalvergroting in de sector.	4
Agrarisch	kalverhouderij	prognose	Vraag Azië groeit	 De consumptie van vlees staat in Europa\nonder druk. Hier staan gezondheid en duurzaamheid hoog op de agenda\nvan de consument. In Europa valt er dus niet veel groei te\nverwachten, maar wereldwijd zal de vraag nog wel groeien. En ook in\ndit segment zal de extra vraag met name uit Azië moeten komen. Voor\nkalfsvlees geldt dat de Verenigde Staten sinds vorig jaar weer een\nafzetmarkt is. De extra afzet is dan hard nodig en voor Nederlandse\nkalverhouders geldt dat  de kwaliteit van Nederlands rund- en\nkalfsvlees een  belangrijk onderscheidend aspect blijft.	5
Agrarisch	kalverhouderij	prognose	Rendement stabiel ondanks  hervorming\nlandbouwbeleid	 Zowel het inkomen uit bedrijf als de\nopbrengsten waren stabiel voor de vleeskalverhouders. De daling van\nde toeslagrechten werd in de keten gecompenseerd door lagere\nprijzen van kalveren en voerpakketten. De contractvergoeding voor\nkalverhouders kon zo zelfs wat toenemen.  ABN AMRO verwacht\nvoor de komende periode een stabilisatie van zowel de prijzen als\nde productie.	6
Agrarisch	melkveehouderij	prognose	Verwachting melkprijs positief: 15% toename in\n2017	 In 2015 daalde de melkprijs behoorlijk.\nDit had te maken met de mondiale groei van de melkproductie terwijl\nde vraag stagneerde.  In 2016 daalde de prijs van melk verder,\nmaar medio 2016 herstelde de prijs zich.  Het snelle herstel\nstabiliseerde begin 2017 op een niveau dat voor veel\nmelkveebedrijven kostendekkend is. De oorzaak van het herstel was\ndat het mondiale aanbod van melk daalde en doordat de EU met\n interventie maatregelen nam om de melkcrisis het hoofd te\nbieden. Wij verwachten dat de melkprijs in de tweede helft van dit\njaar en in 2018 langzaam door stijgt.	7
Agrarisch	melkveehouderij	prognose	Fosfaatreductieplan reduceert ook\nmelkproductie	 Hoewel het over het algemeen goed gaat\nmet de zuivelmarkt, staat de markt voor melkeiwitten nog wel onder\ndruk, mede door de interventievoorraden die boven de markt hangen.\nBoter daarentegen kent een zeer sterke vraag en de prijs van\nmelkvet is erg hoog. De bewustwording van  de consument heeft\nhier mee te maken: de realisatie dat echte boter wellicht niet zo\nongezond is , zorgt voor een hogere vraag naar boter. De uitwerking\nvan het fosfaatreductieplan in Nederland heeft tot gevolg dat de\nproductie afneemt (-3% in 2017).  Daarbij is 2017 een opmaat\nvoor 2018. De productie zal in 2018 verder dalen.	8
Agrarisch	melkveehouderij	prognose	Groei word kostbaar	In 2016 namen de volumes toe, maar doordat de prijs daalde \nten opzichte van 2015, namen de totale opbrengsten af. Doordat er\nschaalvergroting plaatsvindt binnen de melkveehouderij zijn volgens\nde WUR de gemiddelde opbrengsten per bedrijf stabiel gebleven. Het\naantal bedrijven in de melkveehouderij is de afgelopen jaren licht\n gedaald. De stoppersregeling versnelt deze daling in 2017. In\n2016 waren er circa 18.000 bedrijven met melkvee. De fosfaatrechten\nvan deze stoppers zijn nodig voor groei van collega’s. De kosten\nvan deze rechten en daarmee de kosten van marginale groei zijn\nfors.	9
Agrarisch	pluimveehouderij	prognose	Meer kippen onder Beter Leven keurmerk	 Al een aantal jaar is er weinig groei in\nhet aantal bedrijven dat actief is in de pluimveehouderij. De\nschaalvergroting is aan het stagneren, want ook het aantal\nkippen neemt af. In 2016 daalde het aantal kippen met 1,1%. Het\naantal leghennen neemt sterker af (-3,1%), dan het aantal\nvleeskuikens. In Nederland zal de productie van pluimveevlees\nverder afnemen, doordat Nederlandse ondernemers zich meer gaan\nrichten op duurzamere varianten van pluimvee waarvoor meer\noppervlak per dier nodig is. Uit cijfers van Beter Leven blijkt\n dat het aantal vleeskuikens en leghennen dat gehouden wordt\nonder het beter leven keurmerk sterk is gegroeid.	10
Agrarisch	pluimveehouderij	prognose	Lage prijzen voor pluimveevlees en eieren	De prijs van zowel het pluimveevlees als de prijs van eieren is\nin 2016 gedaald. Belangrijkste oorzaak van de prijsdaling is het\nhoge aanbod in Europa. Met name in Oost-Europa is de productie van\neieren en pluimveevlees toegenomen. De Europese productie zal ook\nin 2017 nog hoog zijn en dit zorgt voor een blijvende druk op de\nprijzen. De export speelt een belangrijke rol voor vlees en eieren.\nVoor eieren is Duitsland een zeer belangrijk exportland, maar voor\nhet pluimveevlees is het Verenigd Koninkrijk een belangrijke\nexportmarkt. De gevolgen van de Brexit kunnen vanaf  in 2018\neen rol gaan spelen voor de export van pluimveevlees.	11
Agrarisch	pluimveehouderij	prognose	Opbrengst eieren afgenomen	 De lagere prijzen in 2016 voor\npluimveevlees werd gecompenseerd door daling van de kosten van voer\nen eendagskuikens. Hierdoor steeg de voerwinst voor reguliere\nbedrijven.  De opbrengsten voor eieren nam met gemiddeld 4,9%\naf maar de variatie in resultaten tussen de verschillende\nhouderijsystemen verschilt sterk. Behalve op voliëre bedrijven nam\nde voerwinst op de meeste bedrijven toe. Voor de komende jaren\ngeldt dat supermarkten zich richten op het verduurzamen van hun\naanbod, wat zal leiden tot verdere groei van deze markt.  Voor\n2017 verwacht ABN AMRO stabilisering van de markt voor\npluimveevlees waarbij de export van minder edele kipdelen\nbelangrijk is voor het totaalrendement in de keten. In de legsector\nverwachten we prijsdruk in de markt voor kolonie eieren,\nstabilisatie in scharrel en toename van vraag en prijs in het\nbiologische en vrije uitloop segment.	12
Agrarisch	sierteelt	prognose	Arealen lopen terug	 In 2016 zijn voor nagenoeg alle\ncategorieën de arealen teruggelopen. Niet alleen de arealen zijn\nteruggelopen, ook het aantal bedrijven neemt al jaren (in sterkere\nmate) af. In 2016 nam het aantal bedrijven \nHet areaal nam met 6% af. De Nederlandse telers hebben de laatste\njaren moeite met bedrijfsopvolging en het genereren van voldoende\nrendement waardoor bedrijven ophouden te bestaan. Daarnaast is\nlijkt de rozenteelt in Nederland zich te stabiliseren.	13
Agrarisch	sierteelt	prognose	Exportwaarde neemt opnieuw toe: Brexit speelt rol in\n2017 en 2018	 De exportwaarde van sierteeltproducten\nnam in 2016 met circa 6% toe. Bijna 90% van de export van bloemen\nen planten vindt plaats binnen Europa. Met name Duitsland is een\nbelangrijk land. Maar liefst een derde van alle geëxporteerde\nbloemen en planten gaat naar Duitsland. Het Verenigd Koninkrijk\nvolgt op de tweede plek met 12% van alle export van bloemen- en\nplanten. De onzekerheid rond de Brexit zal een belangrijke\n rol blijven spelen voor de export van snijbloemen en\npotplanten. Zowel in 2017, als in 2018.	14
Agrarisch	sierteelt	prognose	Planten en Bloemen hebben tijdsbeeld mee	 De hogere export, maar ook de\nverbetering van de Nederlandse economie droegen bij aan het\nrendement van de sector; 2016 was dan ook een goed jaar. De bloemen\n& planten sector heeft het tijdsbeeld mee. Een groene\nleefomgeving draagt positief bij aan het leefklimaat en\nconsumenten, maar ook bedrijven, overheden en horeca spelen daar\nsteeds vaker op in. Nu in 2017 de inkomens naar verwachting zullen\nstijgen, zullen de volumes in planten & bloemen verder toenemen\n(2%) en door een hogere vraag, zal ook de prijs stijgen.  Voor\n2018 verwachten wij dat de koers van het pond zal dalen, dat zal\nvoor een exportdaling naar het VK leiden. De groei voor 2018\nschatten we daarom lager in: 1%.	15
Agrarisch	varkenshouderij	prognose	Varkensstapel flink afgenomen in 2016	 De varkensstapel is in 2016 met bijna 5%\nflink afgenomen. Gemiddeld ontwikkelt de varkensstapel zich rond de\n0,5%, een afname van 5% is dan ook fors te noemen. De voornaamste\noorzaak van het inkrimpen van de varkensstapel is de prijsval\ngeweest in de afgelopen jaren. Al sinds 2012 daalden de prijzen\nvoor vleesvarkens. In vier jaar tijd nam de prijs met 20% af. Een\ntegenvallende consumptie in combinatie met een hoge productie waren\nhiervan de oorzaak. Hierdoor nam het rendement af en daalde de\nproductie. Ondanks de daling in Nederland steeg de\nzelfvoorzieningsgraad in Europa tot 120 á 125 procent. Wij\nverwachten de komende jaren lichte daling van de Nederlandse\nvarkensstapel.	16
Agrarisch	varkenshouderij	prognose	Prijsstijgingen voor varkenshouders	 Een lagere prijs door het inkrimpen van\nde varkensstapel is een typisch kenmerk van de varkenscyclus.\nIn 2016 steeg de prijs voor vleesvarkens behoorlijk  (8%). De\nprijs van biggen steeg in de eerste twee maanden van 2017 verder en\nnam met circa 30% jaar op jaar toe. De vraagkant staat echter wel\nonder druk. De afzet naar Azië en daarbinnen vooral China is sterk\ngegroeid en lijkt ook voor de toekomst een belangrijke pijler te\nblijven. Toch blijft Europa de belangrijkste exportmarkt.  En\ndaar daalt de consumptie van varkensvlees. De trend om minder vlees\nte eten, vanwege duurzaamheidsredenen (klimaat of dierenwelzijn),\nmaar ook de lage bevolkingsgroei zorgen voor stagnatie.	17
Agrarisch	varkenshouderij	prognose	Goed jaar voor varkenshouders	 De hogere prijs zorgde voor goede\nrendementen bij de varkenshouders. Volgens de WUR was er in de\nvarkenshouderij in 2016 zelfs sprake van een historisch hoog\ninkomen. Een welkome afwisseling van de vorige jaren, waarin er\nsprake was van relatief veel faillissementen door lage rendementen.\nHet aantal bedrijven loopt al een aantal jaren terug en in 2016 nam\nhet aantal bedrijven in de varkenshouderij \nIn 10 jaar tijd is het aantal bedrijven met een derde afgenomen.\nWij verwachten de komende jaren een stevige daling van het aantal\nbedrijven.	18
Agrarisch	visserij	prognose	Vloot gelijk gebleven, maar aantal oudere schepen\ntoegenomen	 Na een aantal jaren van daling is in\n2016 de vissersvloot gestabiliseerd, maar is de samenstelling\nveranderd. Zo is het aantal kotterschepen toegenomen en ook nam het\naantal zeevisserij schepen toe. Het aantal mosselschepen\ndaarentegen daalde naar 51 schepen. De vissersvloot bestaat uit\ncirca 600 schepen. Het grootste deel van deze vloot is ouder dan 20\njaar. In 2016 nam het aantal schepen boven de 20 jaar met 2% toe.\nDe belangrijkste reden voor de veroudering van de vloot is het\ntekort aan ruimte voor investeringen. Voor 2017 verwachten wij dat\nde capaciteit licht toeneemt.	19
Agrarisch	visserij	prognose	Aanvoer vis toegenomen	 Na een aantal jaren van tegenvallende\nprestaties, heeft de Nederlandse visserij het in 2016 financieel\ngoed gedaan. \nnam volgens de WUR met 4% toe: met name de aanvoer van rode poon\nnam toe, maar ook de aanvoer van inktvis en makreel steeg.  De\naanvoer van de grote visserij steeg ook (13%). Vooral haring en\nblauwe wijting droegen bij aan deze stijging. Ook de prijzen\nstegen, waardoor de opbrengsten flink toenamen in 2016. De\nmosselsector kreeg vorig jaar, door het aantreffen van\ntetrodotoxine in mosselen, te maken met een behoorlijk volumedaling\n(34%) en een prijsdaling (21%)	20
Agrarisch	visserij	prognose	In 2017 en 2018 zal Brexit een grote rol\nspelen	De Brexit kan voor vissers een grote impact hebben. Allereerst\nnatuurlijk de economische impact van een tegenvallende handel met\nhet Verenigd Koninkrijk. Maar daarnaast heerst de angst in de\nNederlandse visserijbranche dat wordt besloten om Britse waters\nalleen toegankelijk te maken voor Britse vissers. Dit zou de\nNederlandse visserij schade kunnen berokkenen. Vooralsnog verwacht\nABN AMRO een soft Brexit, dat betekent dat de onderhandelingen, ook\nover de verdeling van de visserijgronden, soepel zullen\nverlopen.	21
Agrarisch	voedingstuinbouw	prognose	Export groente en fruit flink gegroeid	 Met 9% is de export van groente en fruit\nflink gestegen in 2016. De totale exportwaarde kwam hiermee voor\nhet eerst boven de 16 miljard euro uit. Nagenoeg het hele\nlandenspectrum droeg bij aan de groei, maar de hoogste groei\nnoteerde Azië met 13%. Maar ook de export naar het belangrijkste\nexportland Duitsland steeg sterk (8,5%).  En ondanks de Brexit\nviel ook de export naar het Verenigd Koninkrijk licht hoger uit\n(1,3%). De Brexit speelt ook in 2017 en 2018 een belangrijke rol in\nde groente- en fruitbranche. Voor 2017 zal het de export nog niet\nin hoge mate beïnvloeden, maar de verwachting is dat in 2018 de\ngevolgen van de Brexit duidelijker zichtbaar zullen worden.	22
Agrarisch	voedingstuinbouw	prognose	Rendement op hoog niveau	 In 2015 stegen de gemiddelde opbrengsten\nvoor de telers van glasgroente fors. In 2016 bleven de opbrengsten\nvoor deze ondernemers op een hoog niveau.  Voor fruit stegen\nde volumes en de prijs nog wel, maar daar lagen de opbrengsten nog\nop een laag niveau. De inkomsten in de groente- en fruitsector\nstaan al jaren onder druk. De prijsvorming van groente en fruit is\nsterk aanbod gedreven en door hoge concurrentie staan de prijzen\nonder druk. Zo geldt voor appels bijvoorbeeld dat er concurrentie\nis vanuit het zuidelijk halfrond. Bovendien is, met behulp van EU\nsubsidies, de productie uit Polen toegenomen. Door de Rusland\nboycot komen deze Poolse appels ook op de Duitse markt die juist\nvoor Nederland belangrijk is.	23
Agrarisch	voedingstuinbouw	prognose	Consumentenprijzen groente en fruit\ngestegen	 De consumentenprijzen van  groenten\nen fruit kenden een relatief sterke groei met respectievelijk 4,3%\nen 4,5%.  Ook vorig jaar stegen deze categorieën het\nsterkst.  De groente- en fruitprijzen zijn volatieler dan\nandere prijzen. Dat komt doordat deze prijzen sterk aanbod gedreven\nzijn en in sterke mate afhankelijk van het weer. Zo heeft het koude\nweer in Spanje eind 2016 voor een prijsstijging gezorgd voor een\naantal groentesoorten.  Voor 2017 verwacht ABN AMRO dat de\ndruk op de prijzen blijft bestaan, maar dat de volumes voor\ngroente  De sector heeft\ngeïnvesteerd in kleinverpakkingen en relaties met retailers en dat\nheeft zijn vruchten afgeworpen.	24
Bouw	architectenbureaus	prognose	Herstel woningmarkt belangrijk voor architecten	Het grootste gedeelte van de opdrachten van architecten betreft\nopdrachten voor nieuwe woningen. Daarom profiteren architecten nu\nvan de opleving van de woningmarkt wat zich met enige vertraging\nvertaalt in de bouw van nieuwe woningen. Het aantal\nwoningtransacties steeg in 2016 met 20,5 procent, maar naar\nverwachting zal de komende jaren de woningmarkt in rustiger\nvaarwater komen. De transacties zullen in 2017 met 5% stijgen en in\n2018 dalen met 5%. Het aantal verkochte nieuwbouwwoningen steeg in\n2016 met 10 procent. In 2016 werden 53.872 nieuwe woningen gebouwd,\neen stijging van 11,3 procent ten opzichte van 2015.	25
Bouw	architectenbureaus	prognose	Tarieven architecten stijgen weer	In navolging van het herstel van de woningmarkt en woningbouw,\nkunnen architecten weer hogere prijzen vragen. Het eerste herstel\nwas in 2015 al zichtbaar, toen stegen de tarieven van architecten\nmet 0,3%, niet gecorrigeerd voor inflatie. In 2016 zette de\nontwikkeling door. Toen stegen de tarieven met 1,7%. Dit heeft\nervoor gezorgd dat de omzet in 2016 ook flink steeg. In 2016 is het\naantal architectenbureaus met maar 1 werknemer licht gedaald. Nu\nhet weer beter gaat met de architectenbureaus zijn zzp’ers die\nnoodgedwongen voor zichzelf waren begonnen weer in dienst gegaan\nvan een groter bureau.	26
Bouw	architectenbureaus	prognose	Nieuwe opdrachten architecten in woningbouw	Dat de woningbouw belangrijk is voor architecten, blijkt ook uit\nde nieuwe opdrachten die architecten krijgen. In de eerste drie\nkwartalen van 2016 steeg het aantal ontvangen opdrachten met 14\nprocent. Dit kwam door meer opdrachten voor nieuwe woningen en\nrenovatie van woningen. Architecten kregen minder opdrachten voor\nde renovatie en nieuwbouw van utiliteitsgebouwen. Wel hebben de\narchitecten nog veel minder opdrachten dan voor de crisis.	27
Bouw	grond--weg-waterbouw	prognose	Overheidsinvesteringen van grote invloed op gww	De overheidsinvesteringen zijn zoals gezegd van grote invloed op\nde gww. De afgelopen jaren is er door de Rijksoverheid meer\ngeïnvesteerd in het Deltafonds, bedoeld voor het bewaken van de\nwaterkwaliteit- en veiligheid. De investeringen in het Deltafonds\nnemen in 2017 sterk af, maar daarna is er weer groei te zien. De\ninvesteringen in het Infrastructuurfonds nemen vanaf 2017 weer toe.\nDit betekent dat per saldo de investeringen van de overheid vanaf\n2018 toe gaan nemen, met gemiddeld 1,3 procent per jaar. Vooral de\nwegenbouwers kunnen hiervan profiteren.	28
Bouw	grond--weg-waterbouw	prognose	Branches gww ontwikkelen zich wisselend	De branches binnen de gww ontwikkelden zich wisselend in 2016.\nDe omzet van natte waterbouwers daalde met 26 procent j-o-j in de\neerste drie kwartalen van 2016. Het feit dat de Rijksoverheid\nminder investeert in het Deltafonds speelde hen parten. De andere\nbranches binnen de gww deden het beter. De omzet van de kabel- en\nbuizenleggers steeg met 11,5 procent in 2016. Zij profiteerden van\nde toenemende bouw van nieuwe woningen De omzet van bouwers van\nwegen, tunnels en spoorwegen steeg met 1,6 procent in 2016.	29
Bouw	grond--weg-waterbouw	prognose	Orderportefeuille stijgt licht	De orderportefeuille van gww-bouwers steeg heel licht in 2016\nvan 5,8 naar 6 maanden. De orderportefeuille is nog wel een stuk\nlager dan die van de woning- en utiliteitsbouwers, die lag in\ndecember 2016 op 9,9 respectievelijk 8,9 maanden. Maar de\norderportefeuille ligt wel hoger dan het langetermijngemiddelde van\n5,7 maanden. De orderportefeuille van de wegenbouwers steeg heel\nlicht van 5,6 naar 5,7 maanden. De orderportefeuille van de grond-\nen waterbouwers steeg van 6,1 naar 6,4 maanden.	30
Bouw	groothandel-hout-bouwmaterialen	prognose	Verhuizen zet aan tot verbouwen	De woningmarkt is belangrijk voor de groothandel in\nbouwmaterialen, omdat een verhuizing vaak betekent dat er verbouwd\nwordt in het nieuwe (of oude) huis. Kleine aannemers en ook\nparticulieren kopen hun materiaal daarvoor bij de groothandel in.\nDe verwachting is dat de woningmarkt in 2017 en 2018 minder hard\ngaat groeien. Vooral de woningtransacties zijn van belang. In 2016\nsteeg het aantal transacties met 20,5 procent. De verwachting is\ndat het aantal transacties in 2017 met 5 procent groeit en in 2018\nmet 5 procent daalt.	31
Bouw	groothandel-hout-bouwmaterialen	prognose	Ontwikkeling kleine bouwers van belang voor groothandel	Vooral de kleine bouwers doen hun inkopen bij de groothandel, al\nontstaat steeds meer concurrentie van grote bouwmarkten. Grote\nbouwers slaan de groothandel over en kopen rechtstreeks in bij de\nindustrie. De kleine bouwers hadden in 2016 een topjaar, hun omzet\nsteeg met 8,5 procent. De kleine bouwers actief in de woning- en\nutiliteitsbouw zagen hun omzet met 9,3 procent stijgen. Daarmee\nlaten ze de grote bouwers ruim achter zich. De middelgrote bouwers\nzijn aan een inhaalrace bezig. Hun omzet steeg in 2016 met 11,5\nprocent. De kleine bouwers profiteren van het herstel van de\nwoningmarkt. De verwachting is dat zij het in 2017 en 2018 ook goed\nblijven doen, maar dat het groeitempo wel wat zal afnemen.	32
Bouw	groothandel-hout-bouwmaterialen	prognose	Hout- en bouwmaterialenindustrie graadmeter voor\ngroothandel	De producenten van hout- en bouwmaterialen zijn belangrijk voor\nde groothandel in bouwmaterialen, omdat de groothandel bij de\nindustrie hun producten inkoopt. De omzet van de groothandel wordt\ndaarom voor een groot deel bepaald door de afzetprijzen van de\nindustrie. De afzetprijzen voor zowel houtproducten als\nbouwmaterialen stegen in 2016. Van houtproducten met 4,3 procent en\nvan bouwmaterialen met 0,7 procent. Dit zorgt voor extra prijsdruk\nbij de groothandel.	33
Bouw	hout-bouwmaterialenindustrie	prognose	Nieuwbouw van belang voor verder herstel	De bouwmaterialenindustrie is sterk afhankelijk van de nieuwbouw\nen dus van de grote opdrachtgevers. Afgelopen jaar is de\nnieuwbouwproductie van woningen wederom sterk gestegen, maar er\nwordt vooral veel materiaal gebruikt bij de nieuwbouw van\nutiliteitsgebouwen en in de grond-, water- en wegenbouw (gww). In\n2017 is herstel van de utiliteitsbouw te verwachten en vanaf 2018\nzal de gww gaan aantrekken. Hiervan kan de bouwmaterialenindustrie\nprofiteren.	34
Bouw	hout-bouwmaterialenindustrie	prognose	In- en uitvoer nemen toe door herstel bouwsector	De invoer van zowel hout als bouwmaterialen steeg in 2016 als\ngevolg van de sterke groei van de bouwproductie. De invoer van hout\nsteeg met 4,6 procent en de invoer van bouwmaterialen met 7,5\nprocent. Ook de uitvoer nam in 2016 toe, van hout met 0,7 procent\nen van bouwmaterialen met 10,3 procent. De invoerprijzen van hout\ndaalden in 2016 met 1 procent, wat gunstig is voor de Nederlandse\nproducenten van houtmaterialen.  De invoerprijzen van\nbouwmaterialen stegen met 1,4 procent. Dit konden de\nbouwmaterialenproducenten waarschijnlijk doorberekenen aan hun\nklanten, want hun omzet steeg hard in 2016.	35
Bouw	hout-bouwmaterialenindustrie	prognose	Bezettingsgraad bouwmaterialenindustrie herstelt verder	De bezettingsgraad (benutting van beschikbare\nproductiecapaciteit) van de bouwmaterialenindustrie laat herstel\nzien. De bezettingsgraad van de bouwmaterialenindustrie steeg in\n2016 van 79,9 procent naar 81 procent. De bezettingsgraad van de\nhoutindustrie daalde in 2016 heel licht van 83,7 procent naar 83,6\nprocent. De bezettingsgraad van de houtindustrie bevindt zich wel\nboven het langjariggemiddelde, die van de bouwmaterialenindustrie\nnog niet. De bouwmaterialenindustrie kan verder profiteren van de\naantrekkende nieuwbouw en in 2018 van de aantrekkende\ninfrastructuur.	36
Bouw	ingenieursbureaus	prognose	Internationale onzekerheden risico voor ingenieurs	In 2016 werden we opgeschrikt door een aantal onverwachte\neconomische ontwikkelingen, waarvan de uitslag van het Brexit\nreferendum en de verkiezing van Trump als president van de\nVerenigde Staten de belangrijkste waren. De verwachte negatieve\neconomische ontwikkelingen van met name het Brexit referendum zijn\nvooralsnog uitgebleven. Nu het Britse parlement premier May\ntoestemming heeft gegeven om de artikel 50-procedure te starten,\nkan de onzekerheid weer oplopen. De grote ingenieursbureaus zijn\nveelal actief buiten Nederland en hebben daarom als eerste last van\ndeze onzekerheden. Dit is een risico voor hen.	37
Bouw	ingenieursbureaus	prognose	Investeringen infrastructuur vanaf 2018 gunstig	De investeringen in de infrastructuur door de Rijksoverheid zijn\nbelangrijk voor ingenieurs. Deze investeringen gaan vanaf 2018 weer\ngroeien. Dit komt doordat er vanaf 2018 weer meer geïnvesteerd\nwordt in de infrastructuur. In de waterveiligheid wordt sinds 2015\nminder geïnvesteerd. Maar per saldo nemen de investeringen vanaf\n2018 weer toe. Er zal vanaf dan vooral meer in wegen worden\ngeïnvesteerd.	38
Bouw	ingenieursbureaus	prognose	Orderportefeuille ingenieurs daalde in 2016	De orderportefeuille van ingenieurs steeg lange tijd, maar daar\nis in 2016 verandering in gekomen. In november 2015 bedroeg de\norderportefeuille nog 6 maanden. De orderportefeuille is daarna\ngestaag gedaald naar 4,8 maanden in november 2016. Ingenieurs zijn\nwel positiever over hun orders voor de komende maanden. Ze zijn\nminder positief over hun winstgevendheid. Volgens het EIB was de\nwerkgelegenheidsverwachting positief.	39
Bouw	installatiebedrijven	prognose	Ontwikkelingen industrie van belang	Na de utiliteitsbouw is de industrie de\nbelangrijkste sector voor installateurs. Naar verwachting groeit de\nindustrie in 2017 met 2 procent en in 2018 met 2,3 procent. De\ninstallateurs zijn vooral afhankelijk van de procesindustrie, zoals\nde chemie, de metaalproductenindustrie en de voedings- en\ngenotmiddelenindustrie. Voor al deze branches wordt groei verwacht\nin 2016 en 2017.	40
Bouw	installatiebedrijven	prognose	Transformatie is een kans en noodzaak	Transformatie van gebouwen is een kans voor installateurs. Een\nbelangrijk deel van de transformatie betreft het inpassen van\ninstallaties, het gebouw staat namelijk al. Het aantal\ntransformaties neemt gestaag toe, nu steeds duidelijker wordt dat\ner noodzaak is tot omvormen van leegstaande gebouwen. In de periode\njanuari 2012 tot en met juni 2015 werden 39.656 woningen gecreëerd\ndoor middel van transformatie. Bijna 25 procent in kantoren en 12\nprocent in winkels. Leegstaande kantoren staan vaak in de\nbinnenstad waardoor het kansrijk is om ze te transformeren.	41
Bouw	installatiebedrijven	prognose	Orderportefeuille installateurs stijgt	De orderportefeuille van installateurs steeg in november 2016\nten opzichte van mei 2016. In november bedroeg de orderportefeuille\n6,8 maanden, terwijl die in mei nog 6,3 maanden bedroeg. De\norderportefeuille is flink gestegen sinds het dieptepunt in\nnovember 2013 toen de orderportefeuille 4,8 maanden bedroeg.\nVolgens het EIB zijn installateurs positiever over hun resultaat en\nde prijsontwikkeling.	42
Bouw	utiliteitsbouw	prognose	Vergunningen nieuwbouw stijgen weer	De nieuwbouw van utiliteitsgebouwen zal in 2017 en 2018 gaan\ngroeien. Het aantal afgegeven vergunningen voor nieuwe\nutiliteitsgebouwen steeg in 2016 met 1,6 procent en de waarde van\ndeze vergunningen met 4 procent. Het aantal en de waarde van de\nafgegeven vergunningen voor nieuwe combinatie bedrijfshallen en\nkassen steeg. Voor nieuwe kantoren nam de waarde van de\nvergunningen toe. Voor nieuwe hallen en loodsen en winkels steeg\nhet aantal afgegeven vergunningen. De leegstand van kantoren begint\naf te nemen en door de economische groei is er meer vraag naar\nnieuwe, duurzame kantoren. De leegstand van winkels neemt nog\ntoe.	43
Bouw	utiliteitsbouw	prognose	Transformatie is een kans	Door de hoge leegstand, aantrekkende woningmarkt en schaarse\nruimte in de stad wordt er steeds meer belang gehecht aan het\ntransformeren van leegstaande gebouwen naar woningen. In de periode\njanuari 2012–juni 2015 zijn er volgens het CBS 39.656 woningen\ngecreëerd door middel van transformatie. Ter vergelijking, in deze\nperiode zijn er 165.687 nieuwbouwwoningen opgeleverd. Transformatie\nvan gebouwen is een groeimarkt. Dit is een kans voor\nutiliteitsbouwers, waar zij wel concurrentie ondervinden van\nwoningbouwers. De vergunningen die hiervoor worden afgegeven worden\nook onder de woningbouw geschaard.	44
Bouw	utiliteitsbouw	prognose	Orderportefeuille utiliteitsbouwers stijgt	De orderportefeuille van utiliteitsbouwers steeg in 2016 van 7,5\nmaanden naar 8,9 maanden. De orderportefeuille ligt inmiddels weer\nboven het niveau van voor de crisis. De orderportefeuille is sinds\n2000 nog niet zo hoog geweest. De verklaring voor deze hoge\norderportefeuille moet gezocht worden in het feit dat bouwers die\nnog in de utiliteitsbouw actief zijn voldoende werk hebben.	45
Bouw	woningbouw	prognose	Woningmarkt is de groeimotor	De groei van de woningbouw wordt veroorzaakt door de gunstige\nontwikkelingen op de woningmarkt. Dit was in 2016 al het geval en\nzal in 2017 en 2018 ook zo zijn. Wel zal het groeitempo afnemen. De\nwoningmarkt herstelt niet meer alleen in de Randstad, in heel\nNederland stijgen de woningtransacties. Ook de woningprijzen\nstijgen in steeds meer gebieden hard. Dit heeft vooral een positief\neffect op de nieuwbouw van woningen. Maar verhuizingen zorgen ook\nvoor renovatiewerkzaamheden.	46
Bouw	woningbouw	prognose	Rekening houden met de demografische ontwikkelingen	De demografische ontwikkelingen lijken een\nlangetermijnontwikkeling waar we nog geen rekening mee hoeven\nhouden, maar de demografie beïnvloedt de woningbouw nu al. Er komen\nsteeds meer eenpersoonshuishoudens en de bevolking wordt steeds\nouder. Hier moeten opdrachtgevers en bouwers van nieuwe woningen\nrekening mee houden. Er is behoefte aan kleinere woningen, omdat\ndeze betaalbaarder zijn. Ook moeten woningen levensbestendig\nzijn.	47
Bouw	woningbouw	prognose	Grondprijzen ook omhoog	In navolging van de woningprijzen, zijn ook de grondprijzen hard\ngestegen. In 2016 stegen de grondprijzen met 2 procent, terwijl de\nprijzen van bestaande koopwoningen met 5,1 procent stegen.\nGrondprijzen stegen lange tijd harder dan de prijzen van\nkoopwoningen. Daardoor namen de kosten voor ontwikkelaars ook toe,\nwat slecht was voor de marges die op nieuwe woningen behaald konden\nworden. In 2016 kwam dit meer in evenwicht.	48
Food	agf-industrie	prognose	Gezond ‘kant-en-klaar’ groeit fors	Sommige trends in de AGF-branche zijn al een paar jaar geleden\ningezet. Nu deze lijken te versnellen, wordt hun impact op de omzet\nvan de AGF-industrie steeds duidelijker. Zo zien we gemaksproducten\nals kant-en-klaarmaaltijden jaarlijks gemiddeld 10 procent\ntoenemen. Dat vooral de gezondere varianten binnen deze\nproductgroep floreren, is niet vreemd: het bewustzijn onder\nconsumenten dat goede voeding belangrijk is, groeit nog steeds.	49
Food	agf-industrie	prognose	Ook export stijgt	Bereide en geconserveerde groenten vertegenwoordigen een\nuitvoerwaarde van 3,3 miljard euro. Hiermee nemen ze een belangrijk\ndeel van de totale export van groente en fruit voor hun rekening.\nIn 2016 steeg de uitvoerwaarde van de AGF-industrie met 10 procent.\nOngeveer een kwart van de AGF-export is op Duitsland gericht, en 15\nprocent gaat richting Verenigd Koninkrijk. De uitvoer naar beide\nlanden nam toe, maar dit jaar is de Brexit een belangrijk thema.\nVoor de hele foodsector, en dus ook voor de AGF-industrie.	50
Food	agf-industrie	prognose	Gevolgen Brexit vallen nog mee	Tot dusver heeft de Brexit geen sporen achtergelaten in de\nAGF-industrie. Voor de totale foodsector ligt dit iets anders: hier\ndaalde de export naar het Verenigd Koninkrijk met 2 procent. In\n2017 verwachten we een soft Brexit. Dat wil zeggen:\nnormale onderhandelingen tussen de EU en het Verenigd Koninkrijk\nmet relatief weinig obstakels. Bij een hard Brexit\nverlopen de onderhandelingen juist stroef, met grotere gevolgen\nvoor alle partijen.	51
Food	brood-deegwarenindustrie	prognose	Brood en banket goedkoper	De laatste jaren was de berichtgeving over de consumptie van\nbrood- en banketproducten minder positief. Dit zette de branche\nonder druk. Het effect was onder meer zichtbaar in de\nconsumentenprijs van brood, die 1 procent daalde in 2016. Dit is\nrelatief veel, want de broodprijs is doorgaans vrij stabiel en kent\nhooguit minimale stijgingen of dalingen. De reden voor deze daling\nligt aan de inkoopkant; de prijs van tarwe daalt al jaren\nachtereen. Naar verwachting zal de broodprijs ook in 2017 onder\ndruk blijven staan. Voor zoete bakkerijproducten geldt deels\nhetzelfde. In 2015 lag de verkoopwaarde hiervan 15% onder het\nniveau van 2013. Wij verwachten dat deze daling inmiddels is\ngestabiliseerd en voorspellen een vergelijkbaar prijspeil in\n2017.\n 	52
Food	brood-deegwarenindustrie	prognose	Kansen door vergrijzing	De brood- en deegwarenindustrie is een brede branche met\nverschillende nichespelers. Hoewel de verkoopwaarde is gedaald,\nlopen de categorieën sterk uiteen. Zo zakt het aandeel van de\ngrootste groepen, zoals brood, taart en koek. Daar staat weer groei\nvan de ontbijtgranen en granenrepen tegenover. Uit onderzoek van\nGlobal Data blijkt dat de granenrepen vooral populair zijn bij\njonge kinderen én ouderen. Door de toenemende vergrijzing vormt met\nname die laatste consumentengroep een aantrekkelijke markt.\n 	53
Food	brood-deegwarenindustrie	prognose	Weinig faillissementen, maar meer\nopheffingen	Net als het jaar ervoor, gingen er in 2016 weinig ondernemingen\nfailliet in de brood- en deegwarenindustrie: vijftien in totaal,\ntwee meer dan in 2015. Het aantal opheffingen steeg wel sterk. In\n2016 stopten 230 ondernemers met hun bedrijf, terwijl dat er in\n2015 slechts 180 waren. Vooral kleinere bedrijven trekken de\nstekker er zelf uit. Zij ondervinden concurrentie van supermarkten\ndie hun assortiment in termen van kwaliteit en beleving hebben\nverbeterd.	54
Food	drankenindustrie	prognose	Export omhoog	De uitvoerwaarde van dranken nam in 2016 met 2,5 procent toe. Er\nging voor circa vier miljard euro de grens over. Het grootste deel\nhiervan waren alcoholhoudende dranken (70%). Het Verenigd\nKoninkrijk is een belangrijke afzetmarkt: maar liefst 10 procent\nvan de totale export gaat hierheen. Ondanks de Brexit steeg dit\npercentage in 2016 flink.	55
Food	drankenindustrie	prognose	Omzet slijterijen daalt al vijf jaar	In Nederland geven we circa één miljard euro per jaar uit aan\nbier. Met 670 miljoen euro ligt dit bedrag voor sterke dranken iets\nlager. Het meeste besteden we aan wijn: jaarlijks zo’n twee miljard\neuro. Hoewel we vooral in de supermarkt alcoholhoudende dranken\nkopen, houden slijterijen hun aandeel nog vrij goed vast. Hun omzet\ndaalt wel al vijf jaar op rij, maar dit feit past in het grotere\nplaatje: speciaalzaken verliezen terrein op de supermarkten.	56
Food	drankenindustrie	prognose	Consument ‘drinkt’ steeds bewuster	De consumptie van frisdrank is in vier jaar met 10 procent\nafgenomen. Een vergelijkbare daling zien we bij sappen. De oorzaak\nis een steeds bewustere consument. Mineraal- en bronwaters, waters\nmet een smaakje en thee nemen juist in populariteit toe. Volgens\nstatistieken van sectorvereniging Nederlandse Brouwers steeg de\nbierconsumptie in 2016 met 1,4 procent. Pils is hierbij de\nbelangrijkste categorie, maar het gebruik hiervan daalde in deze\nperiode juist (-0,1%). Opvallend genoeg zijn we vorig jaar flink\nmeer speciaalbier en alcoholvrij bier gaan drinken (+13%\nrespectievelijk +18%). Het liefst hebben we bier van eigen bodem:\nslechts 15 procent van het bier dat we drinken is geïmporteerd.	57
Food	groothandel-in-voedingsmiddelen	prognose	Binnenlandse consumptie én export groeien	In 2016 steeg de totale particuliere consumptie in Nederland met\ngemiddeld 2 procent. Het groeivolume voor supermarkten liep hiermee\ngelijk, voor horeca was dit zelfs 6 procent. Aan voeding gaven we\nzo’n 3 procent meer uit, in lijn met het langetermijngemiddelde.\nDeze groeicijfers stuwden de omzet van de groothandels. Daarnaast\nnam de export van voedingsmiddelen toe, vooral naar Duitsland. De\nuitvoer van AGF-producten steeg, net als die van kaas en cacao.	58
Food	groothandel-in-voedingsmiddelen	prognose	Aantal faillissementen stabiel laag	In 2016 gingen er 63 groothandels in food failliet. Een laag\nniveau, dat strookt met een aantrekkende omzet. Wel opvallend is\nhet stijgende aantal opheffingen onder groothandels in\nvoedingsmiddelen. Hielden in 2015 nog 835 handelaren het voor\ngezien, in 2016 waren dit er 1.150. Deze stijging van bijna 40\nprocent duidt op een competitieve markt, waarin het lastig is om je\nvan concurrenten te onderscheiden.	59
Food	groothandel-in-voedingsmiddelen	prognose	Duitsland belangrijkste afzetmarkt	Voor groothandels in voedingsmiddelen is Duitsland een\nbelangrijk exportland. Met 9 à 10 procent van hun totale\nbestedingen geven Duitsers net zo veel uit aan voeding en\nniet-alcoholische dranken als wij. Dat lijkt veel, maar vergeleken\nmet andere EU-landen is het relatief weinig. Toch zijn er meer\nparallellen met onze oosterburen. Ook de Duitse consument heeft\ngroeiende verwachtingen als het om voedingskwaliteit gaat en\nbeweegt zich steeds meer richting organische- en\nfairtradeproducten. De Duitse economie groeide in 2016 met 1,8\nprocent. Voor 2017 verwachten we een vergelijkbaar\ngroeipercentage.	60
Food	visindustrie	prognose	Stijgende export vooral Europees feestje	In 2016 steeg de exportwaarde van vis met 12 procent. De totale\nexportwaarde bedroeg 3,4 miljard euro. Een forse stijging, mede\ndankzij Aziatische en Amerikaanse import. Toch is deze stevige plus\nvooral een Europees succes, waarmee vis een uitzonderingspositie\ninneemt ten opzichte van andere food-branches. Net als in 2015,\ngroeide vorig jaar de export naar Zuid-\nen Oost-Europa hard. Doordat de economie ook in deze landen\naantrekt, eten ze daar meer vis. Met een toename van 50 procent in\ntien jaar staat de visexport op een zeer hoog niveau.	61
Food	visindustrie	prognose	Consument hecht waarde aan certificering	Uit onderzoek van Marine\nStewardship Council (MSC) blijkt dat consumenten bij FMCG vaker\nnaar merk en prijs kijken dan naar duurzaamheid. Dit geldt niet\nvoor vis: 68 procent van de viseters zegt het belangrijk te vinden\nom duurzame vis te kopen. Hetzelfde onderzoek toont aan dat\nonafhankelijke certificering vertrouwen wekt onder consumenten.\nInmiddels is 10 procent van de totale wereldwijde visvangst\nafkomstig van vissers met het MSC-label.	62
Food	visindustrie	prognose	Vooral ouderen en welgestelden eten meer\nvis	De helft van de Nederlandse consumenten eet wekelijks minimaal\néén keer vis, en zo’n 15 procent zelfs twee keer. Onderzoek van het\nCBS leert dat 65-plussers en huishoudens in de hogere\ninkomensklassen het vaakst vis eten. Verklaarbaar, want de\nconsumentenprijs van vis steeg de laatste tien jaar harder dan die\nvan vlees. Toch groeide de afgelopen jaren de afzet van de\nvisindustrie: in vijf jaar tijd nam de verkoopwaarde van vis met 25\nprocent toe.	63
Food	vleesindustrie	prognose	Export naar Azië met 42% gestegen	In 2016 nam de vleesproductie in Nederland met 8 procent toe.\nEen flinke stijging, vooral dankzij meer geslachte runderen. De\nuitvoerwaarde van vlees ging in dezelfde periode met 2 procent\nomhoog. Met name de uitvoer naar Azië steeg (42%),terwijl de export\nbinnen de EU met 1 procent daalde. Zoals voor veel andere\nfoodproducten, zijn Frankrijk, Duitsland en het Verenigd Koninkrijk\nde belangrijkste afzetmarkten. De export naar Duitsland steeg vorig\njaar nog wel (+1%), maar die naar Frankrijk en het Verenigd\nKoninkrijk daalden (-2% om -6%).	64
Food	vleesindustrie	prognose	Varken populairst in Europa, exportkansen liggen\ndaarbuiten	Europeanen eten relatief veel vlees per capita, waarbij vooral\nvarkensvlees geliefd is. Exportkansen liggen met name buiten\nEuropa. In veel Aziatische en Afrikaanse landen wordt nog relatief\nweinig vlees gegeten, terwijl de bevolking én welvaart er snel\ngroeien. Ter vergelijking, het populairste vlees in India is kip:\neen gemiddelde Indiër eet er jaarlijks 1,7 kilo van. In Europa is\ndat 22,7 kilo per hoofd van de bevolking.\n 	65
Food	vleesindustrie	prognose	Vlakke Europese vraag naar schapenvlees	In Europa is schapenvlees het minst populair. Het wordt\nhoofdzakelijk geproduceerd in Frankrijk, Griekenland, Ierland,\nSpanje en het Verenigd Koninkrijk. Hier is dan ook de\nschapenpopulatie het grootst. De vraag naar schapenvlees in de EU\nis relatief vlak, maar netto is Europa wel een importeur.\nSchapenvlees is een gewaardeerd ingrediënt in sommige delen van het\nMidden-Oosten, maar de belangrijkste groeimarkten zijn China en\nRusland.	66
Food	zuivelindustrie	prognose	Azië snelste zuivelgroeier	In 2016 nam de productie van de zuivelindustrie met 3 procent\ntoe; de exportwaarde van zuivelproducten steeg met hetzelfde\npercentage, vooral dankzij uitvoer binnen Europa en naar Azië.\nEuropa is de belangrijkste afzetmarkt voor onze zuivelindustrie,\nmaar Azië groeit harder. Vooral kaas doet het daar goed, omdat het\ner als een luxe wordt gezien. De toenemende welvaart in – met name\n– China versterkt de vraag naar dit soort exclusieve producten. In\ntien jaar verdubbelde de exportwaarde naar Azië. Ongeveer één van\nde vijf Nederlandse zuivelproducten vindt zijn weg naar dit\ncontinent.	67
Food	zuivelindustrie	prognose	Prijsstijging zuivel zet door	Na een forse daling in 2015, vonden de zuivelprijzen in 2016\nweer hun weg omhoog. Voor 2017 verwachten we dat deze prijsstijging\ndoorzet. Voor Nederland geldt dat het fosfaatplafond een\nbelangrijke rol gaat spelen in het verminderen van de productie.\nDaar staat een hogere vraag vanuit China tegenover, vooral naar\nmelkpoeder en boter. Hierdoor zal de prijs medio 2017 en 2018 flink\nstijgen.	68
Food	zuivelindustrie	prognose	Consumentenprijs melk en kaas gedaald	Ook de consumentenprijzen zijn de afgelopen twee jaar flink\ngedaald. In 2015 kelderde de prijs van kaas met 22 procent, gevolgd\ndoor een verdere afname van 3 procent het jaar erop. De prijs van\nverse melk zakte in die periode 4 procent (2015) en daarna nog eens\n1 procent (2016). De boterprijs steeg onverwacht sterk. Veel\nconsumenten vervingen margarine door boters met meer vet, wat de\n(internationale) vraag naar boter stuwde.	69
Industrie	basismetaalindustrie	prognose	Verhoogd prijsrisico	De impact van het niveau en de beweeglijkheid van\ngrondstofprijzen is groot. Niet alleen is de inkoop van industriële\nmetalen van belang, maar de branche houdt relatief gezien ook hoge\nvoorraden aan en daarop loopt zij een prijsrisico (en kans).\nDaarbij komt dat de productie van basismetaalproducten erg\nenergie-intensief is en daardoor de impact van prijsbewegingen in\nenergiegrondstoffen ook groot is. In 2016 en 2017 zullen de meeste\nmetaal- en energieprijzen toenemen. Dit creëert enerzijds\nonzekerheid bij afnemers (fluctuerende afzetprijzen), en anderzijds\nnemen de kosten voor energieverbruik toe.	70
Industrie	basismetaalindustrie	prognose	Omzetgroei onder druk van grondstofprijzen	Ook het verband tussen grondstofprijzen en omzetgroei is hoog.\nEen afname in de grondstofprijzen gaat gepaard met dalende\nafzetprijzen. En bij een gelijkblijvende of afnemende vraag naar\nbasismetaalproducten daalt de omzet vervolgens. De sterke relatie\nmet grondstofprijzen zorgt ervoor dat de groei in omzet een zeer\ngrillig patroon krijgt. Gedurende 2016 laten de meeste\ngrondstofprijzen een herstel zien en wij verwachten dat deze trend\ngedurende 2017 zich doorzet, mede dankzij een stabielere Chinese\neconomie en een sterkere groei van de Amerikaanse economie.	71
Industrie	basismetaalindustrie	prognose	Prijskracht van bedrijven is laag	De prijskracht varieert sterk per type bedrijf. Zo hebben\nstaalbedrijven relatief weinig prijskracht, aangezien deze\nbedrijven doorgaans zowel machtige afnemers (automotive,\nenergiesector) als toeleveranciers (ijzererts) hebben. De\nprijskracht bij basismetaalverwerkende bedrijven is ook laag, met\nname ten opzichte van toeleveranciers. Maar deze bedrijven kunnen\nover meer prijskracht beschikken naarmate zij dichter bij de\nafnemer zitten en meer toegevoegde waarde leveren en/of\nco-producent zijn.	72
Industrie	chemische-industrie	prognose	Groei van de export	De Nederlandse chemie lijkt succesvol in het vinden van\ngroeimarkten buiten Europa. Dat is gunstig, want de\nconcurrentiekracht in de eurozone staat onder druk. Export blijft\neen belangrijke aanjager voor groei, vooral naar gebieden buiten de\neurozone. Maar daar kampt de branche met twee problemen. Buiten de\neurozone (Midden-Oosten) worden chemische producten tegen lagere\n(energie)kosten gemaakt en dit leidt tot een ongelijk speelveld.\nDaarnaast zal de relatief sterke euro dit jaar geen impuls geven\naan extra groei van de afzet in de niet-eurozone.	73
Industrie	chemische-industrie	prognose	Impact van trends in olie- en gasprijs is zeer hoog	De relatie tussen de olieprijs en de afzetprijs in de chemische\nindustrie is zeer sterk, aangezien olie een belangrijke inputfactor\nvormt in het productieproces. Komend jaar kan de branche nog\nprofiteren van de relatief lage olieprijs, maar de prijs zal\ngedurende 2017 verder herstellen. Hierdoor zal de afzetprijs ook\ntoenemen. Ongeveer de helft van het totale energieverbruik in de\nbranche bestaat uit gas. En aangezien ABN AMRO verwacht dat de\ngemiddelde gasprijs in 2017 zal dalen ten opzichte van 2016, zal\ndit gunstig uitwerken op de marges.	74
Industrie	chemische-industrie	prognose	Vooral efficiency en kostenbeheersing op de agenda	De concurrentiepositie van bedrijven in de basischemie is vooral\ngebaseerd op prijs, want onderscheidend vermogen opbouwen met\neindproducten is lastig. De fijnchemische bedrijven hebben hier\nminder last van, aangezien de eindproducten uit dit segment meer\nunieke eigenschappen hebben. Voor de bedrijven in de basischemie\nblijven efficiency en kostenbeheersing dus belangrijke thema’s.\nNaast procesverbetermethodes zullen ook milieuaspecten, duurzaam\nproduceren, uitputting van hulpbronnen, schaarste van grondstoffen\nen ‘biobased’ meer aandacht krijgen.	75
Industrie	elektro-en-technische-apparatenindustrie	prognose	Productie- en omzetgroei zijn erg grillig	De productiegroei laat een positieve trend zien en schommelt al\nmeer dan 14 maanden boven zijn lange termijn gemiddelde groei. Maar\nde productiegroei laat op maandbasis zeer grote uitschieters naar\nboven en beneden zien. Zo is in het eerste kwartaal van 2016 de\nproductie sterk gegroeid (met 15 procent op jaarbasis) en op het\neerste gezicht vormt dat een goede basis voor de rest van het jaar.\nMaar gezien de grilligheid vormt dat zeker geen zekerheid. Want in\nhet tweede en derde kwartaal neemt het groeitempo sterk af. De\nomzet staat nog onder druk, waar een zwakkere binnenlandse vraag\naan ten grondslag ligt.	76
Industrie	elektro-en-technische-apparatenindustrie	prognose	Export vooral naar Duitsland en het Verenigd Koninkrijk	De exportintensiteit (dat is de exportwaarde versus de totale\nomzet) ligt in deze branche op gemiddeld 68 procent. De\ngrootste handelspartners zijn Duitsland en het Verenigd Koninkrijk\nen de verwachting is dat de export naar deze landen verder zal\ngroeien. De geëxporteerde producten betreft vooral (onderdelen van)\ntelecommunicatietoestellen. Dit zijn met name de groeiparels in de\nexport en deze zullen ook komend jaar blinken. De groei van de\nexport van elektrische apparaten (krachtwerktuigen e.d.) zal wat\nstroever verlopen.	77
Industrie	elektro-en-technische-apparatenindustrie	prognose	Kleinschalige branche maar solide basis	Zoals zoveel branches binnen de industriële sector, wordt ook\ndeze branche gekarakteriseerd door kleinschaligheid. Meer dan 85\nprocent van het aantal bedrijven binnen deze branche heeft niet\nmeer dan 20 werknemers in dienst. De gemiddelde faillissementsgraad\nligt in deze branche sinds 2009 op 1,3 procent. De afgelopen twee\njaar lag deze ratio beduidend lager. Ook het gemiddelde\nbedrijfsresultaat (voor belasting en afschrijvingen) staat met 8,3\nprocent ruim boven het sectorgemiddelde van 7,8 procent.	78
Industrie	machine-industrie	prognose	Klein aantal bedrijven, maar van groot belang	Sinds 2015 is het aantal bedrijven in de machinebouw weer aan\nhet toenemen en ligt het aantal in 2016 op bijna 3.000. De groei\nhoudt verband met de toenemende vraag vanuit het buitenland. Het\nbelang van machinebouw in Nederland is groot. Met een totale\ntoegevoegde waarde van bijna 9 miljard euro heeft de\nmachine-industrie een aandeel van circa12 procent in de totale\ntoegevoegde waarde in de sector industrie en een aandeel van\nongeveer 1,5 procent in het totale BBP. De toegevoegde waarde per\nbedrijf ligt zelfs beduidend hoger dan het gemiddelde in de totale\nindustrie.	79
Industrie	machine-industrie	prognose	Trends export en in valuta hebben grote impact	De branche is sterk op het buitenland georiënteerd en de\nexportintensiteit is hoog. De verhouding exportwaarde versus de\ntotale omzet ligt op circa 65 procent. Hierdoor lopen bedrijven met\neen grote nadruk op export naar niet-eurozone een verhoogd\nvalutarisico. In 2017 zal de euro afzwakken en dat is een gunstige\nuitgangspositie. Want hierdoor kan de vraag vanuit niet-eurozone\ngebieden enigszins groeien, aangezien Nederlandse industriële\nproducten dan relatief goedkoop worden. Daarbij komt dat\ngroeivertragingen in opkomende landen (met name China) de branche\nparten zou kunnen spelen.	80
Industrie	machine-industrie	prognose	Herstel bezettingsgraad laat nog even op zich wachten	De bezettingsgraad schommelt rond zijn langetermijngemiddelde en\nhet herstel zet nog niet door. Dit valt deels samen met de relatief\nzwakke buitenlandse vraag, als gevolg van de mondiale economische\nonrust. Ondernemers zijn in dit mondiale economische klimaat nog\nonvoldoende bereid om grote risico’s te nemen en om al te forse\nuitbreidingsinvesteringen te doen. Het goede nieuws is echter dat\neind 2016 de positie van en het sentiment over de binnen- en\nbuitenlandse orderportefeuille positiever is. Mede hierdoor denken\nwij dat de bezettingsgraad in 2017 weer kan herstellen.	81
Industrie	metaalproductenindustrie	prognose	Grondstofprijzen werken door in afzetprijs	De impact van trends in grondstofprijzen is relatief hoog. Het\naardolieverbruik in de metaalproductenindustrie is aanzienlijk\n(aandeel 41 procent van de energiemix). Het aandeel aardgas- en\nelektriciteitsverbruik ligt lager. Sterke fluctuaties in olie- en\ngasprijzen brengen sterke beweeglijkheid in de afzetprijzen met\nzich mee en dat creëert onzekerheid bij klanten. Ook industriële\nmetaalprijzen (aluminium, koper, staal) spelen een rol, alhoewel\nhier het prijsrisico grotendeels bij de opdrachtgever ligt.	82
Industrie	metaalproductenindustrie	prognose	Kleinschalige branche met overcapaciteit	Met 10.630 bedrijven begin 2016 is de metaalproductenindustrie\nde grootste branche in aantal bedrijven binnen de sector industrie.\nDe branche bestaat echter uit een groot aantal kleine bedrijven: 91\nprocent van het totaal aantal bedrijven heeft niet meer dan twintig\nwerknemers in dienst. Het totaal aantal bedrijven is sinds 2007 met\n26 procent gegroeid. Het aantal faillissementen ligt op een\nrelatief hoog niveau. Mede gezien het hoge aantal bedrijven in de\nbranche duidt dit deels op overcapaciteit.	83
Industrie	metaalproductenindustrie	prognose	Voordeel door meer efficiency	De concurrentiedruk is toegenomen, onder meer door de\nkwaliteitsslag van veel buitenlandse producenten, die in veel\ngevallen tegen lagere kosten soortgelijke producten aanbieden. De\nlaatste jaren hebben veel bedrijven geïnvesteerd in automatisering\nvan het productieproces, met als doel om productie- en\ntoeleveringsprocessen verder te optimaliseren. Dit leidt tot\nverhoging van de arbeidsproductiviteit, kortere doorloop- en\nomsteltijden en minder faalkosten.	84
Industrie	meubelindustrie	prognose	Afhankelijk van economische trends	De Nederlandse economie groeit dit jaar en daar profiteert deze\nconjunctuurgevoelige branche van. Het aantal woningtransacties\nblijft dit jaar stabiel, de consumentenbestedingen nemen toe en de\nuitgaven aan woonmeubels blijft op peil. De markt voor\nkantoormeubilair is afhankelijk van de commercieel onroerend goed\nmarkt, die ook een sterk cyclisch karakter heeft. En aangezien het\neconomisch tij voor het bedrijfsleven relatief gunstig is, betekent\ndit dat investeringen in kantoormeubelen en bedrijfsinterieurs\nzullen toenemen.	85
Industrie	meubelindustrie	prognose	Export is een groeimarkt	Terwijl het merendeel van de bedrijven zich met zijn\nbedrijfsactiviteiten richt op de binnenlandse markt, krijgt de\nexport zo langzamerhand steeds meer aandacht. De exportmarkt voor\nin Nederland gefabriceerde meubelen is de laatste paar jaar sterker\ngegroeid. De export naar gebieden buiten de eurozone bleek hierbij\nde groeiparel. Maar België, Duitsland en het Verenigd Koninkrijk\nzijn verreweg nog de grootste afzetgebieden voor Nederlandse\nmeubelen.	86
Industrie	meubelindustrie	prognose	Groot aantal kleine bedrijven met goede resultaten	Deze branche is zeer kleinschalig van aard. Bijna 80 procent van\nhet totaal aantal bedrijven kan worden getypeerd als\neenmansbedrijf. Maar misschien is deze kleinschaligheid juist de\nkracht van de branche, want de financiële resultaten zijn relatief\ngoed. De nettowinstmarge procent\n(periode 2011-2015). Daartegenover staat dat zodra de economische\ntegenwind toeneemt, de faillissementsgraad in deze branche relatief\nsterk stijgt.	87
Industrie	rubber-kunststofproductenindustrie	prognose	Omzetgroei afhankelijk van buitenlandse vraag	De rubberproductenindustrie is voor omzetgroei vooral\nafhankelijk van het buitenland en kent een hoge exportintensiteit\n(van circa 56 procent). De kunststofindustrie bedient daarentegen\nook veel binnenlandse eindgebruikers, zoals de\nverpakkingsmiddelenindustrie. De branche kenmerkt zich, evenals\nzijn belangrijkste afzetmarkten, door een hoge mate van\nconjunctuurgevoeligheid. Grondstoffen vormen een aanzienlijk deel\nvan de kostprijs van de producten en dit brengt onzekerheid met\nzich mee bij sterk beweeglijke grondstofprijzen.	88
Industrie	rubber-kunststofproductenindustrie	prognose	De afzetprijs verliest terrein in 2016	De trend in de olieprijs heeft doorgaans impact op de afzetprijs\nin deze branche. De relatief lage olieprijs zorgt ervoor dat de\ninkoopkosten onder controle blijven. Ook de uitschieters in de\nolieprijs op maandbasis zijn vele malen sterker zijn dan de\nmaandelijkse fluctuaties in de afzetprijs van rubber- &\nkunststofproducten. Door minder volatiliteit in de afzetprijs kan\nde orderintake in stand worden gehouden. En de vraag naar rubber-\nen kunststofproducten hield in 2016 goed stand. Want terwijl de\nafzetprijs licht daalde, nam de omzet tot en met oktober met 2,7%\ntoe.	89
Industrie	rubber-kunststofproductenindustrie	prognose	Export groeit gematigd	In 2016 is de export van rubber- en kunststofwaren licht\ntoegenomen. De branche exporteert vooral naar de EU; circa 85\nprocent van de uitvoerwaarde gaat naar dit werelddeel. Duitsland,\nBelgië en het Verenigd Koninkrijk zijn hier de belangrijkste\nhandelspartners. De belangrijkste afzetgebieden buiten Europa zijn\nAzië en Noord en Zuid-Amerika, met een gezamenlijk aandeel van 10\nprocent in de totale exportwaarde. Over de export naar landen\nbuiten de eurozone lopen bedrijven een valutarisico. Op de\nbinnenlandse markt is de bouw een belangrijke afnemer.	90
Industrie	transportmiddelenindustrie	prognose	Hoge exportintensiteit brengt valutarisico	De branche heeft op verschillende manieren te maken met\nvalutarisico. Enerzijds wordt een deel van de grondstoffen die de\nbranche verwerkt (indirect) verrekend in dollars. Anderzijds is de\nbranche ook sterk exportgericht. In 2016 zal de euro ten opzichte\nvan de dollar afzwakken. Dit maakt de inkoop van grondstoffen in\ndollars duurder en daardoor nemen de grondstofkosten toe. Dit werkt\nnegatief door op de marges van bedrijven. Maar een zwakkere euro\nheeft ook tot gevolg dat de export naar gebieden buiten de eurozone\nweer kan toenemen.	91
Industrie	transportmiddelenindustrie	prognose	Vraag naar duurzame consumptiegoederen nog gunstig	De auto-onderdelenindustrie is met name op de buitenlandse markt\ngericht. Dit segment heeft baat bij een toenemende vraag naar\nonderdelen voor wegvoertuigen die specifiek bestemd zijn voor de\neurozone. De eurozone groeit komend jaar gematigd, waarbij de\nverwachtingen voor de consumptie nog gunstig zijn. Per saldo werkt\ndit positief door op de vraag naar duurzame consumptiegoederen. De\nvertragingen zitten in opkomende markten en daar zullen de mondiaal\nopererende bedrijven (zoals scheepsbouw) last van hebben.	92
Industrie	transportmiddelenindustrie	prognose	Kleinschalige branche en sterk exportgericht	De branche telt begin 2016 in totaal 2.020 bedrijven. Hiervan\nbevindt zich ongeveer de helft in drie provincies: Zuid-Holland\n(355), Noord-Holland (340) en Noord-Brabant (330). De branche is\nsterk gefragmenteerd en kleinschalig: 90 procent van het totaal\naantal bedrijven heeft niet meer dan 20 werknemers in dienst. Veel\nvan deze bedrijven hebben belang bij groei van de autoproductie in\nDuitsland, maar ook het Verenigd Koninkrijk, België en Frankrijk.\nIn deze landen laat de output van auto’s in 2016 gunstige\ngroeicijfers zien. Wij denken dat deze trend zich in 2017\ndoorzet.	93
Leisure	attractieparken-dierentuinen	prognose	Vertrouwen van de consument is hoog	Het consumentenvertrouwen staat begin 2017 rond het hoogste\npunt sinds de zomer van 2007. Bovendien neemt het besteedbaar\ninkomen door de consument verder toe: met 1,9% in 2017 en met 1,7%\nin 2018. In de periode 2015-2016 vertaalde de\ninkomensverbetering zich niet altijd in hogere uitgaven. Wij\nverwachten dat een deel van het gespaarde inkomen alsnog wordt\nbesteed. Ook attractieparken kunnen daarvan profiteren. Daarbij is\nhet wel belangrijk dat bijvoorbeeld het horeca-aanbod aansluit op\nde verwachtingen bij de consument.\n 	94
Leisure	attractieparken-dierentuinen	prognose	Investeringen betalen zich uit	Verschillende vormen van vrijetijdsbesteding concurreren met\nelkaar. Dit is ook te zien onder attractieparken. In de afgelopen\njaren hebben we interessante investeringen gezien. De komst van\ntwee reuzenpanda’s zal een positieve invloed hebben op het bezoek\naan het Ouwehands Dierenpark in Rhenen. Ook is er door\nattractieparken geïnvesteerd in het vernieuwen van attracties en\nslaapplaatsen. Wij denken dan ook dat attractieparken\naantrekkelijker zijn geworden voor de bezoeker.	95
Leisure	attractieparken-dierentuinen	prognose	Profiteren van een stijging van toerisme	Voor attractieparken is het inkomend toerisme eveneens van\nbelang. In de afgelopen vier jaar steeg het buitenlands toerisme in\nons land met 34% (in overnachtingen). Onder meer vanuit Duitsland\nen België was een sterke stijging te zien. Toeristen uit onze\nbuurlanden zijn voor de Nederlandse dagrecreatie potentiële\nklanten, maar dit geldt ook voor toeristen met aan andere afkomst.\nOok voor 2017 verwachten we dat het toerisme (onder meer uit\nDuitsland) in ons land toeneemt.	96
Leisure	campings-vakantieparken	prognose	Consument kiest voor vakantiehuisje	Vakantieparken met huisjes trekken de kar binnen deze branche.\nHet aantal overnachtingen bij hen nam sinds 2012 met 18,4 procent\ntoe, terwijl het aantal overnachtingen bij campings in diezelfde\ntijdsspanne slechts met 0,4 procent toenam. De groei in de\nverblijfsrecreatie moet vooral komen van buitenlandse toeristen.\nDaardoor hebben zij een steeds groter aandeel in het totale bezoek.\nIn 2012 kwam nog 79 procent van de overnachtingen door binnenlandse\ntoeristen, in 2017 was dit 73 procent.	97
Leisure	campings-vakantieparken	prognose	Toename toerisme verwacht	Geholpen door de positieve economische omstandigheden\nvoorzien we een groei van het aantal overnachtingen in de\nverblijfsrecreatie in 2017. Daarbij verschillen de ontwikkelingen\nwel per regio, zoals ook in de afgelopen jaren te zien was. Zo is\nin Zeeland het bezoek aan de vakantiehuisjes in de afgelopen\nvier jaar flink toegenomen, onder meer door een toename van het\nbezoek vanuit Duitsland. Sowieso is bijna vier op de tien\novernachtingen in de Zeeuwse verblijfsrecreatie, van een Duitse\ntoerist.	98
Leisure	foodservice	prognose	Consument heeft vertrouwen	Het consumentenvertrouwen staat in de beginmaanden van 2017 op\nhet hoogste punt sinds 2007, en de koopkracht van de consument\nstijgt. Dit heeft een positief effect op de horeca. Het percentage\nconsumenten dat graag buitenshuis dineert, luncht of ontbijt,\ngroeide in de afgelopen jaren al. De foodservice-groothandels\nprofiteren hier indirect ook van: er ontstaat immers meer vraag\nnaar de voedingsmiddelen die zij leveren.	99
Leisure	foodservice	prognose	Dynamiek in foodservice-branche	Het zwaartepunt van de foodservice-branche zit bij een klein\naantal grote bedrijven, die goed zijn voor het overgrote deel van\nde inkomsten in de branche. Toch zit er nog veel dynamiek in de\nbranche, wat ook zorgt voor uitdagingen. Zo distribueren cateraars\nook zelf food-producten. Bovendien koopt een aantal kleine\nhoreca-initatieven (bijvoorbeeld in de retail) in bij de\nsupermarkt. Een deel van de omzet van foodservicegroothandels\nlekt hierdoor weg naar andere kanalen.	100
Leisure	foodservice	prognose	Beweging naar duurzaamheid en gezondheid	Voor Foodservice-groothandels is het belangrijk op de\nduurzaamheid van hun producten letten. De vraag naar vers en\nbiologisch is toegenomen, terwijl ook de herkomst van de producten\nbelangrijk wordt gevonden. Voedsel van lokale leveranciers wordt\nsteeds belangrijker in de duurzame foodserviceketen. Het is\nbelangrijk voor Foodservice-groothandels om de trends aan het eind\nvan de keten goed te monitoren, en hierop in te spelen.	101
Leisure	hotels	prognose	Stijging toerisme gunstig voor hotels	Het toerisme is een sterke drijver voor hotels. In de laatste\nvier groeide zowel het aantal hotelgasten (in totaal met 23\nprocent) als het aantal hotelovernachtingen (in totaal met 22\nprocent). Vooral in West-Nederland en Oost-Nederland nam het aantal\nhotelovernachtingen snel toe. Hotels profiteren daarbij van de\neconomische groei in grote herkomstlanden, en daarbij van de\nopkomende populariteit van Europese stedentrips. Door de\nsterke vraag naar een hotelovernachting, stegen de prijzen voor een\nhotelovernachting in 2016 met ruim 8 procent: de sterkste stijging\nin minimaal twintig jaar tijd. Voor 2017 verwachten wij weer een\nprijsstijging.	102
Leisure	hotels	prognose	Luxe en comfort of een lage prijs?	Ook hotels maken een verschuiving naar het luxesegment. Het\naantal plannen voor zwembaden, fitnesscentra en/of andere vormen\nvan welness lagen vorig jaar op een recordniveau (Hotelbouwplannen). Wij zien\nkansen voor hotels die deze aspecten goed weten te vermarkten, maar\nook voor budgethotelketens die zich richten op het bieden op een\noptimaal gemak tegen een relatief lage prijs. Wanneer er een dip\nkomt in de economie en/of het toerisme, zal de hotelbranche wel\nforser beconcurreerd worden door de verblijfsrecreatie en Airbnb.\nHet aantal overnachtingen via Airbnb steeg in de laatste jaren\nfors: van 75.000 in 2012 naar 1,4 miljoen in 2016.	103
Leisure	kunst-cultuur	prognose	Museumwereld optimistisch	Voor het huidige jaar verwachten we wederom een toename van het\nmuseumbezoek. Musea zijn daar zelf ook optimistisch over gestemd\n(bron: Conjunctuurwijzer.nl). Er liggen bovendien kansen voor musea\nom de verkopen van eten en drinken en souvenirs op te hogen. Acht\nop de tien museum- en theaterbezoekers is bereid om extra te\nbetalen voor een exclusieve rondleiding of tastbare herinnering,\nzoals een foto. Dit biedt mogelijkheden om de bestedingen per\nbezoeker, thans EUR 2,10 voor musea en EUR 3,60 voor theaters,\naanzienlijk te verhogen.	104
Leisure	kunst-cultuur	prognose	Theaters worstelen met verlies subsidies	Bij de theaters kwamen de overheidsbezuinigingen op\ncultuursubsidies hard aan. Theaters zagen sinds 2012 per saldo het\nbezoek afnemen, in tegenstelling tot concerten, dansvoorstellingen\nen cabaretvoorstellingen. Hoewel meer dan de helft van de\nNederlanders interesse heeft om naar het theater te gaan, bezoekt\nslechts 17 procent daadwerkelijk het theater. Bij theaters besteedt\nde consument meer dan in musea aan bijvoorbeeld koffie en hapjes.\nOok hier zijn nog veel mogelijkheden om met exclusieve\nrondleidingen, fotomomenten en souvenirs de bestedingen door de\nbezoeker te verhogen.	105
Leisure	kunst-cultuur	prognose	Bioscoop blijft krachtig medium	In 2016 ging het bezoek aan bioscopen met 3,7 procent omhoog,\nmede door de groei van het aantal zalen. Ondanks dat het kijkgedrag\nvan de consument deels verschuift naar online, blijft de bioscoop\neen krachtig medium waar de consument graag naartoe gaat voor een\navondje uit. Voor 2017 verwachten we opnieuw een toename aan\nbezoek. Naast de grote, commerciële bioscopen is er ook plek voor\nniche-bioscopen met een bijzonder filmaanbod en een gericht aanbod\nvan horeca.	106
Leisure	restaurants	prognose	Meer te besteden in 2017 en 2018	Het besteedbaar inkomen van consumenten steeg in de periode\n2015-2016. Echter vertaalde de inkomensverbetering zich niet geheel\nin de uitgaven door de consument, mede door de voorzichtigheid bij\nconsumenten over hun eigen financiële situatie. Een deel van het\ngespaarde inkomen wordt in 2017 alsnog uitgegeven. De particuliere\nconsumptie stijgt naar verwachting in 2017 met 2,1 procent, waar\nvorig jaar nog sprake was van een stijging van 1,7 procent.	107
Leisure	restaurants	prognose	Consument eet graag buitenshuis	Voor restaurants is het gunstig dat de behoefte van de consument\nom buitenshuis te dineren in de afgelopen jaren groeide. Van de\nconsumenten gaf in 18% in 2016 aan minimaal een keer per week\nbuitenshuis te dineren. In 2008 was dit nog 13% (FSIN). Ook is de\nmate waarin consumenten buitenshuis lunchen en\nontbijten Daar is voor\nhoreca-ondernemingen nog een flinke groei te realiseren.	108
Leisure	travel	prognose	Groei toerisme, maar ook risico’s	Tussen 2012 en 2015 daalde het aantal door Nederlanders geboekte\nvakanties. De uitgaven hieraan stegen echter wel. In de eerste\nmaanden van 2017 namen de vakantieboekingen toe, gesteund door de\ntoename aan toerisme. Hoewel wij verdere groei van het toerisme\nverwachten, zijn er ook risicofactoren. Zo kan het toerisme uit het\nVK afzwakken bij een mogelijke Brexit. Ook terreurangst\nkan tot vraaguitval leiden. Dergelijke situaties zijn\nuitdagend voor touroperators, die veel tickets en accommodaties\nvooruit boeken. Daarnaast maken prijsstijgingen rondom\nvakantiepieken het voor touroperators moeilijker om de marges op\npeil te houden.	109
Leisure	travel	prognose	Online strategie doorslaggevend voor succes	Inmiddels vindt 83 procent van alle uitgaven aan vliegtickets en\nlogies-accomodaties in ons land, online plaats. Een goede\nvindbaarheid en profilering online is voor Travel-bedrijven dan ook\ncruciaal: zowel voorafgaand aan het boeken, als tijdens de reis van\nde klant zelf. Aan de andere kant zijn bekende Nederlandse\nonline travel agency’s (ota’s) als Booking.com en Travelbird.com\n(internationaal) succesvol. Daarbij concurreert de reisbranche ook\nmet Airbnb, die reeds ‘tours en ervaringen’ op de locatie zelf\nbiedt, aangeboden door lokale experts. Bij de reiziger leeft de\nbehoefte hieraan.	110
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	prognose	Innovatie, kostenverlaging en uitstekende relaties zijn\nkey	Door het verminderen van investeringen in de sector, maar ook\nhet kritisch kijken naar de kosten door producenten, staan de omzet\nen marges van contractors, toeleveranciers en dienstverleners onder\ndruk. Concurrentie tussen de spelers is enorm omdat de hoeveel werk\nsterk is teruggelopen. Wel hebben bedrijven vaak een zeer lange en\ngoede relatie met opdrachtgevers waardoor ze zich beter kunnen\naanpassen aan deze nieuwe omstandigheden. Prijzen zullen in de\nkomende jaren onder druk blijven, wat de branche dwingt om de\nkostenstructuur structureel te verlagen.	111
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	prognose	Nieuwe markten en nieuwe regios	De bouw van nieuwe windparken op zee in Nederland en omringende\nlanden zullen kansen blijven bieden voor toeleveranciers en\nservicebedrijven in de offshore-branche gedurende de komende jaren.\nDit zal in de komende jaren uitgebreid kunnen worden naar andere\nregios waar offshore windparken worden geplaatst. Ook zal er op\ntermijn meer werk komen voor de ontmanteling van\nproductieplatformen waar de resterende olie en gas in het veld niet\nlanger economisch of technisch geproduceerd kan worden.\nInternationaal buiten Europa zal er een sterkere focus komen op\nonshore productie van olie en gasvelden.	112
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	prognose	De opkomst van hernieuwbaar	In 2015 heeft de NAM 28,1 miljard kuub aardgas uit het\nGroningen-veld gewonnen. In 2016 is dit maximaal 27 miljard kuub,\ntenzij er meer gas nodig is als gevolg van extreem weer. Naar\nverwachting zal de gasproductie in Nederland de komende jaren\nverder worden afgebouwd. Dit zal negatief zijn voor Nederlandse\nbedrijven en toeleveranciers, maar ook voor de aardgasbaten en de\neconomische groei, vooral in de regio. Het effect zal slechts voor\neen klein deel worden gecompenseerd door toegenomen kansen voor\nbedrijven die betrokken zijn bij extra invoer van gas of LNG.	113
Retail	autoretail	prognose	Daling van nieuwverkopen, occassionverkoop gestegen	De verkoop van nieuwe personenauto’s daalde in 2016 naar\nbijna 383.000. Hoewel wij verwachten dat de nieuwverkopen stijgen\nin 2017, lijkt de consument minder waarde te hechten aan het\nbezitten van een nieuwe auto. Daarentegen steeg de occasionverkoop\nvorig jaar met 4,5%. Vooral de tweedehands-modellen van Volkswagen\nwerden volop verkocht, en ook die van Peugeot waren gewild. Mede\ndankzij de betere economische omstandigheden (de uitgaven aan\nvoertuigen zijn gestegen) verwachten wij voor 2017 wel een stijging\nvan de nieuwverkopen en een stabilisering van de occasions.	114
Retail	autoretail	prognose	Stabilisatie inkomsten uit onderhoud en reparatie	De omzet uit onderhoud en reparatie is cruciaal.\nMerkdealers, universele autobedrijven en fastfitters strijden om\nmarktaandeel in een markt die al jaren krimpt. De oorzaken achter\nde trendmatige daling zoals auto’s die betrouwbaarder zijn, grotere\nonderhoudsintervallen hebben en minder kilometers maken, blijven.\nEchter de groei van het wagenpark, de sterke vraag naar occasions,\neen toename van het aantal APK’s en de economische groei die minder\nreden geeft onderhoud uit te stellen, zullen tijdelijk zorgen voor\neen stabilisatie.	115
Retail	autoretail	prognose	Private lease als sleutel naar omzetgroei?	Er bestaat wel een risico dat die inkomsten uit onderhoud\nafnemen, vanwege de opkomst van private lease. Private\nlease-contracten hebben immers veelal een kortere looptijd dan die\nvoor zakelijke lease, wat kan resulteren in minder onderhoud. Het\naantal contracten is groeiende. Dat bedrijven in toenemende\nmate gebruikmaken van mobiliteitsbudgetten, geeft deze ontwikkeling\neen impuls.	116
Retail	bouwmarkten	prognose	Huizenmarkt stuwt verkoopvolumes	De toename van het aantal transacties op de woningmarkt is\ngunstig voor de bouwmarkten. In 2016 nam het aantal\nhuizentransacties met 20,5% toe, mede door de lage hypotheekrente.\nHoe meer huizen er verkocht worden, hoe meer er normaliter wordt\nverbouwd: er bestaat dan ook een significante\ncorrelatie tussen het aantal verkochte huizen en de\nverkoopvolumes van bouwmarkten. Voor 2017 verwachten we een groei\nvan 5% van transacties in de woningmarkt: dit moet leiden tot groei\nvoor bouwmarkten, maar wel in een lager tempo dan in 2016.\n 	117
Retail	bouwmarkten	prognose	Concurrentie groot	De concurrentie in deze branche is echter groot. De gemiddelde\nmarge op het bedrijfsresultaat daalde vorig jaar dan ook naar 1,7%.\nDe aanwezigheid van grote internationale spelers en\nhun plannen tot uitbreiding verscherpen die concurrentie. Door\nhun schaalgrootte zij groot inkopen en lage\nprijzen bieden in de winkel. Het is aan de inkoopkant gunstig dat\nde eerder verwachte opmars van de dollar (waardoor inkoop duurder\nkan worden) waarschijnlijk \ntoch niet plaatsvindt.	118
Retail	bouwmarkten	prognose	Andere uitdagingen	Er bestaan meer uitdagingen voor de bouwmarkten. Zo moet de\nconsument steeds meer eigen geld inbrengen bij het kopen van een\nhuis. Dit kan een reden zijn om een huis te kopen waar weinig aan\nverbouwd hoeft te worden. Daarnaast lijken jongere generaties\nminder affiniteit met klussen te hebben dan voorheen. Voor\nbouwmarkten is het de uitdaging aantrekkingskracht te behouden;\nbijvoorbeeld door een focus service, op zzp’ers of door zich te\nrichten op complete\nwoninginrichting.	119
Retail	drogisterijen	prognose	Aanhoudende vraag naar verzorgingsproducten	Er is een aanhoudende vraag naar verzorgingsproducten in de\nmarkt, wat de verkoopvolumes van drogisterijen stuwt. Vorig jaar\nstegen de verkoopvolumes van drogisterijen met 2%. De branche heeft\ngoed staande gehouden tijdens de crisis: de verkoopvolumes liggen\nzelfs al ruim 5% boven précrisisniveaus. De vergrijzing biedt ook\nhoop voor deze branche. In 2040 zijn er anderhalf keer zoveel\n65-plussers als nu. Drogisterijen kunnen profiteren, mits ze\nhier goed op inspelen met hun aanbod en service.	120
Retail	drogisterijen	prognose	Grote concurrentie, druk op de marges	De concurrentie in de drogisterijenbranche is groot, ook door de\ngroei van de verkoop via internet en het gegeven dat branchevreemde\nspelers (als supermarkten) ook verzorgingsproducten verkopen. Begin\n2010 waren er nog 2872 vestigingen van drogisterijen, begin\n2017 zijn dat er nog 2722. De winstmarges van drogisterijen zijn in\nhet afgelopen jaar iets gedaald. Deze zijn echter nog altijd\nbovengemiddeld in de Retail-sector: de gemiddelde marge op het\nbedrijfsresultaat van een drogisterij is 6,2%.	121
Retail	drogisterijen	prognose	Samenwerking in de sector	Door de grote concurrentie is samenwerking een aantrekkelijke\noptie voor drogisterijen. Samenwerking via franchise-constructies\nkomt dan ook veel voor. Dit is \nkansrijk en uitdagend tegelijk. Kansrijk omdat de\nfranchisenemer de vrijheid heeft om te ondernemen en dus een local\nhero te worden, terwijl hij/zij online kan meeliften op verkopen\nvan de franchisegever. Uitdagend omdat het dan wel essentieel is\ndat er passende afspraken zijn gemaakt over de verdeling van de\ninternetverkopen.	122
Retail	groothandel-non-food	prognose	Particuliere consumptie stijgt	Groothandels non-food profiteren van de stijging van de\nparticuliere consumptie in ons land. Winkeliers verkopen daardoor\nnamelijk meer non-food-producten, en zij kopen in bij deze\ngroothandels. In 2016 steeg de particuliere consumptie met 1,7% en\nvoor 2017 verwachten we zelfs een stijging van 2,1%. Dit heeft een\npositief effect op de omzetontwikkeling van de groothandels in\nnon-food-producten. Sinds 2007 steeg de omzet van deze branche met\nbijna een derde, waarbij de groei onder meer bij de groothandels in\nmedische artikelen lijkt te zitten.\n 	123
Retail	groothandel-non-food	prognose	Handel neemt toe	De economische ontwikkelingen buiten Nederland zijn voor de\ngroothandels ook van zeer groot belang. Voor hen is het gunstig dat\nin veel afzetmarkten sprake is van economische groei. Voor 2017 en\n2018 verwachten wij dan ook een toename van de export vanuit\nNederland van ruim 4% per jaar, en van de import met 4,5% per jaar.\nDe handel in bijvoorbeeld kleding, schoenen en optische\ninstrumenten nam in 2016 In dat jaar steeg de omzet\nvan groothandels non-food met 6,6%.	124
Retail	groothandel-non-food	prognose	Hogere winstmarges	Geholpen door zijn diversiteit aan afzetmarkten hebben\ngroothandels non-food hun winstgevendheid in de afgelopen jaren\nflink op weten te schroeven. De marges op het\nbedrijfsresultaat van groothandels in non-food stegen tussen 2009\nen 2015 van 4,5% naar 7,1%. Groothandels in mode en in\nwoninginrichting zaten daarbij in 2015 zelfs boven de 8%.	125
Retail	kledingwinkels	prognose	Consument heeft vertrouwen	Voor de kledingbranche is het vertrouwen van consumenten een\nbelangrijke indicator. Dit consumentenvertrouwen staat begin 2017\nrond het hoogste niveau sinds de zomer van 2007. Consumenten zien\nde huidige periode ook als gunstig om grote aankopen te doen. Vorig\njaar nam de particuliere consumptie dan ook met 1,7% toe. Voor 2017\nverwachten we een toename van de consumptie van 2,1%, en voor 2018\nvan 1,6%.\n 	126
Retail	kledingwinkels	prognose	Dollar belangrijke indicator	De koers van de dollar is belangrijk voor kledingzaken, omdat de\ninkoop vaak in dollars of gerelateerde valuta wordt afgerekend.\nSterke bewegingen in de dollar doorlopen de keten en komen na 9 tot\n12 maanden bij de winkelier in kleding terecht. Het was dan ook een\nuitdaging dat de dollar vanaf april 2014 tot eind 2015 met ongeveer\n23% steeg in waarde, ten opzichte van de euro. Het lukte de sector\nom dit in 2016 deels door te berekenen. Voor nu is het positief dat\nde eerder verwachte verdere stijging van de dollar waarschijnlijk\ntoch niet plaatsvindt.	127
Retail	kledingwinkels	prognose	Druk op winstgevendheid, aantal webwinkels neemt toe	Hoewel de prijzen door kledingwinkels vorig jaar iets stegen,\nwordt dit wel beperkt door de grote concurrentie. Sinds 2007 stegen\nde prijzen van kleding met nog geen 1%, terwijl de totale inflatie\nin die tijdsspanne 15% was en de invoerprijzen ook flink zijn\ntoegenomen. Er is dan ook sprake van margedruk. Vorig jaar daalde\nhet gemiddelde bedrijfsresultaat van kledingwinkels naar -0,8%. Ook\nneemt de concurrentie vanuit internetspelers toe. Er zijn nu liefst\n8720 webwinkels in kleding; dit zijn er drieduizend meer dan begin\n2014.	128
Retail	supermarkten	prognose	Stijging van eenpersoonshuishoudens	De samenleving individualiseert. In 2006 was nog 35 procent van\nde particuliere huishoudens een eenpersoonsgezin, in 2016 ging dit\nal richting de 38%. Leden van samengestelde huishoudens gedragen\nzich bovendien vaak als eenpersoonshuishouden, bijvoorbeeld\nvanwege werk. Hierdoor wordt het efficiënt omgaan met tijd\nbelangrijk en doet de consument op een andere manier zijn\nboodschappen. Deze verdeelt de consument bijvoorbeeld in\nkorte-termijn-bezoekjes doordeweeks en deels via internet. Het is\nbelangrijk voor supers om hierop in te spelen.	129
Retail	supermarkten	prognose	Winkeldichtheid is hoog	Binnen een afstand over de weg kilometer kan\nde consument uit gemiddeld 22 supermarkten kiezen. De opkomst van\nnieuwe (online) toetreders en de concurrentie vanuit de\nnon-food-sector verscherpt die concurrentie alleen maar. Wij\nverwachten dat het aantal vestigingen in het middensegment afneemt\nin de komende jaren. We verwachten wel een toename van kleinere\n(stads)supermarkten: gericht op de kortetermijnboodschap (met\nbijvoorbeeld kant-en-klare producten). Grotere supermarkten zullen\nmeer inspelen op beleving.	130
Retail	supermarkten	prognose	Consument geeft meer uit	Tijdens de crisis bezuinigde de consument vooral op aankopen van\nnon-foodproducten. Het aandeel van voedingsmiddelen in de totale\nuitgaven steeg vanaf 2007 van 8,5 procent naar 9,4 procent. Voeding\nbehoort immers tot de eerste levensbehoeften. Toch zijn ook\nsupermarkten gebaat bij groei van de economie en toenemende\nconsumentenuitgaven. Wij verwachten voor 2017 een toename van de\nparticuliere consumptie met 2,1% en voor 2018 met 1,6%.	131
Retail	winkels-in-consumentenelektronica	prognose	Vraag vanuit de consument naar de producten	De vraag naar consumentenelektronica (denk aan smartphones) is\naanhoudend. Door ontwikkelingen in de halfgeleiderindustrie worden\nde producten ook steeds slimmer en nemen de mogelijkheden toe.\nSmartphones en tablets worden ook steeds vaker gebruikt om\nbijvoorbeeld media te consumeren, of om producten te kopen. Het\nvooruitzicht dat diverse elektronicaproducten (als koelkasten)\n‘smart’ worden, kan gunstig uitwerken op de toekomstige vraag naar\ndie producten.	132
Retail	winkels-in-consumentenelektronica	prognose	Grote prijsdruk	Mede door de opkomst van de online-markt is er een zeer grote\nprijsdruk op consumentenelektronica ontstaan. Sinds 2005 zijn de\nprijzen van consumentenelektronica met bijna 46% procent gedaald,\nterwijl het algehele prijspeil in Nederland in die periode met 18%\nsteeg. De marges op het bedrijfsresultaat zijn dun, en daalde in\nhet afgelopen jaar verder: naar 0,5%. Naar verwachting wordt het\nook in 2017 lastig om de prijzen te verhogen.\n 	133
Retail	winkels-in-consumentenelektronica	prognose	Particuliere consumptie stijgt	Het consumentenvertrouwen staat rond het hoogste niveau sinds de\nzomer van 2007. Dit resulteert ook in hogere uitgaven: vorig jaar\nsteeg de particuliere consumptie met 1,7%, voor 2017 gaan we uit\nvan een groei van 2,1% en voor 2018 verwachten we een plus van\n1,6%. De bestedingen aan ‘duurzame goederen’ (waar\nconsumentelektronica ook toe behoort) zitten dan ook in de lift,\nwat hoopgevend is voor winkels in consumentenelektronica.	134
Retail	woonwinkels	prognose	Woningmarkt aanjager voor groei	Het aantal transacties op de woningmarkt nam vorig jaar met\nliefst 20% toe, mede door de lage hypotheekrente. Dit is een zeer\nbelangrijke indicator voor de woonwinkels. Bij een toename van de\nverkopen van woningen ontstaat er bijvoorbeeld meer vraag naar\nvloeren, meubilair en andere woonartikelen. Bijvoorbeeld\nkeukenwinkels wisten vorig jaar een flinke groei realiseren. Voor\n2017 verwachten we wel \nvertraging van de groei op de woningmarkt.	135
Retail	woonwinkels	prognose	Bedrijfsresultaat verschilt per branche	De concurrentie in de branche is flink. En niet in de laatste\nplaats omdat bijvoorbeeld ook bouwmarkten zich profileren op het\ndecoratieve vlak. Maar woonwinkels ondervinden bijvoorbeeld ook\nhinder van merkkledingwinkels, die soms ook woonartikelen verkopen.\nToch wisten gemengde woonwinkels in 2016 de winstmarges te\nverhogen, evenals keuken- en badkamerzaken en meubelzaken. Kurk- en\nparketzaken zagen de marges wel dalen.	136
Retail	woonwinkels	prognose	Consumentenvertrouwen hoog, consument geeft meer uit aan\ninrichting huis	Begin 2017 stond het consumentenvertrouwen rond het hoogste\nniveau sinds de zomer van 2007. Consumenten zijn zeer positief over\nde economische situatie, en voorzichtiger over hun eigen financiële\nsituatie. Ze zien de huidige periode wel als gunstig om grote\naankopen te doen. De particuliere consumptie neemt dan ook toe:\ndeze steeg in 2016 met 1,7% en stijgt in 2017 en 2018 naar\nverwachting verder. De uitgaven aan woninginrichting\nnamen vorig jaar met 4% toe.	137
Technologie-Media-Telecom	drukkerijen	prognose	Digitale transformatie	Consumenten en bedrijven nuttigen traditionele printproducten\nvaker digitaal. Dat heeft zijn weerslag op de drukkerijsector.\nSinds 2009 zijn er 875 bedrijven verdwenen. Nu zijn er nog 3585\nover, waarvan 2095 eenmanszaken (voornamelijk ZZP’ers). De 3585\novergebleven drukkerijen bevinden zich in zware\nmarktomstandigheden. Er is sprake van een overcapaciteit aan\ndrukpersen. Die overcapaciteit is op zich al moeilijk uit de markt\nte halen, maar tegelijkertijd zet de digitalisering van de\nsamenleving gewoon door. De sector wist de afgelopen jaren knap\nomzetgroei in het buitenland te behalen, maar de export beslaat\nslechts 10% van de totale omzet van de branche en per saldo daalde\nde omzet dus fors.	138
Technologie-Media-Telecom	drukkerijen	prognose	Grote overcapaciteit zorgt voor prijsdruk	Er is overcapaciteit in de branche. Om de productie nog\nenigszins op peil te houden moesten drukkerijen erg lage prijzen\nbieden. Vooral massa-drukwerk moest het ontgelden. Door druk op het\nbedrijfsresultaat en de structuur van het bedrijf (bezit\ndrukpersen) is het een uitdaging om nieuwe verdienmodellen te\nontsluiten. De situatie leidde tot vele kostenbesparingen. Het\naantal banen in de branche is fors achteruit gegaan. Werkten er in\n2010 nog 33.000; in 2015 waren daar slechts 23.000 van over.	139
Technologie-Media-Telecom	drukkerijen	prognose	Ondernemersvertrouwen gestegen	Hoewel de situatie verre van rooskleurig en wij nog geen herstel\nvoorzien, zijn er ook lichtpuntjes in deze branche. De economische\nsituatie verbeterd: de bedrijfsinvesteringen en consumentenuitgaven\nnemen toe. Naar verwachting zetten die ontwikkelingen in 2017 door.\nHet ondernemersvertrouwen in deze branche is vorig jaar flink\nverbeterd. De laatste jaren was er een dalende trend in het aantal\nfaillissementen in de grafische industrie. En de digitalisering zal\nook in de komende jaren doorzetten.	140
Technologie-Media-Telecom	ict-hardware	prognose	Economie en digitalisering	De continuering van herstel in de economie is gunstig voor\nbedrijven uit deze branche. Wij voorzien 2,4 procent economische\ngroei in 2017. De uitgaven van bedrijven en consumenten en de\nzullen naar verwachting toenemen, evenals de export. Dat heeft\nmogelijk een positieve invloed op de vraag naar ICT Hardware.\nBovendien bevindt het bedrijfsleven zich in een fase van digitale\ntransformatie. Daarbij is het belangrijk is dat ICT-apparatuur\naanwezig is die deze ontwikkeling ondersteunt en aankan.	141
Technologie-Media-Telecom	ict-hardware	prognose	Investeringen in ICT-apparatuur	Bedrijven zijn al jaren volop bereid om te investeren in\nICT-apparatuur. Er is wel een verschuiving te zien. De\ninvesteringen in telecommunicatie-apparatuur stijgen sterker dan de\ninvesteringen in computers. Er lijkt een verschuiving gaande in de\nvraag van computers en printers naar mobiele apparatuur.	142
Technologie-Media-Telecom	ict-hardware	prognose	Prijsdruk en online concurrentie	Er sprake van prijsdruk op ICT-apparatuur. Dat geldt zeker voor\nelektronica, wat aan het eind van de keten goed te zien is. Winkels\nin consumentenelektronica moesten hun prijzen in tien jaar tijd\nbijna halveren. Prijsdruk is ook voor de ICT-groothandels een\nblijvende uitdaging, ook omdat hun producten gevoelig zijn voor\nonline concurrentie. De omzet van de groothandels in ICT steeg in\n2015 nog met 7,1%, maar daalde in 2016 met 1,9%.	143
Technologie-Media-Telecom	it-software-services	prognose	Bedrijven bereid tot investeringen	De groei van de economie is een gunstige factor voor\nIT-bedrijven. Klanten zijn daardoor immers meer bereid om te\ninvesteren in IT. De bedrijfsinvesteringen in software namen vorig\njaar met 2,9 procent toe tot 18,6 miljard Euro, terwijl hun\nuitgaven aan telecommunicatie-apparatuur zelfs met 7,3 procent\nstegen tot 1,2 miljard Euro. Bedrijven investeren ook strategisch;\nhet aantal fusies en overnames binnen de branche is flink\ntoegenomen. Vorig jaar waren er maar liefst 500 fusies of\novernames; een jaar eerder nog 395.	144
Technologie-Media-Telecom	it-software-services	prognose	Tekort aan hoogopgeleid IT-personeel	Het aantal IT-bedrijven dat een belemmering ervaart aan een\ntekort aan geschikt personeel is in het afgelopen jaren flink\ntoegenomen. In 2013 zag 6,4% procent van de IT-ondernemers dit nog\nals belemmering, inmiddels is dit 28,3 procent. Hoewel het\nbewustzijn van de problematiek toeneemt en de studie Informatica\nlangzaamaan aan populariteit wint, is het tekort aan hoogopgeleid\nIT-personeel groot. Er is vooral een tekort aan\nsoftware-ontwikkelaars, specialisten in computertalen en\ndata-analisten. Het tekort aan personeel begint nu, samen met\nandere productiebelemmeringen, een wissel te trekken op de\nomzetgroei van de branche.	145
Technologie-Media-Telecom	it-software-services	prognose	Digitale transformatie stuwt branche omhoog	In diverse sectoren van het bedrijfsleven is sprake van digitale\ntransformatie, waarbij IT een steeds belangrijker onderdeel binnen\nde bedrijfsprocessen wordt. Denk bijvoorbeeld aan de zorg en de\nindustrie. Software, data-analyse, algoritmen en sensoren spelen\neen steeds belangrijkere rol. IT-bedrijven profiteren van deze\nontwikkeling. Software, cloud en virtualisatie zijn voorbeelden van\ngroeimarkten binnen de IT-branche.	146
Technologie-Media-Telecom	reclamebureaus	prognose	Economisch klimaat verbetert	Het verbeterende economische klimaat biedt hoop voor deze\nconjunctuurgevoelige branche. De particuliere consumptie neemt naar\nverwachting met 2,1 procent toe in 2016. De bedrijfsinvesteringen\nnamen vorig jaar met 4,8 procent toe (gecorrigeerd voor\nprijseffecten), maar deze groei zwakt af tot 3 procent in 2017. De\neconomische groei heeft normaal gesproken een gunstig effect op de\nadvertentiebestedingen. Daar zit voor reclamebureaus dus\nbedrijvigheid in.	147
Technologie-Media-Telecom	reclamebureaus	prognose	Advertentiebestedingen nemen in print af, in online toe	De advertentiebestedingen laten een dubbel beeld zien. De\nadvertentie-inkomsten voor printuitingen (kranten, tijdschriften)\ndalen al jaren op rij. De groei zit in de advertentiebestedingen\nvoor internetuitingen. Die groeiden tussen 2010 en 2016 met 53% tot\nmeer dan 1,6 miljard Euro. Het aantal bedrijven neemt de laatste\njaren licht af. Er zijn nu ruim 28.000 bedrijven actief in de\nbranche.	148
Technologie-Media-Telecom	reclamebureaus	prognose	Tekort aan IT-personeel kan belemmering zijn	Door de forse groei van de online advertentiebestedingen is de\nreclamewereld zich meer online gaan oriënteren en meer opgeschoven\nrichting de IT-branche. Kennis over bijvoorbeeld computertalen\nwordt daarom ook in deze branche steeds belangrijker. Dat is een\nuitdaging, omdat er in ons land een tekort bestaat aan hoogopgeleid\nIT-personeel. Dat kan voor een reclamebureau dat zich grotendeels\nonline oriënteert (bijvoorbeeld in het verhandelen van\nadvertentieruimte) een belemmering vormen.	149
Technologie-Media-Telecom	telecom	prognose	Traditionele diensten lopen terug, dataverkeer neemt toe	De inkomsten uit traditionele diensten zijn gekrompen. Zo\nhalveerden de inkomsten uit vaste telefonie tussen 2010 en 2015.\nDoor de opkomst van ‘over the top’-partijen als Whatsapp, gebruikt\nde consument telecommunicatie anders. Het dataverkeer neemt rap\ntoe. Aanbieders veranderen daarom de structuur van abonnementen. Op\ndataverkeer zit echter een beperkte ‘pricing power’ en het blijft\nlastig om omzetgroei te realiseren. De ontwikkelingen op de\nzakelijke markt volgen daarbij vertraagd de consumentenmarkt.	150
Technologie-Media-Telecom	telecom	prognose	Fusies in telecomsector	Consolidatie is een steeds aantrekkelijkere business case\ngeworden. Ten eerste lijkt de klant kritischer geworden over zijn\ntelecomabonnement, nu connectiviteit tot eerste levensbehoefte\nverworden is. Ten tweede zijn investeringen in netwerkkwaliteit\nen/of dienstverlening cruciaal. Netwerkintegratie over landsgrenzen\nheen is nog lastig; binnenlandse consolidatie is aantrekkelijker.\nVanaf begin 2007 waren er 150 fusies in de branche en nam het\naantal bedrijven af van 1450 naar 1180.	151
Technologie-Media-Telecom	telecom	prognose	Nieuwe ronde investeringen op komst	De telecombranche staat bekend als kapitaalintensief, waarbij\ninvesteringen in netwerken cruciaal zijn. Daarbij is een nieuwe\ngeneratie mobiele netwerken in aantocht, genaamd 5G. Deze lijkt\nvanaf ongeveer 2020 operationeel te worden. Hierdoor ontstaat vanaf\n2018 een hoger investeringsklimaat voor betreffende partijen.\nVerondersteld wordt dat 5G een cruciale rol gaat spelen bij\n‘internet of things’ waarbij apparaten steeds vaker via het\ninternet met elkaar verbonden zijn.	152
Technologie-Media-Telecom	televisie-omroepen	prognose	Economische omstandigheden verbeteren	De particuliere consumptie neemt naar verwachting toe in 2017.\nDat is gunstig voor de ontwikkeling van reclame-inkomsten. Tijdens\nde crisis bleven de reclame-inkomsten via tv op peil: met EUR 984\nmiljoen stonden die in 2016 rond precrisisniveaus. Sinds 2013 zijn\ndeze weer licht aan het stijgen. Dit is te danken aan de groei in\ninkomsten uit spotreclame (in reguliere reclameblokken), die de\ndaling van non-sport bestedingen (reclame buiten de blokken)\ncompenseerde.	153
Technologie-Media-Telecom	televisie-omroepen	prognose	Sportevenementen helpen omroep	Producenten van tv-content boekten in 2016 een omzetgroei van\n4,1%. Een jaar eerder was dit nog 7,7%. De omzet van de omroepen\nnam licht toe met 1,3% in 2016. Daarbij speelt mee dat in 2016\nzowel de Olympische Spelen als het EK voetbal plaatsvonden. In 2015\nontbrak er een dergelijk groot evenement. Te verwachten valt dat in\n2017 de reclamebestedingen voor tv juist weer wat terug zullen\nlopen bij gebrek aan een groot sportevenement.	154
Technologie-Media-Telecom	televisie-omroepen	prognose	Kijkgedrag verandert in loop der jaren	Het kijkgedrag van de consument verandert. De Nederlander\nkeek in 2016 gemiddeld 183 minuten per dag televisie, een daling\nvan 3,7 procent ten opzichte van 2015 (Bron: SKO). In dit cijfer\nontbreekt het aandeel tv via internet en on-demand. De laatste\njaren is het kijken van tv-producties via smartphones en tablets\neveneens gestegen. Voor televisie-omroepen is het dus zeer\nbelangrijk om online en mobiel een goede vertegenwoordiging te\nhebben.	155
Technologie-Media-Telecom	uitgeverijen	prognose	Mediaconsumptie verschuift naar digitaal	De mediaconsumptie is in de afgelopen jaren verschoven, van\nprint naar digitaal. Dat raakt uitgevers van diverse soorten media,\nzoals kranten en tijdschriften. De betaalde gerichte oplages van\nkranten liepen afgelopen jaar terug met 120.000 naar 2.370.000. De\ndigitale abonnementen stegen in de afgelopen jaren sterk en\nafgelopen jaar is het miljoen bereikt. Uitgevers ontwikkelen\nmodellen om aan dat groeiende digitale bereik geld te verdienen,\nzowel via nieuwe advertentievormen als via betaalde online content.\nDie verandering kost tijd.	156
Technologie-Media-Telecom	uitgeverijen	prognose	Aantrekken economie gunstig voor advertentie-inkomsten	Het aantrekken van de economie is positief voor de uitgeverijen.\nDe particuliere consumptie stijgt naar verwachting in 2017 met 2,1\nprocent, en bedrijven blijven investeren. Dat kan positief\nuitwerken op de advertentie-bestedingen. In de afgelopen jaren\nstonden deze onder druk. De opbrengsten van advertenties uit\ndagbladen daalde tussen 2011 en 2016 van 518 miljoen naar 342\nmiljoen(*) ; de advertentiesopbrengsten in dagbladen daalde in\ndezelfde periode van 213 miljoen naar 134 miljoen Euro. De\nonline-advertentiemarkt is tussen 2010 en 2016 met 53% gegroeid tot\nruim 1,6 miljard Euro.	157
Technologie-Media-Telecom	uitgeverijen	prognose	Schaalgrootte	In het licht van het uitdagende klimaat van de afgelopen jaren\n(de crisis en digitalisering) heeft er een consolidatieslag\nplaatsgevonden in meerdere segmenten. Vanaf 2007 vonden er maar\nliefst 265 fusies plaats van uitgevers van boeken, tijdschriften of\nkranten. Er worden tegelijkertijd ook veel nieuwe uitgeverijen\nopgericht, waardoor het aantal in de markt actieve uitgevers is\ntoegenomen. In totaal zijn er 3575 uitgevers actief, waarvan bijna\ndriekwart eenmanszaken.	158
Transport-en-Logistiek	binnenvaart	prognose	Tankvaart – Binnenvaart compenseert tegenvallende overslag	Haven Rotterdam\nDe tankvaartvolumes zijn in 2016 toegenomen, met 4,8 procent.\nVooral het binnenlands vervoer en de aanvoer van natte bulk nam in\n2016 toe. In de haven van Rotterdam werd er 0,5 procent minder\nnatte bulk overgeslagen. Er werd vooral minder aardolie\novergeslagen. De binnenvaart wist dit te compenseren door meer\nnatte bulk vanuit het buitenland naar Nederland te vervoeren en via\nNederland door te voeren naar andere landen.	159
Transport-en-Logistiek	binnenvaart	prognose	Droge bulkvaart – Herstel verwacht	Voor het deelsegment droge lading is het vervoer van steenkolen,\nertsen en cokes van groot belang. Het vertegenwoordigt, gemeten\nnaar gewicht, samen circa 65 procent van het vervoer. 2016 was een\nslecht jaar voor wat betreft het vervoerde volume doordat er minder\nsteenkolen werden gebruikt bij de productie van elektriciteit. Voor\n2017 is weer wat herstel te verwachten door toename van het vervoer\nvan zand en grind voor de bouwsector. Op de lange termijn zal het\nvervoer van steenkolen afnemen doordat steeds meer\nsteenkolencentrales gesloten worden. Op de korte termijn is hier\nnog geen sprake van.	160
Transport-en-Logistiek	binnenvaart	prognose	Concurrentie – Van andere modaliteiten	De binnenvaart komt steeds meer in beeld als alternatief voor\nhet wegvervoer nu de congestie op de weg steeds verder toeneemt,\nmaar de fijnmazigheid van het wegvervoer blijft een\nconcurrentievoordeel voor deze modaliteit. Concurrentie voor de\nbinnenvaart komt van de verbetering van de Betuweroute over het\nspoor. Totdat de werkzaamheden zijn afgerond, moeten\ngoederentreinen worden omgeleid. Dit kan juist voordelig zijn voor\nde binnenvaart, want de binnenvaart kan hierdoor in beeld komen als\nalternatief.	161
Transport-en-Logistiek	expediteurs	prognose	Tweedeling – Economische groei vooral in Nederland, risico’s\nliggen in het buitenland	Naar verwachting groeit de consumptie in 2017 en 2018 nog flink\ndoor. Dit zorgt ervoor dat de volumes toenemen in een aantal\nNederlandse sectoren, zoals de detailhandel en de bouwsector.\nInmiddels stijgen de grondstofprijzen weer en voor 2017 wordt\nverdere groei verwacht. Risico’s voor de groei liggen voornamelijk\nin het buitenland. Internationale onzekerheden blijven bestaan,\nzoals de onderhandelingen over de Brexit. De expediteurs gericht op\nde internationale markt zullen dan ook meer risico’s op hun\ngroeiprognoses moeten incalculeren, dan expediteurs gericht op het\nbinnenland.	162
Transport-en-Logistiek	expediteurs	prognose	Digitale transformatie – Veranderend speelveld	Het samenbrengen van vracht en transporteur is een van de\nkerntaken van een expediteur. In de doorgaans weinig transparante\ntransportmarkt heeft een particuliere of kleinzakelijke verlader\nveelal een ervaren gids nodig om ervoor te zorgen dat goederen\njuist worden vervoerd. Die rol van het samenbrengen van vraag en\naanbod wordt steeds meer digitaal ingevuld, door middel van\nportals. Maar ook andere \ndigitale ontwikkelingen, zoals 3D printen, robotisering en big\ndata veranderen het speelveld voor expediteurs.	163
Transport-en-Logistiek	expediteurs	prognose	Complexere wereld – Biedt kansen, maar brengt ook risico’s\nmee	Geopolitieke spanningen zorgen ervoor dat de wereld steeds\ncomplexer wordt. Maar ook regelgeving met betrekking tot veiligheid\nen de steeds machtigere consument zorgt voor uitdagingen. In deze\ningewikkelde dynamiek is het belangrijk voor verladers om grip op\nhun logistiek proces te houden. De expertise van de expediteur kan\nhierbij helpen. Maar ook gebeurt het dat de verlader voor de vlucht\nvoorwaarts kiest en logistiek in eigen handen neemt.	164
Transport-en-Logistiek	goederenvervoer-over-spoor	prognose	Economische groei – Economie Duitsland met 1,8 procent\ngegroeid	Naast de extra volumes van de binnenvaart in het eerste halfjaar\nvan 2016, heeft het spoorvervoer ook geprofiteerd van de\neconomische groei in Nederland en Duitsland. Maar liefst 92 procent\nvan de goederen die over het spoor worden vervoerd gaan de grens\nover. De meeste goederen worden afgevoerd (73 procent), daarvan\ngaat 76 procent naar Duitsland. Hierbij worden goederen vanuit\nNederland (veelal de haven van Rotterdam) naar een buitenlandse\nbestemming vervoerd. Slechts 27 procent is aanvoer. Dit gebrek aan\nevenwicht tussen aan- en afvoer zorgt dat er relatief veel leeg\nvervoerd moet worden.	165
Transport-en-Logistiek	goederenvervoer-over-spoor	prognose	Betuweroute – Aansluiting Duitsland later gereed	Op langere termijn kunnen spoorvervoerders profiteren van de\naansluiting van de Betuweroute in Duitsland door de aanleg van een\nextra derde spoor. De oplevering stond gepland voor 2022. Inmiddels\nheeft staatssecretaris Sharon Dijksma aangegeven dat het niet\nlanger realistisch is dat 2022 gehaald gaat worden. Tot die tijd\nmoeten gebruikers van de Betuweroute rekening houden met\nomleidingen  voor goederentreinen. Daardoor kunnen\nspoorvervoerders op kortere termijn last hebben van\ncapaciteitsbeperkingen. Dit is nadelig voor goederenvervoerders\nover het spoor, omdat Duitsland de belangrijkste bestemming voor\nhen is.	166
Transport-en-Logistiek	goederenvervoer-over-spoor	prognose	Industrie – Metaal en Chemie belangrijke sectoren voor	Spoorvervoer\nDe metaalindustrie en de chemische industrie zijn belangrijke\ngebruikers van het spoorvervoer. De verwachtingen voor de industrie\nzijn positief. De chemische industrie en de staalindustrie hebben\nwel te kampen met concurrentie uit China. Dit geeft druk op de\ntarieven, waardoor de ondernemers in dit deelsegment het lastig\nhebben. Maar door een economische groei in Duitsland en de eurozone\nzullen de volumes toch licht groeien.	167
Transport-en-Logistiek	goederenwegvervoer	prognose	Bouw – Aangetrokken bouwproductie gunstig voor\nwegtransport	De sterk aangetrokken woningmarkt zorgt voor meer activiteit in\nde bouw. In 2016 groeide de bouwproductie met 7,1 procent en voor\nzowel 2017 als 2018 verwacht ABN AMRO een volumegroei van \n4,5 procent. Daarnaast nemen ook de consumentenbestedingen toe.\nHierdoor stijgen de verkopen in de detailhandel. Vooral de \nonline verkopen maken een flinke groei door. Deze twee factoren\nzijn de belangrijkste drivers voor vrachtvolumegroei in\nNederland.	168
Transport-en-Logistiek	goederenwegvervoer	prognose	Dieselprijs – Prijs stijgt na drie jaar weer	Na drie jaren van daling, steeg de dieselprijs in 2016 weer met\n11,2 procent. Dit als gevolg van de gestegen olieprijs. ABN AMRO\nverwacht op korte termijn een daling van de olieprijs, maar op de\nlange termijn gaat de olieprijs naar verwachting weer stijgen. De\ndaling van de dieselprijs zien we al terug in de eerste maanden van\n2017, als gevolg van de dalende olieprijs. Op de lange termijn zal\nde dieselprijs naar verwachting weer gaan stijgen. Veel ondernemers\nin de branche hebben een brandstofclausule waardoor veranderende\ndieselprijzen op de korte termijn geen invloed op de marges zal\nhebben.	169
Transport-en-Logistiek	goederenwegvervoer	prognose	Faillissementen – Economische groei zorgt voor minder\nfaillissementen	In 2016 gingen er 83 bedrijven actief in het goederenvervoer\nover de weg failliet, waarvan 75 bedrijven en 8 eenmanszaken. In\n2015 waren dit er nog 113, een daling van 26,5 procent. De\neconomische groei en het herstel van de bouw en detailhandel dragen\nhier in belangrijke mate aan bij. De faillissementsgraad (aantal\nfaillissementen gedeeld door het aantal bedrijven) is nog wel hoog.\nDe faillissementsgraad in het goederenvervoer over de weg bedraagt\n0,78 procent, terwijl die voor alle sectoren in Nederland gemiddeld\n0,32 procent bedraagt.	170
Transport-en-Logistiek	opslag	prognose	Grondstofprijzen – Nog veel opslag, ondanks stijgende\nprijzen	De olieprijs is in 2016 weer gestegen, maar bevindt zich nog op\neen relatief laag niveau. Hierdoor wordt nog steeds veel olie\nopgeslagen in de hoop dat de prijzen verder zullen stijgen. De\nbezettingsgraad van opslagbedrijven in olie nam daardoor in 2016\ntoe. Dit was bijvoorbeeld het geval bij Vopak. Ook de \nprijzen van agrarische grondstoffen staan nog onder druk.	171
Transport-en-Logistiek	opslag	prognose	E-commerce – Hoge ingebruikname van logistiek vastgoed	Volgens makelaarsorganisatie \nDynamis is in 2016 het aanbod van logistiek vastgoed met 24\nprocent afgenomen. De opname van logistiek vastgoed daalde met 8\nprocent, maar ligt nog steeds op een hoog niveau. Er wordt veel\nnieuw vastgoed gebouwd in opdracht van de nieuwe eigenaren. Dit\nzijn vaak online retailers. De bouwers lopen hierbij weinig risico.\nDit betekent vaak dat een ander distributiecentrum in Nederland\ngesloten wordt. Dit is een positieve ontwikkeling, want de\ndistributiecentra die gesloten worden zijn vaak verouderd en vragen\nom herstructurering van het gebied.	172
Transport-en-Logistiek	opslag	prognose	Duurzaam – Logistiek vastgoed steeds efficiënter en\nduurzamer	Voor vastgoed in het algemeen, maar zeker ook voor logistiek\nvastgoed is duurzaamheid van blijvend belang. Er wordt steeds\nduurzamer gebouwd, waarbij er ook aandacht is voor circulair\nbouwen. Daarnaast is energie-efficiëntie een belangrijk aspect bij\nduurzaam vastgoed. Verder zorgt vergaande logistieke\ndienstverlening bij e-commerce zoals one day delivery ervoor dat\nook het logistieke vastgoed hier voor geëquipeerd moet zijn.\nRobotisering en automatisering zijn hierin key.	173
Transport-en-Logistiek	short-sea-shipping	prognose	Overcapaciteit – Druk op tarieven kan afnemen	Tegenvallende economische groei in het verleden zorgde voor\nlagere volumes. De financiële crisis en de eurocrisis hadden tot\ngevolg dat er overcapaciteit in de markt ontstond. Voor de crisis\nin 2008 werden er veel nieuwe schepen gebouwd die tijdens of na de\ncrisis in gebruik genomen werden. Dit zorgde voor overcapaciteit en\ndruk op de tarieven. Inmiddels worden er nog maar weinig nieuwe\nschepen gebouwd, waardoor de druk op de tarieven kan afnemen.	174
Transport-en-Logistiek	short-sea-shipping	prognose	Haven van Rotterdam – Overslag containers licht gestegen in\n2016	Rotterdam is voor short sea shipping de belangrijkste haven.\nVoor het achterlandvervoer van de Rotterdamse haven neemt de\nbinnenvaart twintig procent van het containervervoer voor haar\nrekening, wegvervoer veertig procent en spoor circa tien procent.\nIn het achterlandvervoer van containers heeft short sea shipping\neen aandeel van dertig procent. Dit aandeel is wel aan het slinken.\nVooral binnenvaart wint aan marktaandeel.  De overslag van\ncontainers kende een behoorlijke groei in het verleden. Na een\ndaling in 2015 nam de overslag van containers in 2016 weer met 0,7\nprocent toe.	175
Transport-en-Logistiek	short-sea-shipping	prognose	Brexit: Verenigd Koninkrijk belangrijke bestemming voor short\nsea shipping	Dertig procent van de goederen die via short sea shipping worden\nvervoerd vinden hun weg van en naar het Verenigd Koninkrijk.\nHiermee is het Verenigd Koninkrijk een van de belangrijkste\nbestemmingen voor short sea shipping. Daarom vormt de Brexit een\nbedreiging voor deze modaliteit. Maar het kan ook een kans zijn\nwanneer meer goederen via Nederland vervoerd worden. Het effect van\nhet Brexit referendum is tot nu toe meegevallen. Inmiddels is het\nArtikel 50 verzoek ingediend en zullen de onderhandelingen starten.\nDe uitkomst van de onderhandelingen is nog uiterst onzeker, maar\nkunnen de short sea shipping zeker raken.	176
Utilities	wind-solar	prognose	Investeringen in windenergie stijgen verder	In 2015 is de windcapaciteit in Europa met 12,8 GW (+6,3\nprocent) toegenomen. De totale Europese windcapaciteit kwam daarmee\nop 142 GW. In Nederland kwam de totale capaciteit op 3,38 GW,\nwaarvan ruim 3 GW op land. De komende jaren zullen investeringen in\nde branche sterk blijven waardoor de capaciteit aan windvermogen in\nNederland zal stijgen tot 6 GW voor wind op land in 2020, en 4,45\nGW voor wind op zee in 2023. Als de doelstellingen zijn gehaald dan\nzal het aandeel wind in de totale energiemix 6,1 procent bedragen\nin 2023, waarvan 3,2 procent offshore.	177
Utilities	wind-solar	prognose	Aandeel zonne-energie neemt snel toe	Van zonne-energie is lastig is om een totaaloverzicht te krijgen\nvan het precieze geïnstalleerde vermogen aan PV capaciteit omdat\nveel projecten lokaal zijn. Ongeveer 70 procent van de zonnepanelen\nligt op daken van woningen. In 2014 is zo’n 300 MW aan capaciteit\nbijgeplaatst versus 375 MW in 2013. Door de combinatie van lagere\nprijzen voor zonnepanelen en verbeterd rendement zal de groei van\nPV-capaciteit de komende jaren doorzetten. Hoewel de\nsalderingsregeling nog loopt tot 2020, zal de regering al in 2016\nde regeling evalueren en met een voorstel komen voor de jaren na\n2020.	178
Utilities	wind-solar	prognose	Energie-efficiency belangrijk hulpmiddel	De Nederlandse doelstellingen voor het opwekken van duurzame\nenergie zijn 14 procent in 2020 en 16 procent in 2023. Dit is\nonderdeel van het beleid richting 100 procent aanbod van\nhernieuwbare energie in 2050. In 2014 was 5,6 procent gerealiseerd.\nHierbij werd de stijging deels verklaard door het grotere aanbod\nhernieuwbare energie, maar een groot deel ook door een daling van\nhet totale eindverbruik van energie. Daaruit blijkt dat\nenergie-efficiency een belangrijk hulpmiddel kan zijn bij het\nbehalen van de doelstellingen.	179
Zakelijke-dienstverlening	accountantskantoren	prognose	Marktvolume neemt toe	De groeiende economie en bedrijvigheid pakken gunstig uit voor\nde vraag naar accountantsdiensten. Ook neemt het aantal bedrijven\nen instellingen die wettelijk gecontroleerd moeten worden, toe.\nVerder worden er ten behoeve van een betere kwaliteit meer uren\ngestopt in controleactiviteiten. Daar staat tegenover dat door\nstandaardisering, digitalisering en automatisering handmatige\nwerkzaamheden afnemen en branchevreemde partijen de\naccountantsmarkt betreden. Per saldo neemt het marktvolume wel\ntoe.	180
Zakelijke-dienstverlening	accountantskantoren	prognose	Samenstelpraktijk de kurk waar de\naccountancy op drijft	Het percentage van advies gerelateerde diensten van de omzet\nblijft met ongeveer 12% over de afgelopen 8 jaar opmerkelijk\nconstant voor de kleinere en middelgrote accountants. In de\nsamenstel praktijk vindt inderdaad druk op de marges plaats maar\nniet zo groot als wij in eerste instantie dachten. Door de crisis\nvan 2009 hebben veel kantoren geïnvesteerd in procesoptimalisatie\nen besparingen in de personeelskosten. Het neveneffect hiervan is\ndat de samenstel praktijk nog langer een cash cow kan blijven. Veel\npartijen werken samen: ofwel door middel van het investeren in een\n‘wasstraat’ voor het maken van een jaarverslag ofwel door met\npartners te investeren in de vereisten die nodig zijn voor het in\nstand houden van de controle praktijk. Gevaar bestaat dat nieuwe\ntoetreders vanuit de ICT wereld de marges in de samenstel praktijk\nversneld kunnen uithollen.\n 	181
Zakelijke-dienstverlening	accountantskantoren	prognose	Advisering biedt nog geen soelaas	Door meer diensten met een hoge toegevoegde waarde te\nontwikkelen, kan de tariefdruk op standaarddiensten worden omzeild.\nEr wordt vooral gedacht aan het uitbreiden van adviesdiensten\nrichting de opdrachtgever. Hierbij gaat het ook nog om een\nproactieve wijze van adviseren. De verschuiving naar meer\nadvisering verloopt echter moeizaam, mede omdat het tijd vergt\nvoordat de accountant zich de adviesbekwaamheden heeft eigen\ngemaakt. Op de korte termijn zien wij daarom de adviesomzet niet\nsubstantieel toenemen.	182
Zakelijke-dienstverlening	advocatenkantoren	prognose	Markt voor diensten van advocaten stijgt	De juridisering van de samenleving zet nog steeds door wat\npositief is voor de markt voor advocaatdiensten. Verder stimuleert\nnieuwe wet- en regelgeving zoals op arbeidsrechtelijk gebied de\nbehoefte aan juridische hulp. Gunstig is ook dat het aantal fusies\nen overnames verder stijgt. Er zijn echter ook factoren die de\nmarktgroei afzwakken zoals de verhoogde toetredingsdrempel als\ngevolg van hogere griffierechten en bezuinigingen op gesubsidieerde\nrechtsbijstand. Per saldo zien wij de markt verder groeien.	183
Zakelijke-dienstverlening	advocatenkantoren	prognose	Concurrentie vanuit diverse hoeken	De concurrentie in de branche neemt toe. Steeds meer\nbuitenlandse partijen betreden de markt. Tegelijkertijd neemt de\nversnippering in forse mate toe. Bijna 90 procent van de\nadvocatenkantoren heeft nu minder dan vijf werknemers in dienst.\nVerder breiden accountantskantoren hun juridische tak uit. Vooral\nin het segment onder het topsegment van juridisch advies wordt de\nconcurrentie gevoeld. Daarentegen voeren advocatenkantoren ook\nsteeds meer forensisch onderzoek uit; vanouds het terrein van\naccountants.	184
Zakelijke-dienstverlening	advocatenkantoren	prognose	Grote kantoren profiteren van hun internationale network. De\nvraag naar M&A blijft sterk.	De advocatuur lijkt immuun voor de veranderingen die zich in\nandere sectoren volstrekken. Met name de grote kantoren aan de\nZuidas profiteren van de economische opleving en het grote aantal\novernames. Binnen de grote kantoren zien we een verschil tussen\nkantoren die met name in de Nederlandse markt opereren (AEX) en\nkantoren die profiteren van een internationaal netwerk. De kleine\ngespecialiseerde kantoren hebben een goede uitgangspositie vanwege\nhun lagere kostenbasis en specifieke toegevoegde waarde. Het zijn\nmet name de grote regionale kantoren die last hebben van druk op de\nmarges en een te hoge kostenstructuur.	185
Zakelijke-dienstverlening	beveiligingsbedrijven	prognose	Structurele factoren ondermijnen volume	Gunstig voor de beveiligingsmarkt is de verdere groei van de\nNederlandse economie en daarmee van de bedrijvigheid. \nNegatieve structurele zaken blijven echter het marktvolume\nondermijnen. Zo daalt het aantal bedrijfsgebouwen en m2\nbedrijfsruimte door een efficiënter gebruik van bedrijfslocaties,\nautomatisering en thuiswerken. Ook gaat de rijksoverheid door met\nhet inbesteden van beveiligingsdiensten.\n 	186
Zakelijke-dienstverlening	beveiligingsbedrijven	prognose	Tariefdruk ‘fact of life’	De branche is zeer kleinschalig van aard en klanten zien vooral\nmanbewaking als een ‘commodity’. De concurrentie is dan ook hevig\nen de tariefdruk sterk. Hierdoor wordt er steeds meer technologie\ningezet om de efficiency van het beveiligingswerk te verhogen.\nVerwacht wordt dat het beveiligingswerk steeds meer gaat opschuiven\nvan manbeveiliging naar beveiliging op afstand. Daardoor daalt het\nvolume aan beveiligingsdiensten, maar stijgen de tarieven. per\nsaldo blijft er weinig omzetgroei over.	187
Zakelijke-dienstverlening	beveiligingsbedrijven	prognose	Uitbreiding dienstenpakket moet omzet verhogen	Beveiligingsbedrijven proberen in toenemende mate inzicht te\nkrijgen in de beveiligingsproblemen en –doelstellingen van hun\nopdrachtgevers. Ze kunnen daar dan proactief op reageren en\noplossingsrichtingen voor aangeven. Door meer in te zetten op het\nadviseren van hun klanten wordt hun toegevoegde waarde verhoogd wat\nde omzet ten goede moet komen. Deze uitbreiding van het\ndienstenpakket vergt echter tijd en leidt op de korte termijn nog\nniet tot een substantiële opwaartse druk op de omzet.	188
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	prognose	Aantal geldvorderingen neemt af	Met de verder groeiende economie stabiliseert het aantal\nconsumenten en bedrijven met een betalingsachterstand hooguit.\nDaarbij blijft het gemiddelde bedrag aan leningen en kredieten\nonder druk staan vanwege de meer voorzichtige houding van de\nverstrekkers. Negatief voor de markt voor geldvorderingen is ook de\nverdere verschuiving van het innen naar het voorkomen van\nvorderingen. Positief is wel dat de preventieve werkzaamheden omzet\nopleveren en het productenpakket wordt uitgebreid met bijvoorbeeld\ndebiteurenbeheer.	189
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	prognose	Concurrentie en prijsdruk nemen toe	Het aandeel van het kleinere incassobureaus neemt gestaag toe.\nInmiddels heeft ruim 90 procent van de incassobureaus minder dan 5\nwerknemers. De voortschrijdende schaalverkleining zorgt bij\nincasso’s voor een intensieve strijd om opdrachten en\nprijsdruk.\nDaarnaast oefenen grote schuldeisers die standaardvorderingen\nhebben uitstaan zoals ziektekostenverzekeraars, energiebedrijven en\ntelecombedrijven, grote druk uit op de deurwaarderstarieven.	190
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	prognose	Aantal ambtshandelingen daalt	Het aantal ambtshandelingen van gerechtsdeurwaarders neemt\nverder af. Dit wordt onder meer veroorzaakt door de alsmaar\ntoenemende griffierechten. Maar ook de verschuiving van inning naar\npreventie van geldvorderingen in het incassotraject speelt hier een\nrol. Hierdoor neemt het aantal vorderingen zonder een rechterlijke\ntussenkomst af. Wel vergt deze manier van werken meer arbeidsuren.\nBij gecombineerde deurwaarders- en incassopraktijken neemt het\naandeel van ambtelijke handelingen in de totale omzet dan ook\naf.	191
Zakelijke-dienstverlening	notariskantoren	prognose	Woningmarkt stijgt verder	Jaarlijks kunnen de verschillende praktijken grote uitslagen\nlaten zien in het aantal akten. Een rol hierbij spelen onder meer\nde economische ontwikkeling (denk aan woningverkopen),\noverheidsbesluiten (bijvoorbeeld schenkingen) en het voeren van\ncollectieve promotiecampagnes (bijvoorbeeld levenstestament).\nVerwacht wordt dat de bedrijvigheid en de koopkracht op de korte\ntermijn toenemen wat positief is voor de markt van de notaris. In\nhet bijzonder groeit ook de woningmarkt verder, hoewel de groei\nafzwakt.	192
Zakelijke-dienstverlening	notariskantoren	prognose	Tariefdruk structureel	De tarieven in het notariaat staan al geruime tijd onder druk.\nDit is vooral bij de onroerendgoedpraktijk het geval. Daar zijn\nverschillende redenen voor. Zo zijn klanten steeds beter\ngeïnformeerd en worden zij in toenemende mate prijsbewust. Ook\nworden steeds meer diensten van de notaris gezien als een\nstandaarddienst. De klant verwacht dat een dergelijke dienst\nefficiënt wordt uitgevoerd en acceptabel geprijsd is. Voorlopig zal\nde prijsdruk aanhouden, mede ook door de opmars van branchevreemde\npartijen.\nDaarnaast bestaat er zorg bestaat over de impact van blockchain-\ntechnologie op de werkzaamheden van de notaris.	193
Zakelijke-dienstverlening	notariskantoren	prognose	Aanmeten andere competenties vergt tijd	Om de omzet te behouden is de branche gedwongen in te spelen op\nde veranderende klant, de prijsdruk en branchevreemde partijen. Zo\nprobeert men nieuwe klanten aan te boren, de omzet per klant te\nverhogen of nieuwe diensten met een hoge toegevoegde waarde aan te\nbieden. Instrumenten hiertoe zijn onder meer promotiecampagnes, een\npro actievere adviseursrol richting klanten en het warm maken van\nklanten voor meer complexe diensten. De notaris moet zich hiervoor\nechter andere competenties eigen maken, wat tijd kost.	194
Zakelijke-dienstverlening	schoonmaakbedrijven	prognose	Structurele factoren remmen volumegroei	De Nederlandse economie groeit de komende jaren verder. Dit\nbevordert de bedrijvigheid waar de schoonmaakmarkt van profiteert.\nHet volume blijft echter wel onderhevig aan structurele negatieve\nontwikkelingen. Zo wordt er meer thuis gewerkt waardoor er minder\nkantoorruimte nodig is. Ook drukt een efficiënter gebruik van de\nbedrijfslocaties het aantal m2 bedrijfsruimte. Tenslotte zet de\noverheid haar inbestedingsbeleid voort. Op de langere termijn is de\ngroei van het schoonmaakvolume daarom beperkt.	195
Zakelijke-dienstverlening	schoonmaakbedrijven	prognose	Schoonmaakmarkt is een vechtmarkt	Er zijn enkele grote spelers en heel veel kleine spelers. Sinds\n2007 is het aantal bedrijven met minder dan vijf werkzame personen\nmet bijna 75 procent toegenomen. Inmiddels heeft bijna 90 procent\nvan de bedrijven minder dan vijf werknemers. Daarnaast wordt\nschoonmaak gezien als een ‘commodity’ waardoor prijsverhogingen\nmoeilijk zijn door te voeren. In combinatie met het structureel\nafnemende aantal m2 bedrijfsruimte is het dan ook niet\nverwonderlijk dat de schoonmaakmarkt een vechtmarkt is met lage\nmarges.	196
Zakelijke-dienstverlening	schoonmaakbedrijven	prognose	Minder tariefdruk door inleving in klant	Om de tariefdruk af te zwakken, brengt de branche steeds meer de\nwaarde van schoonmaak naar voren bij klanten. Denk bijvoorbeeld aan\nde toenemende nadruk op het aspect gastvrijheid en de beleving van\nwerknemers en bezoekers. Ook nemen schoonmaakbedrijven steeds meer\ninitiatieven om de doelstellingen van hun klanten te doorgronden en\naan te geven hoe schoonmaak daarin past. Verder leidt het meedenken\nmet de cliënt over de schoonmaakwijze en de contractvorm tot een\nhogere waardering van het schoonmaakbedrijf.	197
Zakelijke-dienstverlening	uitzendbureaus	prognose	Economische groei en flexibilisering stuwen markt	De uitzendmarkt profiteert sterk van de groei van de economie.\nDit los van de structurele verschuiving van vaste naar flexibele\narbeidscontracten waar het uitzendcontract een van is. Werkgevers\nvoelen er namelijk steeds minder voor om werknemers in vaste dienst\nte nemen. Dit onder meer door de complexer wordende\narbeidswetgeving en daaraan verbonden risico’s. De belangrijkste\naanjager van flexibele arbeidsrelaties is echter de behoefte van\nwerkgevers om de personeelskosten mee te laten bewegen met de\nmarkt.\nLees ook.\nen Lees\nook (Engelse versie).	198
Zakelijke-dienstverlening	uitzendbureaus	prognose	Traditioneel uitzenden is een ‘commodity’	Het uitzenden voor de traditionele momenten ‘piek en ziek’ is\ntot een ‘commodity’ verworden. Daarnaast hebben opdrachtgevers\nsteeds meer inzicht gekregen in de kosten van een uitzendkracht\nvoor het uitzendbureau. Beide factoren brengen daarom voor het\ntraditioneel uitzenden prijsdruk met zich mee. Daarbij komt dat\nmede door digitalisering de toetredingsdrempel tot uitzenden\nalsmaar lager wordt. Al met al is het moeilijk hier onderscheidend\nin te zijn, tenzij men zeer efficiënt is en tot de kostenleiders\nbehoort of unieke toegang heeft tot een economische nichemarkt.\nLees\nook:	199
Zakelijke-dienstverlening	uitzendbureaus	prognose	Uitbreiding dienstenpakket moet omzet op peil houden	Hoewel de branche profiteert van de economische groei, zijn er\nstructurele uitdagingen. Zo daalt door automatisering het aantal\nbanen waarvoor een lage scholing voldoet. Dit zijn banen waar het\nalgemene uitzendbureau zich op richt. Ook neemt in de flexschil van\nwerkgevers het aandeel van uitzendkrachten af ten gunste van\ntijdelijke arbeidscontracten en zzp’ers. Uitzendbureaus zijn\ndaardoor genoodzaakt andere arbeid gerelateerde diensten aan te\nbieden, en het liefst met een hogere toegevoegde waarde zoals\n‘recruiting’.\nUitzenders moeten met hun dienstenaanbod anticiperen op de\nontwikkelingen bij inleners: de contractvorm wordt steeds minder\nrelevant.	200
\.


--
-- Name: prog_table_prog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('prog_table_prog_id_seq', 400, true);


--
-- Data for Name: trend_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY trend_table (sector, branche, type, head, body, trend_id) FROM stdin;
Agrarisch	akkerbouw	trend	Vervolgstappen in verduurzaming	De samenhang tussen structuur, mineralen en bodemleven bepaalt\nhoe weerbaar en gezond gewassen zijn. Door juiste teeltwisseling\ntoe te passen, de grond niet te zwaar te belasten en tijdig te\nbemesten, blijft de kwaliteit van de grond op peil. Ook voor\npachtgronden en ruilpercelen is dit van groot belang. Vergroening\nvan de chemische middelen vraagt om versnelling en een level\nplaying field. Ook consumenten en ngo’s volgen akkerbouwers\nkritisch. \nLees meer.	1
Agrarisch	akkerbouw	trend	Waardevolle informatie door verdere digitalisering	Door de grote diversiteit aan verwerkers, handelaren en\nverkoopconstructies, is het voor akkerbouwers moeilijk om het\nverkoopmoment van hun producten te bepalen en strategische\nbeslissingen te onderbouwen. Goede markt- en prijsinformatie\nontbreekt. De digitalisering van gegevens gaat de akkerbouwer\nhelpen zijn bedrijfsvoering te optimaliseren. De markt- en\nteeltinformatie komen breed beschikbaar om onderbouwde keuzes te\nmaken. Dit gaat verder dan alleen precisielandbouw. Lees\nmeer.	2
Agrarisch	akkerbouw	trend	Van origine gezond	Steeds meer onderzoek bevestigt dat je met gezonde voeding onder\nandere obesitas en diabetes type 2 kunt voorkomen.\nAkkerbouwproducten staan als grondstoffen op de ‘schijf van vijf’\nen passen bij een gezonde levensstijl. Het is noodzakelijk dit\nonder de aandacht van de consument te brengen en zijn bewustzijn op\ndit gebied te vergroten, bijvoorbeeld door meer transparantie. Ook\nde medische wereld benadrukt steeds vaker dat voldoende gezond eten\ngoed is voor preventie van ziekten en versneld herstel.	3
Agrarisch	kalverhouderij	trend	Innovaties in voeding om kosten te reduceren	De daling van de toeslagrechten en de toegenomen kosten voor\nmestafzet dwingen ondernemers in de kalfsvleesketen te zoeken naar\ncompensatie om het rendement op peil te houden. Dit doen zij\nbijvoorbeeld door innovaties binnen het voerpakket. Een deel van de\nzuivelgrondstoffen wordt vervangen door plantaardige ingrediënten.\nEen ander voorbeeld is het gebruik van losse grondstoffen in vaste\nof vloeibare vorm. Daarbij is het belangrijk dat gezondheid,\nvleeskwaliteit en – kleur op hoog niveau blijven. Deze\nkostenverlagende innovaties zijn, samen met de gedaalde\ninkoopprijzen van nuchtere kalveren effectief geweest. De\ncontracten voor witvlees zijn het afgelopen jaar zelfs licht\nverbeterd.	4
Agrarisch	kalverhouderij	trend	Gezondere dieren, betere kwaliteit	Kalverhouders hebben beperkte mogelijkheden om zieke dieren\npreventief te behandelen met diergeneesmiddelen. Diergezondheid is\ndaarom erg belangrijk. Daardoor is er veel aandacht voor\ninvesteringen in hygiëne en stalklimaat. Maar ook voor samenwerking\nmet de melkveesector om zo biestverstrekking en de kwaliteit van de\nkalveren te verbeteren. En de beschikbare informatie over de dieren\nte vergroten zodat de opvang van jonge dieren aansluit bij hun\nbehoeften. Hogere gezondheid verbetert de dierprestaties, de\nkwaliteit van het eindproduct en versterkt het duurzame karakter\nvan de sector.	5
Agrarisch	kalverhouderij	trend	Ontwikkeling van nieuwe afzetmarkten	Meer dan negentig procent van het Nederlandse kalfsvlees wordt\ngeëxporteerd. De afzet van blank kalfsvlees krimpt in traditionele\nafzetmarkten als Italië en Frankrijk. Hiervoor moeten andere\nafzetmarkten worden gezocht, veelal buiten Europa. De opening van\nde markt in de VS en enkele landen in het Midden-Oosten bieden\nmogelijkheden net als de doorontwikkeling van nieuwe\nkalfsvleesconcepten. Verdere differentiatie of zelfs\nmerkontwikkeling bieden kansen voor het versterken van de mondiaal\nsterke positie van Nederlands kalfsvlees.	6
Agrarisch	melkveehouderij	trend	Fosfaatrechten worden het nieuw quotum	De reductie van het aantal koeien in 2017 heeft flinke impact,\nmaar is slechts een opmaat naar 2018. Dan volgt de wettelijke\nintroductie van fosfaatrechten plus nog een laatste extra\nreductie. Daarmee komt de sector in een situatie die hetzelfde aan\nvoelt als de tijd van melkquotering. Nationale groei is beperkt en\ngroei op bedrijfsniveau is kostbaar door benodigde fosfaatrechten.\nEn dat terwijl de wereldmarkt lonkt en kansen leek te bieden voor\ngroei van Nederland als zuivelland.	7
Agrarisch	melkveehouderij	trend	Investeren in zorgvuldige melkveehouderij\n 	De toekomst van de zuivelketen ligt door milieubegrenzingen niet\nzozeer in groei van volume maar in groei van toegevoegde waarde. De\nbasis is goed; de Nederlandse zuivelsector zit in de mondiale\nkopgroep en heeft toegang tot belangrijke groeimarkten. Verdere\nuitbouw van de sterke punten als en kwaliteit en imago vereisen\nextra inspanningen maar er is geen weg terug. Focus op de bovenkant\nvan de markt is de beste remedie tegen negatieve gevolgen van\nprijsvolatiliteit. De marktdynamiek blijft, maar het zorgt wel voor\nhogere pieken en minder diepe dalen.	8
Agrarisch	melkveehouderij	trend	Schommelende zuivelprijzen als nieuwe\nrealiteit	De zuivelmarkt is in de loop van 2016 hersteld. Het onderscheid\ntussen de sterke positie van melkvet en de zwakke positie van\nmelkeiwit is opvallend. Vet en boter zijn in de VS niet langer\ntaboe. Wij verwachten een voorzichtige verdere stijging van de\nmelkprijs. Voor een volgende piek is 2017 nog te vroeg, de\ninterventievoorraden hebben een remmende werking op prijsherstel.\nDe groei van de wereldbevolking en van de welvaart zorgen ook voor\nde lange termijn voor positieve vooruitzichten. Positief én\nvolatiel.	9
Agrarisch	pluimveehouderij	trend	Concepten met een goed verhaal achter het product	Consumenten zoeken steeds meer naar vlees of eieren met een goed\nverhaal. Door de vraag naar herkomst, dierenwelzijn en smaak maken\nvleesconcepten als Goed Nest Kip, Nieuwe Standaard Kip, beter\nleven-ster kip en biologische kip een sterke opmars door. Bij\neieren zie je deze trend terug in vrije uitloop- en biologische\neieren. De productie vindt veelal plaats in vraag gestuurde ketens.\nDe verbinding tussen boer en consument is daarbij een\nspeerpunt.	10
Agrarisch	pluimveehouderij	trend	Kip en ei in opmars	Er wordt meer kip en ei gegeten door de veranderende\nsamenstelling van de bevolking in\nNoordwest-Europa, het gezondheidsimago en ook de lage prijs in een\ntijd van beperkte koopkracht. Dit zorgt ervoor dat de kip- en\neierconsumptie per persoon in Europa stijgt. Door in te spelen op\nbovenstaande consumententrends ontstaan mogelijkheden voor verdere\ngroei.	11
Agrarisch	pluimveehouderij	trend	Investeren in zorgvuldige pluimveehouderij	De groei van de totale Nederlandse veestapel zorgt ook voor\nstijgende kosten in de pluimveehouderij. Ondernemers betalen meer\nvoor mestafzet, milieubelasting, vergunningen en dierrechten. Het\nbelang van hoge productiviteit en lagere kosten is daarom groot.\nPluimveehouders investeren in mestverwerking\nen digitalisering van voer-, klimaat- en administratiesystemen.\nDeze slimme systemen ondersteunen een zorgvuldige en duurzame\npluimveehouderij.	12
Agrarisch	sierteelt	trend	Positieve effecten op welzijn	De positieve effecten van bloemen en planten op het welzijn van\nmensen worden algemeen erkend. Woon-, leef-, herstel- en\nwerkomgevingen hebben nog veel vergroeningspotentie. Er komen\nnieuwe ideeën op een relatief traditionele markt: van groene\nbelevingen in hotels tot stadslandbouw en abonnementen op\nboeketten. De verwachting is dat nieuwe toetreders deze markt\nzullen openbreken als de huidige marktpartijen kansen laten liggen.\nLeer meer.	13
Agrarisch	sierteelt	trend	De consument kan kwaliteitsverschillen niet onderscheiden	Als producent van snijbloemen en planten wil je dat de consument\ntevreden is over zijn of haar aankoop. De kans op een\nherhalingsaankoop is dan groter. Voor consumenten is heldere\ninformatievoorziening belangrijk. Hoe vers is het product? Hoelang\nkan ik er van genieten? In het huidige systeem duurt het soms lang\nvoordat bloemen of planten plant de consument bereiken. Hoe oud\nzijn de rozen op Valentijnsdag of moederdag? Tracking en tracing\n,en daarmee ook een kortere verblijftijd in de keten, wordt\nnoodzakelijk.	14
Agrarisch	sierteelt	trend	Inzicht in milieu-impact geeft potentie voor verduurzaming	De laatste vijftien jaar heeft de sector veel geïnvesteerd in\nverduurzaming van het productieproces en verlaging van de\nmilieubelasting. Bijvoorbeeld via verwaarding van reststromen,\nzonnepanelen en aardwarmte. Er is momenteel veel discussie over de\nmilieu-impact van de productie van bloemen en planten De\nmilieu-impact zou onafhankelijk bepaald moeten worden. De LCA\nmethodiek lijkt een goede methode om productiemethoden en keten te\nbeoordelen. Dit inzicht geeft tevens mogelijkheden om de bestaande\nproductie verder te verduurzamen. \nLees meer.	15
Agrarisch	varkenshouderij	trend	Vlees met een verhaal	Steeds meer consumenten willen vlees met een goed verhaal. Door\ndeze vraag naar herkomst, dierenwelzijn en smaak maken\nvleesconcepten zoals vlees met beter leven ster, biologisch\nvarkensvlees en Keten Duurzaam Varkensvlees een sterke opmars door.\nNieuwe ketens en concepten ontstaan op initiatief van supermarkten,\nvleesverwerkers en veehouders. De verbinding tussen boer en\nconsument en transparantie over de herkomst zijn belangrijke\nspeerpunten om het consumentvertrouwen te verbeteren. In deze\nketens zijn consumententrends meestal het vertrekpunt.	16
Agrarisch	varkenshouderij	trend	Kostenbesparing en mestafzet	De Nederlandse varkenshouder heeft een belangrijk\nconcurrentienadeel, de milieukosten. Vooral kosten voor mestafzet,\n–verwerking en dierrechten, drukken zwaar op het rendement. Dit\nnadeel heeft er in geresulteerd dat de Nederlandse varkenshouder\nbijzonder kostenbewust en productief is. Investeringen in mestverwerking,\nslimme voer-, klimaat- en administratiesystemen helpen om de kosten\nin de hand te houden. 2017 is een belangrijk jaar voor de\nmelkveehouderij, maar ook voor de varkenshouderij. Het behoud van\nde derogatie (de toestemming om meer mineralen op landbouwgrond te\ngebruiken) staat op het spel en heeft direct gevolgen voor de\nkosten van mestafzet.	17
Agrarisch	varkenshouderij	trend	Investeren in gezondere dieren	Dieren met een hoge gezondheid dragen bij aan efficiënte\nproductie en hebben minder vaak een behandeling met een\ndiergeneesmiddel nodig. Daarnaast biedt vlees van heel gezonde\ndieren die niet zijn behandeld met diergeneesmiddelen, kansen voor\nmarkten die hier gevoelig voor zijn. Deze win-win aanpak vraagt wel\nom investeringen in gezondheid, hygiëne maatregelen en soms in\nbedrijfssystemen als “bedrijfs-all-in, all-out”. Nieuwe technieken,\ndata en sensoren maken een nog zorgvuldiger en transparante\nvarkenshouderij mogelijk.	18
Agrarisch	visserij	trend	Focus op gezond imago	Afgelopen jaren verbeterden de financiële resultaten in de\nvisserij sterk. Stijgende visprijzen, lagere olieprijzen en minder\nbrandstofverbruik hebben de rentabiliteit omhoog gestuwd. Door het\neconomische herstel geven consumenten bovendien meer toe aan hun\nbehoefte aan gezond voedsel. Het positieve imago van vis profiteert\nhiervan. De Nederlandse visserij speelt hierop in door meer\naandacht te vragen voor het ‘kwaliteitslabel Nederland’. Dit kan de\nfinanciële resultaten nog verder positief beïnvloeden.	19
Agrarisch	visserij	trend	Verduurzaming zet door	De visserijsector is de richting van verdere verduurzaming van\nde Nederlandse kottervloot ingeslagen. De MDV-kotter, voortgekomen\nuit het project Masterplan Duurzame Visserij, heeft hieraan een\npositieve bijdrage geleverd. Afgelopen jaren zijn er daarnaast\nmeerdere duurzame stappen gezet door onder andere investeringen in\nbodemvriendelijke, brandstofbesparende (en dus\nrendementsverhogende) vismethoden. Ook de komende jaren blijft de\nsector ontwikkelen, zoals bijvoorbeeld in selectievere\nvisserijtechnieken. Ook overheden en ngo’s spelen hierin een\nactieve rol.	20
Agrarisch	visserij	trend	Nauwere ketensamenwerking	Afgezien van quotering, wordt er bijna niet gestuurd op\nvangsten. Natuurlijke omstandigheden beïnvloeden de hoeveelheden\ngevangen vis. Het vakmanschap van de visser is vaak gericht op een\nzo groot mogelijke vangst binnen de toegestane quota, terwijl de te\nleveren hoeveelheid vaak al vastligt bij handel en retailers.\nUitdaging is om aanbod en vraag beter op elkaar af te stemmen. Door\neen vangstplan op te stellen, geven de producentenorganisaties hier\nal vorm aan, terwijl daarnaast langzamerhand meerdere initiatieven\ntot verdere samenwerking tussen de visser en de handel tot stand\nkomen.	21
Agrarisch	voedingstuinbouw	trend	Voeding wordt persoonlijker	Consumenten worden zich steeds meer bewust van wat zij eten.\nGezondheid en duurzaamheid zijn belangrijke aspecten die steeds\nvaker worden gerelateerd aan voeding. In verschillende levensfases\nhebben mensen behoefte aan verschillende voedingsstoffen. Een baby\nheeft een andere behoefte dan een tiener of een bejaard persoon.\nDaarnaast hebben bijvoorbeeld topsporters ook andere\nvoedingspatroon. Groente en fruit zijn belangrijke bronnen voor\ndeze voedingsstoffen. Nieuwe apps en sensoren geven inzicht in\nvoedingswaarde en ondersteunen gebruikers hun persoonlijke doelen\nte halen. \nLees meer.	22
Agrarisch	voedingstuinbouw	trend	Inzicht in milieu-impact geeft potentie voor verduurzaming	De laatste vijftien jaar heeft de sector veel geïnvesteerd in\nverduurzaming van het productieproces en verlaging van de impact op\nhet milieu. Bijvoorbeeld via verwaarding van reststromenen\ninvesteringen in zonnepanelen en aardwarmte. Er is momenteel veel\ndiscussie over de milieu-impact van de productie van groenten en\nfruit. Deze moet onafhankelijk bepaald kunnen worden. De LCA\nmethodiek lijkt een goede methode om productiemethoden en keten te\nbeoordelen op milieu-impact. Dit inzicht geeft tevens mogelijkheden\nom de bestaande productie verder te verduurzamen. \nLees meer.	23
Agrarisch	voedingstuinbouw	trend	Meer focus op gezondheidsaspecten van Groente en Fruit	Steeds meer onderzoek bevestigt dat je met gezonde voeding onder\nandere obesitas en diabetes type 2 kunt voorkomen. Vooral verse en\nonbewerkte groenten en fruit passen goed bij een gezonde\nlevensstijl. Het is noodzakelijk dit onder de aandacht van de\nconsument te brengen en zijn bewustzijn op dit gebied te vergroten.\nOok de medische wereld benadrukt steeds vaker dat voldoende groente\neten goed is voor preventie van ziekten en versneld herstel.\nLees meer.	24
Bouw	architectenbureaus	trend	SMART architect	Architecten zijn de creatievelingen in het ontwerpproces dat aan\nhet bouwen vooraf gaat. Hier worden de eerste lijnen uitgezet. De\nkracht van de architect ligt in de combinatie van creativiteit,\nkennis én verbinden binnen en buiten de sector. Met die creatieve\nwendbaarheid creëer je een voorsprong. Door slimmer samenwerken,\nkennis van de nieuwste technologische ontwikkelingen en\n(materiaal)innovaties kan zowel architectuur als duurzaamheid naar\neen hoger niveau worden gebracht. Hiermee creëer je vanaf het begin\n oplossingen die niet bereikt zouden worden in traditionele,\nmeer lineaire, businessmodellen. Dat is de toegevoegde waarde van\neen SMART architect. Lees \nhier meer over de meerwaarde van creativiteit.	25
Bouw	architectenbureaus	trend	Digitalisering wordt zichtbaar	De voortdurende digitalisering van de sector kan gezien worden\nals een kans voor de architect. Digitalisering stopt niet bij BIM,\nmaar gaat via VR/AR, het materialenpaspoort en Blockchain nog veel\nverder. De architect kan juist nu het verschil maken in het\nontwerptraject, en dat wordt in een steeds vroegere fase van het\nontwerp al zichtbaar. Virtual Reality (VR) en Augmented Reality\n(AR) bieden kansen voor betere communicatie, een beter proces,\nlagere faalkosten en meer tevreden klanten. Dat telt voor alle\nbranches. In de bouwsector zijn de architecten de aangewezen partij\nom deze digitale handschoen op te pakken. Lees hier\nmeer over digitalisering in de bouw.	26
Bouw	architectenbureaus	trend	Vormgeven aan duurzaamheid	Duurzaamheid is ook voor de bouwsector belangrijker dan ooit. En\ndit gaat niet minder worden. Duurzaamheid gaat een volgende fase in\nnu er meer en meer voorbeelden zijn dat we van een lineaire naar\neen circulaire economie gaan. Architecten dienen steeds vaker in de\nontwerpfase al rekening te houden met enkele belangrijke principes\nvan de circulaire economie; reduce, reuse en recycle. Co-creatie in\nde bouwketen, toepassing van nieuwe technologieën en bewustwording\ngaan hier het verschil maken. Architecten kunnen met deze kennis in\nhuis een belangrijke positie innemen in het circulaire\nontwerptraject. Ze geven vorm aan deze nieuwe duurzaamheid. Meer\nover architecten en circulair ontwerpen in bijgaande \nvlog.	27
Bouw	grond--weg-waterbouw	trend	Bouwen in de binnenstad	De trek naar de stad zorgt ervoor dat nieuwbouw en onderhoud een\nconstante factor zijn in het straatbeeld van de stad. De moderne\nstadsbewoner accepteert die overlast (stank, geluid, afzettingen\netcetera) niet zonder meer. Bouwers zullen daarom steeds meer\nmoeten samenwerken met zowel de omgeving als de opdrachtgever. In\ngoede samenwerking en met betere communicatie kan gezorgd worden\nvoor een beter, duurzamer en minder verstorend proces. Zo kan\nbouwmaterieel met Het\nNieuwe Draaien en door nieuwe brandstoftechnieken (bijvoorbeeld\nGTL fuel) zuiniger, stiller én schoner werken. Nieuwe functies\n(omgevingsmanager) en technologieën  (de Bouwapp) helpen met de\ncommunicatie. Lees meer over ontwikkelingen in de binnenstad in\nonze publicatie over Smart Cities (hier\nen \nhier).	28
Bouw	grond--weg-waterbouw	trend	Risk én return	Afgelopen jaren was er een tendens waarneembaar dat meer en meer\nrisico’s door aannemers werden geaccepteerd.  Dat heeft niet\nalleen te maken met nieuwe contractvormen, maar ook met de\naanbestedingsmarkt. Bij andere contractverantwoordelijkheden horen\nook andere werkzaamheden en daardoor vaak hogere risico’s. Die\nrisico’s moeten weloverwogen worden aangegaan, met een\ngecalculeerde inschatting van het risico, de kosten van mitigatie\nof verzekering en een grondige afweging van de eventuele\nconsequenties. Met specifiek contract- en risicomanagement zijn de\nrisico’s te managen. Het voordeel is dat de concurrentie niet\nalleen meer op prijs is en dat er tegen het hogere risico ook een\nhogere return staat…	29
Bouw	grond--weg-waterbouw	trend	Smart infra	Inzicht in wie wat waar doet, is de basis voor een beter project\nen een betere samenwerking. Veel werken zijn groots, complex,\nondergronds en ‘just in time’. Voor wat betreft het bouwproces kan\nmonitoring en realtime communicatie zorgen voor optimalisatie\nhiervan. Een sleutelrol is weggelegd voor Internet of Things en Big\nData. Als met behulp van track and trace-systemen bekend is waar\nhet product is, kan het bouwproces efficiënter worden  en\nverstoringen worden beperkt. Voorbeelden met de Bouwhub en\nstadslogistiek tonen aan dat hier nog veel (efficiency) winst\nbehaald kan worden. Lees er meer over in onze publicatie over\nTransport en Logistiek in Smart cities (hier en \nhier).	30
Bouw	groothandel-hout-bouwmaterialen	trend	Digitale dienstverlening	De grotere aannemers werken steeds meer met integrale digitale\nmodellen (zoals BIM), waarbij onderdelen direct bij de leverancier\nkunnen worden ingekocht. In navolging van BIM gaat ook de digitale\nshowroom met Virtual Reality en Augmented Reality (VR/AR) een grote\nrol spelen in de oriëntatiefase. De leveranciers die hun producten\ndigitaal op orde hebben, worden gevonden en gezien. Het wordt voor\nde handel in bouwmaterialen steeds uitdagender om relevant te\nblijven. Dienstverlening gaat een steeds belangrijkere rol spelen\nin de onderscheiding. Lees er hier meer\nover.	31
Bouw	groothandel-hout-bouwmaterialen	trend	Wat doet de doe-het-zelver?	Uit onderzoek van ABN AMRO blijkt dat de particuliere\ndoe-het-zelfklusser van tegenwoordig steeds minder zelf doet.\nBouwmarkten hebben dit gemerkt aan de teruglopende omzet. Door\ngebrek aan tijd en vaardigheden bij particulieren, zijn de omzetten\nvan klusbedrijven en groothandels gestegen. De aantrekkende\nwoningmarkt versterkt deze ontwikkeling. Vanwege die grote vraag\nkunnen kosten van klusbedrijven stijgen. Dat kan als gevolg hebben\ndat particulieren toch weer meer zelf gaan klussen met een\nomzetverschuiving naar de bouwmarkten als gevolg. Lees er hier meer\nover.	32
Bouw	groothandel-hout-bouwmaterialen	trend	Omnichannel voor de groothandel	ABN AMRO-onderzoek uit 2014 toont aan dat er voor\ndoe-het-zelvers en de groothandel nog nauwelijks online\nbestelmogelijkheden waren. Anno 2017 is dit wel anders. Vooral de\ndoe-het-zelfhandel is online veel beter te vinden. Niet alleen met\nproducten, maar ook met specificaties en gefilmde\ngebruikshandleidingen voor de vakman en doe-het-zelver. De\nkoppeling van het back-end systeem aan de online bestelmodus maakt\ninzichtelijk of het product op voorraad is. Weer een zorg minder\nvoor de klant. Lees er \nhier meer over.	33
Bouw	hout-bouwmaterialenindustrie	trend	Klantgericht bouwen	Bouwen kan klantgerichter, slimmer, sneller, duurzamer en\ntegelijkertijd beter betaalbaar worden dankzij de innovatiekracht\nvan toeleveranciers. De (hout- en bouwmaterialen)industrie was\nlange tijd vooral producent van een eindproduct, maar schuift\nsteeds verder op naar partner voor co-design, levering, montage en\ngarantie van een totaalproduct.  Extra service en\ndienstverlening gaan tot het standaardpakket behoren; zo komt het\n steeds vaker voor dat een producent het hele geïnstalleerde\nproduct levert in plaats van een bouwpakket. Hiermee gaan ook\nontwerp- en bouwrisico’s geleidelijk over naar de leverancier. Lees\nhier meer.	34
Bouw	hout-bouwmaterialenindustrie	trend	Digitaal produceren	Het assortiment van de producent is niet meer alleen in een folder\nte bekijken, maar ook in een showroom. Steeds vaker is het product\nook digitaal te downloaden,  alle\nspecificaties (materiaal/grondstoffen). Mede door in BIM te werken,\nkan een  ontwerpteam complete bouwdelen intekenen en\nuitwerken. Vervolgens kan  de aannemer de hele order met de\njuiste BIM-applicaties verwerken en doorsturen naar het\ngeautomatiseerde machinepark van de producent. Hiermee wordt de\nproducent ook steeds meer een tailormade-aanbieder. Daarbij kan hij\nopschuiven in de bouwketen (naar voren én naar achter). Lees\ner hier meer over in onze \npublicatie over de industrialisering in de bouw	35
Retail	groothandel-non-food	trend	Nieuwe kansen als ketenregisseur	Groothandels spelen hierop in door de rol van ketenregisseur op\nzich te nemen. Door voor- of achterwaartse integratie met eigen\nafzetkanalen of eigen productie, proberen ze meer grip te krijgen\nop de keten. Groothandels kunnen retailers ontzorgen door extra\ndienstverlening aan te bieden. Bijvoorbeeld met e-fulfilment en\norder (robot)picking. Maar ook door centraal de retouren van\nwebshops te verzorgen.	134
Bouw	hout-bouwmaterialenindustrie	trend	Duurzaam en duurzamer…	De productie van bouwmaterialen is een energie intensieve\nindustrie. De carbon footprint van de  gehele bouwketen wordt\nvoor een belangrijk deel veroorzaakt door de industrie in de\nsector. Het wordt voor bedrijven in de sector steeds belangrijker\nom inzicht te hebben in hun CO2 productie en maatregelen te nemen\nvoor CO2 reductie. Van alle geproduceerde elementen zullen in een\nmateriaalpaspoort de (gerecyclede) grondstoffen bekend zijn. Een\nbelangrijke voorwaarde voor een start van de circulaire energie.\nEen volgende stap in die circulaire economie kan zijn dat de\nbouwmaterialen industrie nieuwe verdienmodellen gaat genereren door\nde ontkoppeling van gebruik en bezit (met andere worden, eigendom\nblijft van haar grondstoffen en producten). Lees \nhier meer over onze ervaringen met circulair bouwen.	36
Bouw	ingenieursbureaus	trend	Verder met verduurzaming	Duurzaamheid is ook voor de bouwsector belangrijker dan ooit. En\nhet gaat niet minder worden. Duurzaamheid gaat zowel over energie,\nCO2 reductie en klimaatverandering als over leefbare steden,\ngezondheid, arbeidsomstandigheden en gebruikscomfort. Op alle\nfronten zijn creatieve ingenieurs en adviseurs nodig om de\nnoodzakelijke impuls te ondersteunen. Duurzaamheid gaat ook over de\ntransitie van een lineaire naar een circulaire economie. Die\ntransitie gaat ook veel vergen én opleveren voor de advies en\ningenieursbureaus. Lees \nhier meer over de circulaire economie.	37
Bouw	ingenieursbureaus	trend	Specialiseren of generaliseren	Steeds meer ingenieursbureaus worden grote, internationale\nspelers die zich richten op grootschalige projecten en/of een\nportefeuillebenadering hanteren. Leading thema’s voor de grote\nNederlandse ingenieursbureaus zijn: design, urban development\n(grootstedelijke ontwikkeling en infra),\nenergietransitie/verduurzaming, waterhuishouding en offshore. De\nmiddelgrote bureaus met ongeveer 100 fte treden vaak op als\nketenpartner op projectniveau met een grote bouwaannemer of met de\nopdrachtgever (publiek en privaat). Vaak hebben deze partijen hun\neigen ingenieursafdelingen ingekrompen of afgestoten, waardoor ze\nafhankelijk zijn van kennisinkoop. Bij voorkeur integraal, bij één\nloket.	38
Bouw	ingenieursbureaus	trend	Verschuiving in de keten, verschuiving in\nverantwoordelijkheid	In een complexere wereld met meer mogelijkheden én risico’s,\nwordt de rol van ingenieursbureaus steeds belangrijker voor\nopdrachtgevers. Zekerheid is voor veel opdrachtgevers essentieel:\n‘better safe than sorry’. Ingenieursbureaus spelen hierop in met\nvergaande ontwikkeling en integratie van hun kennis en kunde. De\ngrotere opdrachtgevers verwachten ook tactisch en strategisch\nadvies. Het verdienmodel gaat steeds vaker van betaling op\nurenbasis naar een fixed fee. Dit biedt de kans om integraal en\nlangjarig betrokken te zijn. Die kansen bevatten ook nieuwe\nverantwoordelijkheden én risico’s voor ingenieurs.	39
Bouw	installatiebedrijven	trend	Personeel, personeel, personeel…	De installatiebedrijven hebben tegelijkertijd meerdere\nuitdagingen: consumentwensen veranderen (abonnementen en gebruik in\nplaats van bezit), de verduurzaming en de energietransitie zetten\nonverminderd door en de technologische ontwikkelingen gaan sneller\ndan ooit. Allemaal mooie kansen en groeiende markten om op in te\nspelen. Een positief perspectief. Maar, waar is na de crisis van de\nafgelopen jaren de monteur met up-to-date kennis, met de juiste\ncommunicatieve en klantgerichte vaardigheden en de tijd om al de\nuitdagingen aan te pakken? De krapte op de arbeidsmarkt is een rem\nop de groei en de mogelijkheden in de sector. Lees er meer over in\nonze \npublicatie.	40
Bouw	installatiebedrijven	trend	Servitization	In de traditionele rol levert de installateur een installatie.\nSteeds vaker hoort daar (langjarig) onderhoud bij. Dit komt onder\nandere vanwege de complexiteit van nieuwe installaties en onze\nafhankelijkheid van die systemen. In de toekomst wordt dat niet\nminder. Er komt meer focus op ‘service’. Het eigendom van de\ninstallaties ligt niet per sé bij de gebruiker; hij wil betalen\nvoor een dienst op het moment dat hij er gebruik van maakt. Voor\ngrootverbruikers zijn ‘service level agreements’\n(prestatiecontracten) en circulair inkopen niet meer weg te denken\nuit de pay per use-economie. Het levert installateurs meer kennis\nvan klanten en klantwensen op. En dat levert meerwaarde. Lees er\nmeer over in onze \npublicatie.	41
Bouw	installatiebedrijven	trend	Veranderende rollen, dus…	Transformatie, renovatie en verduurzaming zijn dé trend. Daarbij\nhoren connectivity, Internet of Things, en data….big predictive\ndata! Middels je gebouwinstallatie altijd en overal overzicht en\ncontrole hebben over prestaties, comfort, veiligheid én kosten: dat\nis de toekomst voor de installatiesector. Het belang en de\nafhankelijkheid van installaties voor duurzaamheid, comfort en\nveiligheid neemt in álle projecten toe. Installateurs krijgen niet\nalleen een belangrijkere positie in de realisatie, maar ook in\nadvies, service en onderhoud. Met zoveel belangen en posities in de\nbouwketen, kan de installateur de hoofdaannemer van morgen\nzijn.	42
Bouw	utiliteitsbouw	trend	Veranderende vraag kantorenmarkt	Kantoren en overheidsgebouwen waren een belangrijk deel van de\nomzet van de utiliteitsbouw. Die omzet is grotendeels weggevallen.\nDe afgelopen jaren, en nu nog, is de transformatie markt wel goed\nop gang gekomen. Hierdoor is het aantal leegstaande kantoren\nafgenomen.  Nu de economie weer groeit, sluit het bestaande\nkantorenaanbod niet meer aan bij de veranderende vraag. Werknemers\nkomen meer centraal te staan, 90 procent van de totale\nkantoorkosten zijn te beschouwen als personeelskosten. Daar kan het\nverschil voor de huurders en gebruikers gemaakt\nworden. Lees meer.	43
Bouw	utiliteitsbouw	trend	Arbeidsmarkt en arbeidsproductiviteit	De crisis heeft grote gevolgen gehad voor de arbeidsmarkt in de\nbouw. Gezien de verwachte groei van de bouwproductie, vooral in\nwoningbouw en duurzame renovatie, zijn op korte termijn meer\nwerknemers nodig. Die schaarste aan personeel heeft impact op de\nplanning en op de kosten. Op de langere termijn krijgt de bouw\nte maken met complexere projecten, andere bouwmethodieken en\nvergrijzing van het personeel.  structurele\nveranderingen als digitalisering, industrialisering, robotisering\nen procesoptimalisatie in de keten hebben invloed op het\npersoneelsbestand. Deze ontwikkelingen gaan  zorgen voor de\nnoodzakelijke verhoging van productiviteit in de \nDat vergt andere werknemers in plaats van meer werknemers. Lees er\nmeer over in onze publicatie.	44
Bouw	utiliteitsbouw	trend	Duurzaamheid en verder…	Energievebruik is jarenlang een maatstaf geweest voor de\nduurzaamheid van een gebouw. En nog steeds, getuige de recente\nregelgeving om bestaande kantoorgebouwen te verplichten in 2023 tot\nenergielabel C gerenoveerd te zijn, en tot energielabel A in 2030.\nDe volgende fase van verduurzaming is de overgang van een lineaire\nnaar een circulaire economie. In het huidige lineaire systeem\nworden grondstoffen omgezet in producten die aan het einde van hun\nlevensduur worden vernietigd (take, make, waste). De circulaire\neconomie is een economisch systeem dat bedoeld is om\nherbruikbaarheid van producten en grondstoffen te maximaliseren en\nwaarde vernietiging te minimaliseren (reduce, reuse, recycle). Als\nABN Amro zijn we al op weg naar die toekomst en realiseren we\nmomenteel een paviljoen dat maximaal inzet op de principes van de\ncirculaire economie. Lees hier en \nhier meer over de verduurzamingsmogelijkheden en onze\ncirculaire expertise	45
Bouw	woningbouw	trend	Arbeidsmarkt en arbeidsproductiviteit	De crisis heeft grote gevolgen gehad voor de arbeidsmarkt in de\nbouw. Gezien de verwachte groei van de bouwproductie, vooral in de\nwoningbouw en duurzame renovatie, zijn op korte termijn meer\nwerknemers nodig. Die schaarste aan personeel heeft impact op de\nplanning en op de kosten. Op de langere termijn krijgt de bouw\nte maken met complexere projecten, andere bouwmethodieken en\nvergrijzing van het personeel.  structurele\nveranderingen als digitalisering, industrialisering, robotisering\nen procesoptimalisatie in de keten hebben invloed op het\npersoneelsbestand. Deze ontwikkelingen gaan  zorgen voor de\nnoodzakelijke verhoging van productiviteit in de \nDat vergt andere werknemers in plaats van meer werknemers. Lees er\nmeer over in onze publicatie.	46
Bouw	woningbouw	trend	Meer stedelijk wonen, maar dan anders	De behoefte aan nieuwe woningen is gigantisch: ruim één miljoen\nin de periode tot 2030. Een groot deel daarvan moet in de steden\nkomen. Gezien de markt en de doelgroep in die steden is er behoefte\naan andere woonproducten. Het park is je tuin, het café je\nwerkplek,  Airbnb biedt die extra\nlogeerkamer en als je al met auto gaat, is die van SnappCar of\nBlaBlaCar De prijsontwikkeling en de ‘deeleconomie’ hebben grote\nimpact op het wonen in de stad.  Dat resulteert in kleinere\nwooneenheden met een grote diversiteit; van mobiele, tijdelijke\ntiny houses voor de stadsnomade tot high tech-micro appartementen\nmet robo-furniture voor de millenials.	47
Bouw	woningbouw	trend	Investeer in duurzaamheid	Om de doelstellingen uit het Energieakkoord te halen wordt een\nenergielabel C per 2023 verplicht gesteld voor kantoren (gevolgd\ndoor een energielabel A per 2030). De bestaande woningvoorraad is\nveel groter dan de bestaande kantoorvoorraad.  Alleen al\ndaarom kan zo’n kantoormaatregel  op de bestaande\nwoningvoorraad een enorme impact hebben. Hier schuilt een immense\nkans voor de verduurzaming van Nederland. Een kans die alleen maar\nwinnaars oplevert. Want een energie neutrale woning heeft veel\nvoordelen. Niet alleen een hele lage CO2 uitstoot maar ook een hele\nlage energierekening én een hogere vastgoedwaarde.  Met de\nhuidige lage rentestand, is de terugverdientijd ook een stuk\nkorter. Investeer daarom nu in duurzaamheid. Lees er \nhier en \nhier meer over.	48
Food	agf-industrie	trend	Kookgemak in de professionele keuken	De buitenhuisconsumptie groeit harder dan de thuisconsumptie, en\ndaarmee neemt in de professionele keuken ook de behoefte aan gemak\ntoe. Groenten vervangen steeds vaker een deel van het vlees, zeker\nals ze creatief zijn bereid. Dit heeft veel te maken met hun\nduurzame en gezonde karakter. Ook maatschappelijk gezien heeft\n‘groen’ de wind dus mee. Partijen in de AGF-handel en -verwerking\nkunnen waarde toevoegen door hun afnemers te ontzorgen.\nBijvoorbeeld met bewerkte AGF in kleinere, handzaam verpakte\nporties. In de foodservice zorgen deze voor tijdwinst en garanderen\nze constante kwaliteit. Denk ook aan verrassende AGF-menusuggesties\nals het gaat om smaak, herkomst of verschijningsvorm.\n 	49
Food	agf-industrie	trend	Schaalvergroting zet door	De prijs van onbewerkte producten stond de laatste jaren onder\ndruk en hangt steeds meer af van ontwikkelingen op de wereldmarkt.\nSchaalvergroting lijkt hierop een belangrijk antwoord. Dit zien we\ndan ook terug tussen alle schakels van de AGF-keten: achterwaarts,\nvoorwaarts en bij partijen met dezelfde functie. Eisen aan\nkwaliteit of duurzaamheid (biologisch) die consument en retailer\nstellen, dwingen de sector om meer te focussen op oorsprong en\nbetrouwbare aanvoer. Dat wil zeggen: genoeg en van superieure\nkwaliteit. En dan is er nog de relatie tussen consument en boer,\ndie elkaar steeds vaker opzoeken. Deze directe ontmoetingen\nstimuleren transparantie en zetten vraagtekens bij de toegevoegde\nwaarde van sommige tussenschakels. Kortere ketens, langjarige\nrelaties en de afzet van een breed productpakket bepalen in\ntoenemende mate de rentabiliteit van bedrijven.	50
Food	agf-industrie	trend	Flexibel datagebruik	Voor AGF-verwerkers betekent ‘waarde toevoegen’ steeds meer\ndata driven zijn. En die data ook flexibel gebruiken. Ze\nmoeten de retailer dus niet alleen bijstaan met betrouwbare en\ngeverifieerde track & trace-instrumenten, maar ook\nklaarstaan als de consument met zijn smartphone daadwerkelijk\nQR-codes op verpakkingen gaat scannen en de boer wil ‘zien’.\nBereiders kunnen op hun beurt via data analytics steeds\nbeter voorspellen welke maaltijden beter verkopen tijdens een\nzonnige of juist regenachtige dag. Zo grijpt de consument dus nooit\nmis. Bovendien gaat het verspilling in de supermarkt tegen.\nAGF blijft voor Europese retailers een zeer belangrijke\ncategorie. Door de hoge marges, maar ook vanuit maatschappelijk\noogpunt: gezond doet het namelijk goed. Toegankelijke,\nmakkelijke en lekkere AGF-producten versterken het duurzame\nkarakter van foodretailers.	51
Food	brood-deegwarenindustrie	trend	Veranderende vraag dwingt tot\nflexibiliteit	In de afgelopen jaren is er minder brood gegeten. Belangrijke\noorzaken hiervan zijn de populariteit van alternatieve\nontbijtproducten en gezondheidsvragen van consumenten rond brood.\nZe eten wel brood, maar:\n– minder vaak\n– op andere momenten en plaatsen (buitenshuis/onderweg)\n– gevarieerder (luxere soorten)\nDit dwingt industriële broodbakkerijen tot innovatie en de\ndaarbij horende flexibele  productiecapaciteit. Alleen dan\nkunnen ze efficiënt meerdere soorten brood maken en snel inspelen\nop nieuwe trends. Samengevat: industriële bakkers kunnen zich\nspiegelen aan een veranderende markt met meer focus op\nbroodconsumptie buitenshuis.	52
Food	brood-deegwarenindustrie	trend	Gezondheidstrend houdt aan	Ook de komende jaren blijft het thema ‘gezondheid’ het aanbod\nvan brood, banket en koek beïnvloeden. Minder suiker, vet, zout en\ntoevoegingen: het blijft een speerpunt voor de sector. Dit komt\nvoornamelijk doordat consumenten steeds bewuster met eten bezig\nzijn. In de samenstelling van hun voedsel zoeken ze naar ‘speciale’\nproducten, waardoor ook het aanbod van ‘verantwoorde’ deegwaren\ntoeneemt. De branche toont zelf initiatief; een campagne moet het\nimago van brood verbeteren. Mogelijk helpt dat, maar het beste\nantwoord blijft vooruitlopen op het veranderende eetgedrag van de\nconsument. Dat wil zeggen: innoveren op productniveau en\nanticiperen op de plekken waar hij zijn eten koopt.	53
Food	brood-deegwarenindustrie	trend	Innovatie essentieel binnen strategische\npartnerships	Supermarkten verkopen zo’n 70 procent van alle brood- en\ndeegwaren. Retailers kunnen zich ermee onderscheiden op\nassortiment, beleving en kwaliteit. Dit maakt deze categorie tot\neen belangrijk loyaliteitsinstrument. Klanten verwachten, versheid,\nkeuze én kwaliteit. In deze sterk concurrerende markt zoeken\nretailers – samen met leveranciers – daarom constant naar\ninnovatieve producten om een voorsprong te creëren. Dit leidt tot\nexclusieve, vaak langdurige samenwerking tussen beiden. Het belang\nvan efficiëntie en een streven naar schaalvergroting aan\ninkoopzijde blijven allicht belangrijk. Maar ook een proactieve\nhouding van bakkerijen als het gaat om productontwikkeling\nverstevigt hun band met retailers.	54
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	trend	Digitalisering van standaarddiensten	Door diensten geheel of gedeeltelijk online aan te bieden, wordt\nhet incasso- of gerechtelijk traject versoepeld en\ngestandaardiseerd. Dit kan variëren van online klantdossiers\ninzien, tot zogeheten ‘Online Dispute Resolution’ waarmee\ngeschillen buiten de rechter om kunnen worden opgelost. \nLees meer.	202
Food	drankenindustrie	trend	De weg naar het schap: innovatie en meer\nklantkennis	Voor zowel private label- als merkfabrikanten wordt adviseren en\ninnoveren belangrijker om schapruimte veilig te stellen. Retailers\nverwachten steeds meer proactiviteit van hun leveranciers. De\nconsumptie van frisdranken en vruchtsappen staat onder druk,\nterwijl producten die gezond zijn (en dit uitstralen op assortiment\nof formule) aan waarde winnen.\nDe gewenste reactie hierop is proactieve innovatie, soms\nexclusief voor een bepaalde retailer. Innovatie is ook het\nbelangrijkste wapen om het belang van promoties te verkleinen. Zo\nbrouwen sommige grote bierbrouwers ongefilterd pils en verkopen ze\ndit in luxere verpakkingen. Hiermee spelen ze ‘groots’ in op de\nvraag naar ambachtelijk speciaalbier.	55
Food	drankenindustrie	trend	Schaalvergroting zet door	Ook vorig jaar waren er acquisities. Naast schaalvergroting of\neen breder productportfolio, waren dit de voornaamste beweegredenen\nhiervoor:\n-kostprijsvoordeel\n-toegang tot nieuwe (internationale) afzetkanalen\n-nieuwe producten en kennis voor een gedifferentieerd\nproductaanbod\nHet aandeel van private labels zit in heel Europa in de knel,\nmede door promotiedruk van\nA-merken. Het is nu eenmaal lastig om én goedkoper te produceren én\nmaximaal te innoveren. Deze spagaat stimuleert de trend waarbij\nmerkfabrikanten hun productie bij private labels onderbrengen. Die\nbeschikken immers over een efficiënt productieproces en feilloze\nlogistiek (co-packaging).	56
Food	drankenindustrie	trend	Duurzaamheid domineert agenda, proactiviteit\nloont	Of het nu gaat om minder alcoholgebruik of suiker in frisdrank:\nduurzaamheid blijft ook voor de internationale drankenindustrie hét\nthema. De frisdrankbranche zet collectief stappen om ruim 10\nprocent minder suiker en calorieën in hun producten te doen.\nBijvoorbeeld door middel van suikervervangers of kleinere\nverpakkingen.\nPrivate label- en merkfabrikanten die niet afwachten, zijn in\ntrek bij retailers. Zij leggen latente behoeftes bloot en reageren\nproactief op veranderende consumptiepatronen. Daarnaast adviseren\nze over de nieuwste trends. Zo creëren ze onderscheidende formules\nen bezorgen ze drankencategorieën een duurzame uitstraling.	57
Food	groothandel-in-voedingsmiddelen	trend	Ook foodservicegroothandel wordt\ndatagedreven	De foodservicegroothandel kan steeds beter waarde toevoegen met\nbestelgemak en inspiratie, beide online. Ook op maat gemaakte\nmenusuggesties doen het goed. Zo wordt het bedrijfsmodel van de\ngroothandel steeds meer datagedreven, met een focus op ontzorgen.\nDe volgende stap is kennis en data in concrete adviezen vertalen,\nom mee te bouwen aan foodserviceconcepten die snel zijn aan te\npassen aan het veranderend consumentengedrag. Op termijn zou –\nnaast geleverde producten – tarifering van geleverde diensten een\nnieuw element van het verdienmodel kunnen worden.\n 	58
Food	groothandel-in-voedingsmiddelen	trend	Geen dozen schuiven, maar kennis delen	Dat de consumptie buitenshuis aantrekt en we meer aan voeding\nuitgeven, maskeert deels de structurele problemen bij\nfoodservicegroothandels zonder onderscheidende propositie. Alleen\nvoorraad aanhouden, op prijs concurreren en vracht van a naar b\nrijden, zijn functies die eenvoudig kunnen verdwijnen. Ze maken\ndeze bedrijven kwetsbaar voor een faillissement of overname. Dit\nwakkert consolidatie in het groothandel-landschap verder aan.\nOndernemingen die over de keten heen kijken, hebben het gunstigste\ntoekomstperspectief. Zij kennen en begrijpen de veranderingen bij\nde klant van de klant, en kunnen voorspellen welke nieuwe segmenten\ner ontstaan. Deze kennis delen ze actief met hun afnemers.	59
Food	groothandel-in-voedingsmiddelen	trend	Scenarioplanning: een must voor internationale\ngroothandel	Betrouwbaarheid, kwaliteit en voedselveiligheid zijn nog steeds\nbelangrijke pijlers voor Nederland als exportland. Toch leggen de\nboycot vanuit Rusland en de Brexit onze risico’s pijnlijk bloot.\nInternationaal georiënteerde handelsbedrijven – bijvoorbeeld in AGF\n– zijn steeds meer overgeleverd aan geopolitieke ontwikkelingen,\nprijs-/valutaschommelingen en exportbeperkingen. Om deze risico’s\nte spreiden, is het van belang om proactief uit te kijken naar\nalternatieve afzetmarkten. Ook al lever je hier niet direct (grote\nvolumes) aan (, toch is de opbouw van kennis en een netwerk op dit\npunt essentieel. Scenarioplanning, langetermijnvisie, snelle\nwendbaarheid en zowel risico’s als kansen in kaart brengen: deze\nzaken bieden het beste toekomstperspectief.	60
Food	visindustrie	trend	Vaker vis? Alleen met innovatie	Het blijft een uitdaging om de Nederlandse visconsumptie verder\nop te krikken. Kijk je door een Europese bril, dan eten we relatief\nweinig vis. Onze vangst gaat veelal de grens over, inclusief het\ngrote aandeel schol en tong. Visproducten kunnen nog nadrukkelijker\nworden gepositioneerd als alternatief voor vlees.\nRetailers blijven op zoek naar aantrekkelijke producten in het\nvisschap. Ook al is het nog op bescheiden schaal, steeds meer\nsupermarkten introduceren speciale counters waar klanten\npersoonlijk advies krijgen over de aankoop en bereiding van verse\nvis. Dergelijke initiatieven tillen de totale beleving van vis als\nproductgroep naar een hoger plan.\nDe sector kan zichzelf ook helpen. Door onderscheidende,\ngemakkelijke en aantrekkelijk ogende  producten en concepten\nte ontwikkelen. Op alle fronten: van verpakking tot duurzaamheid en\nbereidingsgemak; ook voor professionele keukens. Denk aan kleinere,\nhandzame porties – of producten die ook minder ervaren personeel\nkan bereiden.\n 	61
Food	visindustrie	trend	Groeiende vraag naar eiwitrijk voedsel	Een groeiende wereldbevolking en meer welvaart stimuleren de\nvraag naar betaalbare, kwalitatief hoogwaardige eiwitten. Vis\nspeelt hierin een steeds belangrijkere rol. De visconsumptie stijgt\ndan ook, vooral in de niet-westerse wereld. In minder ontwikkelde\nlanden is vis zelfs de belangrijkste bron van dierlijk eiwit.\nGekweekte vis heeft hierin een groeiend aandeel. Om van deze trend\nte profiteren, kan de Nederlandse vissector nog meer gebruikmaken\nvan zijn reputatie en omvang. We staan bekend als leverancier van\nkwalitatief hoogwaardige voedingsmiddelen. Toch zullen Nederlandse\nvisbedrijven ook moeten focussen op producten met een hoge\ntoegevoegde waarde voor de binnenlandse markt.\n 	62
Food	visindustrie	trend	Duurzaamheid is key	Behalve als gezond alternatief voor vlees, is vis ook gebaat bij\neen duurzaam imago. De consument weegt klimatologische en\necologische impact steeds vaker mee in zijn aankopen. Terecht of\nniet, negatieve berichtgeving-hebben het imago van vis niet altijd\ngoed gedaan.\nRetailers stellen dan ook steeds hogere eisen. Gekweekt of\ngevangen, vis moet traceerbaar en duurzaam zijn. Keurmerken als MSC\nen ASC werken kostprijsverhogend, maar zijn tegelijkertijd steeds\nvaker een voorwaarde om aan de retail te mogen leveren. De twee\nbelangrijkste manieren om traceer- en duurzaamheid te realiseren,\nzijn:\n-nauwe samenwerking in de (mondiale) aanvoerketen\n-ontwikkeling van nieuwe visconcepten\nVooral het tweede punt biedt leveranciers kansen, waarbij\ninnovatie de consument meer en gedetailleerder inzicht geeft.	63
Retail	woonwinkels	trend	Slimme inzet van innovatie	Augmented reality geeft consumenten in de voorfase van het\noriëntatieproces de kans om meubilair te ‘testen’ in hun eigen\nomgeving. Hierbij worden ruimtes in huis verrijkt met virtuele\nproductbeelden, zodat de klant een goed beeld krijgt of het\nmeubelstuk past. Dit past uitstekend bij de groeiende behoefte van\nde klant aan inspiratie\nop het gebied van wooninterieur. De mogelijkheden van augmented\nreality in retail zijn nog maar in de beginfase.	146
Food	vleesindustrie	trend	Differentiatie, verduurzaming of kennisexport:\nketensamenwerking is key	Door consumentenvoorkeuren, supermarkten, ngo’s en regelgeving\nkomt de duurzame lat in onze vleesketens steeds hoger te liggen.\nNaast dierenwelzijn, speelt ook klimaatimpact\n(CO2–footprint) een grotere rol. Dit biedt de\nkomende jaren kansen voor differentiatie in concepten. Wel moeten\nvraag en aanbod dan (nog) intensiever op elkaar worden afgestemd in\nopeenvolgende ketenschakels: van vermeerdering tot verwerking en\ntransport. Wie niet voor de wereldmarkt produceert (focus op\nefficiency) en wil groeien, moet met ketenpartners aan de slag om\nvleesconcepten verder te verduurzamen. Binnen Europese deelmarkten\nliggen kansen om onze kennis over bovenwettelijke vleesconcepten te\nvermarkten.\n 	64
Food	vleesindustrie	trend	Meer focus op foodservice en\nvoedingsmiddelenindustrie	In veel landen groeit de consumptie buitenshuis harder dan de\nthuisconsumptie. Dit komt vooral doordat:\n– onze koopkracht is gestegen;\n– met name jongeren meer buiten de deur eten en \ndrinken;\n– hier meer locaties voor zijn gekomen.\nOok vleeswerkers profiteren hiervan. Met name als het gaat om\nsysteemgastronomie: bewerkte producten, gericht op\nkookgemak bij industriële gebruikers en in de professionele keuken.\nBij productontwikkeling zullen verwerkers dus meer als een kok\nmoeten gaan denken. En begrijpen hoe binnen foodservice de focus\nverschuift richting gemak, duurzaamheid en ‘ultravers’.	65
Food	vleesindustrie	trend	Groeikansen voor efficiëntere ketens, zeker in	Azië\nIn heel West-Europa stagneert de vleesconsumptie, vooral door\nzorgen over vermeende gezondheidsrisico’s, dierenwelzijn en\nklimaatimpact. Wereldwijd ligt dat anders. Buiten Europa stijgen de\nmiddeninkomens, waardoor er de komende tien jaar meer behoefte aan\nhoogwaardige proteïne ontstaat, onder andere uit vlees. Dit geldt\nvooral voor Azië. Deze ontwikkeling vraagt om een sterke focus op\nkostprijs. En daarmee om constante verbetering van de\ntoeleveringsketen op het gebied van efficiency, schaal en\nproductiviteit. Pluimveevlees is van nature goedkoper. Vanwege de\nlage CO2–footprint, en doordat bij de\nconsumptie religieuze bezwaren een beperkte rol spelen. Kijk je\nnaar uitvoervolumes, dan heeft dit vlees een goede uitgangspositie\nvoor export. Geopolitieke ontwikkelingen dwingen\nexportondernemingen wel om meer aandacht te besteden aan\nscenarioplanning. Ook kunnen ze hun kennis over de brede\ndiversiteit aan wereldmarkten proactief verdiepen.	66
Food	zuivelindustrie	trend	Fosfaatplafond: uitdaging voor hele keten	Vanwege de Nederlandse overschrijding van het fosfaatplafond en\nde daardoor ingezette inkrimping van de veestapel ziet het plaatje\ner voor de hele zuivelketen even wat anders uit . Door de\nafschaffing van het melkquotum waren veel investeringen de\nafgelopen jaren gericht op een groeiend aanbod. Nu die melkstroom\nafneemt, zal de zuivelindustrie scherper moeten kijken naar hoe je\nmelk kunt verwaarden. Waar ligt nu de grootste toegevoegde waarde,\nen de winst? Kleine zuivelproducenten kiezen voor ambachtelijkheid\nen grijpen terug op oude recepten. Ook wordt er meer op\nduurzaamheid gefocust. Dat blijkt bijvoorbeeld uit de aandacht voor\nweidegang, en het vermarkten van gedifferentieerde producten die\nhiervan zijn afgeleid.	67
Food	zuivelindustrie	trend	Mondiale vraag naar hoogwaardig eiwit blijft\ngroeimotor	De wereldbevolking groeit, net als de mondiale welvaart. Dit\nmaakt producten met kwalitatief hoogwaardige eiwitten – waaronder\nzuivel – ook de komende jaren een belangrijke groeimotor voor de\nindustrie. De Nederlandse zuivelsector is van nature exportgericht,\nen dus sterk afhankelijk van geopolitieke ontwikkelingen en\ninternationale economische trends. Onmiskenbare voorbeelden: de\nRussische voedselboycot, vraaguitval in China en het grote mondiale\naanbod aan melkproducten. Na deze gebeurtenissen zijn de markten\ninmiddels iets bijgedraaid, en ook de internationale afzet weer in\nbelang zal toenemen.  Wil de zuivelindustrie zich niet laten\novervallen door grillige exportontwikkelingen, dan is\nscenarioplanning vereist en zal zij actief op zoek moeten blijven\nnaar (niche)markten.	68
Food	zuivelindustrie	trend	Internationale samenwerking en\nkennisexport	Om minder afhankelijk van import te zijn, koersen steeds meer\nlanden – zoals China – richting zelfvoorzienendheid. Dit doen ze\nonder andere door samen te werken met westerse zuivelbedrijven, of\ndeze over te nemen. Zo krijgen ze meer grip op de mondiale\nzuivelstromen. Daarnaast investeren ze fors in de ontwikkeling van\nde eigen melkveehouderij en zuivelverwerkende industrie. Nederland\nis een vooraanstaand zuivelland; de Nederlandse zuivelindustrie kan\nwaarde toevoegen door onze vergevorderde expertise en technologie\nte exporteren. Dit gebeurt al,  kijkende naar het relatief\ngrote aantal studenten van buiten de EU dat ‘kennis tankt’ aan\nWageningen University & Research.	69
Healthcare	curatieve-zorg	trend	Zorg op afstand	Een deel van de zorg voor en na de daadwerkelijke behandeling,\nzal buiten het ziekenhuis plaatsvinden. Enerzijds door andere\nzorgverleners anderzijds door de patiënt zelf met behulp van\ne-health toepassingen. Dit heeft diverse voordelen. De patiënt kan\nook vanuit huis vragen aan de medisch specialist of de verzorgen\nstellen; en door e-health toepassingen is er meer inzicht in de\ngezondheid van de patiënt, zowel bij de patient als bij de\nzorgverleners. Therapie- of medicatietrouw is een belangrijke\npotentiële verbetering door zorg op afstand. Zij kan resulteren in\neen grote verbetering van de gezondheid.	70
Healthcare	curatieve-zorg	trend	Strategische allianties	Goede samenwerking in de regio wordt steeds belangrijker. Niet\nalleen om als instelling goed op de ingreep zelf te kunnen\nfocussen, maar ook om de voor- en nazorg door andere partijen te\nkunnen laten leveren. Het netwerk wordt steeds belangrijker; zowel\nde relatie met andere zorgverleners als die met andere\nvakgroepen.\nDat laatste is het gevolg van een ontwikkeling die twee kanten\nop gaat. Enerzijds komen er steeds meer generalisten om de algemeen\nkwetsbare oudere binnen en buiten het ziekenhuis zo goed mogelijk\nte kunnen ondersteunen. Anderzijds ontstaan er door toegenomen\nkennis en voortschrijdende techniek steeds meer superspecialismen,\nwaardoor er binnen vakgroepen (ook binnen de regio) gewerkt wordt\naan de verdeling van taken.\nEen fusie is hiervoor niet vereist. Een strategische alliantie\nis een goede samenwerkingsvorm waarbij elke organisatie haar\nzelfstandigheid bewaart, en de focus kan leggen op de eigen\nexpertise.	71
Healthcare	curatieve-zorg	trend	Vormgeven aan duurzaamheid	In de zorg ligt de focus op de mens en niet op de middelen.\nDaarmee is grondstoffenduurzaamheid een gebied dat tot nu toe\nminder aandacht kreeg. Ook de zorg zal zich steeds meer focussen op\nvermindering van het gebruik van grondstoffen en daarop afgerekend\nworden. Dat kan op diverse manieren. Denk aan een andere manier van\nhet omgaan met voeding of aan het gebruik van apparatuur in\ndeeltijd.\nBij het ontwerpen van gebouwen is al wel een toenemende focus op\nduurzaamheid te zien. Zowel het mogelijk hergebruik van materialen\ndie nu als afval beschouwd worden, als het gebruik van hernieuwbare\nenergiebronnen in de vorm van zonnepanelen en\nwarmte-koudeopslaginstallaties neemt in aantal toe.	72
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	trend	Waardepropositie van deurwaarders staat onder druk	Griffierechten blijven toenemen. Dit maakt de diensten van een\ngerechtsdeurwaarder duurder en daarmee minder aantrekkelijk.\nLees ook:	203
Healthcare	langdurige-zorg	trend	Samenwerken met andere zorgdomeinen	Instellingen gaan zich steeds meer organiseren in een netwerk\nvan zorgverleners. Daarmee worden ze een onderdeel van de diverse\nmogelijkheden die de burger heeft om met behulp van ondersteuning\nhet leven zo lang mogelijk zelfstandig te kunnen leven. Door\nsamenwerking met huisartsen, revalidatie-instellingen, thuiszorg,\nwijkverpleging en ziekenhuizen kan de langdurigezorginstelling zich\nfocussen op de intramurale zorg, waarbij de burger passende\nondersteuning krijgt.	73
Healthcare	langdurige-zorg	trend	Tijdelijke intramurale zorg	Doordat mensen die zorg nodig hebben langer thuis blijven wonen,\ndoen zich daar ook meer incidenten voor waarna zij in sommige\ngevallen tijdelijk niet meer thuis kunnen wonen. In 2016 heeft dit\ntot overbelasting van de spoedeisende hulpposten van de\nziekenhuizen geleid. In 2017 heeft er een forse uitbreiding\nplaatsgevonden van het aantal ‘huisartsenbedden’ zoals de\ntijdelijke opvang nu wordt genoemd. Dit aantal zal in de toekomst\nverder toenemen. Binnen instellingen in de langdurige zorg zullen\nafdelingen ontstaan met tijdelijke intramurale zorg.	74
Healthcare	langdurige-zorg	trend	Vormgeven aan duurzaamheid	Duurzaamheid is ook voor de langdurigezorgsector van toenemend\nbelang. Duurzaamheid gaat een volgende fase in nu er meer en meer\nvoorbeelden zijn dat we van een consumptieve, lineaire economie\novergaan naar een circulaire. In de langdurige zorg is duurzaamheid\neen combinatie van meerdere factoren, waarbij duurzame huisvesting,\ngepaste voeding en duurzame inzetbaarheid van de medewerkers de\nbelangrijkste zijn.	75
Industrie	basismetaalindustrie	trend	Focus op operationele efficiency 	De metaalprijzen staan onder druk, energie is in West-Europa\nrelatief duur en de kapitaalinvesteringen in de branche zijn hoog.\nZolang er wereldwijd geen level playing field is, moeten\nbedrijven in de Nederlandse basismetaalindustrie zich specialiseren\nen hun kosten zo veel mogelijk drukken met efficiëntere\nproductieprocessen. Ook de bezettingsgraad van de fabriek moet\nomhoog. De marges worden hierdoor groter, maar er ontstaat ook\nkwetsbaarheid doordat de productieprocessen minder flexibel\nworden.	76
Industrie	basismetaalindustrie	trend	Druk op verlaging milieu-impact	Reductie van energie- en grondstofgebruik wordt ook\nmaatschappelijk steeds belangrijker. Internationale wet- en\nregelgeving wordt strenger en de consument laat meer van zich\nhoren. De productie moet schoner, met minder effect op milieu en\nleefomgeving. In 2005 zijn de Nederlandse metallurgische industrie\nen gieterijen al gestart met een gezamenlijk initiatief om de\nenergie-efficiëntie in 2030 met 50 procent te verbeteren. Doel: de\nconcurrentiepositie én het imago van de branche opschroeven.	77
Industrie	basismetaalindustrie	trend	Productinnovatie voor aansluiting bij\neindmarkten	De afzetmarkten voor de basismetaalindustrie veranderen snel.\nBijvoorbeeld in de auto- en transportmiddelenindustrie, machinebouw\nen verpakkingsindustrie vinden veel technologische innovaties\nplaats. Deze markten kijken constant naar het product en de\nmaterialen waarvan het gemaakt is. Steeds vaker worden\nalternatieven voor metaal overwogen. Door te investeren in nieuwe\nlegeringen en betere materiaaleigenschappen, kan de branche de\naansluiting bij haar eindmarkten behouden. Ook de hoge\nrecyclebaarheid van metalen kan hiervoor worden ingezet.	78
Industrie	chemische-industrie	trend	Chemie voorloper in Smart Industry	De chemie en voedingsmiddelenindustrie plukken als eerste de\nvruchten van slimme technologie en software. Door slimme sensoren\nte gebruiken, processen in de hele keten aan elkaar te koppelen en\nBig Data-analyes uit te voeren, kunnen chemiebedrijven hun\nproductieprocessen verder optimaliseren en voorsorteren naar\nvoorspelbaar onderhoud (predictive of condition based\nmaintenance) en onderhoud op afstand (remote\nmaintenance). Tegelijk brengen de nieuwe technologieën de kans\nop menselijke fouten in het productieproces omlaag. \nLees meer.	79
Industrie	chemische-industrie	trend	Van bio-afbreekbare naar herbruikbare chemie en materialen	Door de veranderende kijk op duurzaamheid en de opkomst van de\ncirculaire economie, groeit de markt voor biogebaseerde chemie en\nmaterialen. Afbreekbaarheid is niet langer het streven; de nadruk\nligt op herbruikbaarheid en spaarzaam omgaan met fossiele\ngrondstoffen. Naar verwachting kan de nieuwe generatie\nbiokunststoffen (drop-ins) rekenen op een hoge\nmarktacceptatie; ze zijn 100 procent herbruikbaar en machinaal\nprobleemloos te verwerken. Met een hogere olieprijs in aantocht\nkunnen biogebaseerde chemie en biokunststoffen straks ook op kosten\nconcurreren met fossiele grondstoffen. \nLees meer.	80
Industrie	chemische-industrie	trend	Nederlandse investeringen in biogebaseerde chemie lopen\nachter	Brancheorganisatie European Bioplastics voorspelt dat de\nwereldwijde productiecapaciteit van biokunststoffen zal toenemen\nvan 1,7 miljoen ton in 2014 tot zo’n 7,8 miljoen ton in 2019. Vanaf\n2017  versnelt de groei naar verwachting enorm. Grote\nbedrijven lopen voorop. IKEA wil bijvoorbeeld dat alle kunststoffen\nin zijn producten in 2020 voor 100 procent uit gerecyclde\ngrondstoffen of biomassa bestaan. De Nederlandse chemie moet wel\naan de bak. De Topsector streeft naar 15 procent biobased en 10\nprocent gerecyclede grondstoffen in 2030. Maar de meeste\nbio-investeringen vinden nu nog buiten Europa plaats.	81
Industrie	elektro-en-technische-apparatenindustrie	trend	Fabrikanten verschuiven naar service, toeleveranciers\nnaar modules en producten	Fabrikanten halen steeds meer omzet uit dienstverlening en\nminder uit traditionele machine- en apparatenverkoop\n(Servitization). Service is niet langer een kostenpost,\nmaar een kans om afnemers beter van dienst te zijn en extra omzet\nte genereren. Lees\nhier meer over Servitization.\nVan toeleveranciers wordt verwacht dat ze complete producten of\nmodules kunnen maken (Productization). Wat competenties\nbetreft, schuiven zij dichter naar het oem’erschap\ntoe. Lees\nhier meer over productization.	82
Industrie	elektro-en-technische-apparatenindustrie	trend	Internet of Things verbindt alle\napparaten	Internet of Things (IoT) is in de industrie aan een opmars\nbezig. Zowel productiemachines als producten staan steeds vaker met\nelkaar in verbinding. De industrie gebruikt IoT vooral om de\nefficiency van processen te verhogen en daarmee kosten te verlagen.\nMaar het is ook een middel om nieuwe, onderscheidende diensten te\nverkopen. Met nieuwe services als onderhoud-op-afstand,\nvoorspelbaar onderhoud en pay-per-use kunnen fabrikanten\nhun toegevoegde waarde vergroten en afnemers verder ontzorgen.\nLees meer.	83
Industrie	elektro-en-technische-apparatenindustrie	trend	Vergroting internationale eindmarkten	Naast een uitstekende positie in Nederland, hebben bedrijven in\nde branche vaak een sterke positie in een internationale\nnichemarkt. De verschuiving naar het buitenland zet steeds verder\ndoor. Een logische ontwikkeling, want door snelle technologische\nontwikkelingen en veranderende klantwensen nemen de kosten voor\nR&D toe. Alleen in een groeiende internationale afzetmarkt zijn\ndeze toenemende investeringen terug te verdienen.	84
Industrie	machine-industrie	trend	De uitdaging van ‘standaard-maatwerk’	Machinebouwers staan voor de constante uitdaging om efficiënt te\nwerken én maatwerk te leveren. Door machines modulair te\nontwikkelen, ontstaat een vorm van ‘standaard maatwerk’. Maar dat\nvraagt wel meer van toeleveranciers. In plaats van onderdelen,\nmoeten zij complete producten of modules kunnen maken en\nassembleren. Als Original Module Manufacturer werken ze\nsamen met de machinebouwer aan de product roadmap. Zo\nontstaat een hechte relatie en wederzijdse afhankelijkheid.\nLees meer.	85
Industrie	machine-industrie	trend	Servitization: van product naar service	Machinebouwers halen steeds meer omzet uit dienstverlening en\nminder uit traditionele verkoop. Service is niet langer een\nkostenpost, maar een mogelijkheid om afnemers beter van dienst te\nzijn en extra omzet te genereren. Diensten als onderhoud-op-afstand\nen voorspelbaar onderhoud zijn hier voorbeelden van. Verhuur, lease\nen pay-per-use zijn verdienmodellen die zich op service\nconcentreren. Afnemers betalen per maand of draaiuur en onderhoud\nzit bij de prijs inbegrepen. Hiermee kunnen machinebouwers een\nlock-in met hun afnemers creëren. Lees\nmeer.	86
Industrie	machine-industrie	trend	Internet of Things verbindt alle\napparaten	‘Smart Industry’ is de verzamelnaam voor robotisering,\n3D-printing en Internet of Things (IoT): alle drie zijn in opmars.\nWaar robots en 3D-printers steeds meer worden ingezet, wordt IoT\nvaak nog beperkt gebruikt voor efficiency-verhoging en\nkostenverlaging. Maar IoT is ook een middel om nieuwe,\nonderscheidende diensten te verkopen aan afnemers. Naast een\nopen source-interface die communicatie tussen machines van\nverschillende merken mogelijk maakt, moeten machinebouwers ook\ninvesteren in sensoren en software die het machinegebruik door\nklanten in kaart brengen. \nLees meer.	87
Industrie	metaalproductenindustrie	trend	Productization: van onderdelen naar producten	Machinebouwers ontwikkelen steeds meer modulair om hun klanten\nefficiënt te kunnen blijven bedienen. Voor deze vorm van ‘standaard\nmaatwerk’ wordt meer van de metaalketen verwacht. Grote verspaners\nen plaatbewerkers moeten bijvoorbeeld complete producten of modules\nkunnen maken, in plaats van losse onderdelen. Hiermee worden ze\nOriginal Module Manufacturer en hebben ze veel\ncompetenties in de mechatronica nodig. Ook op logistiek vlak moeten\nze de machinebouwer kunnen ontzorgen. \nLees meer.	88
Industrie	metaalproductenindustrie	trend	Internet of Things verbindt de keten	Internet of Things (IoT) is in de industrie aan een opmars\nbezig. Zowel productiemachines als producten zijn steeds vaker met\nelkaar verbonden. De industrie gebruikt IoT vooral om de efficiency\nvan processen te verhogen. Maar het is ook een middel om\nonderscheidende diensten en nieuwe verdienmodellen te ontwikkelen.\nOm aangehaakt te blijven bij de ontwikkelingen, moet de metaalketen\nde komende jaren investeren in software en automatisering; dé\nvoorwaarden voor verdere ketenintegratie en succesvolle datadeling.\nEn daarmee voor betere producten en processen. \nLees meer.	89
Industrie	metaalproductenindustrie	trend	Meer efficiënt dankzij LEAN en QRM	Om kostenefficiënt te kunnen produceren, is een geoptimaliseerd\nproductieproces noodzakelijk. Dit is tegelijk een voorwaarde voor\nhet succesvol gebruik van IoT. Voor de optimalisatie is volledig\ninzicht in alle stappen van het productieproces nodig. De werknemer\nop de fabrieksvloer heeft hierin een cruciale rol. Door op de\nfabrieksvloer te investeren in Lean of Quick Response Manufacturing\n(QRM), kunnen doorlooptijden worden verkort, gaan de kosten omlaag\nen de efficiency omhoog. Ook de flexibiliteit van het\nproductieproces verbetert, waardoor metaalbedrijven sneller op de\nwensen van hun klanten kunnen inspelen. \nLees meer.	90
Industrie	meubelindustrie	trend	Meer behoefte aan maatwerk en\ninnovatie	Meubelmakers staan voor de uitdaging om in te spelen op de\ngroeiende behoefte aan maatwerk. Van fabrikanten vraagt dit\nvergaande automatisering en een andere inrichting van processen. Zo\nis modulair bouwen in opkomst en zetten steeds meer bedrijven\nQuick Response Manufacturing (QRM) in om doorlooptijden te\nverkorten, efficiency te vergroten en kosten te verlagen. QRM\nbevordert de flexibiliteit van het productieproces; dat komt de\nconcurrentiekracht van bedrijven ten goede. \nLees meer.	91
Industrie	meubelindustrie	trend	Op zoek naar nieuwe duurzame concepten	Duurzaamheid is steeds meer een kwaliteitskeurmerk waarmee de\nbranche zich kan onderscheiden. In de circulaire economie zijn\nproducten onderdeel van een kringloop; ze kunnen eindeloos worden\ngebruikt. Dit vraagt om duurzame materialen en een andere manier\nvan produceren. Concepten als design-for-disassembly\ngroeien: producten kunnen makkelijk worden ontmanteld en opnieuw\nopgebouwd. Ook passen steeds meer bedrijven een levenscyclusanalyse\ntoe. Hiermee kunnen ze zien wat de milieubelasting van een product\nis tijdens de hele levenscyclus: van grondstof tot afvalverwerking.\nLees meer.	92
Industrie	meubelindustrie	trend	Van kop tot staart: nieuwe\nsamenwerkingsvormen	Meubelfabrikanten zijn de afgelopen jaren zwaar getroffen door\ndalende omzetten en teruglopende consumentenbestedingen. Veel\nwoonwinkels waaraan zij leverden, bestellen nu bij goedkopere\nfabrikanten in Oost-Europa en Azië. Dit dwingt fabrikanten en\nleveranciers tot een strategische heroriëntatie. Bijvoorbeeld een\ndeel van hun activiteiten (internationaal) uitbesteden en zich\nconcentreren op design, marketing en verkoop, terwijl de\nleverancier het meubilair produceert. In de projectenmarkt, zoals\nde inrichting van kantoorpanden, is deze aanpak al succesvol\ngebleken. Lees\nmeer.	93
Industrie	rubber-kunststofproductenindustrie	trend	Efficiënt produceren blijft cruciaal	Door internationale concurrentiedruk investeert de\nkunststofindustrie constant in automatisering en robotisering,\nzodat het machinepark 24 uur per dag onbemand kan draaien.\nProductiemachines worden steeds sneller en energiezuiniger, maar\nook slimmer en completer. Slimmer door innovatieve technieken,\nbijvoorbeeld om omsteltijden te verkorten of diagnoses te stellen\nvia een app. Completer door systeemoplossingen voor geïntegreerde\nrobot- en transportbesturing en aansluiting op MES- en\nERP-systemen. \nLees meer.	94
Industrie	rubber-kunststofproductenindustrie	trend	Ontzorging zorgt voor verhoogde klantafhankelijkheid	De vraag naar kleine series en maatwerk groeit. Steeds vaker\nwillen afnemers ontzorgd worden, van ontwikkeling en assemblage tot\nlogistiek. Meestal neemt de afhankelijkheid van enkele grote\nklanten hierdoor toe. Hoewel ook de samenwerking intensiveert en\nklanten loyaler worden, zijn de verhoudingen tussen fabrikant en\nklant niet altijd gelijk. Nederlandse kunststofbewerkers zijn\nrelatief klein en hebben daardoor weinig onderhandelingsmacht. Door\nde toegenomen klantconcentratie kan uitstel van orders zorgen voor\nmeer omzetfluctuatie en druk op het werkkapitaal. Lees meer.	95
Leisure	travel	trend	Verleiden met persoonlijke reviews	Liefst 95 procent van alle reizigers kijkt eerst naar\nreviews voor ze een reis boeken. Ongeveer 20 tot 40 procent noemt\ndit zelfs een doorslaggevende factor. Een recensie van een\nbackpacker is echter weinig relevant voor een getrouwd stel. En dus\nworden nu ook de reviews steeds scherper ingestoken op de juiste\ndoelgroep. Slimme reisaanbieders spelen hier op in, door\ncontent(blokken) op de website dynamisch aan te\npassen. elke afzonderlijke bezoeker te ontvangen\nmet positieve recensies van gelijkgestemden. Een verleidelijker\nvisitekaartje is nauwelijks Lees\nmeer.	119
Industrie	rubber-kunststofproductenindustrie	trend	Gebruik van biogebaseerde kunststoffen en recyclaat groeit\nsnel	Biogebaseerde kunststoffen en recyclaat zijn in opmars.\nAangedreven door nieuwe wetgeving, maar vooral door een grotere\nvraag vanuit de verpakkingsindustrie. Kwaliteit en verkrijgbaarheid\nworden beter en constanter, het aantal toepassingen groeit. In\nverpakkingen, maar ook in consumentenproducten en de bouw. Naar\nverwachting kan de nieuwe generatie biokunststoffen\n(drop-ins) rekenen op een hoge marktacceptatie; ze zijn\n100 procent herbruikbaar en machinaal probleemloos te verwerken.\nMet een hogere olieprijs in aantocht kunnen biokunststoffen straks\nook op kosten concurreren met fossiele grondstoffen. \nLees meer.	96
Industrie	transportmiddelenindustrie	trend	Gebruikskosten steeds krachtiger\nverkoopargument	De transportmiddelenindustrie is een zeer gevarieerde sector:\nscheeps- en trailerbouw, fietsproducenten en toeleveranciers aan de\nautomotive zijn de belangrijkste branches. Juist hun afnemers\nvinden total cost of ownership steeds\nbelangrijker. De kosten van bijvoorbeeld energieverbruik,\nonderhoud, vervanging van slijtdelen en reiniging zijn soms een\nveelvoud van de aanschafprijs. Afnemers zoeken steeds meer gemak en\nontzorging, en baseren hun keuze dan ook vaker op prijs en\ngebruikskosten. Ook leidt dit tot kansen voor remanufacturing.\nLees hier meer over remanufacturing.	97
Industrie	transportmiddelenindustrie	trend	Toeleveranciers zijn belangrijk voor de circulaire\nauto	Met het emissieschandaal rond Volkswagen, energielabels en de\nsnelle opkomst van elektrische fietsen en auto’s is duurzaamheid\nals onderscheidend vermogen steeds belangrijker geworden. De focus\nverschuift langzaam van lagere brandstofconsumptie en\nuitstootreductie naar hergebruik en manieren om de levensduur van\ntransportmiddelen te verlengen. Door met gerecyclede en\nbiogebaseerde materialen te werken, vermindert het verbruik van\nschaarse (fossiele) grondstoffen. Toeleveranciers die hierin kunnen\nvoorzien, worden steeds belangrijker voor grote fabrikanten.\nLees hier ons rapport over de Circulaire auto.	98
Industrie	transportmiddelenindustrie	trend	De deeleconomie rukt op	Aangezwengeld door successen in de consumentenmarkt, zoals\nSpotify, Uber en NextDoor, worden ook duurzame consumptiegoederen\nsteeds meer gedeeld: van boten en auto’s tot aanhangers en\nkruiwagens. Fabrikanten bieden zelf ook diensten aan. In Duitsland\nheeft BMW al zijn eigen autodeeldienst: DriveNow. In navolging van\nGeneral Motors en Ford . Door deelgebruik veranderen de eisen aan\ntransportmiddelen. Denk aan nieuwe systemen voor toegangsbeheer en\nde vastlegging van ge- en verbruikgegevens. \nLees meer.	99
Leisure	attractieparken-dierentuinen	trend	Van kortingen naar VIP-ervaringen	Liefst 9 op de 10 bezoekers\nplant graag vanuit huis in detail zijn attractieparkbezoek.\nOpmerkelijk is dat 80 procent van de bezoekers graag betaalt voor\neen extra ervaring. Denk daarbij aan een exclusieve rondleiding,\neen gepersonaliseerde souvenir of een leuke foto. Maar denk ook het\nreserveren van bepaalde attracties, parkeerplaatsen of diners.\nEigen alles waar je als bezoeker je reisgenootschap mee kan\nverrassen. ABN AMRO ziet haar relaties liever investeren in\nVIP-ervaringen, dan in\nkortingsacties. Lees\nmeer	100
Leisure	attractieparken-dierentuinen	trend	Safety first	Veiligheid is een essentieel onderdeel van bezoekerservaringen.\nSlimme inzet van mobiele telefoons biedt interessante nieuwe\nmogelijkheden. Bijvoorbeeld inzicht in het gedrag van bezoekers.\nProblemen kunnen hierdoor al in een vroeg stadium worden\ngesignaleerd. Ontstaan er noodsituaties? Dan kunnen hulpdiensten de\nomstandigheden goed inschatten en bezoekers via hun mobiele\ntelefoon naar de veiligste (nood)uitgang dirigeren. \nLees meer\n.	101
Leisure	attractieparken-dierentuinen	trend	Denk vanuit de ‘customer journey’	Succesvolle dagattracties blijven investeren in hun personeel en\nonderzoeken systematisch waar en hoe ze de gastbeleving kunnen\noptimaliseren. Er lijkt vooral winst te halen tussen de silo’s:\nwelke problemen lost u op door niet in afdelingen, maar in\ncustomer journeys te denken? Hoe kunt u kleinere\ngeldstromen slim combineren, zowel online als on-site? In het\ninterview met Arend Hardorff leest u meer over imagineering, een\ntechniek om juist dit gedisciplineerd te organiseren.	102
Leisure	campings-vakantieparken	trend	Kansen door ‘hotelisering’	Vakantieparken en campings kunnen inspelen op de behoefte aan\nluxe en comfort. Hierbij kunnen ze zich laten inspireren door de\nhotelbranche. Zo kunnen ze gasten aan zich binden met een op maat\ngesneden aanbod en extra services: van flexibel in- en uitchecken,\neen ontbijtservice en een kinderoppas tot massages en arrangementen\nmet leuke attracties en activiteiten in de omgeving. Kansrijk is\nook het inzetten van lokale experts, zoals bijvoorbeeld Airbnb dat\nsinds dit jaar doet. Lokale enthousiastelingen kunnen dan door\ngasten worden ingehuurd om een rondleiding, (stads)wandeling of\nbezoek aan een evenement te verzorgen. Lees\nmeer.	103
Leisure	campings-vakantieparken	trend	Inspireren met augmented reality	Pokémon Go veroverde binnen een maand de wereld. Deze hype toont\nde mogelijkheden van Augmented Reality aan: de technologie waarmee\ndigitale informatie via een mobiele telefoon of ander device aan de\nwerkelijkheid wordt toegevoegd. Een storytelling-tool bij uitstek,\nwaarmee reizigers en gasten tijdens hun hele customer journey\nkunnen worden geïnspireerd. Maar ook het vakantiepark en haar\nomgeving te leren kennen. Bovendien hebben consumenten ook steeds\nmeer behoefte aan mogelijkheden om hun digitale devices op een\nvernieuwende manier te gebruiken. Partijen die er in slagen deze\nhonger te voeden, nemen absoluut een voorsprong op de\nconcurrentie. Lees\nmeer.	104
Leisure	campings-vakantieparken	trend	Rammelende websites verdienen update	Internet is dé manier om de moderne consument te verleiden. Maar\nwebsites zijn vaak rommelig ingedeeld, voorzien van een verouderd\nboekingssysteem of niet geoptimaliseerd voor mobiel gebruik.\nBovendien is er vaak weinig aantrekkelijk beeldmateriaal. Met\nandere woorden: het belangrijkste uithangbord rammelt aan alle\nkanten. Hoe staat uw website ervoor? \nLees meer.	105
Leisure	foodservice	trend	Nadruk op ambacht	In Nederland is eten méér dan alleen je maag vullen. Steeds meer\nconsumenten willen ‘echtheid’. Ze zoeken naar authentieke mensen en\noprechte verhalen, liefde, eenheid, familie en bovenal passie. Ook\nals ze maaltijden laten bezorgen. Maar hoe maakt u van pizza en\nfastfood een feestje? Misschien door iets te maken dat nergens\nanders verkrijgbaar is. Of door de nadruk op uw ambacht te leggen,\nen producten aan te bieden die dit versterken. \nLees meer.	106
Leisure	foodservice	trend	Scheidslijnen verdwijnen	Het Nederlandse foodlandschap verandert snel. De consument trekt\nzich weinig meer aan van scheidslijnen die ooit door ambacht,\nwetgeving en verdienmodellen zijn getrokken. Verswinkels hebben\nsteeds vaker een eet-/koffiehoek. Combinaties van foodservice en\nfoodretail vinden we tegenwoordig overal: bijvoorbeeld op stations,\nbij pretparken, musea en bakkerijen. De dertig grootste formules\nnemen inmiddels het leeuwendeel van de omzet voor hun rekening:\nbijna 33 miljard euro, op een totale omzet van ruim 57 miljard\neuro. \nLees meer.	107
Leisure	foodservice	trend	De shift naar instant messaging	Op diverse horecalocaties zorgen bestelzuilen voor een toename\nvan de ordergrootte. Opvallend is dat ‘schermen’daar beter zijn in\nhet ‘upsellen’ dan de eigen medewerkers. Ook de populariteit van\ninstant messaging-apps groeit razendsnel. Vooruitlopende marketeers\nverschuiven de focus op mobiele aanwezigheid daarom van hun eigen\napp naar deze berichtjesdiensten. Naast direct contact met de\nconsument, kunnen ze allerlei relevante diensten aanbieden. Voor\nveel gasten voelt instant messaging als een natuurlijke vorm van\nmobiel communiceren, zelfs wanneer een computer (Chatbot)\nantwoordt. Lees\nmeer.	108
Leisure	hotels	trend	Meer winst door extra’s voor de gast	Wie begrijpt hoe de winstgevendheid en loyaliteit samenkomen\nvoor het beste resultaat onder de streep, kan zijn\nloyaliteitsprogramma daar effectiever op inrichten. Om vervolgens\nmet extra’s te investeren in het verhogen van de loyaliteit van\nwinstgevende gasten. En niet in de terugkeer van gasten die\nonvoldoende winstgevend gedrag vertonen.\nMogelijkheden in overvloed. De gemiddelde bezettingsgraad van\nNederlandse hotels is 62 procent. Tegelijkertijd ons land ruim 1\nmiljoen ZZP’ers. De sterke toename van het aantal ééndaagse\nvluchten en zelfrijdende auto’s dempt de vraag naar bedden op de\nlangere termijn. Het per uur verhuren van kamers, vergaderruimtes\nen andere faciliteiten biedt dus als extra ook een aantrekkelijke\ngroeimogelijkheid. Lees\nmeer.	109
Leisure	hotels	trend	De juiste boodschap op het juiste moment	Hotels investeren fors in marketingcommunicatie. Toch bereiken\nzij reizigers nog vaak op het verkeerde moment. Interessante\noplossing is geo-targeting. Zo maakt Facebook communiceren met\n(potentiële) gasten in de directe omgeving mogelijk. Daar kun\nje interessante dingen mee doen, bewees de Red Roof Inn vorig jaar\nal. De budgethotelketen richtte een mobiele advertentiecampagne op\nvoor Amerikaanse reizigers die waren gestrand op het vliegveld of\nop door files getroffen wegen. Met als resultaat een stijging van\nmaar liefst 60 procent van het aantal last minute\nboekingen. Lees\nmeer.	110
Leisure	hotels	trend	Hotelkamer verkopen wordt goedkoper	ABN AMRO ziet een daling van de ‘distributiekosten’, ofwel de\nkosten om een hotelkamer te verkopen. Toenemende datatransparantie\nen nieuwe toepassingen van TripConnect, Google en Amadeus zetten\ndruk op de marges van tussenpersonen. Ook Europese wetgeving speelt\neen rol. Zo wordt het voor hotels juridisch eenvoudiger om\npakketten en prijzen te communiceren via eigen kanalen. De grootste\nuitdaging voor de hoteliers hierbij: vaste gasten ook online\nherkennen, en ze dus niet telkens als nieuwe gasten\nbehandelen. Lees\nmeer.	111
Leisure	kunst-cultuur	trend	Definieer het bestedingsdoel	Musea zijn steeds minder afhankelijk van subsidies. Crowdfunding\nen fondsen op naam worden steeds \nefficiënter aangetrokken. Liefst 80 procent van (met name de\ngrotere) musea voorziet in 2017 een stijging van de eigen\ninkomsten. Desondanks zit 20 procent van de musea, poppodia en\nfestivals nog altijd in zwaar weer (bron: Conjunctuurwijzer.nl).\nMet een scherp gedefinieerd bestedingsdoel is er ruimte om\ninkomsten te genereren. Bijvoorbeeld via contactloos doneren,\ngiftcards en obligaties met uitsluitend maatschappelijk\nrendement. Bekijk\nde korte film.	112
Leisure	kunst-cultuur	trend	Van analoog naar digitaal. En visa versa	Door digitalisering raken bezoekers ook meer betrokken bij de\ncollectie. Via Google kunnen bezoekers virtueel en meestal gratis\ndoor musea wandelen of spelletjes spelen via Google Glass. Met apps\nen augmented reality kan het verhaal van de kunstenaar verteld\nworden. Ook de Museumvereniging helpt mee. Met haar\n‘MuseumkaartMatch’ vind je voortaan heel makkelijk iemand die ook\nop zoek is naar jou. Voor een trip naar een expositie aan de andere\nkant van het land. Of voor een bezoekje aan dat leuke museum in de\nbuurt. Lees\nmeer.	113
Leisure	kunst-cultuur	trend	Een optimale bezetting	De prijzen van vliegtickets worden bepaald op basis van de\nbeschikbare stoelen. Dit heet ‘dynamic pricing’. Samen met\nprijsdifferentiatie (verschillen tussen een business class- en\neconomy-stoel) zorgt dit voor drukbezette vliegtuigen. Per saldo\nmaakt het vliegen toegankelijk voor een breed publiek. Nederlandse\nmusea, theaters en filmhuizen kunnen ook van deze methode\nprofiteren. Hierdoor daalt het aantal onverkochte tickets voor\nminder populaire dagdelen. Bovendien stimuleert deze prijsstrategie\nbezoekers om bijvoorbeeld een Museumkaart of Cinevillepas aan te\nschaffen. Lees\nmeer.	114
Leisure	restaurants	trend	Gezonder, goedkoper, vaker beschikbaar	Buitenshuis eten zit in de lift. Toch vindt 72 procent van de\nNederlanders uit eten gaan nog steeds te duur. Zo neemt de helft\nvan de sporters water mee van thuis. Ruim een kwart neemt\nboterhammen mee. Een op de drie sporters geeft aan nooit iets te\nkopen in de sportkantine. Bij de toeschouwers geeft zelfs 39\nprocent aan nooit iets te kopen in de kantine of langs de\nlijn. Waarom? Te duur. Te ongezond. Of niet beschikbaar. Op\ntal van locaties zijn flexibele uitgiftepunten een\noplossingen. Zo kunnen promotieteams de gezonde snacks ook\n‘langs de lijn’ aanbieden. Lees\nmeer.	115
Leisure	restaurants	trend	Serveer meer buiten de hoofdmaaltijd	Volgens ABN AMRO is er nog een wereld te winnen door de aankoop\nvan bijgerechten, drankjes en desserts te stimuleren. Ook met\ngevarieerde porties spreekt u effectief nieuwe doelgroepen aan,\nzoals gezinnen. Bovendien brengt dit kansen voor maaltijdbezorging\nmet zich mee. Restaurants hebben nog meer knoppen om aan te\ndraaien. Transparantie en lef tonen in de prijsbepaling,\nbijvoorbeeld. Bied koffie en frisdranken in verschillende maten,\nvormen en dus ook (lagere) prijzen aan. Eventueel margeverlies kunt\nu goedmaken met meer omzet uit andere producten en\ndiensten. Lees\nmeer.	116
Leisure	restaurants	trend	Eten of gegeten worden?	ABN AMRO voorziet dat het aandeel eet- en drinkgelegenheden in\ntraditionele winkelcentra verdrievoudigt naar 21% in 2025. Dit\nleidt tot margedruk bij ondernemers in de sector. Hoe speelt u\nhierop in? Slim omgaan met tijd is zinvol. Door bijvoorbeeld iets\nextra’s of kortingen te bieden buiten de piekuren. Maar de grootste\nwinst zit bij inkoop. Minder diversiteit in toeleveranciers zorgt\nvoor een betere onderhandelingspositie. Ook schaalvergroting helpt.\nKunt u overhead spreiden over meerdere vestigingen? Dan dalen uw\nkosten per tafel per uur. Lees\nmeer.	117
Leisure	travel	trend	Geavanceerde gezichtsherkenning	Lange wachtrijen als gevolg van securitychecks helpen voorkomen?\n‘Big spenders’ of raddraaiers in het publiek identificeren en hen\nmaatwerk bieden? Technologie voor gezichtsherkenning wordt steeds\ngeavanceerder. Het gebruik van deze technologie moet reizigers\neen duidelijk voordeel opleveren. Er moet helder en\nondubbelzinnig over het gebruik worden gecommuniceerd. Voor\nbedrijven die gezichtsherkenning vanuit deze insteek willen\ninzetten, liggen momenteel talrijke mogelijkheden in het verschiet.\nLees\nmeer\n.	118
Retail	groothandel-non-food	trend	Groeiende druk op positie	De traditionele positie van de groothandel blijft onder druk\nstaan. Fabrikanten kunnen via internet lokale consumenten en\nbuitenlandse afnemers direct bereiken, waardoor de groothandel haar\nrol van betekenis dreigt te verliezen.	133
Leisure	travel	trend	De chatbot helpt reizigers snel op weg!	Binnen 30 seconden een\nvlucht boeken? Het kan door het eenvoudigweg aan de computer te\nvragen. Chatbots zijn bezig met een razendsnelle opkomst in de\ntravelsector. Heel binnenkort gaan deze kunstmatig intelligente\nreisvrienden zelfs proactief met ons praten.\nDoor de webcare- en serviceafdeling via de chatbot met klanten\nte laten communiceren worden ze niet alleen efficiënter en\nklantvriendelijker maar ook veel goedkoper. Zoals Virgin Trains,\ndat klantreacties via e-mail niet alleen veel sneller beantwoordt,\nmaar de benodigde manuren voor de verwerking daarvan dankzij een\nchatbot met liefst 85 procent heeft verlaagd. \nLees meer	120
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	trend	Verdere internationalisering	ABN AMRO verwacht dat de trend van verdere internationalisering\nin de branche de komende jaren zal doorzetten. Dit geldt voor\ntoeleveranciers aan de olie- en gassector, maar ook voor wind op\nzee. Nieuwe mogelijkheden treden op in de winning van olie en gas\nop land in veel grote olieproducerende landen. Voor toeleveranciers\nmet een internationale tak zijn de vooruitzichten daarom iets\ngunstiger. M&A en consolidering kunnen hierin een belangrijke\nrol spelen.	121
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	trend	Grotere rol hernieuwbare energie	ABN AMRO verwacht dat hernieuwbare energie een veel grotere rol\ngaat spelen in de energievoorziening. Dit betekent niet dat de\nolie- en gasindustrie van de ene op de andere dag zal verdwijnen.\nAls schoonste brandstof van de drie zal aardgas de sterkste groei\ngeven. Maar al zal de olievraag over tien jaar niet meer groeien,\ndan zal er nog steeds veel nieuwe olie gevonden en in productie\nmoeten worden genomen om afnemende productie uit bestaande velden\nte compenseren.	122
Olie-en-Gas	toeleveranciers-aan-de-olie-gasindustrie	trend	Uitbreiding energiemix	ABN AMRO verwacht een geleidelijke uitbreiding van de energiemix\nen meer competitie tussen de verschillende brandstoffen. ABN AMRO\ngaat uit van een geleidelijk herstel van de olieprijs gedurende dit\njaar. De prijs van aardgas zal langer laag blijven. De snelheid van\neen herstel  zal sterk afhankelijk zijn van de politieke\nbesluiten die regeringen nemen en de innovaties die bestaande en\nnieuwe bedrijven doorvoeren.	123
Retail	autoretail	trend	Gewijzigde bijtelling en fiscaliteit	De fiscale wetgeving is per 2017 gewijzigd: 4% bijtelling voor\nvolledig elektrische auto’s  en 22% voor alle overige\nmodellen.  Hybride lijkt hiermee voor de leaserijder uit de\ngratie.  De gewijzigde bijtelling, het veranderende\nklantgedrag waarbij er meer vraag naar tweedehands voertuigen is,\nheeft in 2016 tot een daling van 14,7% geleid. \nIn 2017 verwachten we een herstel naar circa 420.000 nieuwe\nauto’s, deels veroorzaakt door verdere groei van \nprivate lease.\n 	124
Retail	autoretail	trend	Overcapaciteit in het dealernetwerk	Doordat auto’s kwalitatief beter worden, consumenten anders\n(digitaal) aankopen en er minder gereden wordt, is overcapaciteit\nin de markt ontstaan. Dit leidt tot consolidaties in het\ndealernetwerk. Merken spelen hierop in door vestigingen te sluiten\nof te verkopen. Fabrikanten nemen steeds vaker taken van importeurs\nen dealers over, zoals Tesla. Ook importeurs en dealers doen\nonderling vaker elkaars werk.	125
Retail	autoretail	trend	Gedeelde mobiliteit en elektrisch connected rijden	In de toekomst zal  \ngedeelde mobiliteit toenemen omdat consumenten andere\nkoopbeslissingen nemen, meer beleving willen en steden overvol\nraken. Delen wordt het nieuwe bezit. Toekomstige  elektrische\nauto’s grotere capaciteit en\nactieradius. Voor het gemak kunnen bij tankstations  volle\ninwisselbare accu’s geruild  worden. De electrische connected\nauto bepaalt de optimale route, navigeert veilig, laat u uitstappen\nen parkeert zichzelf. Met een toekomstige tik op de smartphone komt\nde gedeelde auto aangereden.	126
Retail	bouwmarkten	trend	Online omzet groeit gestaag	De online omzet nam toe naar ongeveer 3,1 procent in 2016. De\nmarkt ervaart overcapaciteit aan winkelvloeroppervlakte. Daarom\nblijven bouwmarkten meer branchevreemd assortiment toevoegen, zoals\nfietsen, sportattributen en meubels. Een breder assortiment geeft\nde consument meer redenen om een bouwmarkt te bezoeken. Hiermee\nproberen ondernemers klanten aan zich te blijven binden.	127
Retail	bouwmarkten	trend	Gemak door stadswinkels en expertise	Consumenten blijven voor doe-het-zelfproducten fysieke\nbouwmarkten bezoeken, omdat ze deze vaak snel nodig hebben.\nOpkomende kleinere stadswinkels met een  basisassortiment\nkomen klussers daarin tegemoet: dicht bij huis kopen ze hier kleine\nklusmaterialen. Kleinere stadswinkels zie je ook bij woon- en\nmediawinkels. Bij bouwmarkten groeit de vraag naar expertise en\nkennis over klusprojecten. \nVakkundig personeel dat in staat is om uitleg en advies te\ngeven, wordt dus steeds belangrijker. \nRobots kunnen daar op termijn een rol in spelen. Consumenten\nzijn op zoek naar kennis: online tijdens het oriëntatieproces én in\nde fysieke winkel.	128
Retail	bouwmarkten	trend	Meer concurrentie vereist nieuwe strategieën	De komst van internationale spelers als Hornbach en Bauhaus, die\nmikken op grote volumes en lage prijzen, zorgen voor meer\nconcurrentie en prijsdruk. Branchevreemde aanbieders van\ndoe-het-zelfproducten versterken dit. Denk aan Action en Bol.com.\nDe trend ‘van bezit naar gebruik’ is in opkomst. Leenplatform\nPeerby Go speelt in op deze deeleconomie, waarbij consumenten\nspullen verhuren aan elkaar. In 2016 gebruikte 20 procent van\nNederlanders een deelplatform. In 2013 was dit nog maar 6 procent\n(Kaleidos Research, 2016). Een echte reactie van\ntraditionele spelers in de sector blijft vooralsnog uit.	129
Retail	drogisterijen	trend	Online groeit	Door toename van het aantal e-tailers als Bol.com,\nonlinedrogist.nl en drogist.nl, groeit de online omzet van 7,3 naar\n8,4 procent in 2016 (bron Gfk). De consument \noriënteert zich online voor de aankoop van een\ndrogisterijartikel. Voor traditionele drogisterijen wordt een\nomnichannel-aanpak dus noodzakelijk en vereist de nodige\ninvesteringen. Slimme huis-speakers als Amazon Echo, Alexa en\nGoogle Home kunnen op stemcommando bijvoorbeeld producten online\nbestellen. E-tailers moeten consumenten in de oriëntatiefase aan\nhun webshop te binden. Een goed logistiek proces verlaagt de\ndrempel om vooral herhalingsaankopen online te bestellen.	130
Retail	drogisterijen	trend	Klant blijft kritisch op prijs	De consument blijft zeer prijsbewust. Door toenemende\nconcurrentie in de branche van onder andere Kruidvat, Trekpleister,\nAction, Big Bazar en Op=Op Voordeelshop, is de promotiedruk in de\nwinkels circa 40 tot 45 procent. Ook blijft de concurrentie vanuit\nsupermarkten, apothekers en parfumerieën toenemen.	131
Retail	drogisterijen	trend	Vergrijzing als onderscheidend vermogen	Het is voor de verschillende drogisterijformules moeilijk zich\nte onderscheiden. Dat geringe onderscheidend vermogen richt zich\nbij drogisterijen vooral op de prijs-kwaliteitverhouding. De\nverkoop van huismerken neemt toe. In 2030 is echter 23,8% van de\nbevolking 65 plus (bron: CBS). Nu is dit nog 18,5%. De 65 plussers\nkopen gemiddeld minder spullen maar hebben toenemende aandacht voor\ngezondheid en beleving. Qua assortiment en dienstverlening biedt\ndit drogisterijen groeipotentie. Om klanten te binden is lokaal\nondernemerschap bij succesvolle drogisterijen alsmede \ndeskundig personeel nog steeds een cruciale factor.	132
Retail	groothandel-non-food	trend	Digitalisering en big data	Door digitalisering en \nbig data zullen groothandels vraag en aanbod beter op elkaar\nkunnen afstemmen. Resultaat: hogere omloopsnelheden en kortere\nlevertijden. Nieuwe exportmarkten buiten West-Europa bieden\ngroeikansen voor groothandels. Exporterende groothandels profiteren\nvan de lagere eurokoers. Maar als ze in andere valuta inkopen, kan\ndit leiden tot hogere inkoopkosten. Deze proberen ze door te\nberekenen aan de consument om de impact op hun marge te\nverkleinen.	135
Retail	kledingwinkels	trend	Omnichannel is de standaard met beleving in de winkel	In 2016 groeide de online fashion omzet van 16 naar 20 procent\n(Thuiswinkel Markt Monitor, 2016). Het online kanaal dient zowel\nals verkoopkanaal als oriëntatiemiddel. Consumenten willen online\nén offline blijven winkelen en een eenduidige winkelervaring\nbeleven. Een goede reden voor retailers om digitale en fysieke\nwinkels samen te voegen tot een omnichannel-shopomgeving.\nConsumenten blijven  fysiek kleding shoppen en de\nwinkelbeleving wordt daarbij belangrijker. Fast fashion-ketens\nbieden beleving door snel wisselende outfits te bieden voor lage\nprijzen. Slimme technologie gaat daarbij \ndata vertalen naar bruikbare inzichten om eenvoudiger\nvoorkeuren en gedrag van klanten te kunnen bepalen. Daarnaast\nbieden persoonlijke service en technologische ontwikkelingen als\nvirtual reality, artificial intelligence en interactieve\npasspiegels de mogelijkheid om een nieuwe (winkel)omgeving te\ncreëren waarin consumenten vermaakt, geïnspireerd  en op\ntoegankelijke wijze geadviseerd kunnen worden. Lees meer.	136
Retail	kledingwinkels	trend	Retailers met een missie	Vanwege de opvallend lage prijsniveaus in fast fashion en de\nimpactvolle productie omstandigheden, ontwikkelen consumenten meer\noog voor \nduurzamere productie. Zij hebben meer sympathie voor retailers\nmet een missie om de (nabije) omgeving te helpen of om de keten\ncirculair te maken, waarbijvoorbeeld Filippa K, Mud Jeans, TOMs en\nPatagonia initiatieven in ondernemen. Deze retailers ontplooien\nnieuwe mogelijkheden om consumenten te helpen inzien dat ze\nsituaties thuis, lokaal of wereldwijd positief kunnen veranderen.\nKledingmerken in het midden- en hoge segment spelen hierop in met\nduurzamere kledinglijnen. Consumenten willen zich steeds meer\nverbinden met de merken die ze kopen en dragen. Dit gaat verder dan\nenkel de behoefte aan het product.	137
Retail	kledingwinkels	trend	Locatiemanagement belangrijker dan ooit	Sinds 2005 is het aantal bezoekers in de gemiddelde winkelstraat\nmet bijna 23 procent gedaald (Locatus). Mede door de groei van\nonline kledingverkopen en gewijzigde consumentenbestedingen steeg\nde \nleegstand tot 2016 in de winkelstraten. Deze ontwikkeling eist\ndat retailers strategische afwegingen maken omtrent hun locaties:\nsluiten, juist openen, de vestigingsduur en het totaal aan\nwinkelvloeroppervlakte. De vestigingsplek moet blijven aansluiten\nop de wensen en locatie van de doelgroep. Flexibiliteit in retail\nformats is nodig om klanten lokaal blijvend te kunnen \nverrassen waarbij ‘one size fits one’ steeds meer van\ntoepassing is. \nSamenwerking in het winkelgebied blijft daarbij cruciaal.	138
Retail	supermarkten	trend	Bescheiden groei online boodschappen doen	Van de totale supermarktomzet bedroeg het online aandeel in\n2016 2,9 procent. Vooralsnog is het online kanaal niet winstgevend.\nNaar verwachting stijgt dit in 2025 naar 9 procent. Toch blijft de\nsupermarktdichtheid in Nederland hoog in vergelijking met\nomliggende landen als België, Duitsland en Frankrijk. Strategische\nheroverweging van het aantal en type vestigingen wordt belangrijker\nnaarmate de online omzet groeit. Big data blijft daarbij van belang\nom zowel online als in de fysieke supermarkt persoonlijke\naanbiedingen te kunnen verzorgen. \nLees meer.	139
Retail	supermarkten	trend	Meer behoefte aan gemak	Disruptieve partijen als Picnic en HelloFresh spelen in op de\ngroeiende klantbehoefte aan gemak. In reactie hierop openen\ngevestigde supermarkten meer kleine stadswinkels (tot 400\nm2 winkelvloeroppervlak) met flexibelere openingstijden.\nOok groeit het aantal grotere supermarkten (vanaf 1.000\nm2) met flexibelere openingstijden, pick-up points, en\neet- en zitgelegenheid. Het aantal middelgrote supermarkten met een\nwinkelvloeroppervlakte van 400 m2 tot 1.000\nm2 zal afnemen. Het toevoegen van foodservice elementen\nzoals bij Jumbo-La Place zal meer navolging krijgen. Lees meer.	140
Retail	supermarkten	trend	Gezond voedsel wint terrein	De belangstelling voor gezonde voedingsmiddelen neemt toe.\nSupermarkten en nichespelers als Marqt en Landmarkt spelen hierop\nin met een \ngezonder en verser basisassortiment. Ook worden biologische en\nregionale producten vaker in het assortiment opgenomen.\nTraditionele supermarkten en speciaalzaken in Foodretail verliezen\nhierdoor mogelijk omzet. Hun kansen liggen op de terreinen van\nkwaliteit, expertise (ambacht),winkelbeleving en hun rol als\nsociale ondernemer zoals bij het tegengaan van \nvoedselverspilling.	141
Retail	winkels-in-consumentenelektronica	trend	Online omzet zet door	In 2016 is de online omzet in consumentenelektronica en witgoed\ngestegen van 24 naar 28 procent. De producten lenen zich bij\nuitstek voor digitale aanschaf, omdat ze goed te vergelijken zijn\nop basis van productfunctionaliteiten. \nPrijs en kwaliteit blijven de belangrijkste drivers voor\nconsumenten. Productbeoordelingen en consumentenreviews hebben\ngrote invloed op het aankoopgedrag van consumenten, dus online\nbeschikbaarheid en vindbaarheid hiervan is cruciaal.	142
Retail	winkels-in-consumentenelektronica	trend	Daling aantal winkels	Doordat een deel van de omzet van fysieke elektronicawinkels\nnaar webshops verschuift, is er overcapaciteit aan\nwinkelvloeroppervlakte. Het aantal fysieke verkooppunten in\nelektronica en witgoed daalt, en blijft naar verwachting afnemen.\nHeeft een \nomnichannel-propositie een goede balans tussen online en\noffline, dan biedt de sector nog steeds mogelijkheden. Zo\nonderscheidt winkelformule Coolblue zich via een\nomnichannel-propositie met een breed assortiment en extra service,\nzoals bezorging en installatie van witgoed. Voor haar klanten is\ngemak belangrijker dan prijs. Convenience wordt de nieuwe\nloyaliteit.	143
Retail	winkels-in-consumentenelektronica	trend	Kennis primair, beleving secundair	Consumenten blijven elektronicawinkels bezoeken vanwege de\nkennis en kunde van het personeel. Persoonlijk advies,\ninstallatie en service bieden de retailer kansen om consumenten\nnaar de fysieke winkel te trekken. De vergrijzing biedt daarbij\nkansen. Door winkels in te richten als ‘belevingscentra’, kunnen\nproducten worden gedemonstreerd en getest. Mediamarkt werkt\nbijvoorbeeld samen met leveranciers voor productdemonstraties. En\nKamera Express heeft een experience store waar klanten\nprofessionele camera’s kunnen uitproberen. De combinatie van\nexpertise en beleving zorgt voor een optimale productpresentatie\naan de klanten. \nLees meer.	144
Retail	woonwinkels	trend	Herstel zet door	De branche heeft zich herstelt dankzij het aanhoudende\nconsumentenvertrouwen en de toenemende huizenverkoop. Maar de\nconcurrentie blijft groot, en er komen steeds meer branchevreemde\naanbieders zoals bouw- en tuincentra bij. Daarnaast zijn er grote\nonline spelers en fabrikanten die rechtstreeks aan de eindgebruiker\nleveren. Een \nomnichannel-aanpak is noodzakelijk, omdat consumenten\nzich steeds meer via internet oriënteren.	145
Retail	woonwinkels	trend	Beleving blijft cruciaal	Om klanten te verleiden naar de winkel te (blijven) komen, is\nbeleving in de woonwinkel cruciaal. Het aanbod is vaak onvoldoende\nonderscheidend. Door individualisering willen consumenten een stem\nhebben in het ontwerp. MyKea en Made.com bieden deze vorm van\nmass customization. De aantrekkelijkheid van woonmeubelboulevards\nis beperkt en mede daardoor is er sprake van overcapaciteit aan\nwinkelvloeroppervlakte. Dit zal leiden tot noodzakelijke\nherinrichting van deze winkelgebieden, relocatie en tot \nnoodzakelijke samenwerking in deze gebieden.	147
Technologie-Media-Telecom	drukkerijen	trend	Geautomatiseerde drukwerkfabrieken	Volumes in de branche krimpen, wat heeft geleid tot\novercapaciteit en toenemende concurrentie. Deze concurrentie daagt\ndrukkerijen uit om het productieproces te automatiseren; ze moeten\nopdrachten efficiënt kunnen verwerken tegen lage prijzen.\nDoor  combineren kan er goedkoper en\nsneller geproduceerd worden.\nLees meer.	148
Technologie-Media-Telecom	drukkerijen	trend	Internetverkoop	Orders komen steeds vaker binnen via (een) internet (portal). De\nonline dienstverlening van drukkerijen is steeds beter op orde.\nHierdoor kunnen drukkerijen uiteenlopende markten bedienen met een\ngrote verscheidenheid aan diensten en producten.\n \n 	149
Technologie-Media-Telecom	drukkerijen	trend	Innovatieve diensten	Klanten zoeken naar een goede communicatiemix van papier en\nonline. Om hierover te kunnen adviseren bieden drukkerijen nieuwe\ndiensten aan zoals vormgeving  en consultancy. Vaak in\nsamenwerking met creatieve bedrijven of zzp’ers. Voor\ngespecialiseerd drukkers liggen er kansen in nieuwe technieken en\nhightech printwerk, zoals 3D-printing en printed electronics.\nLees meer.	150
Technologie-Media-Telecom	ict-hardware	trend	Toegevoegde waarde diensten	Door gebrek aan een nieuwe massa-gadget, is de hardewaremarkt\nmomenteel verzadigd. De economische groei heeft wel voor\ninhaalinvesteringen gezorgd. Daarnaast vraagt de transitie naar\nmobiele devices en cloud computing om nieuwe\nhardware-configuraties. Op zoek naar groeikansen bieden\ngroothandels nieuwe diensten, zoals verhuur, betalen voor gebruik\nen bredere IT-services. Bijvoorbeeld gericht op ondersteuning bij\nvraagstukken rondom cloud computing-transities.\nLees meer.	151
Technologie-Media-Telecom	ict-hardware	trend	Aantal devices met dataverbinding groeit	De markt voor kantoorapparatuur en desktop-pc’s is een\nvervangingsmarkt. Maar het aantal wearables, apparaten en objecten\nmet een internetverbinding groeit snel. Veel sectoren denken na\nover mogelijke nieuwe businessmodellen en boren hiervoor nieuwe\ndatabronnen aan. Dit vereist extra investeringen in hardware.\nLees meer.	152
Technologie-Media-Telecom	ict-hardware	trend	Circulaire Economie	Het internet en de steeds voortgaande digitalisering faciliteren\neen groot aantal circulaire oplossingen in de markt. Een transitie\nnaar een volledig modulaire productie van onder meer computers,\nIT-apparatuur en elektronica vormt een logische oplossing richting\neen meer duurzame hardwarebranche. De levensduur van bijvoorbeeld\nsmartphones en tablets is vaak goed te verlengen door vervanging\nvan onderdelen. Het is ook de enige manier om e-waste in de\ntoekomst te voorkomen.	153
Technologie-Media-Telecom	it-software-services	trend	Specialisatie	Cloud computing levert schaalvoordelen op. In de markt voor\nopslag en rekenkracht zorgen grote platformen als Microsoft, Google\nen Amazon voor prijsdruk. Voor kleinere IT-bedrijven is dit de\nreden om zich te specialiseren; daarmee voorkomen ze margedruk.\nSpecialiseren kan in horizontale markten, bijvoorbeeld ERP of HRM.\nMaar ook in verticale markten liggen kansen, bijvoorbeeld in de\ngezondheidszorg, industrie of financiële dienstverlening\n(fintech).\nLees meer.	154
Technologie-Media-Telecom	it-software-services	trend	Cybersecurity	De toename van cybercrime is een logisch gevolg van de\nstrategische positie die informatietechnologie inneemt in de\nsamenleving. In ons dagelijks leven speelt internet inmiddels een\ncentrale rol, en de impact op het bedrijfsleven wordt steeds\ngroter. Cybersecurity is voor bedrijven in alle sectoren een nieuw\nbedrijfsrisico. Andere kant van de medaille: het levert\nIT-bedrijven nieuwe kansen op.\nLees meer.	155
Technologie-Media-Telecom	it-software-services	trend	Nieuwe soorten bedrijven	Binnen de categorie IT software  en services bevinden zich\nook nieuwe bedrijven die niet passen binnen de traditionele\ndefinitie van deze branche. Denk bijvoorbeeld aan hostingbedrijven,\ninternetbedrijven of deelplatformen die op basis van nieuwe\nbusinessmodellen snel weten te groeien. Van deze categorie\nbedrijven is nog weinig data beschikbaar omdat ze niet vallen onder\nde bestaande statistische classificatie. Hun economische impact\ngroeit: ze genereren nieuwe banen en groeien vaak\ninternationaal.	156
Technologie-Media-Telecom	it-software-services	trend	Circulaire Economie	Het internet en de steeds voortgaande digitalisering faciliteren\neen groot aantal circulaire oplossingen in de markt. Technologie in\nde vorm van sensoren, netwerkverbindingen, software en\ncloud-toepassingen heeft het potentieel de opkomst van de\ncirculaire economie te versnellen. Dit maakt TMT-sector tot\nhofleverancier van andere sectoren zoals Industrie, Bouw, Retail,\nAgri en Food. Voor de IT- en Telecom-sector is de circulaire\neconomie een nieuwe motor voor groei.	157
Technologie-Media-Telecom	reclamebureaus	trend	Advertentiebudgetten verschuiven naar online	Online advertising is fors gegroeid en sinds 2014 zelfs het\ngrootste advertentiemedium. Google en Facebook hebben hierin\neen aandeel van rond 60%. De meetbaarheid en het bereik die zij\nbieden, trekt advertentiebudgetten als een magneet aan. Voor\nuitgeverijen, (andere) internetplatformen en mediabureaus \nbetekent dit stevige concurrentie. Voor deze partijen is het\nbelangrijk de strategie aan te scherpen op het vlak van content,\nmobiel, klantloyaliteit, verticals, transparantie en integrale\ndienstverlening.\nLees meer.	158
Technologie-Media-Telecom	reclamebureaus	trend	Dynamiek tussen internetbureaus	Investeerders tonen toenemende interesse: Nordian nam een belang\nin Oxyma. Met Waterland als investeerder volgt Dept een\ninternationale groeistrategie.  eFocus werd overgenomen door\nhet Franse Valtech. Daarnaast bewegen traditionele dienstverleners\nzich in de markt van internetbureaus: zowel Deloitte Digital als\nAccenture Digital behoren inmiddels tot de marktleiders.\nLees meer.	159
Technologie-Media-Telecom	reclamebureaus	trend	Nieuwe competenties	Door de verschuiving naar online als belangrijkste\nadvertentiekanaal zijn nieuwe competenties nodig. Naast\nIT-bedrijven,  hebben marketingbureaus moeite met het\naantrekken van  de juiste IT-specialisten. Voor de overheid en\nhet bedrijfsleven is het nu zaak om door te pakken, ook door\nomscholingstrajecten tot IT-specialisten nog nadrukkelijker te\nstimuleren. Daarmee kan een deel van het grote aantal openstaande\nvacatures worden ingevuld.\nLees meer.	160
Technologie-Media-Telecom	telecom	trend	Verschillende vormen van communicatie integreren	Telecombedrijven bieden steeds meer gebundelde diensten aan.\nMobiele en vaste aanbieders werken samen. Hierdoor wordt het\nmogelijk om quad play aan te bieden: internet, televisie, vaste en\nmobiele telefonie in één abonnement. Zakelijke klanten zoeken\nsteeds vaker oplossingen waarbij vaste en mobiele telefonie\ngeïntegreerd worden. Zo zijn werknemers bereikbaar ongeacht de\nlocatie, het apparaat of het telefoonnummer.\nLees meer.	161
Technologie-Media-Telecom	telecom	trend	Internetbellen verovert de zakelijke markt	Snelle internetverbindingen(breedband via adsl, kabel of\nglasvezel) zijn voor vrijwel iedereen beschikbaar. Hierdoor kunnen\nconsumenten en bedrijven bellen via het internet, en neemt\ntraditioneel bellen af. Voor telecom en IT-bedrijven is vooral de\nMKB+ markt (50-249 seats) een interessante groeimarkt. Bedrijven\nkiezen voor cloud IT en telefonie diensten vanwege flexibiliteit,\nlagere kosten, betalen voor gebruik en uitbesteding aan een\nspecialist.\nLees meer.	162
Technologie-Media-Telecom	telecom	trend	Nieuwe groeimarkten gezocht	De concurrentie om de klant is groot, ook in de zakelijke markt.\nDit zorgt voor margedruk. Nieuwe partijen weten particuliere\nklanten te lokken met content en een verbeterde gebruikservaring.\nTelecombedrijven zoeken onderscheidend vermogen, bijvoorbeeld met\nsportzenders en eigen content. Of door te nieuwe groeimarkten te\nverkennen zoals Internet of Things en Cybersecurity.\nLees meer.	163
Technologie-Media-Telecom	telecom	trend	Circulaire Economie	Het internet en de steeds voortgaande digitalisering faciliteren\neen groot aantal circulaire oplossingen in de markt. Technologie in\nde vorm van sensoren, netwerkverbindingen, software en\ncloud-toepassingen heeft het potentieel de opkomst van de\ncirculaire economie te versnellen. Dit maakt TMT-sector tot\nhofleverancier van andere sectoren zoals Industrie, Bouw, Retail,\nAgri en Food. Voor de IT- en Telecom-sector is de circulaire\neconomie een nieuwe motor voor groei.	164
Technologie-Media-Telecom	televisie-omroepen	trend	Streaming	Films, series en documentaires aanbieden via een online platform\n(‘streaming’) is een belangrijke trend binnen televisie. Het biedt\ntoegang tot nieuwe informatie over wat kijkers boeit. Weinig mensen\nweten dat Netflix de hitserie House of Cards produceerde\nop basis van kijkersvoorkeuren.\nLees meer.	165
Technologie-Media-Telecom	televisie-omroepen	trend	Grote vraag	In de strijd om de mediaconsument is het cruciaal om\naansprekende content te bieden. De vraag naar bewegend beeld is\nfors, ook van telecombedrijven en andere nieuwe partijen.\nProducenten van tv-content profiteren hiervan. Nederland heeft een\nsterke creatieve reputatie op het gebied van internationaal\nsuccesvolle formats, en zit dus in een kansrijke positie.	166
Technologie-Media-Telecom	televisie-omroepen	trend	Nieuwe skills	Televisiekijken doen we niet meer altijd met z’n allen in de\nhuiskamer. Consumenten rijgen schermen aan elkaar, mogelijk gemaakt\ndoor snelle internetverbindingen in combinatie met tablets en\nsmartphones. Formats moeten op al deze platformen toegankelijk\nzijn. Dit vraagt om nieuwe skills van tv-producenten.\nLees meer.	167
Technologie-Media-Telecom	uitgeverijen	trend	Advertentiebudgetten verschuiven naar online	Online advertising is fors gegroeid en sinds 2014 zelfs het\ngrootste advertentiemedium. Google en Facebook hebben hierin een\naandeel van rond 60%. De meetbaarheid en het bereik die zij bieden,\ntrekt advertentiebudgetten als een magneet aan. Voor uitgeverijen,\n(andere) internetplatformen en mediabureaus betekent dit stevige\nconcurrentie. Voor deze partijen is het belangrijk de strategie aan\nte scherpen op het vlak van content, mobiel, klantloyaliteit,\nverticals, transparantie en integrale dienstverlening.\nLees meer.	168
Technologie-Media-Telecom	uitgeverijen	trend	Digitalisering printmedia laat versnelling zien	Consumenten beschikken momenteel en masse over smartphones en\ntablets. Beide apparaten hebben een steeds grotere impact op het\ngedrag en de belevingswereld. Pas sinds 2012 laat het aandeel\nvolledig digitale krantenabonnementen jaarlijks significante\nstijgingen zien. Op de boekenmarkt heeft de introductie van de\ntablet minder effect gehad. De digitalisering neemt hier jaarlijks\ngestaag toe. Vorig jaar is 6,9% van de boeken digitaal\nverkocht.\nLees meer.	169
Technologie-Media-Telecom	uitgeverijen	trend	Nieuwkomers richten zich op het ontbundelen en herbundelen van\ncontent	Online is de bereidheid om te betalen lager. Consumenten zijn\ngewend geraakt aan gratis platformen met een advertentiemodel.\nNieuwe en bestaande spelers zoeken naar manieren om\nmediaconsumenten te laten betalen voor content. Blendle\nexperimenteert met abonnementsvormen. Bestaande spelers richten\nzich meer op online door bewegend beeld te integreren en\nuitsluitend digitale tijdschriften te produceren, bijv.\nAmayzine.\nLees meer.	170
Transport-en-Logistiek	binnenvaart	trend	Binnenvaart nu vol in beeld als duurzame\nmodaliteit	Het Klimaatakkoord van Parijs eist transitie naar schoner en\nCO2-armer vervoer. De economische groei toont kwetsbaarheid van\nbestaande (weg) infrastructuur. Dit is hét momentum voor de\nbinnenvaartsector. Beprijzing van deze duurzame modaliteit moet\nbeter beloond worden door verladers. Van de weg naar het schip is\neen eerste stap; moderne motorisering hoort hier bij. Visie en\nmotivatie zijn leidend, niet StageV regelgeving. Bestaande\ncapaciteit efficiënter benutten, daar ligt de toekomst!	171
Transport-en-Logistiek	binnenvaart	trend	Upgrade van het ondernemerschap is\ngewenst	Anno 2017 is de gepassioneerde varende ondernemer strategisch\nbinnenvaartondernemer\ngeworden. U bepaalt de nieuwe koers. Actuele financials bevestigen\nde juiste richting, of vragen om direct bijsturen. Verandering moet\nom uw bedrijfsvoering te optimaliseren (hybride motorisering,\nzonnepanelen). Duurzaam ondernemen vraagt een investering in uw\nschip én u als ondernemer. Laag water kan prettig zijn, maar mag\nniet DE reden zijn van een goed jaar; het fundament moet steviger\nzijn.	172
Transport-en-Logistiek	binnenvaart	trend	Samenwerking blijft ook in 2017 en 2018 top of\nmind	Innovatie vanuit toeleveranciers (motorisering) en samenwerking\nmet andere varende ondernemers (in coöperatieverband) zijn bepalend\nvoor een gezondere binnenvaartsector. De impact van veranderende goederenstromen\n(kolen, containers) technologische innovaties (3D-printing), en het\nvinden van voldoende (jong) personeel zijn thema’s die de sector\nmoet oplossen. Samen sterker, zowel verenigd via een\nbrancheorganisatie of via bundeling van verschillende kwaliteiten\nmaakt uw positie toekomstbestendig.	173
Transport-en-Logistiek	expediteurs	trend	Vernieuwen is de enige weg naar toegevoegde waarde	De wereld van de expediteur verandert snel. Trends als\nglobalisering, near shoring, data-technologie, maar ook 3D printing\nzijn leidend. Daarbij beïnvloedt de digitale transformatie\nbestaande logistieke processen continu, zie bijvoorbeeld de\nmogelijke impact van block chain technologie. De verbinding die de\nexpediteur maakt tussen vraag en aanbod stelt steeds hogere eisen\naan zijn rol als strategisch logistiek specialist. Logistieke\nkennis gecombineerd met informatie technologie staan centraal. Dát\nis de toegevoegde waarde waarop de expediteur zijn rol verder moet\nuitbouwen.	174
Transport-en-Logistiek	expediteurs	trend	Specialisme biedt kansen in complexe logistiek	Het verschil tussen logistiek dienstverleners en de traditionele\nrol van de expediteur wordt kleiner. Een eigen identiteit is\nmogelijk door te specialiseren in een niche of hooggekwalificeerd\nte zijn op het gebied van informatie-uitwisseling en documentatie.\nDe markt van de expediteur is met name gericht op internationale\nlogistieke ketens. Dit blijft een complex speelveld met een\nbehoefte aan professionele expediteurs die steeds meer end-to-end\noplossingen aan kunne bieden.	175
Transport-en-Logistiek	expediteurs	trend	Onboarding van jonge denkkracht	De huidige jonge generatie gaat versnelling brengen in uw\nveranderende rol als expediteur. Zij brengen denkkracht met kennis\nvan IT, denken niet enkel meer primair vanuit goederenstromen. Zij\nzetten de norm voor de toekomst die gisteren begonnen is. Online\nplatforms en algoritmes zijn leidend in de aansturing van vraag en\naanbod. Logistieke efficiëntie en Co2 reductie zijn actuele\nvraagstukken. Dit vraagt om een organisatie-aanpassing met ruimte\nvoor een vernieuwende, transparante cultuur.	176
Transport-en-Logistiek	goederenvervoer-over-spoor	trend	Spoor positioneert zich in de totale\nvervoersketen	Het spoor positioneert zich sterker als schone en betrouwbare\nmodaliteit. Beschikbaarheid van data maken internationale\nvervoerketens steeds inzichtelijker. Logistieke dienstverleners\nzoeken vaker de mogelijkheden\nvan het spoor voor hun opdrachtgevers. Krachtige\ninitiatieven als NewWays koppelen heen- en retourlading van\nverschillende partijen aan elkaar, waardoor nieuwe mogelijkheden\nontstaan. De alliantievorming op deepsea-vervoer biedt potentie aan\nhet spoorgoederenvervoer als ideale achterland-aansluiting vanuit\nde Zeehavens.	177
Transport-en-Logistiek	goederenvervoer-over-spoor	trend	Economie, duurzaamheid en congestie zetten spoor in de\nspotlight	Economische groei betekent stijgende vervoersvolumes. Met name\nwegvervoer merkt een toenemende congestiedruk wat vraagt om\nalternatieve oplossingen. In combinatie met de toenemende aandacht\nvoor Co2 reductie wint het spoorgoederenvervoer terrein. De\nintroductie Lean & Green Off-Road gaat efficiëntie opleveren en\nbiedt potentie aan de modaliteit spoor. Recente nieuwsberichten\ntonen aan dat veel van de bestaande spoorvervoerders hun\nspoordiensten uitbreiden. Ook de Chinese spoorroute is de\nincubatietijd voorbij. Punt van zorg blijft de voortgang van de\nrealisatie van het Derde Spoor.	178
Transport-en-Logistiek	goederenvervoer-over-spoor	trend	Informatie uitwisselen en samenwerken moet tandje\nhoger	De spoorsector innoveert zeker wel, maar minder zichtbaar dan\nbijvoorbeeld wegtransport. Wellicht is het nog te vroeg voor\nzelfrijdende treinen, maar het spoor leent zich bij uitstek\nhiervoor. Andere initiatieven als Route lint en Smart sense\ncontainer geven aan dat technologie en informatie ook binnen de\nspoormodaliteit definitief hun plaats hebben gekregen. Winst is te\nbehalen op het gebied van samenwerking. Dat geldt zowel voor\nveilige data-uitwisseling tussen partijen onderling als het\nERMTS-initiatief op Europees niveau.	179
Transport-en-Logistiek	goederenwegvervoer	trend	Versterken van de positie op de arbeidsmarkt	De aantrekkende economie heeft gevolg voor de arbeidsmarkt in wegtransport.  We\nsignaleren tekort aan chauffeurs en een relatief snelle\nvergrijzing. Bijkomende gevolg is een toenemend ziekteverzuim en\ntegelijkertijd afnemende productiviteit. Duurzame inzetbaarheid én\nbehoud van het huidige personeel zijn belangrijke thema’s. Gezien\nde krapte op de arbeidsmarkt zal de sector Transport en Logistiek\neen extra tandje bij moeten schakelen om ook nieuwe mensen naar\nzich toe te trekken.	180
Transport-en-Logistiek	goederenwegvervoer	trend	Economische groei stelt nieuwe eisen aan optimaal vervoer\n2016 was een sterk jaar voor de	transport sector. Deze trend zet zich voort in 2017.  De\ncombinatie van arbeidsmarktkrapte, toenemende vervoersvolumes,\ncongestie en focus op reductie van\nCO2 uitstoot vormt een bijzonder grote uitdaging. De druk op\neen optimale inzet van vervoerscapaciteit neemt toe, en verspilling\nmoet worden terug-gebracht. Inzicht in logistieke processen bij\nverladers vormt daarbij het startpunt. Stadsdistributie en bouwlogistiek zijn\ninitiatiefrijke deelsegmenten. Maar denk ook aan  nieuwe concepten die zijn\ngelanceerd.	181
Transport-en-Logistiek	goederenwegvervoer	trend	Technologie en data leiden uw innovatie	Nieuwe technologie en\nconcepten worden steeds meer\nontwikkeld in samenwerking met ketenpartners. De sterk toegenomen\ncongestie vraagt om route-optimalisatie door real time traffic information. Hierbij\nwordt ook de kracht van waardevolle data onderkend. Veel van deze\ninformatie is al beschikbaar, wat flexibele transportplanning en\nonline communicatie met opdrachtgevers mogelijk maakt. Nieuwe\ndatatechnologie gecombineerd met grondige analyse zijn leidend voor\ninnovatie op bestaande processen.	182
Transport-en-Logistiek	opslag	trend	Logistiek vastgoed groeit verder	De sector investeert aanhoudend in vastgoed. E-commerce volumes\nvraagt om grootschalige distributiecentra, met name rond de bekende\nlogistieke hotspots. Nederland is een aantrekkelijk vestigingsland met\ngunstig financieel klimaat voor (internationale) beleggers en\ngebruikers. De markt voor sale-and-lease-back transacties is\ngroeiende. Schaarste aan beschikbare grondruimte zal leiden tot een\nhuurprijsstijging in tegenstelling tot die locaties waarbij nog\nvoldoende ontwikkelruimte is.	183
Transport-en-Logistiek	opslag	trend	Modern logistiek vastgoed geeft voordeel	Logistieke dienstverleners willen strategisch investeren in de\nlogistieke optimalisatie, dus ook in vastgoed. Naast uitbreiding in\nvierkante meters zijn efficiency, en concentratie belangrijke\nmotieven voor duurzame\nnieuwbouw. Denk aan BREEAM-certificering, zonnepanelen, LED\nverlichting en recycling van warmte, afval en water. Dit leidt tot\nlagere energielasten en een gezond binnenklimaat (stil, goede\nverlichting) voor de medewerkers. Andere innovatie is er op het\ngebied van hoger en flexibel bouwen.	184
Transport-en-Logistiek	opslag	trend	Urbanisatie zet deur open naar nieuwe vastgoedbehoefte	De snel groeiende urbanisatie geeft bijzondere uitdagingen op\ngebied van belevering van de stad. Dat geldt voor bouwlogistiek,\npakketbelevering en de bevoorrading van winkels en restaurants. Een\ngeheel nieuwe visie moet worden ontwikkeld op het thema duurzame stadsdistributie en\nbouwlogistiek. Er komt een groeiende behoefte aan kleinere\ndistributiecentra in de rand van stedelijke gebieden. Dit zal\nkansen bieden voor de herontwikkeling van zowel bestaand, alsmede\nnieuw te ontwikkelen logistiek vastgoed.	185
Transport-en-Logistiek	short-sea-shipping	trend	Regelgeving vraagt om capaciteiten op divers gebied	Short sea ondernemingen hebben te maken met uitgebreide Europese\nWet en Regelgeving (IMO) op gebied van uitstootnormen (low sulpher,\nbalast water, Co2 en Nox). Gezien de diversiteit die deze subsector\nkenmerkt betekent het in de praktijk een grote uitdaging om\ncompliant te blijven aan deze regelgeving. Ondernemers hebben\nfinancierings- en personele capaciteit nodig om de nieuwe regels\npraktisch toe te passen. Enkel een gezamenlijke\nverantwoordelijkheid van alle ketenpartijen kan leiden tot een\nrendabele investering. Dit zal de consolidatietrend verder\nstimuleren.	186
Transport-en-Logistiek	short-sea-shipping	trend	Short sea kan zich als modaliteit opnieuw positioneren	Alliantievorming bij deepsea-rederijen leidt tot herschikking\nvan de “first call” bij Europese zeehavens. Short Sea als “deep sea\nshipping feeder traffic” is cruciaal voor het accommoderen van de\nintra-Europese logistiek.. Met name voor producten met relatief\nlage waarde en hoge volumes. Deze modaliteit voor internationaal\nvervoer heeft potentie als serieus alternatief binnen de logistieke\nketen. De door-to-door service zal moeten worden aangescherpt, o.m.\ndoor samenwerkring met andere modaliteiten. Het is tijd voor short\nsea om zich als modaliteit opnieuw te positioneren.	187
Transport-en-Logistiek	short-sea-shipping	trend	Innovatie en Human Capital	Innovatie en human capital zijn toekomstbepalende thema’s voor\nde maritieme sector. Op het gebied van innovatie wordt de\nontwikkeling van autonoom transport in de scheepvaart nauw gevolgd,\nnaast aandacht voor vernieuwing ten behoeve van een veilige en\nschone scheepvaart. Voor het behoud van de toppositie binnen het\nmaritieme cluster is een gezonde ontwikkeling van de arbeidsmarkt\nnoodzakelijk. Sector moet inzetten op het aantrekken van jong en\nhoog opgeleid personeel om aan te sluiten op de snel veranderende\narbeidsmarkt, gericht op innovatief ondernemen.	188
Utilities	wind-solar	trend	Aandeel hernieuwbare energie stijgt	Het aandeel hernieuwbare energie in de energiemix zal blijven\ntoenemen, wat goed is voor de branche. Binnenkort zal de regering\nkomen met plannen hoe invulling te gaan geven aan de (Europese)\n2030 doelstellingen. Ook zal het nut en de noodzaak van\nsubsidieregelingen zoals voor zonne-energie de salderingsregeling\ngeëvalueerd gaan worden. Zolang hernieuwbare energie afhankelijk\nblijft van subsidies zal het politieke beleid ten aanzien hiervan\nwel een onzekere factor blijven met betrekking tot\ninvesteringsbeslissingen.	189
Utilities	wind-solar	trend	Minder contracten	Het aantal contracten bij de bouw van een park wordt steeds\nminder. Voorheen waren er rustig meer dan tien contracten en dan\nmoest de sponsor/energiebedrijf al deze partijen managen. De\nhuidige trend is dat deze contracten veel vaker worden gemanaged\ndoor slechts twee tot vijf grote partijen. Banken vinden dit\naangenaam. Liever dat er twee grote partijen zijn die zelf de\nsub-aannemers managen, dan dat er tien verschillende aannemers door\nhet project gemanaged moeten worden.	190
Utilities	wind-solar	trend	Efficientere productie en lagere kosten	De offshore wind markt wordt steeds meer volwassen en de\nwaardeketen krijgt met de langetermijn-tender steeds meer\nzekerheden. Dit resulteert in efficiëntere productie en services,\nhetgeen de kosten van de windenergie doet dalen. Zo is ook de\nNederlandse tender ingericht, en het lijkt er op dat de markt de\ngeprognotiseerde kostenreductie van 40 procent daadwerkelijk kan\nleveren.	191
Zakelijke-dienstverlening	accountantskantoren	trend	Aangescherpte regels dwingen kantoren tot keuzes	Door scherpere wet- en regelgeving moet de kwaliteit van audits\nomhoog. Deze slag maken kost tijd en moeite, die niet alle\naccountantskantoren kunnen opbrengen. Sommige accountants zien\ndaarom af van hun auditdiensten. Andere kantoren kiezen ervoor om\ndeze juist wél aan te bieden. Ze gebruiken de service als\ninstrument om zich als complete dienstverlener in de markt te\nzetten. \nLees meer.	192
Zakelijke-dienstverlening	accountantskantoren	trend	Centrale rol voor Management Informatie Systemen	Management Informatie Systemen zijn een essentieel onderdeel van\nde waardepropositie van accountants. Het mes snijdt aan twee\nkanten: klanten krijgen realtime inzicht in hun performance,\nterwijl accountants de data kunnen gebruiken om hun adviezen en\naudits aan te scherpen. Lees\nmeer. 	193
Zakelijke-dienstverlening	accountantskantoren	trend	Accountancy vergt combinatie van vaardigheden	Accountants hebben andere vaardigheden nodig. Analytische kracht\nblijft essentieel, maar moet vaker worden ingezet op Big Data- en\nBlockchain-vraagstukken. Inlevingsvermogen en sociale vaardigheden\nzijn vooral belangrijk voor de adviespraktijk. Een bedrijfscultuur\ndie dit ondersteunt en het mogelijk maakt om creatieve\nklantoplossingen te creëren, is hiervoor noodzakelijk.\nDe ‘zachte’ – bedrijfscultuur- kant krijgt ook binnen de\naccountancy steeds meer aandacht: het wordt een belangrijke basis\nvan onderscheidend vermogen. Ook voor het vinden en binden van\ntalent aan de eigen organisatie.\nLees meer.\n\nLees hier ook meer.	194
Zakelijke-dienstverlening	advocatenkantoren	trend	Complexer speelveld voor kleine kantoren	Voor regionale kantoren is het moeilijker om klanten te binden\nen bedienen. Grote advocatenkantoren zijn in het voordeel; via hun\ninternationale netwerk trekken ze makkelijk multinationals als\nklant aan. Ook hebben ze voldoende middelen om IT-investeringen te\ndoen, die nodig zijn om eenvoudig werk uit te besteden of te\nautomatiseren. Voor regionale kantoren is dit moeilijker: zij\nhebben een kleiner netwerk en een beperkt budget. \nLees meer.	195
Zakelijke-dienstverlening	advocatenkantoren	trend	Adviseren of standaardiseren?	Advocaten die zich op een nichemarkt richten, doen het goed. In\nde markt verschijnen steeds meer nieuwe, jonge bedrijven die een\nspecifieke juridische dienst sneller, beter en goedkoper aanbieden\ndan traditionele partijen. Soms komen deze nieuwkomers niet uit de\nadvocatuur, maar bijvoorbeeld uit de ICT. Het gaat meestal om\neenvoudige diensten, die makkelijk te standaardiseren zijn. Advies\nbij complexere vraagstukken is een stuk moeilijker te\nautomatiseren. Het lijkt er dus op dat de keuze gaat tussen advies\nop maat en digitalisering. \nLees meer.	196
Zakelijke-dienstverlening	advocatenkantoren	trend	Met alleen kennis bent u er niet	Empathische en commerciële vaardigheden worden steeds\nbelangrijker. Ook de advocaat moet meer achter nieuwe business aan\njagen; in dat opzicht verschilt hij niet van de accountant of\nconsultant. Daarnaast moeten advocaten hun sterke specialistische\nkennis combineren met goede sociale vaardigheden. \nLees meer.	197
Zakelijke-dienstverlening	beveiligingsbedrijven	trend	Beveiliging wordt digitaal	Door de overgang van analoge naar digitale beveiliging is de\noperational efficiency in de sector toegenomen. Digitale\nbeeldverwerking, camera’s van hoge kwaliteit en\nvideo-analyseapplicaties zorgen voor meer alertheid en efficiëntie.\nNaast nieuwe apparatuur, vraagt digitale beveiliging andere\nvaardigheden; daarom zijn investeringen in materiaal en personeel\nnodig. \nLees meer.	198
Zakelijke-dienstverlening	beveiligingsbedrijven	trend	Markt van specialisten en allrounders	De markt is sterk verzadigd, waardoor manbewaking tot een\ncommodity is verworden. Ondernemers maken daarom de strategische\nkeuze tussen specialisatie of dienstenuitbreiding. Voor\nspecialisatie liggen de meeste kansen in markten waarvoor speciale\nrichtlijnen gelden: denk aan beveiliging van vliegvelden of grote\nevenementen. Bij een keuze voor uitbreiding wordt beveiliging vaak\naangevuld met diensten als schoonmaken en catering; zo onstaat een\n‘allround facility management’-organisatie. Lees meer.	199
Zakelijke-dienstverlening	beveiligingsbedrijven	trend	Groeiende vraag naar centrale high-tech preventie	Beveiliging is bij steeds meer opdrachtgevers een\nseniormanagement-prioriteit. Met het toenemende bewustzijn over\nrisico’s en bedreigingen groeit ook de interesse in\nbeveilingsgerelateerde onderwerpen. De focus ligt vooral op\npreventieve maatregelen, nieuwe technologieën en de centralisatie\nvan beveiliging om de ‘on-site’ bewaking te vervangen. Lees meer.	200
Zakelijke-dienstverlening	gerechtsdeurwaardersincassobureaus	trend	Voorkomen is beter dan genezen	De dienstverlening van deurwaarders en incassobureaus\nverschuift. In plaats van niet-betaalde bedragen achteraf te innen,\nzetten ze in op preventie van wanbetaling. Via data-analyse brengen\nze het betaalgedrag van klanten in kaart en doen voorspellingen\nvoor de toekomst. Vooral incassobureaus bieden vaak ‘credit\nmanagement’ aan.	201
Zakelijke-dienstverlening	notariskantoren	trend	Behoefte aan samenwerking met specialisten	De aantrekkende huizenmarkt heeft niet voor een sterke\nrendementsverbetering gezorgd; de margedruk bij het passeren van\nhypothecaire transacties groeit. Hierdoor blijft het noodzaak om\nuit te breiden naar dienstverlening rond familie- en\nondernemersrecht. Steeds meer notarissen beseffen dat ze deze\ndiensten alleen in samenwerking met netwerkpartners kunnen\ninvullen, zonder dat ze deze specialisten in dienst hoeven te\nnemen. Lees\nmeer.\nLees ook.	204
Zakelijke-dienstverlening	notariskantoren	trend	Operational efficiency is noodzaak	Disintermediatie in het notariaat blijft doorgaan, doordat\nnieuwe toetreders transparantie brengen in tarieven. Het is dan ook\nzaak om eenvoudige producten, zoals huwelijkse en algemene\nvoorwaarden en samenlevingscontracten, via IT strak in te richten.\nHierdoor verschuift de focus naar operational efficiency. \nLees meer.	205
Zakelijke-dienstverlening	notariskantoren	trend	Proactief maatwerk naast standaarddiensten	Naast efficiënte standaarddiensten, moeten notarissen ook\nproactief maatwerk leveren. Door voorlichtingssessies rond\nwetswijzigingen te organiseren, actief te zijn op social media en\nmee te doen in ondernemersnetwerken, kunnen ze hun klantenkring\nzelfstandig uitbreiden. Bovendien krijgen klanten de kans om hun\nwensen duidelijk te maken. Belangrijke informatie voor de notaris,\ndie hierop in kan spelen.	206
Zakelijke-dienstverlening	organisatie-adviesbureaus	trend	Kenniscombinaties leveren meerwaarde op	Klanten vragen om multidisciplinair advies. Dit betekent dat een\nteam van verschillende specialisten samen aan het vraagstuk van de\nklant werkt. Oplossingen komen tot stand op basis van inbreng uit\nmeerdere disciplines. De combinatie van verschillende soorten\nspecialistische kennis creëert een sterke waardepropositie,\nbijvoorbeeld IT, marketing en management consultancy. \nLees meer.\nLees ook:\n\nen verder:	207
Zakelijke-dienstverlening	organisatie-adviesbureaus	trend	Sectorspecifieke kennis en specialisatie wordt steeds\nbelangrijker	Sectorkennis en ervaring met sectorspecifieke vraagstukken is\nessentieel. Klantoplossingen binnen de agrarische sector kunnen\nmoeilijk binnen retail worden geïmplementeerd. De behoefte aan\nsectorkennis in combinatie met een multidisciplinaire benadering\nvergt veel flexibiliteit van consultants.\nHet gebrek aan innovatiekracht binnen grote bedrijven is een\ngrote kans voor adviesbureaus. Specialisatie wordt steeds\nbelangrijker en ook het beter verwoorden van de waardepropositie:\nweg van uurtje-factuurtje naar revenu sharing en zelfs profit\nsharing. Benchmarking blijft belangrijk voor grote bedrijven.\nLees meer.	208
Zakelijke-dienstverlening	organisatie-adviesbureaus	trend	Groot en klein doen het goed	De topspelers aan de bovenkant van de markt, zoals BCG, McKinsey\nen Bain Company, doen het goed. Net als veel kleine,\ngespecialiseerde consultants. Er komen steeds meer kleine\nadviesbureaus die geen eigen kantoor meer hebben en dus\nconcurrerend zijn in hun kostenstructuur.\nVooral de middelgrote bedrijven hebben het moeilijk. Ze hebben\nniet de zekerheid van een internationaal netwerk, en hun budget om\nte investeren in specialistische kennis is beperkt. \nLees meer.	209
Zakelijke-dienstverlening	schoonmaakbedrijven	trend	Markt van specialisten en allrounders	De markt is sterk verzadigd, waardoor schoonmaak tot een\ncommodity is verworden. Ondernemers maken daarom de strategische\nkeuze tussen specialisatie of dienstenuitbreiding. Voor\nspecialisatie liggen de meeste kansen in de ‘technische’\nschoonmaak, zoals vliegtuigen of installaties reinigen. Bij een\nkeuze voor uitbreiding wordt schoonmaak vaak aangevuld met diensten\nals beveiliging en catering; zo onstaat een ‘allround facility\nmanagement’-organisatie. Lees meer.	210
Zakelijke-dienstverlening	schoonmaakbedrijven	trend	Nieuwe oplossingen voor nieuwe werkvormen	Onze manier van werken verandert op twee manieren. Aan de ene\nkant zorgt Het Nieuwe Werken ervoor dat kantoorruimtes minder\nworden gebruikt. Aan de andere kant past een groeiend aantal\nondernemingen zijn organisatiestructuur aan, vooral door\nzelfsturende teams op te zetten. Hierdoor groeit de behoefte aan\nstrategisch advies over facilitaire diensten en de inrichting van\nde werkomgeving. Lees\nmeer.	211
Zakelijke-dienstverlening	schoonmaakbedrijven	trend	Samenwerking met IT levert innovaties op	De inzet van nieuwe technologieën versterkt de waardepropositie\nvan ondernemers in de schoonmaakbranche. Met name Big Data-gebruik\nkan klanten relevante managementinformatie opleveren, bijvoorbeeld\ninzage in het gebruik van ruimtes of faciliteiten. De samenwerking\nmet IT wordt essentieel. Zo kunnen schoonmaak- en IT-bedrijven apps\nontwikkelen waarmee je een parkeerplaats reserveert, de\nkamertemperatuur aanpast of koffie bestelt. Lees meer.	212
Zakelijke-dienstverlening	uitzendbureaus	trend	Innovatie is een uitdaging	Ondanks de economische rugwind, hebben spelers in HR-services\nmoeite om hun marges te behouden. Het lukt uitzenders, payrollers,\ndetacheerders en zzp-bemiddelaars niet altijd om hun huidige\nwaardepropositie te innoveren. Om hun positie toch zeker te\nstellen, kunnen ze zich explicieter toeleggen op strategisch\nadvies. Een andere optie is om meer verschillende diensten aan te\nbieden, zodat ze klanten volledig kunnen ontzorgen. Lees meer.\nLees\nook:	213
Zakelijke-dienstverlening	uitzendbureaus	trend	Uitzendbureaus bieden aanvullende diensten	Uitzendbureaus kiezen er vaker voor om de flexbehoefte van\nklanten breed in te vullen. Hiervoor bieden ze extra diensten aan,\nzoals payrolling of detachering. Voor klanten is de contractvorm\nondergeschikt aan de mogelijkheid om op elk moment over de juiste\nkennis te beschikken.\nDe huidige krapte op de arbeidsmarkt zorgt er wel voor dat de\ntoegang tot geschikt personeel weer aan importantie wint.\nUitzenders lijken daarbij goede kaarten te hebben middels hun\nwerving- en selectiefunctie.\nLees\nmeer.	214
Zakelijke-dienstverlening	uitzendbureaus	trend	Onzekerheid omtrent payrolling verdwenen	Een recente uitspraak van de Hoge Raad omtrent de zogeheten\nallocatiefunctie van uitzenders en payrollers heeft niet geleid tot\neen verbod op payrolling als flexinstrument (de payroller is\njuridische werkgever).\n \nLees meer.	215
\.


--
-- Name: trend_table_trend_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('trend_table_trend_id_seq', 430, true);


--
-- Data for Name: znw_in_prog_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY znw_in_prog_table (znw_prog_id) FROM stdin;
\.


--
-- Name: znw_in_prog_table_znw_prog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('znw_in_prog_table_znw_prog_id_seq', 1, false);


--
-- Data for Name: znw_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY znw_table (znw, znw_id) FROM stdin;
\.


--
-- Name: znw_table_znw_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('znw_table_znw_id_seq', 1, false);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: con_of_znw_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY con_of_znw_table
    ADD CONSTRAINT con_of_znw_table_pkey PRIMARY KEY (con_of_znw_id);


--
-- Name: con_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY con_table
    ADD CONSTRAINT con_table_pkey PRIMARY KEY (con_id);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: generic_words_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY generic_words
    ADD CONSTRAINT generic_words_pkey PRIMARY KEY (generic_word_id);


--
-- Name: info_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY info_table
    ADD CONSTRAINT info_table_pkey PRIMARY KEY (info_id);


--
-- Name: prog_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY prog_table
    ADD CONSTRAINT prog_table_pkey PRIMARY KEY (prog_id);


--
-- Name: trend_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY trend_table
    ADD CONSTRAINT trend_table_pkey PRIMARY KEY (trend_id);


--
-- Name: znw_in_prog_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY znw_in_prog_table
    ADD CONSTRAINT znw_in_prog_table_pkey PRIMARY KEY (znw_prog_id);


--
-- Name: znw_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY znw_table
    ADD CONSTRAINT znw_table_pkey PRIMARY KEY (znw_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

