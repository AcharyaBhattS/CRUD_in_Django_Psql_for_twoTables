PGDMP         %                {         	   PgsDBtoPy    15.2    15.2     $           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            %           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            &           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            '           1262    21699 	   PgsDBtoPy    DATABASE     |   CREATE DATABASE "PgsDBtoPy" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Hindi_India.utf8';
    DROP DATABASE "PgsDBtoPy";
             	   innovapgs    false            �            1259    21723    invoice    TABLE     �   CREATE TABLE public.invoice (
    bill_id integer NOT NULL,
    customer_id integer NOT NULL,
    customer_name character varying(100),
    bill_date date NOT NULL,
    amount_paid real NOT NULL
);
    DROP TABLE public.invoice;
       public         heap 	   innovapgs    false            �            1259    21722    invoice_bill_id_seq    SEQUENCE     �   CREATE SEQUENCE public.invoice_bill_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.invoice_bill_id_seq;
       public       	   innovapgs    false    217            (           0    0    invoice_bill_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.invoice_bill_id_seq OWNED BY public.invoice.bill_id;
          public       	   innovapgs    false    216            �           2604    21726    invoice bill_id    DEFAULT     r   ALTER TABLE ONLY public.invoice ALTER COLUMN bill_id SET DEFAULT nextval('public.invoice_bill_id_seq'::regclass);
 >   ALTER TABLE public.invoice ALTER COLUMN bill_id DROP DEFAULT;
       public       	   innovapgs    false    217    216    217            !          0    21723    invoice 
   TABLE DATA           ^   COPY public.invoice (bill_id, customer_id, customer_name, bill_date, amount_paid) FROM stdin;
    public       	   innovapgs    false    217   '       )           0    0    invoice_bill_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.invoice_bill_id_seq', 4, true);
          public       	   innovapgs    false    216            �           2606    21728    invoice invoice_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_pkey PRIMARY KEY (bill_id);
 >   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_pkey;
       public         	   innovapgs    false    217            !   M   x�3�4�tL�,�4202�54�56�05�2�4�N�M,*H̃��ZrqsZp�����2�&����� ݖ�     