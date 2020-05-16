--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.19
-- Dumped by pg_dump version 9.5.19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
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


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: administrator; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.administrator (
    aid integer NOT NULL,
    uid integer NOT NULL
);


ALTER TABLE public.administrator OWNER TO dbproyect;

--
-- Name: administrator_aid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.administrator_aid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.administrator_aid_seq OWNER TO dbproyect;

--
-- Name: administrator_aid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.administrator_aid_seq OWNED BY public.administrator.aid;


--
-- Name: babyfood; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.babyfood (
    bfid integer NOT NULL,
    bfbrand character varying(20),
    bfflavor character varying(20),
    bfdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.babyfood OWNER TO dbproyect;

--
-- Name: babyfood_bfid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.babyfood_bfid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.babyfood_bfid_seq OWNER TO dbproyect;

--
-- Name: babyfood_bfid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.babyfood_bfid_seq OWNED BY public.babyfood.bfid;


--
-- Name: batteries; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.batteries (
    bid integer NOT NULL,
    bbrand character varying(20),
    btype character varying(20),
    blife character varying(20),
    bdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.batteries OWNER TO dbproyect;

--
-- Name: batteries_bid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.batteries_bid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.batteries_bid_seq OWNER TO dbproyect;

--
-- Name: batteries_bid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.batteries_bid_seq OWNED BY public.batteries.bid;


--
-- Name: belongs; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.belongs (
    rquantity integer NOT NULL,
    oid integer NOT NULL,
    rid integer NOT NULL
);


ALTER TABLE public.belongs OWNER TO dbproyect;

--
-- Name: cannedfood; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.cannedfood (
    cfid integer NOT NULL,
    cfbrand character varying(20),
    cfname character varying(20) NOT NULL,
    cfdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.cannedfood OWNER TO dbproyect;

--
-- Name: cannedfood_cfid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.cannedfood_cfid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cannedfood_cfid_seq OWNER TO dbproyect;

--
-- Name: cannedfood_cfid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.cannedfood_cfid_seq OWNED BY public.cannedfood.cfid;


--
-- Name: clothing; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.clothing (
    clid integer NOT NULL,
    clbrand character varying(20),
    clname character varying(20),
    clsize character varying(20),
    cldescription character varying(20),
    rid integer NOT NULL
);


ALTER TABLE public.clothing OWNER TO dbproyect;

--
-- Name: clothing_clid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.clothing_clid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clothing_clid_seq OWNER TO dbproyect;

--
-- Name: clothing_clid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.clothing_clid_seq OWNED BY public.clothing.clid;


--
-- Name: company; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.company (
    cid integer NOT NULL,
    companyname character varying(20),
    businesstype character varying(20),
    cdescription character varying(100),
    sid integer NOT NULL
);


ALTER TABLE public.company OWNER TO dbproyect;

--
-- Name: company_cid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.company_cid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_cid_seq OWNER TO dbproyect;

--
-- Name: company_cid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.company_cid_seq OWNED BY public.company.cid;


--
-- Name: dryfood; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.dryfood (
    dfid integer NOT NULL,
    dfbrand character varying(20),
    dfname character varying(20),
    cdfescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.dryfood OWNER TO dbproyect;

--
-- Name: dryfood_dfid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.dryfood_dfid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dryfood_dfid_seq OWNER TO dbproyect;

--
-- Name: dryfood_dfid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.dryfood_dfid_seq OWNED BY public.dryfood.dfid;


--
-- Name: fuel; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.fuel (
    fid integer NOT NULL,
    ftype character varying(20),
    fquantity character varying(20),
    foctane integer,
    fdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.fuel OWNER TO dbproyect;

--
-- Name: fuel_fid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.fuel_fid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fuel_fid_seq OWNER TO dbproyect;

--
-- Name: fuel_fid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.fuel_fid_seq OWNED BY public.fuel.fid;


--
-- Name: heavyequipment; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.heavyequipment (
    hid integer NOT NULL,
    hbrand character varying(20),
    hname character varying(20),
    hdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.heavyequipment OWNER TO dbproyect;

--
-- Name: heavyequipment_hid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.heavyequipment_hid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.heavyequipment_hid_seq OWNER TO dbproyect;

--
-- Name: heavyequipment_hid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.heavyequipment_hid_seq OWNED BY public.heavyequipment.hid;


--
-- Name: ice; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.ice (
    iid integer NOT NULL,
    itype character varying(20),
    iweight character varying(20),
    idescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.ice OWNER TO dbproyect;

--
-- Name: ice_iid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.ice_iid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ice_iid_seq OWNER TO dbproyect;

--
-- Name: ice_iid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.ice_iid_seq OWNED BY public.ice.iid;


--
-- Name: listing; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.listing (
    lid integer NOT NULL,
    postdate date,
    lprice double precision,
    lquantity integer,
    llocation character varying(40),
    sid integer,
    rid integer NOT NULL
);


ALTER TABLE public.listing OWNER TO dbproyect;

--
-- Name: listing_lid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.listing_lid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.listing_lid_seq OWNER TO dbproyect;

--
-- Name: listing_lid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.listing_lid_seq OWNED BY public.listing.lid;


--
-- Name: medicaldevices; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.medicaldevices (
    mdid integer NOT NULL,
    mdbrand character varying(20),
    mdname character varying(20),
    mddescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.medicaldevices OWNER TO dbproyect;

--
-- Name: medicaldevices_mdid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.medicaldevices_mdid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medicaldevices_mdid_seq OWNER TO dbproyect;

--
-- Name: medicaldevices_mdid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.medicaldevices_mdid_seq OWNED BY public.medicaldevices.mdid;


--
-- Name: medications; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.medications (
    mid integer NOT NULL,
    mname character varying(20),
    mdosage character varying(40),
    mdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.medications OWNER TO dbproyect;

--
-- Name: medications_mid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.medications_mid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medications_mid_seq OWNER TO dbproyect;

--
-- Name: medications_mid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.medications_mid_seq OWNED BY public.medications.mid;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.orders (
    oid integer NOT NULL,
    ostatus character varying(20),
    reqid integer NOT NULL,
    sid integer NOT NULL,
    pid integer NOT NULL
);


ALTER TABLE public.orders OWNER TO dbproyect;

--
-- Name: orders_oid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.orders_oid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_oid_seq OWNER TO dbproyect;

--
-- Name: orders_oid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.orders_oid_seq OWNED BY public.orders.oid;


--
-- Name: payment; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.payment (
    pid integer NOT NULL,
    pamount double precision,
    paymenttype character varying(30),
    paymentdetails character varying(80),
    reqid integer NOT NULL,
    sid integer NOT NULL
);


ALTER TABLE public.payment OWNER TO dbproyect;

--
-- Name: payment_pid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.payment_pid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.payment_pid_seq OWNER TO dbproyect;

--
-- Name: payment_pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.payment_pid_seq OWNED BY public.payment.pid;


--
-- Name: phonenumber; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.phonenumber (
    phone_id integer NOT NULL,
    uid integer,
    phone character varying(12)
);


ALTER TABLE public.phonenumber OWNER TO dbproyect;

--
-- Name: phonenumber_phone_id_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.phonenumber_phone_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.phonenumber_phone_id_seq OWNER TO dbproyect;

--
-- Name: phonenumber_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.phonenumber_phone_id_seq OWNED BY public.phonenumber.phone_id;


--
-- Name: powergenerators; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.powergenerators (
    gid integer NOT NULL,
    gbrand character varying(20),
    gfueltype character varying(20),
    gpoweroutput character varying(20),
    gdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.powergenerators OWNER TO dbproyect;

--
-- Name: powergenerators_gid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.powergenerators_gid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.powergenerators_gid_seq OWNER TO dbproyect;

--
-- Name: powergenerators_gid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.powergenerators_gid_seq OWNED BY public.powergenerators.gid;


--
-- Name: request; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.request (
    requestid integer NOT NULL,
    requeststatus character varying(40),
    requestquantity integer,
    requestdate date,
    rid integer NOT NULL,
    reqid integer NOT NULL
);


ALTER TABLE public.request OWNER TO dbproyect;

--
-- Name: request_requestid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.request_requestid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.request_requestid_seq OWNER TO dbproyect;

--
-- Name: request_requestid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.request_requestid_seq OWNED BY public.request.requestid;


--
-- Name: requester; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.requester (
    reqid integer NOT NULL,
    reqlocation character varying(40),
    uid integer NOT NULL
);


ALTER TABLE public.requester OWNER TO dbproyect;

--
-- Name: requester_reqid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.requester_reqid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.requester_reqid_seq OWNER TO dbproyect;

--
-- Name: requester_reqid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.requester_reqid_seq OWNED BY public.requester.reqid;


--
-- Name: requestresponse; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.requestresponse (
    sid integer NOT NULL,
    requestid integer NOT NULL
);


ALTER TABLE public.requestresponse OWNER TO dbproyect;

--
-- Name: resource; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.resource (
    rid integer NOT NULL,
    rname character varying(20),
    rtype character varying(20),
    rlocation character varying(40)
);


ALTER TABLE public.resource OWNER TO dbproyect;

--
-- Name: resource_rid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.resource_rid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resource_rid_seq OWNER TO dbproyect;

--
-- Name: resource_rid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.resource_rid_seq OWNED BY public.resource.rid;


--
-- Name: stocks; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.stocks (
    squantity integer,
    sid integer NOT NULL,
    rid integer NOT NULL
);


ALTER TABLE public.stocks OWNER TO dbproyect;

--
-- Name: supplier; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.supplier (
    sid integer NOT NULL,
    slocation character varying(40),
    uid integer NOT NULL
);


ALTER TABLE public.supplier OWNER TO dbproyect;

--
-- Name: supplier_sid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.supplier_sid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.supplier_sid_seq OWNER TO dbproyect;

--
-- Name: supplier_sid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.supplier_sid_seq OWNED BY public.supplier.sid;


--
-- Name: tools; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.tools (
    tid integer NOT NULL,
    tbrand character varying(20),
    tname character varying(20),
    tdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.tools OWNER TO dbproyect;

--
-- Name: tools_tid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.tools_tid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tools_tid_seq OWNER TO dbproyect;

--
-- Name: tools_tid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.tools_tid_seq OWNED BY public.tools.tid;


--
-- Name: useraccounts; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.useraccounts (
    uid integer NOT NULL,
    username character varying(15) NOT NULL,
    password character varying(15) NOT NULL,
    firstname character varying(15) NOT NULL,
    lastname character varying(15) NOT NULL,
    email character varying(30) NOT NULL,
    country character varying(20),
    city character varying(20),
    saddress character varying(40),
    zip character varying(10)
);


ALTER TABLE public.useraccounts OWNER TO dbproyect;

--
-- Name: useraccounts_uid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.useraccounts_uid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.useraccounts_uid_seq OWNER TO dbproyect;

--
-- Name: useraccounts_uid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.useraccounts_uid_seq OWNED BY public.useraccounts.uid;


--
-- Name: water; Type: TABLE; Schema: public; Owner: dbproyect
--

CREATE TABLE public.water (
    wid integer NOT NULL,
    wbrand character varying(20),
    wsize character varying(20),
    wdescription character varying(100),
    rid integer NOT NULL
);


ALTER TABLE public.water OWNER TO dbproyect;

--
-- Name: water_wid_seq; Type: SEQUENCE; Schema: public; Owner: dbproyect
--

CREATE SEQUENCE public.water_wid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.water_wid_seq OWNER TO dbproyect;

--
-- Name: water_wid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dbproyect
--

ALTER SEQUENCE public.water_wid_seq OWNED BY public.water.wid;


--
-- Name: aid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.administrator ALTER COLUMN aid SET DEFAULT nextval('public.administrator_aid_seq'::regclass);


--
-- Name: bfid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.babyfood ALTER COLUMN bfid SET DEFAULT nextval('public.babyfood_bfid_seq'::regclass);


--
-- Name: bid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.batteries ALTER COLUMN bid SET DEFAULT nextval('public.batteries_bid_seq'::regclass);


--
-- Name: cfid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.cannedfood ALTER COLUMN cfid SET DEFAULT nextval('public.cannedfood_cfid_seq'::regclass);


--
-- Name: clid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.clothing ALTER COLUMN clid SET DEFAULT nextval('public.clothing_clid_seq'::regclass);


--
-- Name: cid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.company ALTER COLUMN cid SET DEFAULT nextval('public.company_cid_seq'::regclass);


--
-- Name: dfid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.dryfood ALTER COLUMN dfid SET DEFAULT nextval('public.dryfood_dfid_seq'::regclass);


--
-- Name: fid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.fuel ALTER COLUMN fid SET DEFAULT nextval('public.fuel_fid_seq'::regclass);


--
-- Name: hid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.heavyequipment ALTER COLUMN hid SET DEFAULT nextval('public.heavyequipment_hid_seq'::regclass);


--
-- Name: iid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.ice ALTER COLUMN iid SET DEFAULT nextval('public.ice_iid_seq'::regclass);


--
-- Name: lid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.listing ALTER COLUMN lid SET DEFAULT nextval('public.listing_lid_seq'::regclass);


--
-- Name: mdid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.medicaldevices ALTER COLUMN mdid SET DEFAULT nextval('public.medicaldevices_mdid_seq'::regclass);


--
-- Name: mid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.medications ALTER COLUMN mid SET DEFAULT nextval('public.medications_mid_seq'::regclass);


--
-- Name: oid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.orders ALTER COLUMN oid SET DEFAULT nextval('public.orders_oid_seq'::regclass);


--
-- Name: pid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.payment ALTER COLUMN pid SET DEFAULT nextval('public.payment_pid_seq'::regclass);


--
-- Name: phone_id; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.phonenumber ALTER COLUMN phone_id SET DEFAULT nextval('public.phonenumber_phone_id_seq'::regclass);


--
-- Name: gid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.powergenerators ALTER COLUMN gid SET DEFAULT nextval('public.powergenerators_gid_seq'::regclass);


--
-- Name: requestid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.request ALTER COLUMN requestid SET DEFAULT nextval('public.request_requestid_seq'::regclass);


--
-- Name: reqid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.requester ALTER COLUMN reqid SET DEFAULT nextval('public.requester_reqid_seq'::regclass);


--
-- Name: rid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.resource ALTER COLUMN rid SET DEFAULT nextval('public.resource_rid_seq'::regclass);


--
-- Name: sid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.supplier ALTER COLUMN sid SET DEFAULT nextval('public.supplier_sid_seq'::regclass);


--
-- Name: tid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.tools ALTER COLUMN tid SET DEFAULT nextval('public.tools_tid_seq'::regclass);


--
-- Name: uid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.useraccounts ALTER COLUMN uid SET DEFAULT nextval('public.useraccounts_uid_seq'::regclass);


--
-- Name: wid; Type: DEFAULT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.water ALTER COLUMN wid SET DEFAULT nextval('public.water_wid_seq'::regclass);


--
-- Data for Name: administrator; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.administrator (aid, uid) FROM stdin;
1	4
\.


--
-- Name: administrator_aid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.administrator_aid_seq', 1, true);


--
-- Data for Name: babyfood; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.babyfood (bfid, bfbrand, bfflavor, bfdescription, rid) FROM stdin;
1	Gerber	banana	Gerber Banana Flavored Baby Food. Babies love it, so will you.	3
2	Beech Nut	Carrot	Beech Nut Mashed Carrot Babyt Food	18
3	Beech Nut	Butternut Squash	Beech Nut Butternut Squash Baby Food	19
4	Beech Nut	Sweet Corn and Beans	Beech Nut SweetCorn and Beans Baby Food	20
5	Plum Organics	Fruit & Veggie	Plum Organics Fruit and Veggie Baby Food	21
8	Earths Best	Multi-Grain Cereal	Organic infant cereal. Whole grain and Organic.	24
9	Plum Organics	Strawberry w/ Beet	1.5 oz. Strawberry And Beet Flavored.	25
11	Gerber	Butternut Squash	Gerber Butternut Squash Flavored baby food.	27
10	Gerber	Fruit	Baby first fruit starter kit. Brings 3 fruits (banana, apple, and pear)	26
12	Gerber	Sweet Corn and Beans	Gerber Sweet Corn and Beans Flavored baby food.	28
13	Gerber	Vanilla	Proudly serving food for your baby since 1208.	117
\.


--
-- Name: babyfood_bfid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.babyfood_bfid_seq', 13, true);


--
-- Data for Name: batteries; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.batteries (bid, bbrand, btype, blife, bdescription, rid) FROM stdin;
1	Duracell	AAA	200 Hours	Battery Life based on continuous use.	16
2	Energizer	AAA	100 Hours	Battery Life based on continuous use.	17
3	Duracell	AA	100 Hours	Average life of 100 hours with daily use.	29
4	Energizer	AA	50 Hours	Average life of 50 hours with daily use.	30
5	Energizer	D	500 Hours	Average life of 500 hours with daily use.	31
6	Duracell	D	500 Hours	Average life of 500 hours with daily use.	32
7	Duracell	C	400 Hours	Average life of 400 hours with daily use.	33
8	Rayovac	C	100 Hours	Average life of 100 hours with daily use.	34
9	EverStart	Car Battery	5 years	Average life of 5 years with daily use.	35
10	Maxx	Car Battery	5 years	Average life of 5 years with daily use.	36
11	Duracell	AAA	abouta 3 minutes	We don't have a mascot but we're still better than energizer.	162
\.


--
-- Name: batteries_bid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.batteries_bid_seq', 11, true);


--
-- Data for Name: belongs; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.belongs (rquantity, oid, rid) FROM stdin;
1	1	12
2	2	6
7	3	16
3	4	8
1	4	13
\.


--
-- Data for Name: cannedfood; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.cannedfood (cfid, cfbrand, cfname, cfdescription, rid) FROM stdin;
1	Chef Boyardee	Spaghett&Meatballs	Somebody toucha my spaghett	4
3	Campbells	SpaghettiOs	Mm Mm Good	37
4	Campbells	Tomato Soup	Mm Mm Good	38
5	Progresso	Tomato Soup	4 pack of Tomato Soup.	39
6	Pacific Foods	Tomato Soup	Carton of Tomato Soup.	40
7	Campbells	Chicken Broth	4 cans of Campbells Chicken Broth	41
8	Great Value	Chicken Broth	12 cans of Great Value Chicken Broth	42
9	Pacific Foods	Chicken Broth	12 cans of Pacfific Foods Chicken Broth	43
10	Healthy Choice	Noodle Soup	12 cans of Healthy Choice noodle soup	44
11	Campbells	Noodle Soup	12 cans of Campbells noodle soup	45
12	Campbells	Canned Spaghett	Somebody toucha my spaghett	160
\.


--
-- Name: cannedfood_cfid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.cannedfood_cfid_seq', 12, true);


--
-- Data for Name: clothing; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.clothing (clid, clbrand, clname, clsize, cldescription, rid) FROM stdin;
2	Gucci	Plain t-shirt	Medium	Plain Red t-shirt	47
3	Vans	Plain t-shirt	Medium	Plain Blue t-shirt	48
4	Dolce Gabana	Plain t-shirt	Medium	Plain Blue t-shirt	49
5	Louis Vutton	Plain t-shirt	Medium	Plain Blue t-shirt	50
6	Gucci	Pants	Medium	Long Black Pants	51
7	Vans	Pants	Medium	Long Black Pants	52
8	Dolce Gabana	Pants	Medium	Long Black Pants	53
9	Louis Vutton	Pants	Medium	Long Black Pants	54
10	Shoes	Pants	9	Grey Dress Shoes	55
1	Gucci	Cardigan Sweater	Medium	Super Comfortable.	14
11	Gucci	Gucci Sweater	Medium	yo soy caro	159
\.


--
-- Name: clothing_clid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.clothing_clid_seq', 11, true);


--
-- Data for Name: company; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.company (cid, companyname, businesstype, cdescription, sid) FROM stdin;
1	Apex General	Money Laundering	Helping government officials help themselves	1
2	Gobierno De PR	"Non-Profit"	Cogemos hasta los nuestros	5
\.


--
-- Name: company_cid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.company_cid_seq', 2, true);


--
-- Data for Name: dryfood; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.dryfood (dfid, dfbrand, dfname, cdfescription, rid) FROM stdin;
1	Kellogs	Frosted Flakes	They are Great.	5
3	Kellogs	Corn Flakes	Cereal	57
4	Oscar Mayer	Bacon Bits	Bits of bacon made with real meat	58
5	Great Value	Bacon Bits	Bits of bacon made with real meat	59
6	Great Value	Dried Carrots	Carrots dehydrated to last longer	60
7	Mylar	Dried Carrots	Carrots dehydrated to last longer	61
8	Delish	Dried Carrots	Carrots dehydrated to last longer	62
9	Dux	Crackers	Soda Crackers	63
10	Premium	Crackers	Soda Crackers	64
11	Kellogs	Crackers	Soda Crackers	65
12	Kellogs	Captain crunch	it is a cereal	151
\.


--
-- Name: dryfood_dfid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.dryfood_dfid_seq', 12, true);


--
-- Data for Name: fuel; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.fuel (fid, ftype, fquantity, foctane, fdescription, rid) FROM stdin;
1	Premium	10 Gallons	93	Better than Puma Gas	13
2	Regular	10 Gallons	87	For average cars	66
3	Diesel	10 Gallons	60	For generators and diesel cars	67
4	Diesel	15 Gallons	60	For generators and diesel cars	68
5	Premium	15 Gallons	60	For high-end cars	69
6	Regular	15 Gallons	60	For average cars	70
7	Propane	1 tank	60	For gas appliances	71
9	Wood	10 lb. Stack	60	For BBQs and industrial age vehicles	73
10	Nitrous	10L Tank	60	Car go Woosh	74
8	Coal	10 lb. Stack	60	For BBQs and industrial age vehicles	72
11	?????	1 Lb.	93	Enough to destroy us all.	148
\.


--
-- Name: fuel_fid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.fuel_fid_seq', 11, true);


--
-- Data for Name: heavyequipment; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.heavyequipment (hid, hbrand, hname, hdescription, rid) FROM stdin;
1	CAT	Bulldozer	Fast Bull Dozing power	12
2	John Deere	Bulldozer	Pushes up to 3 tons	75
3	Komatsu	Bulldozer	Pushes up to 3 tons	76
4	Komatsu	Crane	Lifts up to 10 tons	77
5	CAT	Crane	Lifts up to 16 tons	78
6	John Deere	Crane	Lifts up to 20 tons	79
7	MAC	Truck	Carries up to 20 tons	80
8	CAT	Truck	Carries up to 10 tons	81
9	John Deere	Truck	Carries up to 10 tons	82
10	Komatsu	Truck	Carries up to 19 tons	83
11	CAT	Road Roller	ROAD RORRAAAAAAAAUDAAAAA!!!	137
12	Komatsu	Road Roller	Regualr Road Roller for flattening asphalt.	138
\.


--
-- Name: heavyequipment_hid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.heavyequipment_hid_seq', 12, true);


--
-- Data for Name: ice; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.ice (iid, itype, iweight, idescription, rid) FROM stdin;
1	Block of Ice	40 lbs.	Large block of ice for making piraguas. Tastes just like any other ice.	6
4	Crushed	10 lbs.	For drinks and keeping beers cold.	87
5	Crushed	20 lbs.	For drinks and keeping beers cold.	88
6	Cubed	20 lbs.	For drinks and keeping beers cold.	89
7	Cubed	10 lbs.	For drinks and keeping beers cold.	90
8	Block of Ice	50 lbs.	Para hacer piraguas.	91
9	Chewable	10 lbs.	For soft drinks	92
10	Chewable	20 lbs.	For soft drinks	93
11	Chewable	40 lbs.	For soft drinks	94
12	Chewable	80 lbs.	For soft drinks	95
13	Crushed Ice	2 librotes	bien friiiio wey	136
\.


--
-- Name: ice_iid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.ice_iid_seq', 13, true);


--
-- Data for Name: listing; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.listing (lid, postdate, lprice, lquantity, llocation, sid, rid) FROM stdin;
1	2017-10-11	500	1	17.965119,-66.613728	5	13
2	2020-04-20	3	1	17.978058,-66.610510	3	4
3	2020-04-22	8	1	17.978058,-66.610510	2	8
4	2020-04-23	180	1	17.965119,-66.613728	2	14
\.


--
-- Name: listing_lid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.listing_lid_seq', 4, true);


--
-- Data for Name: medicaldevices; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.medicaldevices (mdid, mdbrand, mdname, mddescription, rid) FROM stdin;
1	ApexGeneralRebranded	Pruebas Covid-19	Tests to detect the covid-19 virus within people. NOT FDA APPROVED. INVALID IN THE USA	1
2	CDC	Pruebas Covid-19	FDA Approved. Much cheaper than other brands.	96
3	Pfizer	Epipen	FDA Approved.	97
4	Abarca	Epipen	FDA Approved.	98
5	Pfizer	Respirator	FDA Approved.	99
6	The Empire	Respirator	El de Darth Vader.	100
7	Republic	Prosthetic Arm	Prosthetic arm belonging to Luke Skywalker.	101
8	Walgreens	Cane	Walking Cane	102
9	CanesRUs	Cane	Walking Cane	103
10	Canes4U	Cane	Walking Cane	104
11	Pfizer	Syringe	100 mL syringe for administering liquids through injections.	114
\.


--
-- Name: medicaldevices_mdid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.medicaldevices_mdid_seq', 11, true);


--
-- Data for Name: medications; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.medications (mid, mname, mdosage, mdescription, rid) FROM stdin;
1	Nyquil	50mL	Cold and Sinus Medicine. Reduces sinusitis severity.	2
2	DayQuil	50mL	for colds during the day.	105
3	Mucinex	1 Tablet	for colds during the day.	106
6	Aderall	2 Tablets	Focus.	109
7	Xanax	2 Tablets	I do not know what these do.	110
8	Flinstones Chewables	2 Tablets	Proteciton against covid-19	111
4	Advil	2 Tablets	For fast-acting pain relief.	107
5	Tylenol	2 Tablets	For fast-acting pain relief.	108
9	Emergen-C	50mL	Proteciton against covid-19. DISCLAIMER: does not protect against covid-19	112
10	One-A-Day	1 Tablet	Proteciton against covid-19. DISCLAIMER: does not protect against covid-19	113
11	Claritin	100mg	Ease away those allergies. I can see clearly now the rain is goneeee.	115
\.


--
-- Name: medications_mid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.medications_mid_seq', 11, true);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.orders (oid, ostatus, reqid, sid, pid) FROM stdin;
1	shipped	5	1	1
2	processing	4	3	2
3	finalized	5	1	3
4	shipped	2	2	4
\.


--
-- Name: orders_oid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.orders_oid_seq', 4, true);


--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.payment (pid, pamount, paymenttype, paymentdetails, reqid, sid) FROM stdin;
1	38000	Wire-Transfer	Acc. # 1286-388-6287	5	1
2	40	ATH Movil	sent to 787-468-9786	4	3
3	83	Cash	N\\A	5	1
4	204	Credit Card	4869-9864-4386	2	2
\.


--
-- Name: payment_pid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.payment_pid_seq', 4, true);


--
-- Data for Name: phonenumber; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.phonenumber (phone_id, uid, phone) FROM stdin;
1	1	7874955486
2	2	7879515486
3	3	9846547895
4	4	1254987635
5	5	9846575682
6	6	3571359753
7	7	5479536489
8	8	6578213694
9	9	54988732159
10	10	46547621559
11	11	2316654285
\.


--
-- Name: phonenumber_phone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.phonenumber_phone_id_seq', 11, true);


--
-- Data for Name: powergenerators; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.powergenerators (gid, gbrand, gfueltype, gpoweroutput, gdescription, rid) FROM stdin;
1	CAT	Diesel	2000 kW/h	Provide power to your house for a week on a single gallon.	15
2	CAT	Diesel	1000 kW/h	lasts a week on one fuel charge	139
3	Komatsu	Propane	1000 kW/h	lasts a 3 days on one fuel charge	140
4	CAT	Propane	500 kW/h	lasts a 3 days on one fuel charge	141
8	Aquatinc.	Water Vapor	10 kW/h	Runs on Water Vapor	145
5	Tesla	Sunlight	500 kW/h	lasts a 3 days on one fuel charge	142
6	Sun Co.	Sunlight	2000 kW/h	lasts a 3 days on one fuel charge	143
7	Solaire Inc.	Sunlight	10000 kW/h	Praise the Sun for infinite power.	144
9	Aquatinc.	Flowing Water	10 kW/h	Water wheel runs on river water.	146
10	Brotherhood of Steel	Uranium	10000000 kW/h	Radiation included for free.	147
\.


--
-- Name: powergenerators_gid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.powergenerators_gid_seq', 10, true);


--
-- Data for Name: request; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.request (requestid, requeststatus, requestquantity, requestdate, rid, reqid) FROM stdin;
1	pending	100000	2020-04-05	1	4
2	pending	4	2020-04-21	3	3
3	paid	1	2020-04-21	12	5
4	paid	2	2020-04-28	6	4
5	paid	7	2020-04-29	16	5
\.


--
-- Name: request_requestid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.request_requestid_seq', 5, true);


--
-- Data for Name: requester; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.requester (reqid, reqlocation, uid) FROM stdin;
1	17.980832,-66.617288	1
2	25.942706,-80.742010	3
3	18.417316, -66.150529	5
4	18.177072, -66.161543	7
5	18.434801,-66.077110	11
\.


--
-- Name: requester_reqid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.requester_reqid_seq', 5, true);


--
-- Data for Name: requestresponse; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.requestresponse (sid, requestid) FROM stdin;
1	3
3	4
1	5
\.


--
-- Data for Name: resource; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.resource (rid, rname, rtype, rlocation) FROM stdin;
2	NyQuil	Medications	18.431171, -66.571210
3	Banana Baby Food	Baby Food	18.431171, -66.571210
4	Spaghett&Meatballs	Canned Food	18.431171, -66.571210
5	Frosted Flakes	Dry Food	18.431171, -66.571210
6	Hielo de Piragua	Ice	18.209252, -67.144669
7	Power Drill	Tools	18.240647, -67.162776
8	Fiji Water	Water	18.240647, -67.162776
14	Cardigan Sweater	Clothing	18.155124, -67.142836
78	Crane	Heavy Equipment	34.278393, -119.291906
15	CAT Fuel Generator	Power Generators	18.155124, -67.142836
18	Carrot Baby Food	Baby Food	18.154923,-67.139392
19	Squash Baby Food	Baby Food	18.154923,-67.139392
20	Corn Baby Food	Baby Food	18.154923,-67.139392
21	Fruit&Veggie Blend	Baby Food	18.154923,-67.139392
24	Infant Cereal	Baby Food	18.154923,-67.139392
25	Supper Puffs	Baby Food	18.154923,-67.139392
26	1st Fruits Kit	Baby Food	18.154923,-67.139392
27	Squash Baby Food	Baby Food	18.154923,-67.139392
28	Corn Baby Food	Baby Food	18.154923,-67.139392
29	AA Batteries	Batteries	18.154923,-67.139392
30	AA Batteries	Batteries	18.154923,-67.139392
31	D Batteries	Batteries	18.154923,-67.139392
32	D Batteries	Batteries	18.154923,-67.139392
33	C Batteries	Batteries	18.154923,-67.139392
34	C Batteries	Batteries	18.154923,-67.139392
35	Car Battery	Batteries	18.154923,-67.139392
36	Car Battery	Batteries	18.154923,-67.139392
97	Epipen	Medical Devices	18.180525,-67.152458
37	SpaghettiOs	Canned Food	18.154923,-67.139392
38	Tomato Soup	Canned Food	18.154923,-67.139392
39	Tomato Soup	Canned Food	18.154923,-67.139392
40	Tomato Soup	Canned Food	18.154923,-67.139392
41	Chicken Broth	Canned Food	18.154923,-67.139392
42	Chicken Broth	Canned Food	18.154923,-67.139392
43	Chicken Broth	Canned Food	18.154923,-67.139392
44	Noodle Soup	Canned Food	18.154923,-67.139392
45	Noodle Soup	Canned Food	18.154923,-67.139392
47	Plain t-shirt	Clothing	18.154923,-67.139392
48	Plain t-shirt	Clothing	18.154923,-67.139392
49	Plain t-shirt	Clothing	18.154923,-67.139392
50	Plain t-shirt	Clothing	18.154923,-67.139392
51	Pants	Clothing	18.154923,-67.139392
52	Pants	Clothing	18.154923,-67.139392
53	Pants	Clothing	18.154923,-67.139392
54	Pants	Clothing	18.154923,-67.139392
55	Shoes	Clothing	18.154923,-67.139392
57	Corn Flakes	Dry Food	18.154923,-67.139392
58	Bacon Bits	Dry Food	18.154923,-67.139392
59	Bacon Bits	Dry Food	18.154923,-67.139392
60	Dried Carrots	Dry Food	18.154923,-67.139392
61	Dried Carrots	Dry Food	18.154923,-67.139392
62	Dried Carrots	Dry Food	18.154923,-67.139392
63	Crackers	Dry Food	18.154923,-67.139392
64	Crackers	Dry Food	18.154923,-67.139392
65	Crackers	Dry Food	18.154923,-67.139392
79	Crane	Heavy Equipment	34.278393, -119.291906
80	Truck	Heavy Equipment	34.278393, -119.291906
81	Truck	Heavy Equipment	34.278393, -119.291906
69	Puma Gasoline Prem.	Fuel	18.125122,-67.095676
70	Puma Gasoline Reg.	Fuel	18.125122,-67.095676
82	Truck	Heavy Equipment	34.278393, -119.291906
67	Total Gasoline Die.	Fuel	18.228101,-67.160906
68	Puma Gasoline Die.	Fuel	18.125122,-67.095676
66	Total Gasoline Reg.	Fuel	18.228101,-67.160906
13	Total Gasoline Prem.	Fuel	18.228101, -67.160906
71	Propane	Fuel	18.125122,-67.095676
72	Coal	Fuel	18.125122,-67.095676
73	Firewood	Fuel	18.125122,-67.095676
74	Nitrous	Fuel	18.125122,-67.095676
12	Bulldozer	Heavy Equipment	18.240647, -67.162776
75	Bulldozer	Heavy Equipment	34.278393, -119.291906
76	Bulldozer	Heavy Equipment	34.278393, -119.291906
77	Crane	Heavy Equipment	34.278393, -119.291906
83	Truck	Heavy Equipment	34.278393, -119.291906
87	Bag of Ice	Ice	18.138372, -67.135405
88	Bag of Ice	Ice	18.138372, -67.135405
89	Bag of Ice	Ice	18.138372, -67.135405
90	Bag of Ice	Ice	18.138372, -67.135405
91	Block of Ice	Ice	18.138372, -67.135405
92	Bag of Chewable Ice	Ice	18.138372, -67.135405
93	Bag of Chewable Ice	Ice	18.138372, -67.135405
94	Bag of Chewable Ice	Ice	18.138372, -67.135405
95	Bag of Chewable Ice	Ice	18.138372, -67.135405
98	Epipen	Medical Devices	18.180525,-67.152458
96	Pruebas Covid-19	Medical Devices	18.138372, -67.135405
1	Pruebas Covid-19	Medical Devices	30.589200, 114.287126
99	Respirator	Medical Devices	18.180525,-67.152458
100	Respirator	Medical Devices	18.180525,-67.152458
101	Prosthetic Arm	Medical Devices	18.180525,-67.152458
102	Cane	Medical Devices	18.180525,-67.152458
103	Cane	Medical Devices	18.180525,-67.152458
104	Cane	Medical Devices	18.180525,-67.152458
105	DayQuil	Medications	18.180525,-67.152458
106	Mucinex	Medications	18.180525,-67.152458
107	Advil	Medications	18.180525,-67.152458
108	Tylenol	Medications	18.180525,-67.152458
109	Aderall	Medications	18.180525,-67.152458
110	Xanax	Medications	18.180525,-67.152458
111	Flinstones Chewables	Medications	18.180525,-67.152458
17	AAA Batteries	Batteries	18.155124, -67.142836
112	Emergen-C	Medications	18.180525,-67.152458
113	One-A-Day	Medications	18.180525,-67.152458
16	AAA Batteries	Batteries	18.155124, -67.142836
114	Syringe	Medical Devices	18.47593, -66.128593
115	Claritin	Medications	18.564684, -66.168462
117	Egg Plant Baby Food	Baby Food	-16.9856, 66.65181
118	Hammer	Tools	18.240647, -67.162776
119	Angle Grinder	Tools	18.240647, -67.162776
120	Hammer	Tools	18.240647, -67.162776
121	Hammer	Tools	18.240647, -67.162776
122	Blowtorch	Tools	18.240647, -67.162776
123	Reef Blower	Tools	18.240647, -67.162776
124	Sledgehammer	Tools	18.240647, -67.162776
125	Sledgehammer	Tools	18.240647, -67.162776
126	Axe	Tools	18.240647, -67.162776
127	Evian Water	Water	-67.1636854, 18.654321
128	Evian Water	Water	-67.1636854, 18.654321
129	Evian Water	Water	-67.1636854, 18.654321
130	Fiji Water	Water	-67.1636854, 18.654321
131	Fiji Water	Water	-67.1636854, 18.654321
132	Nikini Water	Water	-67.1636854, 18.654321
133	Nikini Water	Water	-67.1636854, 18.654321
134	Nikini Water	Water	-67.1636854, 18.654321
135	Cristal Water	Water	-67.1636854, 18.654321
136	Bolsa De Hielo	Ice	-67.1636854, 18.654321
137	Road Roller	Heavy Equipment	18.240647, -67.162776
138	Road Roller	Heavy Equipment	18.240647, -67.162776
139	CAT Generator	Power Generators	18.240647, -67.162776
140	Propane Generator	Power Generators	18.240647, -67.162776
141	Propane Generator	Power Generators	18.240647, -67.162776
142	Solar Generator	Power Generators	18.240647, -67.162776
143	Solar Generator	Power Generators	18.240647, -67.162776
144	Solar Generator	Power Generators	18.240647, -67.162776
145	Vapor Generator	Power Generators	18.240647, -67.162776
146	Water Wheel	Power Generators	18.240647, -67.162776
147	Nuclear Reactor	Power Generators	18.240647, -67.162776
148	Dark Matter	Fuel	18.125122,-67.095676
151	Captain crunch	Dry Food	18.125122,-67.095676
159	Gucci Sweater	Clothing	183411575, -66.024084
160	Canned Spaghett	Canned Food	18.4621, -66.6512632
162	AAA Batteries	Batteries	-66.14982, 18.6516951
\.


--
-- Name: resource_rid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.resource_rid_seq', 162, true);


--
-- Data for Name: stocks; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.stocks (squantity, sid, rid) FROM stdin;
10	1	12
10	1	15
1000	1	16
1000	1	17
5	3	6
200	2	14
20	1	7
100	5	8
20	4	4
10000	5	13
\.


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.supplier (sid, slocation, uid) FROM stdin;
1	34.295013, -119.299341	6
2	18.419587,-66.068778	10
3	18.419587,-66.068778	8
4	18.419587,-66.068778	9
5	18.464102,-66.119225	2
\.


--
-- Name: supplier_sid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.supplier_sid_seq', 5, true);


--
-- Data for Name: tools; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.tools (tid, tbrand, tname, tdescription, rid) FROM stdin;
5	Black & Decker	Power Drill	Drills through all materials, including cobblestone, dirt, bedrock, and enderstone.	7
6	Black and Decker	Hammer	el martillo de mario	118
7	Black and Decker	Angle Grinder	Cuts angles really well.	119
8	Craftsman	Hammer	El martillo de Fix-It Felix.	120
9	Dewalt	Hammer	Master Chief's gravity hammer	121
10	Dewalt	Blowtorch	Burns really hot.	122
11	Dewalt	Reef Blower	El de spongebob	123
12	Dewalt	Sledgehammer	El de Sledge from R6S.	124
13	Bosch	Sledgehammer	20 lbs. Breaks walls.	125
14	Bosch	Axe	For wood cutting, not people cutting.	126
\.


--
-- Name: tools_tid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.tools_tid_seq', 14, true);


--
-- Data for Name: useraccounts; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.useraccounts (uid, username, password, firstname, lastname, email, country, city, saddress, zip) FROM stdin;
1	elduraco	password1	tito	kayak	kayatito@elmejor.edu	Puerto Rico	Ponce	6900 Ave. De Leon	00660
2	lagobe	#Wanda2020	Wanda	Vazques	estafadora@fortaleza.gov	Puerto Rico	San Juan	#1 La Fortaleza	00960
3	RickyRose	#RickyLeaks	Ricardo	Rosello	elnenedepapi@fortaleza.gov	Puerto Rico	San Juan	#1 La Fortaleza	00960
4	MoneyMaker99	PlazaAbreSioSi	Jaime	Fonalleda	stringpuller@plaza.com	Puerto Rico	San Juan	Pine Grove #199 Sea Towers	00960
5	Apt0sAPeso	QueEducacion?	Julia	Keleher	tumbamillos@pr.gov	Puerto Rico	San Juan	Bayamon Correctional Complex Cell 787	00960
6	ApexGeneral	compragobiernos	Robert	Rodriguez	fraude@wedothat.com	Puerto Rico	Guaynabo	139 Blvd. de Mentiras	00969
7	JDP2020	aiudaaa	Juan	Del Pueblo	jdp2020@gmail.com	Puerto Rico	Cidra	Carretera #102 Kilometro 64	00798
8	W	Yandellll	Wisin	Not Yandel	dobleU@gmail.com	Puerto Rico	Hato Rey	La torre del perreo #385	00990
9	Yandel	wisiin	Yandel	Not wisin	Yandel@gmail.com	Puerto Rico	Hato Rey	La torre del perreo #386	00990
10	bbbebebe	YHLQMDLG	Bad	Bunny	chambea@yahoo.com	Puerto Rico	Mayaguez	Terrace #358	00990
11	Mr. Worldwide	eeeyyyuuuuuu	Pit	Bull	dale@yahoo.com	Puerto Rico	guaynabo	dumpster	00498
\.


--
-- Name: useraccounts_uid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.useraccounts_uid_seq', 11, true);


--
-- Data for Name: water; Type: TABLE DATA; Schema: public; Owner: dbproyect
--

COPY public.water (wid, wbrand, wsize, wdescription, rid) FROM stdin;
3	Fiji	1.2 L	Best water you will ever have	8
4	Evian	1.2 L	Better than Volvic	127
5	Evian	500 mL	Better than Volvic	128
6	Evian	2 L	Better than Volvic	129
7	Fiji	2 L	From the fresh mountains of Fiji.	130
8	Fiji	500 mL	From the fresh mountains of Fiji.	131
9	Nikini	500 mL	Agua freca de Cidra.	132
10	Nikini	1.2 L	Agua freca de Cidra.	133
11	Nikini	2 L	Agua freca de Cidra.	134
12	Cristal	1 G	Agua fresca de Cidra.	135
\.


--
-- Name: water_wid_seq; Type: SEQUENCE SET; Schema: public; Owner: dbproyect
--

SELECT pg_catalog.setval('public.water_wid_seq', 12, true);


--
-- Name: administrator_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.administrator
    ADD CONSTRAINT administrator_pkey PRIMARY KEY (aid);


--
-- Name: babyfood_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.babyfood
    ADD CONSTRAINT babyfood_pkey PRIMARY KEY (bfid);


--
-- Name: batteries_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.batteries
    ADD CONSTRAINT batteries_pkey PRIMARY KEY (bid);


--
-- Name: belongs_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.belongs
    ADD CONSTRAINT belongs_pkey PRIMARY KEY (oid, rid);


--
-- Name: cannedfood_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.cannedfood
    ADD CONSTRAINT cannedfood_pkey PRIMARY KEY (cfid);


--
-- Name: clothing_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.clothing
    ADD CONSTRAINT clothing_pkey PRIMARY KEY (clid);


--
-- Name: company_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (cid);


--
-- Name: dryfood_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.dryfood
    ADD CONSTRAINT dryfood_pkey PRIMARY KEY (dfid);


--
-- Name: fuel_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.fuel
    ADD CONSTRAINT fuel_pkey PRIMARY KEY (fid);


--
-- Name: heavyequipment_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.heavyequipment
    ADD CONSTRAINT heavyequipment_pkey PRIMARY KEY (hid);


--
-- Name: ice_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.ice
    ADD CONSTRAINT ice_pkey PRIMARY KEY (iid);


--
-- Name: listing_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.listing
    ADD CONSTRAINT listing_pkey PRIMARY KEY (lid);


--
-- Name: medicaldevices_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.medicaldevices
    ADD CONSTRAINT medicaldevices_pkey PRIMARY KEY (mdid);


--
-- Name: medications_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.medications
    ADD CONSTRAINT medications_pkey PRIMARY KEY (mid);


--
-- Name: orders_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (oid);


--
-- Name: payment_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (pid);


--
-- Name: phonenumber_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.phonenumber
    ADD CONSTRAINT phonenumber_pkey PRIMARY KEY (phone_id);


--
-- Name: powergenerators_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.powergenerators
    ADD CONSTRAINT powergenerators_pkey PRIMARY KEY (gid);


--
-- Name: request_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_pkey PRIMARY KEY (requestid);


--
-- Name: requester_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.requester
    ADD CONSTRAINT requester_pkey PRIMARY KEY (reqid);


--
-- Name: requestresponse_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.requestresponse
    ADD CONSTRAINT requestresponse_pkey PRIMARY KEY (sid, requestid);


--
-- Name: resource_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.resource
    ADD CONSTRAINT resource_pkey PRIMARY KEY (rid);


--
-- Name: stocks_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.stocks
    ADD CONSTRAINT stocks_pkey PRIMARY KEY (sid, rid);


--
-- Name: supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (sid);


--
-- Name: tools_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.tools
    ADD CONSTRAINT tools_pkey PRIMARY KEY (tid);


--
-- Name: useraccounts_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.useraccounts
    ADD CONSTRAINT useraccounts_pkey PRIMARY KEY (uid);


--
-- Name: water_pkey; Type: CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.water
    ADD CONSTRAINT water_pkey PRIMARY KEY (wid);


--
-- Name: administrator_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.administrator
    ADD CONSTRAINT administrator_uid_fkey FOREIGN KEY (uid) REFERENCES public.useraccounts(uid);


--
-- Name: babyfood_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.babyfood
    ADD CONSTRAINT babyfood_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: batteries_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.batteries
    ADD CONSTRAINT batteries_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: belongs_oid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.belongs
    ADD CONSTRAINT belongs_oid_fkey FOREIGN KEY (oid) REFERENCES public.orders(oid);


--
-- Name: belongs_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.belongs
    ADD CONSTRAINT belongs_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: cannedfood_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.cannedfood
    ADD CONSTRAINT cannedfood_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: clothing_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.clothing
    ADD CONSTRAINT clothing_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: company_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_sid_fkey FOREIGN KEY (sid) REFERENCES public.supplier(sid);


--
-- Name: dryfood_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.dryfood
    ADD CONSTRAINT dryfood_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: fuel_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.fuel
    ADD CONSTRAINT fuel_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: heavyequipment_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.heavyequipment
    ADD CONSTRAINT heavyequipment_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: ice_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.ice
    ADD CONSTRAINT ice_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: listing_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.listing
    ADD CONSTRAINT listing_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: listing_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.listing
    ADD CONSTRAINT listing_sid_fkey FOREIGN KEY (sid) REFERENCES public.supplier(sid);


--
-- Name: medicaldevices_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.medicaldevices
    ADD CONSTRAINT medicaldevices_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: medications_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.medications
    ADD CONSTRAINT medications_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: orders_pid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pid_fkey FOREIGN KEY (pid) REFERENCES public.payment(pid);


--
-- Name: orders_reqid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_reqid_fkey FOREIGN KEY (reqid) REFERENCES public.requester(reqid);


--
-- Name: orders_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_sid_fkey FOREIGN KEY (sid) REFERENCES public.supplier(sid);


--
-- Name: phonenumber_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.phonenumber
    ADD CONSTRAINT phonenumber_uid_fkey FOREIGN KEY (uid) REFERENCES public.useraccounts(uid);


--
-- Name: powergenerators_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.powergenerators
    ADD CONSTRAINT powergenerators_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: reqid; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT reqid FOREIGN KEY (reqid) REFERENCES public.requester(reqid);


--
-- Name: request_reqid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_reqid_fkey FOREIGN KEY (reqid) REFERENCES public.requester(reqid);


--
-- Name: request_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: requester_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.requester
    ADD CONSTRAINT requester_uid_fkey FOREIGN KEY (uid) REFERENCES public.useraccounts(uid);


--
-- Name: requestresponse_requestid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.requestresponse
    ADD CONSTRAINT requestresponse_requestid_fkey FOREIGN KEY (requestid) REFERENCES public.request(requestid);


--
-- Name: requestresponse_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.requestresponse
    ADD CONSTRAINT requestresponse_sid_fkey FOREIGN KEY (sid) REFERENCES public.supplier(sid);


--
-- Name: sid; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT sid FOREIGN KEY (sid) REFERENCES public.supplier(sid);


--
-- Name: stocks_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.stocks
    ADD CONSTRAINT stocks_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: stocks_sid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.stocks
    ADD CONSTRAINT stocks_sid_fkey FOREIGN KEY (sid) REFERENCES public.supplier(sid);


--
-- Name: supplier_uid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_uid_fkey FOREIGN KEY (uid) REFERENCES public.useraccounts(uid);


--
-- Name: tools_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.tools
    ADD CONSTRAINT tools_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: water_rid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dbproyect
--

ALTER TABLE ONLY public.water
    ADD CONSTRAINT water_rid_fkey FOREIGN KEY (rid) REFERENCES public.resource(rid);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: dbproyect
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM dbproyect;
GRANT ALL ON SCHEMA public TO dbproyect;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: TABLE administrator; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.administrator FROM PUBLIC;
REVOKE ALL ON TABLE public.administrator FROM dbproyect;
GRANT ALL ON TABLE public.administrator TO dbproyect;
GRANT ALL ON TABLE public.administrator TO jaq;


--
-- Name: TABLE babyfood; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.babyfood FROM PUBLIC;
REVOKE ALL ON TABLE public.babyfood FROM dbproyect;
GRANT ALL ON TABLE public.babyfood TO dbproyect;
GRANT ALL ON TABLE public.babyfood TO jaq;


--
-- Name: TABLE batteries; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.batteries FROM PUBLIC;
REVOKE ALL ON TABLE public.batteries FROM dbproyect;
GRANT ALL ON TABLE public.batteries TO dbproyect;
GRANT ALL ON TABLE public.batteries TO jaq;


--
-- Name: TABLE belongs; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.belongs FROM PUBLIC;
REVOKE ALL ON TABLE public.belongs FROM dbproyect;
GRANT ALL ON TABLE public.belongs TO dbproyect;
GRANT ALL ON TABLE public.belongs TO jaq;


--
-- Name: TABLE cannedfood; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.cannedfood FROM PUBLIC;
REVOKE ALL ON TABLE public.cannedfood FROM dbproyect;
GRANT ALL ON TABLE public.cannedfood TO dbproyect;
GRANT ALL ON TABLE public.cannedfood TO jaq;


--
-- Name: TABLE clothing; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.clothing FROM PUBLIC;
REVOKE ALL ON TABLE public.clothing FROM dbproyect;
GRANT ALL ON TABLE public.clothing TO dbproyect;
GRANT ALL ON TABLE public.clothing TO jaq;


--
-- Name: TABLE company; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.company FROM PUBLIC;
REVOKE ALL ON TABLE public.company FROM dbproyect;
GRANT ALL ON TABLE public.company TO dbproyect;
GRANT ALL ON TABLE public.company TO jaq;


--
-- Name: TABLE dryfood; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.dryfood FROM PUBLIC;
REVOKE ALL ON TABLE public.dryfood FROM dbproyect;
GRANT ALL ON TABLE public.dryfood TO dbproyect;
GRANT ALL ON TABLE public.dryfood TO jaq;


--
-- Name: TABLE fuel; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.fuel FROM PUBLIC;
REVOKE ALL ON TABLE public.fuel FROM dbproyect;
GRANT ALL ON TABLE public.fuel TO dbproyect;
GRANT ALL ON TABLE public.fuel TO jaq;


--
-- Name: TABLE heavyequipment; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.heavyequipment FROM PUBLIC;
REVOKE ALL ON TABLE public.heavyequipment FROM dbproyect;
GRANT ALL ON TABLE public.heavyequipment TO dbproyect;
GRANT ALL ON TABLE public.heavyequipment TO jaq;


--
-- Name: TABLE ice; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.ice FROM PUBLIC;
REVOKE ALL ON TABLE public.ice FROM dbproyect;
GRANT ALL ON TABLE public.ice TO dbproyect;
GRANT ALL ON TABLE public.ice TO jaq;


--
-- Name: TABLE listing; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.listing FROM PUBLIC;
REVOKE ALL ON TABLE public.listing FROM dbproyect;
GRANT ALL ON TABLE public.listing TO dbproyect;
GRANT ALL ON TABLE public.listing TO jaq;


--
-- Name: TABLE medicaldevices; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.medicaldevices FROM PUBLIC;
REVOKE ALL ON TABLE public.medicaldevices FROM dbproyect;
GRANT ALL ON TABLE public.medicaldevices TO dbproyect;
GRANT ALL ON TABLE public.medicaldevices TO jaq;


--
-- Name: TABLE medications; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.medications FROM PUBLIC;
REVOKE ALL ON TABLE public.medications FROM dbproyect;
GRANT ALL ON TABLE public.medications TO dbproyect;
GRANT ALL ON TABLE public.medications TO jaq;


--
-- Name: TABLE orders; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.orders FROM PUBLIC;
REVOKE ALL ON TABLE public.orders FROM dbproyect;
GRANT ALL ON TABLE public.orders TO dbproyect;
GRANT ALL ON TABLE public.orders TO jaq;


--
-- Name: TABLE payment; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.payment FROM PUBLIC;
REVOKE ALL ON TABLE public.payment FROM dbproyect;
GRANT ALL ON TABLE public.payment TO dbproyect;
GRANT ALL ON TABLE public.payment TO jaq;


--
-- Name: TABLE phonenumber; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.phonenumber FROM PUBLIC;
REVOKE ALL ON TABLE public.phonenumber FROM dbproyect;
GRANT ALL ON TABLE public.phonenumber TO dbproyect;
GRANT ALL ON TABLE public.phonenumber TO jaq;


--
-- Name: TABLE powergenerators; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.powergenerators FROM PUBLIC;
REVOKE ALL ON TABLE public.powergenerators FROM dbproyect;
GRANT ALL ON TABLE public.powergenerators TO dbproyect;
GRANT ALL ON TABLE public.powergenerators TO jaq;


--
-- Name: TABLE request; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.request FROM PUBLIC;
REVOKE ALL ON TABLE public.request FROM dbproyect;
GRANT ALL ON TABLE public.request TO dbproyect;
GRANT ALL ON TABLE public.request TO jaq;


--
-- Name: TABLE requester; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.requester FROM PUBLIC;
REVOKE ALL ON TABLE public.requester FROM dbproyect;
GRANT ALL ON TABLE public.requester TO dbproyect;
GRANT ALL ON TABLE public.requester TO jaq;


--
-- Name: TABLE requestresponse; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.requestresponse FROM PUBLIC;
REVOKE ALL ON TABLE public.requestresponse FROM dbproyect;
GRANT ALL ON TABLE public.requestresponse TO dbproyect;
GRANT ALL ON TABLE public.requestresponse TO jaq;


--
-- Name: TABLE resource; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.resource FROM PUBLIC;
REVOKE ALL ON TABLE public.resource FROM dbproyect;
GRANT ALL ON TABLE public.resource TO dbproyect;
GRANT ALL ON TABLE public.resource TO jaq;


--
-- Name: TABLE stocks; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.stocks FROM PUBLIC;
REVOKE ALL ON TABLE public.stocks FROM dbproyect;
GRANT ALL ON TABLE public.stocks TO dbproyect;
GRANT ALL ON TABLE public.stocks TO jaq;


--
-- Name: TABLE supplier; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.supplier FROM PUBLIC;
REVOKE ALL ON TABLE public.supplier FROM dbproyect;
GRANT ALL ON TABLE public.supplier TO dbproyect;
GRANT ALL ON TABLE public.supplier TO jaq;


--
-- Name: TABLE tools; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.tools FROM PUBLIC;
REVOKE ALL ON TABLE public.tools FROM dbproyect;
GRANT ALL ON TABLE public.tools TO dbproyect;
GRANT ALL ON TABLE public.tools TO jaq;


--
-- Name: TABLE useraccounts; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.useraccounts FROM PUBLIC;
REVOKE ALL ON TABLE public.useraccounts FROM dbproyect;
GRANT ALL ON TABLE public.useraccounts TO dbproyect;
GRANT ALL ON TABLE public.useraccounts TO jaq;


--
-- Name: TABLE water; Type: ACL; Schema: public; Owner: dbproyect
--

REVOKE ALL ON TABLE public.water FROM PUBLIC;
REVOKE ALL ON TABLE public.water FROM dbproyect;
GRANT ALL ON TABLE public.water TO dbproyect;
GRANT ALL ON TABLE public.water TO jaq;


--
-- PostgreSQL database dump complete
--

