PGDMP     ,    #                {         	   PgsDBtoPy    15.2    15.2     %           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            &           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            '           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            (           1262    21699 	   PgsDBtoPy    DATABASE     |   CREATE DATABASE "PgsDBtoPy" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Hindi_India.utf8';
    DROP DATABASE "PgsDBtoPy";
             	   innovapgs    false            �            1259    21708    customer    TABLE     �   CREATE TABLE public.customer (
    customer_id integer NOT NULL,
    customer_name character varying(100) NOT NULL,
    room_no integer DEFAULT 1 NOT NULL,
    checkin_date date NOT NULL,
    checkout_date date NOT NULL
);
    DROP TABLE public.customer;
       public         heap 	   innovapgs    false            �            1259    21707    customer_customer_id_seq    SEQUENCE     �   CREATE SEQUENCE public.customer_customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.customer_customer_id_seq;
       public       	   innovapgs    false    215            )           0    0    customer_customer_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.customer_customer_id_seq OWNED BY public.customer.customer_id;
          public       	   innovapgs    false    214            �           2604    21711    customer customer_id    DEFAULT     |   ALTER TABLE ONLY public.customer ALTER COLUMN customer_id SET DEFAULT nextval('public.customer_customer_id_seq'::regclass);
 C   ALTER TABLE public.customer ALTER COLUMN customer_id DROP DEFAULT;
       public       	   innovapgs    false    215    214    215            "          0    21708    customer 
   TABLE DATA           d   COPY public.customer (customer_id, customer_name, room_no, checkin_date, checkout_date) FROM stdin;
    public       	   innovapgs    false    215   �       *           0    0    customer_customer_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.customer_customer_id_seq', 8, true);
          public       	   innovapgs    false    214            �           2606    21714    customer customer_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public         	   innovapgs    false    215            "   �   x�U���0Dg�_�|NC��?�B�.AB"*D���ը��lO���r�%����ц��.�Y��w(���`K�--H��;��W\�1���n��a`WS�G���������
�m�ֈ��lX_�4�?E����N̼�0�     