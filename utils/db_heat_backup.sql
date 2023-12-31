PGDMP  %    7        
    
    {         
   Heat_local    16.0    16.0     t           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            u           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            v           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            w           1262    16399 
   Heat_local    DATABASE     �   CREATE DATABASE "Heat_local" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'German_Germany.1252';
    DROP DATABASE "Heat_local";
                postgres    false            Y          0    17909    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public       
   flask_user    false    215   (       k          0    18007    change_mgmt 
   TABLE DATA           y   COPY public.change_mgmt (id, heat_sanr, bewertung, status, nael_id, teil_sanr_vor, teil_sanr_danach, impact) FROM stdin;
    public       
   flask_user    false    233   R       m          0    18031    heat_bom 
   TABLE DATA           f   COPY public.heat_bom (id, heat_sanr, bom_id, einsatz_datum, auslauf_datum, teile_sanr_id) FROM stdin;
    public       
   flask_user    false    235   4       [          0    17915 	   heat_sanr 
   TABLE DATA           8   COPY public.heat_sanr (id, heat_sanr, name) FROM stdin;
    public       
   flask_user    false    217   w       ]          0    17924    naels 
   TABLE DATA           ,   COPY public.naels (id, nael_id) FROM stdin;
    public       
   flask_user    false    219   �       _          0    17931    role 
   TABLE DATA           5   COPY public.role (id, name, description) FROM stdin;
    public       
   flask_user    false    221   !       e          0    17962    roles_users 
   TABLE DATA           ;   COPY public.roles_users (id, user_id, role_id) FROM stdin;
    public       
   flask_user    false    227   Y       g          0    17979 
   teile_sanr 
   TABLE DATA           �   COPY public.teile_sanr (id, teil_sanr, change_index, bauteil_art, bauteil_kategorie, wit_id, part_start_date, heat_start_date, part_end_date, heat_end_date) FROM stdin;
    public       
   flask_user    false    229   |       o          0    18048    teile_sanr_vor_nach 
   TABLE DATA           [   COPY public.teile_sanr_vor_nach (id, nael_id, teil_sanr_vor, teil_sanr_danach) FROM stdin;
    public       
   flask_user    false    237   �       a          0    17940    user 
   TABLE DATA           F   COPY public."user" (id, email, username, password, token) FROM stdin;
    public       
   flask_user    false    223   E       q          0    18070    vg_boms 
   TABLE DATA           4   COPY public.vg_boms (id, wit_id, vg_id) FROM stdin;
    public       
   flask_user    false    239          i          0    17995    vgs 
   TABLE DATA           O   COPY public.vgs (id, vg_nr, heat_id, einsatz_datum, auslauf_datum) FROM stdin;
    public       
   flask_user    false    231          c          0    17955    wits 
   TABLE DATA           (   COPY public.wits (id, name) FROM stdin;
    public       
   flask_user    false    225   <       �           0    0    change_mgmt_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.change_mgmt_id_seq', 34, true);
          public       
   flask_user    false    232            �           0    0    heat_bom_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.heat_bom_id_seq', 1, false);
          public       
   flask_user    false    234            �           0    0    heat_sanr_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.heat_sanr_id_seq', 9, true);
          public       
   flask_user    false    216            �           0    0    naels_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.naels_id_seq', 26, true);
          public       
   flask_user    false    218            �           0    0    role_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.role_id_seq', 3, true);
          public       
   flask_user    false    220            �           0    0    roles_users_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.roles_users_id_seq', 3, true);
          public       
   flask_user    false    226            �           0    0    teile_sanr_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.teile_sanr_id_seq', 34, true);
          public       
   flask_user    false    228            �           0    0    teile_sanr_vor_nach_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.teile_sanr_vor_nach_id_seq', 40, true);
          public       
   flask_user    false    236            �           0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 3, true);
          public       
   flask_user    false    222            �           0    0    vg_boms_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.vg_boms_id_seq', 1, false);
          public       
   flask_user    false    238            �           0    0 
   vgs_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.vgs_id_seq', 1, false);
          public       
   flask_user    false    230            �           0    0    wits_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.wits_id_seq', 1, false);
          public       
   flask_user    false    224            Y      x�3OKKI3J536L6����� 1cJ      k   �   x�m�Q�0D��0!Q�K���]T���$�8���d�2,��]�yoݛ�~n]x�M����t`������?iw`[d�\�I\͒� ��y�^��l=A֓m�[��ے����f�F2L��$4&�&V*Nk�����S���i�y}��©��~�>�	Ԁ��L�(�&�4���oQi��q&�01�i��Q��Fћ�4B��y�T��ng      m   3   x�3�4�q�w���4202�54�50G0-8���*�@0-9��b���� s��      [   5   x�3�42�4114��U�pu��4126122����2�|c/F��� ��	B      ]   U   x�-̻�0��Z&�� i\d�?G�Y=��9��}��z��o�ʨ앣rV��]Q��@B��&4�	�x�3��g<�-3?�")      _   (   x�3�LL��̃�\F��ũE`�˘3�$��\1z\\\ B�g      e      x�3�4�4����� �X      g   �   x��ұN�@���.Eg�|g�]�B(,����'m�����(Q>�qN&�X�q���{����p<��ub.�j�
���P�����U���fj@bY��4�`	��R�LXY��q��B<]����L�\La�]?):g1���?�f�s5_�e�ڤ����.�C������0v�0�fZ����z� t�o����	��\>a�^�G>o�2\Oj�S�h���11�I��=�L�A��o�'��{J)����T      o   �   x�=��D!Cפ�9B���T0��1�з�.�*��t!,E�*O�2��ic�ز0S,ц���t�T3\qzl�E7�7P�oA�(q�l��q��9[B���/�Z#��aV�7�5D�C\��$���
��7��̄�6l�m�ZL�N��'����1pܔ����n
��i����} �ŘA�      a   �   x�5�;1���_X�uG�����
텀�	*衜
�ywl�Ͳ;3-��O����p*�>���@�qq��L�=!���-�RF����D�aY�AO�@�xʼ&�N���@_�/�E��.H��a�^Qv���ːP�̛���.�C-��T�m�j)�F�]�      q      x������ � �      i      x������ � �      c      x������ � �     