SET session_replication_role = 'replica';
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY , "name" varchar(150) NOT NULL UNIQUE);
INSERT INTO "auth_group" VALUES(1,'Coordenador');
INSERT INTO "auth_group" VALUES(2,'Comum interno');
INSERT INTO "auth_group" VALUES(3,'Comum externo');
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY , "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY , "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO "auth_permission" VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES(5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES(6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES(8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES(9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES(10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES(11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES(12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES(17,5,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES(18,5,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES(19,5,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES(20,5,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES(21,6,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES(22,6,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES(23,6,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES(24,6,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES(25,7,'add_statusdofreelapagamento','Can add Status de pagamento do freela');
INSERT INTO "auth_permission" VALUES(26,7,'change_statusdofreelapagamento','Can change Status de pagamento do freela');
INSERT INTO "auth_permission" VALUES(27,7,'delete_statusdofreelapagamento','Can delete Status de pagamento do freela');
INSERT INTO "auth_permission" VALUES(28,7,'view_statusdofreelapagamento','Can view Status de pagamento do freela');
INSERT INTO "auth_permission" VALUES(29,8,'add_statusdoprocesso','Can add Status do processo');
INSERT INTO "auth_permission" VALUES(30,8,'change_statusdoprocesso','Can change Status do processo');
INSERT INTO "auth_permission" VALUES(31,8,'delete_statusdoprocesso','Can delete Status do processo');
INSERT INTO "auth_permission" VALUES(32,8,'view_statusdoprocesso','Can view Status do processo');
INSERT INTO "auth_permission" VALUES(33,9,'add_statusdoprocessopagamento','Can add Status de pagamento do processo');
INSERT INTO "auth_permission" VALUES(34,9,'change_statusdoprocessopagamento','Can change Status de pagamento do processo');
INSERT INTO "auth_permission" VALUES(35,9,'delete_statusdoprocessopagamento','Can delete Status de pagamento do processo');
INSERT INTO "auth_permission" VALUES(36,9,'view_statusdoprocessopagamento','Can view Status de pagamento do processo');
INSERT INTO "auth_permission" VALUES(37,10,'add_componente','Can add Componente');
INSERT INTO "auth_permission" VALUES(38,10,'change_componente','Can change Componente');
INSERT INTO "auth_permission" VALUES(39,10,'delete_componente','Can delete Componente');
INSERT INTO "auth_permission" VALUES(40,10,'view_componente','Can view Componente');
INSERT INTO "auth_permission" VALUES(41,11,'add_projeto','Can add Projeto');
INSERT INTO "auth_permission" VALUES(42,11,'change_projeto','Can change Projeto');
INSERT INTO "auth_permission" VALUES(43,11,'delete_projeto','Can delete Projeto');
INSERT INTO "auth_permission" VALUES(44,11,'view_projeto','Can view Projeto');
INSERT INTO "auth_permission" VALUES(45,12,'add_departamento','Can add Departamento');
INSERT INTO "auth_permission" VALUES(46,12,'change_departamento','Can change Departamento');
INSERT INTO "auth_permission" VALUES(47,12,'delete_departamento','Can delete Departamento');
INSERT INTO "auth_permission" VALUES(48,12,'view_departamento','Can view Departamento');
INSERT INTO "auth_permission" VALUES(49,9,'add_centrodecusto','Can add Centro de custo');
INSERT INTO "auth_permission" VALUES(50,9,'change_centrodecusto','Can change Centro de custo');
INSERT INTO "auth_permission" VALUES(51,9,'delete_centrodecusto','Can delete Centro de custo');
INSERT INTO "auth_permission" VALUES(52,9,'view_centrodecusto','Can view Centro de custo');
INSERT INTO "auth_permission" VALUES(53,13,'add_empresa','Can add Empresa de faturamento');
INSERT INTO "auth_permission" VALUES(54,13,'change_empresa','Can change Empresa de faturamento');
INSERT INTO "auth_permission" VALUES(55,13,'delete_empresa','Can delete Empresa de faturamento');
INSERT INTO "auth_permission" VALUES(56,13,'view_empresa','Can view Empresa de faturamento');
INSERT INTO "auth_permission" VALUES(57,14,'add_fornecedor','Can add Fornecedor');
INSERT INTO "auth_permission" VALUES(58,14,'change_fornecedor','Can change Fornecedor');
INSERT INTO "auth_permission" VALUES(59,14,'delete_fornecedor','Can delete Fornecedor');
INSERT INTO "auth_permission" VALUES(60,14,'view_fornecedor','Can view Fornecedor');
INSERT INTO "auth_permission" VALUES(61,15,'add_limitacaoedicao','Can add Limitação de edição');
INSERT INTO "auth_permission" VALUES(62,15,'change_limitacaoedicao','Can change Limitação de edição');
INSERT INTO "auth_permission" VALUES(63,15,'delete_limitacaoedicao','Can delete Limitação de edição');
INSERT INTO "auth_permission" VALUES(64,15,'view_limitacaoedicao','Can view Limitação de edição');
INSERT INTO "auth_permission" VALUES(65,16,'add_localizacaodorecurso','Can add Localização do recurso');
INSERT INTO "auth_permission" VALUES(66,16,'change_localizacaodorecurso','Can change Localização do recurso');
INSERT INTO "auth_permission" VALUES(67,16,'delete_localizacaodorecurso','Can delete Localização do recurso');
INSERT INTO "auth_permission" VALUES(68,16,'view_localizacaodorecurso','Can view Localização do recurso');
INSERT INTO "auth_permission" VALUES(69,17,'add_statusanaliseautrec','Can add Análise AutRec');
INSERT INTO "auth_permission" VALUES(70,17,'change_statusanaliseautrec','Can change Análise AutRec');
INSERT INTO "auth_permission" VALUES(71,17,'delete_statusanaliseautrec','Can delete Análise AutRec');
INSERT INTO "auth_permission" VALUES(72,17,'view_statusanaliseautrec','Can view Análise AutRec');
INSERT INTO "auth_permission" VALUES(73,18,'add_statusanaliseeditorial','Can add Análise editorial');
INSERT INTO "auth_permission" VALUES(74,18,'change_statusanaliseeditorial','Can change Análise editorial');
INSERT INTO "auth_permission" VALUES(75,18,'delete_statusanaliseeditorial','Can delete Análise editorial');
INSERT INTO "auth_permission" VALUES(76,18,'view_statusanaliseeditorial','Can view Análise editorial');
INSERT INTO "auth_permission" VALUES(77,19,'add_statusdoorcamento','Can add Status do orçamento');
INSERT INTO "auth_permission" VALUES(78,19,'change_statusdoorcamento','Can change Status do orçamento');
INSERT INTO "auth_permission" VALUES(79,19,'delete_statusdoorcamento','Can delete Status do orçamento');
INSERT INTO "auth_permission" VALUES(80,19,'view_statusdoorcamento','Can view Status do orçamento');
INSERT INTO "auth_permission" VALUES(81,20,'add_statusdoorcamentoaprovacao','Can add Status de aprovação do orçamento');
INSERT INTO "auth_permission" VALUES(82,20,'change_statusdoorcamentoaprovacao','Can change Status de aprovação do orçamento');
INSERT INTO "auth_permission" VALUES(83,20,'delete_statusdoorcamentoaprovacao','Can delete Status de aprovação do orçamento');
INSERT INTO "auth_permission" VALUES(84,20,'view_statusdoorcamentoaprovacao','Can view Status de aprovação do orçamento');
INSERT INTO "auth_permission" VALUES(85,21,'add_statusdoprocessopagamentofornecedor','Can add Status de pagamento do fornecedor');
INSERT INTO "auth_permission" VALUES(86,21,'change_statusdoprocessopagamentofornecedor','Can change Status de pagamento do fornecedor');
INSERT INTO "auth_permission" VALUES(87,21,'delete_statusdoprocessopagamentofornecedor','Can delete Status de pagamento do fornecedor');
INSERT INTO "auth_permission" VALUES(88,21,'view_statusdoprocessopagamentofornecedor','Can view Status de pagamento do fornecedor');
INSERT INTO "auth_permission" VALUES(89,22,'add_tipodetermo','Can add Tipo de termo');
INSERT INTO "auth_permission" VALUES(90,22,'change_tipodetermo','Can change Tipo de termo');
INSERT INTO "auth_permission" VALUES(91,22,'delete_tipodetermo','Can delete Tipo de termo');
INSERT INTO "auth_permission" VALUES(92,22,'view_tipodetermo','Can view Tipo de termo');
INSERT INTO "auth_permission" VALUES(93,23,'add_historicalprocess','Can add historical Processo');
INSERT INTO "auth_permission" VALUES(94,23,'change_historicalprocess','Can change historical Processo');
INSERT INTO "auth_permission" VALUES(95,23,'delete_historicalprocess','Can delete historical Processo');
INSERT INTO "auth_permission" VALUES(96,23,'view_historicalprocess','Can view historical Processo');
INSERT INTO "auth_permission" VALUES(97,24,'add_process','Can add Processo');
INSERT INTO "auth_permission" VALUES(98,24,'change_process','Can change Processo');
INSERT INTO "auth_permission" VALUES(99,24,'delete_process','Can delete Processo');
INSERT INTO "auth_permission" VALUES(100,24,'view_process','Can view Processo');
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY , "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY , "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO "django_content_type" VALUES(1,'admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'auth','permission');
INSERT INTO "django_content_type" VALUES(3,'auth','group');
INSERT INTO "django_content_type" VALUES(4,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(5,'sessions','session');
INSERT INTO "django_content_type" VALUES(6,'users','user');
INSERT INTO "django_content_type" VALUES(7,'licentia_resources','statusdofreelapagamento');
INSERT INTO "django_content_type" VALUES(8,'licentia_resources','statusdoprocesso');
INSERT INTO "django_content_type" VALUES(9,'licentia_resources','centrodecusto');
INSERT INTO "django_content_type" VALUES(10,'licentia_resources','componente');
INSERT INTO "django_content_type" VALUES(11,'licentia_resources','projeto');
INSERT INTO "django_content_type" VALUES(12,'users','departamento');
INSERT INTO "django_content_type" VALUES(13,'licentia_resources','empresa');
INSERT INTO "django_content_type" VALUES(14,'licentia_resources','fornecedor');
INSERT INTO "django_content_type" VALUES(15,'licentia_resources','limitacaoedicao');
INSERT INTO "django_content_type" VALUES(16,'licentia_resources','localizacaodorecurso');
INSERT INTO "django_content_type" VALUES(17,'licentia_resources','statusanaliseautrec');
INSERT INTO "django_content_type" VALUES(18,'licentia_resources','statusanaliseeditorial');
INSERT INTO "django_content_type" VALUES(19,'licentia_resources','statusdoorcamento');
INSERT INTO "django_content_type" VALUES(20,'licentia_resources','statusdoorcamentoaprovacao');
INSERT INTO "django_content_type" VALUES(21,'licentia_resources','statusdoprocessopagamentofornecedor');
INSERT INTO "django_content_type" VALUES(22,'licentia_resources','tipodetermo');
INSERT INTO "django_content_type" VALUES(23,'licentia_process','historicalprocess');
INSERT INTO "django_content_type" VALUES(24,'licentia_process','process');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY , "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2026-02-21 18:31:49.484146');
INSERT INTO "django_migrations" VALUES(2,'contenttypes','0002_remove_content_type_name','2026-02-21 18:31:49.501486');
INSERT INTO "django_migrations" VALUES(3,'auth','0001_initial','2026-02-21 18:31:49.533150');
INSERT INTO "django_migrations" VALUES(4,'auth','0002_alter_permission_name_max_length','2026-02-21 18:31:49.545597');
INSERT INTO "django_migrations" VALUES(5,'auth','0003_alter_user_email_max_length','2026-02-21 18:31:49.561246');
INSERT INTO "django_migrations" VALUES(6,'auth','0004_alter_user_username_opts','2026-02-21 18:31:49.577007');
INSERT INTO "django_migrations" VALUES(7,'auth','0005_alter_user_last_login_null','2026-02-21 18:31:49.593178');
INSERT INTO "django_migrations" VALUES(8,'auth','0006_require_contenttypes_0002','2026-02-21 18:31:49.601319');
INSERT INTO "django_migrations" VALUES(9,'auth','0007_alter_validators_add_error_messages','2026-02-21 18:31:49.612173');
INSERT INTO "django_migrations" VALUES(10,'auth','0008_alter_user_username_max_length','2026-02-21 18:31:49.628038');
INSERT INTO "django_migrations" VALUES(11,'auth','0009_alter_user_last_name_max_length','2026-02-21 18:31:49.641681');
INSERT INTO "django_migrations" VALUES(12,'auth','0010_alter_group_name_max_length','2026-02-21 18:31:49.650699');
INSERT INTO "django_migrations" VALUES(13,'auth','0011_update_proxy_permissions','2026-02-21 18:31:49.738199');
INSERT INTO "django_migrations" VALUES(14,'auth','0012_alter_user_first_name_max_length','2026-02-21 18:31:49.749743');
INSERT INTO "django_migrations" VALUES(15,'users','0001_initial','2026-02-21 18:31:49.775541');
INSERT INTO "django_migrations" VALUES(16,'admin','0001_initial','2026-02-21 18:31:49.801301');
INSERT INTO "django_migrations" VALUES(17,'admin','0002_logentry_remove_auto_add','2026-02-21 18:31:49.821740');
INSERT INTO "django_migrations" VALUES(18,'admin','0003_logentry_add_action_flag_choices','2026-02-21 18:31:49.831889');
INSERT INTO "django_migrations" VALUES(19,'sessions','0001_initial','2026-02-21 18:31:49.848559');
INSERT INTO "django_migrations" VALUES(20,'licentia_resources','0001_initial','2026-02-22 11:24:57.707095');
INSERT INTO "django_migrations" VALUES(21,'licentia_resources','0002_alter_componente_nome_alter_projeto_nome_and_more','2026-02-23 00:44:51.294744');
INSERT INTO "django_migrations" VALUES(22,'licentia_resources','0003_rename_statusdoprocessopagamento_centrodecusto_and_more','2026-02-24 17:27:18.263811');
INSERT INTO "django_migrations" VALUES(23,'users','0002_alter_user_options_remove_user_departamento_and_more','2026-02-24 17:27:18.438942');
INSERT INTO "django_migrations" VALUES(24,'licentia_process','0001_initial','2026-02-24 23:23:21.064655');
INSERT INTO "django_migrations" VALUES(25,'licentia_process','0002_alter_historicalprocess_capitulo_secao_and_more','2026-02-25 15:45:35.072429');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('1k745ff3lyrds9bod5vp79c2pyha08zb','.eJxVjEEOwiAQRe_C2hAG2wFcuu8ZCAOMVA0kpV0Z765NutDtf-_9l_BhW4vfel78nMRFgDj9bhTiI9cdpHuotyZjq-syk9wVedAup5by83q4fwcl9PKto0aLihDAWDA4WtBICSyPOluDrFg7BczsUuRA6ozaEWY9RBgi2STeH7nUN3w:1vtxHy:nUbGgS0ew_gaTB7U-qqqJ-7YtN5zmFg7E4NX7p-IOR8','2026-03-08 00:25:34.137423');
INSERT INTO "django_session" VALUES('s2vc4tz48zhjc372l2ewhk16yhfrvcas','.eJxVjMsOwiAQRf-FtSE8C7h07zeQYRikaiAp7cr479qkC93ec859sQjbWuM2aIlzZmcm2el3S4APajvId2i3zrG3dZkT3xV-0MGvPdPzcrh_BxVG_daoyRFAyg6L1MqkgGVyyginRClGorAWhQIsBE555aeAmbTFEATp5Nn7AwGyOF4:1vuYiQ:D8VUOp5NsbJdz497wUnAg_FQqN0GUVlrB9mohV7rtWw','2026-03-09 16:23:22.892938');
INSERT INTO "django_session" VALUES('c3kggchyw6y7eriffvxjujfmyh1k8xun','.eJxVjMsOwiAQRf-FtSE8C7h07zeQYRikaiAp7cr479qkC93ec859sQjbWuM2aIlzZmcm2el3S4APajvId2i3zrG3dZkT3xV-0MGvPdPzcrh_BxVG_daoyRFAyg6L1MqkgGVyyginRClGorAWhQIsBE555aeAmbTFEATp5Nn7AwGyOF4:1vuwCA:kCoLfYZXxcwko1kgFFqY2LeTbGenaosYubn12__EaMg','2026-03-10 17:27:38.381795');
CREATE TABLE "licentia_process_historicalprocess" ("id" bigint NOT NULL, "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "volume" integer unsigned NULL CHECK ("volume" >= 0), "pagina" integer unsigned NULL CHECK ("pagina" >= 0), "unidade" integer unsigned NULL CHECK ("unidade" >= 0), "lote" integer unsigned NULL CHECK ("lote" >= 0), "limitacao_anos" integer unsigned NULL CHECK ("limitacao_anos" >= 0), "limitacao_tiragem" integer unsigned NULL CHECK ("limitacao_tiragem" >= 0), "valor_do_processo" decimal NULL, "retranca" varchar(100) NOT NULL, "capitulo_secao" varchar(100) NULL, "titulo_descricao" varchar(200) NULL, "solicitado_para" varchar(200) NULL, "obra_original" text NULL, "codigo_biblioteca_link" text NULL, "observacao_exemplares" text NULL, "limitacao_outros" text NULL, "observacao_editorial" text NULL, "credito_obrigatorio" text NULL, "observacao_autrec" text NULL, "solicitar_imagem" bool NOT NULL, "enviar_formulario" bool NOT NULL, "data_entrada" date NULL, "data_analise_autrec" date NULL, "history_id" integer NOT NULL PRIMARY KEY , "history_date" datetime NOT NULL, "history_change_reason" varchar(100) NULL, "history_type" varchar(1) NOT NULL, "atualizado_por_id" bigint NULL, "centro_de_custo_id" bigint NULL, "componente_id" bigint NULL, "criado_por_id" bigint NULL, "empresa_id" bigint NULL, "fornecedor_id" bigint NULL, "history_user_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "limitacao_edicao_id" bigint NULL, "localizacao_do_recurso_id" bigint NULL, "projeto_id" bigint NULL, "status_analise_autrec_id" bigint NULL, "status_analise_editorial_id" bigint NULL, "status_do_freela_pagamento_id" bigint NULL, "status_do_orcamento_id" bigint NULL, "status_do_processo_id" bigint NULL, "status_do_processo_pagamento_fornecedor_id" bigint NULL, "tipo_de_termo_id" bigint NULL, "status_do_orcamento_aprovacao_id" bigint NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 15:45:46.541879',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste',NULL,NULL,NULL,'','','','','','','',0,0,NULL,NULL,1,'2026-02-25 15:45:46.583421',NULL,'+',NULL,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 15:48:17.683901',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste',NULL,NULL,NULL,'','','','','','','',0,0,NULL,NULL,2,'2026-02-25 15:48:17.733644',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 15:48:54.599776',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','','','','','','',0,0,NULL,NULL,3,'2026-02-25 15:48:54.649702',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 17:17:09.363998',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','','','','','','',0,0,NULL,NULL,4,'2026-02-25 17:17:09.609557',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 17:39:14.412031',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','O fato de o campo "O que mudou?" aparecer vazio indica que o Django não está conseguindo acessar a propriedade que calcula a diferença entre as versões. Isso acontece porque, no loop do histórico, cada record é uma instância da tabela de histórico (gerada pelo simple-history) e não o objeto Process original.



Para corrigir isso de forma definitiva e garantir que apareça algo como "status_do_processo, valor_do_processo", vamos usar uma abordagem que funciona diretamente no objeto de histórico.



1. Adicione este método ao seu Model

O simple-history permite adicionar métodos customizados diretamente à classe histórica. No seu models.py, altere a declaração do histórico para incluir este método auxiliar:','','','','','',0,0,NULL,NULL,5,'2026-02-25 17:39:14.428201',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 17:39:48.444966',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','Se quiser, posso te passar um componente reutilizável de histórico (um include único) que:



detecta automaticamente textos longos



abre modal só quando necessário



formata datas e usuários



converte nomes técnicos dos campos para verbose_name automaticamente (fica muito melhor para o usuário).','','','','','',0,0,NULL,NULL,6,'2026-02-25 17:39:48.478240',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 18:45:46.293518',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','Se quiser, posso te passar um componente reutilizável de histórico (um include único) que:



detecta automaticamente textos longos



abre modal só quando necessário



formata datas e usuários



converte nomes técnicos dos campos para verbose_name automaticamente (fica muito melhor para o usuário).','','','','','',0,0,NULL,NULL,7,'2026-02-25 18:45:46.300329',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,NULL,5,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 18:45:59.916946',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','Se quiser, posso te passar um componente reutilizável de histórico (um include único) que:



detecta automaticamente textos longos



abre modal só quando necessário



formata datas e usuários



converte nomes técnicos dos campos para verbose_name automaticamente (fica muito melhor para o usuário).','','','','','',0,0,NULL,NULL,8,'2026-02-25 18:45:59.941323',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,2,2,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 19:52:06.154378',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'teste 2',NULL,NULL,NULL,'','Se quiser, posso te passar um componente reutilizável de histórico (um include único) que:



detecta automaticamente textos longos



abre modal só quando necessário



formata datas e usuários



converte nomes técnicos dos campos para verbose_name automaticamente (fica muito melhor para o usuário).','','','','','',0,0,NULL,NULL,9,'2026-02-25 19:52:06.170810',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,2,2,NULL,NULL,NULL);
INSERT INTO "licentia_process_historicalprocess" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 19:56:24.110819',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'c0001_6p013p_g28_e002',NULL,NULL,NULL,'','Se quiser, posso te passar um componente reutilizável de histórico (um include único) que:



detecta automaticamente textos longos



abre modal só quando necessário



formata datas e usuários



converte nomes técnicos dos campos para verbose_name automaticamente (fica muito melhor para o usuário).','','','','','',0,0,NULL,NULL,10,'2026-02-25 19:56:24.132959',NULL,'~',1,NULL,NULL,1,NULL,2,1,NULL,NULL,NULL,NULL,1,NULL,2,2,NULL,NULL,NULL);
CREATE TABLE "licentia_process_process" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "volume" integer unsigned NULL CHECK ("volume" >= 0), "pagina" integer unsigned NULL CHECK ("pagina" >= 0), "unidade" integer unsigned NULL CHECK ("unidade" >= 0), "lote" integer unsigned NULL CHECK ("lote" >= 0), "limitacao_anos" integer unsigned NULL CHECK ("limitacao_anos" >= 0), "limitacao_tiragem" integer unsigned NULL CHECK ("limitacao_tiragem" >= 0), "valor_do_processo" decimal NULL, "retranca" varchar(100) NOT NULL UNIQUE, "capitulo_secao" varchar(100) NULL, "titulo_descricao" varchar(200) NULL, "solicitado_para" varchar(200) NULL, "obra_original" text NULL, "codigo_biblioteca_link" text NULL, "observacao_exemplares" text NULL, "limitacao_outros" text NULL, "observacao_editorial" text NULL, "credito_obrigatorio" text NULL, "observacao_autrec" text NULL, "solicitar_imagem" bool NOT NULL, "enviar_formulario" bool NOT NULL, "data_entrada" date NULL, "data_analise_autrec" date NULL, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "centro_de_custo_id" bigint NULL REFERENCES "licentia_resources_centrodecusto" ("id") DEFERRABLE INITIALLY DEFERRED, "componente_id" bigint NULL REFERENCES "licentia_resources_componente" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "empresa_id" bigint NULL REFERENCES "licentia_resources_empresa" ("id") DEFERRABLE INITIALLY DEFERRED, "fornecedor_id" bigint NULL REFERENCES "licentia_resources_fornecedor" ("id") DEFERRABLE INITIALLY DEFERRED, "limitacao_edicao_id" bigint NULL REFERENCES "licentia_resources_limitacaoedicao" ("id") DEFERRABLE INITIALLY DEFERRED, "localizacao_do_recurso_id" bigint NULL REFERENCES "licentia_resources_localizacaodorecurso" ("id") DEFERRABLE INITIALLY DEFERRED, "projeto_id" bigint NULL REFERENCES "licentia_resources_projeto" ("id") DEFERRABLE INITIALLY DEFERRED, "status_analise_autrec_id" bigint NULL REFERENCES "licentia_resources_statusanaliseautrec" ("id") DEFERRABLE INITIALLY DEFERRED, "status_analise_editorial_id" bigint NULL REFERENCES "licentia_resources_statusanaliseeditorial" ("id") DEFERRABLE INITIALLY DEFERRED, "status_do_freela_pagamento_id" bigint NULL REFERENCES "licentia_resources_statusdofreelapagamento" ("id") DEFERRABLE INITIALLY DEFERRED, "status_do_orcamento_id" bigint NULL REFERENCES "licentia_resources_statusdoorcamento" ("id") DEFERRABLE INITIALLY DEFERRED, "status_do_processo_id" bigint NULL REFERENCES "licentia_resources_statusdoprocesso" ("id") DEFERRABLE INITIALLY DEFERRED, "status_do_processo_pagamento_fornecedor_id" bigint NULL REFERENCES "licentia_resources_statusdoprocessopagamentofornecedor" ("id") DEFERRABLE INITIALLY DEFERRED, "tipo_de_termo_id" bigint NULL REFERENCES "licentia_resources_tipodetermo" ("id") DEFERRABLE INITIALLY DEFERRED, "status_do_orcamento_aprovacao_id" bigint NULL REFERENCES "licentia_resources_statusdoorcamentoaprovacao" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_process_process" VALUES(1,'2026-02-25 15:45:46.541879','2026-02-25 19:56:24.110819',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'c0001_6p013p_g28_e002',NULL,NULL,NULL,'','Se quiser, posso te passar um componente reutilizável de histórico (um include único) que:



detecta automaticamente textos longos



abre modal só quando necessário



formata datas e usuários



converte nomes técnicos dos campos para verbose_name automaticamente (fica muito melhor para o usuário).','','','','','',0,0,NULL,NULL,1,NULL,NULL,1,NULL,2,NULL,NULL,NULL,NULL,1,NULL,2,2,NULL,NULL,NULL);
CREATE TABLE "licentia_process_process_atribuido_a" ("id" integer NOT NULL PRIMARY KEY , "process_id" bigint NOT NULL REFERENCES "licentia_process_process" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE "licentia_resources_centrodecusto" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_centrodecusto" VALUES(1,'2026-02-24 18:45:03.367675','2026-02-24 18:45:03.367675','Arte 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(2,'2026-02-24 18:45:08.033457','2026-02-24 18:45:08.033457','Ciências 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(3,'2026-02-24 18:45:13.097459','2026-02-24 18:45:13.097459','Educação Digital 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(4,'2026-02-24 18:45:17.835173','2026-02-24 18:45:17.835173','Educação Física 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(5,'2026-02-24 18:45:22.417894','2026-02-24 18:45:22.417894','Geografia 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(6,'2026-02-24 18:45:27.298160','2026-02-24 18:45:27.298160','História 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(7,'2026-02-24 18:45:31.757271','2026-02-24 18:45:31.757271','L. Espanhola 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(8,'2026-02-24 18:45:37.457337','2026-02-24 18:45:37.457337','L. Inglesa 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(9,'2026-02-24 18:45:42.449240','2026-02-24 18:45:42.449240','L. Portuguesa 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(10,'2026-02-24 18:45:47.561147','2026-02-24 18:45:47.561147','Matemática 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
INSERT INTO "licentia_resources_centrodecusto" VALUES(11,'2026-02-24 18:45:51.841282','2026-02-24 18:45:51.841282','Produção de Texto 6º AO 9º PNLD 2028-2031 - NOVO RUMO',1,1);
CREATE TABLE "licentia_resources_componente" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_componente" VALUES(1,'2026-02-22 23:49:19.636354','2026-02-22 23:52:28.589577','História',1,1);
INSERT INTO "licentia_resources_componente" VALUES(2,'2026-02-23 00:25:04.109600','2026-02-23 00:25:04.109600','Ciências',1,1);
INSERT INTO "licentia_resources_componente" VALUES(3,'2026-02-24 17:31:44.968672','2026-02-24 17:31:44.968672','teste',1,1);
CREATE TABLE "licentia_resources_empresa" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_empresa" VALUES(1,'2026-02-24 18:49:46.606180','2026-02-24 18:49:46.606180','SCRIBA',1,1);
INSERT INTO "licentia_resources_empresa" VALUES(2,'2026-02-24 18:49:52.434128','2026-02-24 18:49:52.434128','NOVO RUMO',1,1);
INSERT INTO "licentia_resources_empresa" VALUES(3,'2026-02-24 18:49:57.640529','2026-02-24 18:49:57.640529','ENSINOLIVRE',1,1);
CREATE TABLE "licentia_resources_fornecedor" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(200) NOT NULL UNIQUE, "razao_social" varchar(200) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_fornecedor" VALUES(1,'2026-02-24 18:50:42.313899','2026-02-24 18:50:42.313899','ART CAPRI','ART CAPRI PRODUÇÕES LTDA',1,1);
INSERT INTO "licentia_resources_fornecedor" VALUES(2,'2026-02-24 18:50:54.076510','2026-02-24 18:50:54.076510','RLIMA','RLIMA DOCUMENTOS DIGITAIS LTDA ME',1,1);
CREATE TABLE "licentia_resources_limitacaoedicao" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_limitacaoedicao" VALUES(1,'2026-02-24 18:51:17.584496','2026-02-24 18:51:23.105272','1 ano',1,NULL);
INSERT INTO "licentia_resources_limitacaoedicao" VALUES(2,'2026-02-24 18:51:29.586218','2026-02-24 18:51:29.586218','2 anos',1,1);
INSERT INTO "licentia_resources_limitacaoedicao" VALUES(3,'2026-02-24 18:51:34.823653','2026-02-24 18:51:34.823653','Sem restrições',1,1);
CREATE TABLE "licentia_resources_localizacaodorecurso" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_localizacaodorecurso" VALUES(1,'2026-02-24 19:01:41.595049','2026-02-24 19:01:41.595049','MIOLO',1,1);
INSERT INTO "licentia_resources_localizacaodorecurso" VALUES(2,'2026-02-24 19:01:46.836780','2026-02-24 19:01:46.836780','MANUAL GERAL',1,1);
INSERT INTO "licentia_resources_localizacaodorecurso" VALUES(3,'2026-02-24 19:01:51.421189','2026-02-24 19:01:51.421189','MANUAL ESPECÍFICO',1,1);
INSERT INTO "licentia_resources_localizacaodorecurso" VALUES(4,'2026-02-24 19:01:56.746994','2026-02-24 19:01:56.746994','INICIAIS',1,1);
INSERT INTO "licentia_resources_localizacaodorecurso" VALUES(5,'2026-02-24 19:02:01.613104','2026-02-24 19:02:01.613104','FINAIS',1,1);
CREATE TABLE "licentia_resources_projeto" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "editora" varchar(100) NOT NULL, "ciclo" varchar(100) NOT NULL, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_projeto" VALUES(1,'2026-02-22 23:32:52.357407','2026-02-22 23:32:52.357407','p013','e002','g28',1,1);
INSERT INTO "licentia_resources_projeto" VALUES(2,'2026-02-22 23:36:29.559263','2026-02-22 23:40:08.064676','p014','e001','g27',1,1);
INSERT INTO "licentia_resources_projeto" VALUES(3,'2026-02-23 00:39:21.372314','2026-02-23 00:39:21.372314','p016','e002','m27',1,1);
CREATE TABLE "licentia_resources_statusanaliseautrec" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusanaliseautrec" VALUES(1,'2026-02-24 18:43:24.686189','2026-02-24 18:43:24.686189','LIVRE',1,1);
INSERT INTO "licentia_resources_statusanaliseautrec" VALUES(2,'2026-02-24 18:43:30.477092','2026-02-24 18:43:30.477092','PEQUENO TRECHO',1,1);
INSERT INTO "licentia_resources_statusanaliseautrec" VALUES(3,'2026-02-24 18:43:37.913542','2026-02-24 18:43:37.913542','SOLICITAR',1,1);
INSERT INTO "licentia_resources_statusanaliseautrec" VALUES(4,'2026-02-24 18:43:52.904544','2026-02-24 18:43:52.904544','AJUSTAR',1,1);
INSERT INTO "licentia_resources_statusanaliseautrec" VALUES(5,'2026-02-24 18:43:58.652669','2026-02-24 18:43:58.652669','NEGADO',1,1);
INSERT INTO "licentia_resources_statusanaliseautrec" VALUES(6,'2026-02-24 18:44:05.106548','2026-02-24 18:44:09.831351','DOMÍNIO PÚBLICO',1,NULL);
CREATE TABLE "licentia_resources_statusanaliseeditorial" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusanaliseeditorial" VALUES(1,'2026-02-24 18:44:24.253599','2026-02-24 18:44:24.253599','LIVRE',1,1);
INSERT INTO "licentia_resources_statusanaliseeditorial" VALUES(2,'2026-02-24 18:44:30.352912','2026-02-24 18:44:30.352912','DOMÍNIO PÚBLICO',1,1);
INSERT INTO "licentia_resources_statusanaliseeditorial" VALUES(3,'2026-02-24 18:44:36.186616','2026-02-24 18:44:36.186616','PEQUENO TRECHO',1,1);
INSERT INTO "licentia_resources_statusanaliseeditorial" VALUES(4,'2026-02-24 18:44:42.058957','2026-02-24 18:44:42.058957','SOLICITAR',1,1);
CREATE TABLE "licentia_resources_statusdofreelapagamento" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusdofreelapagamento" VALUES(1,'2026-02-24 19:03:19.837023','2026-02-24 19:03:19.837023','PAGO',1,1);
INSERT INTO "licentia_resources_statusdofreelapagamento" VALUES(2,'2026-02-24 19:03:24.894652','2026-02-24 19:03:24.894652','SOLICITADO',1,1);
CREATE TABLE "licentia_resources_statusdoorcamento" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusdoorcamento" VALUES(1,'2026-02-24 19:04:13.934390','2026-02-24 19:04:13.934390','PENDENTE',1,1);
INSERT INTO "licentia_resources_statusdoorcamento" VALUES(2,'2026-02-24 19:04:20.956686','2026-02-24 19:04:20.956686','PREVISÃO',1,1);
INSERT INTO "licentia_resources_statusdoorcamento" VALUES(3,'2026-02-24 19:04:25.870571','2026-02-24 19:04:25.870571','RECEBIDO',1,1);
CREATE TABLE "licentia_resources_statusdoorcamentoaprovacao" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusdoorcamentoaprovacao" VALUES(1,'2026-02-24 19:02:30.106076','2026-02-24 19:02:30.106076','PENDENTE',1,1);
INSERT INTO "licentia_resources_statusdoorcamentoaprovacao" VALUES(2,'2026-02-24 19:02:34.405172','2026-02-24 19:02:34.405172','APROVADO',1,1);
INSERT INTO "licentia_resources_statusdoorcamentoaprovacao" VALUES(3,'2026-02-24 19:02:43.887151','2026-02-24 19:02:43.887151','NEGADO',1,1);
CREATE TABLE "licentia_resources_statusdoprocesso" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(1,'2026-02-22 23:58:09.537842','2026-02-24 19:05:48.715861','NEGADO',1,NULL);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(2,'2026-02-23 00:47:06.221649','2026-02-24 19:05:29.319317','ENTRADA',1,NULL);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(3,'2026-02-24 17:28:46.682028','2026-02-24 19:05:36.534294','PENDENTE',1,NULL);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(4,'2026-02-24 19:05:42.180560','2026-02-24 19:05:42.180560','EXCLUÍDO',1,1);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(5,'2026-02-24 19:05:53.867964','2026-02-24 19:05:53.867964','CONFIRMADO',1,1);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(6,'2026-02-24 19:05:59.667937','2026-02-24 19:05:59.667937','AUTORIZADO',1,1);
INSERT INTO "licentia_resources_statusdoprocesso" VALUES(7,'2026-02-24 19:06:04.499610','2026-02-24 19:06:04.499610','LIBERADO',1,1);
CREATE TABLE "licentia_resources_statusdoprocessopagamentofornecedor" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_statusdoprocessopagamentofornecedor" VALUES(1,'2026-02-24 19:03:00.937037','2026-02-24 19:03:00.937037','SOLICITADO',1,1);
INSERT INTO "licentia_resources_statusdoprocessopagamentofornecedor" VALUES(2,'2026-02-24 19:03:06.364312','2026-02-24 19:03:06.364312','PAGO',1,1);
CREATE TABLE "licentia_resources_tipodetermo" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "licentia_resources_tipodetermo" VALUES(1,'2026-02-24 17:49:55.247005','2026-02-24 17:49:55.247005','E-mail',1,1);
INSERT INTO "licentia_resources_tipodetermo" VALUES(2,'2026-02-24 17:50:03.283323','2026-02-24 17:50:03.283323','Termo Scriba',1,1);
INSERT INTO "licentia_resources_tipodetermo" VALUES(3,'2026-02-24 17:50:09.554780','2026-02-24 17:50:09.554780','Termo detentor',1,1);
INSERT INTO "licentia_resources_tipodetermo" VALUES(4,'2026-02-24 17:50:18.417370','2026-02-24 17:50:18.417370','Termo FTD',1,1);
INSERT INTO "licentia_resources_tipodetermo" VALUES(5,'2026-02-24 17:50:24.215828','2026-02-24 17:50:24.215828','Termo Moderna',1,1);
CREATE TABLE "users_departamento" ("id" integer NOT NULL PRIMARY KEY , "criado_em" datetime NOT NULL, "atualizado_em" datetime NOT NULL, "nome" varchar(100) NOT NULL UNIQUE, "atualizado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "criado_por_id" bigint NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "users_departamento" VALUES(1,'2026-02-24 20:04:10.715227','2026-02-24 20:04:10.715227','História',NULL,NULL);
INSERT INTO "users_departamento" VALUES(2,'2026-02-24 20:04:51.928001','2026-02-24 20:04:51.928001','Geografia',NULL,NULL);
INSERT INTO "users_departamento" VALUES(3,'2026-02-24 20:20:16.371814','2026-02-24 20:20:16.371814','Arte',NULL,1);
CREATE TABLE "users_user" ("id" integer NOT NULL PRIMARY KEY , "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "empresa" varchar(100) NULL);
INSERT INTO "users_user" VALUES(1,'pbkdf2_sha256$1000000$p0q1XNYrCpVgGEKZvlkNG2$NqSkQXQUqbeOA9GM3Awww1M1xukolaqs7dgYK4Vp77M=','2026-02-24 17:27:38.364420',1,'admin','','','junior.dias@scriba.com.br',1,1,'2026-02-21 18:32:15.757717',NULL);
INSERT INTO "users_user" VALUES(2,'pbkdf2_sha256$1000000$eqIkay3kgF2hC59bQVOHIW$vG1LwbSpUhuEnEFqCsWoPicGr5/x0GKZsUaMacxncKE=','2026-02-22 00:17:10.757096',0,'junior.dias','Junior','Dias','junior.dias@ensinolivre.com.br',0,1,'2026-02-21 19:00:44.874321','Scriba');
CREATE TABLE "users_user_departamentos" ("id" integer NOT NULL PRIMARY KEY , "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "departamento_id" bigint NOT NULL REFERENCES "users_departamento" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "users_user_departamentos" VALUES(2,2,2);
INSERT INTO "users_user_departamentos" VALUES(3,2,1);
CREATE TABLE "users_user_groups" ("id" integer NOT NULL PRIMARY KEY , "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "users_user_groups" VALUES(10,2,1);
CREATE TABLE "users_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY , "user_id" bigint NOT NULL REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "users_user_groups_user_id_5f6f5a90" ON "users_user_groups" ("user_id");
CREATE INDEX "users_user_groups_group_id_9afc8d0e" ON "users_user_groups" ("group_id");
CREATE INDEX "users_user_user_permissions_user_id_20aca447" ON "users_user_user_permissions" ("user_id");
CREATE INDEX "users_user_user_permissions_permission_id_0b93982e" ON "users_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "licentia_resources_componente_atualizado_por_id_eb9d2bfa" ON "licentia_resources_componente" ("atualizado_por_id");
CREATE INDEX "licentia_resources_componente_criado_por_id_77b21423" ON "licentia_resources_componente" ("criado_por_id");
CREATE INDEX "licentia_resources_projeto_atualizado_por_id_b033f722" ON "licentia_resources_projeto" ("atualizado_por_id");
CREATE INDEX "licentia_resources_projeto_criado_por_id_3a4c5481" ON "licentia_resources_projeto" ("criado_por_id");
CREATE INDEX "licentia_resources_statusdofreelapagamento_atualizado_por_id_2914435d" ON "licentia_resources_statusdofreelapagamento" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusdofreelapagamento_criado_por_id_02e3b016" ON "licentia_resources_statusdofreelapagamento" ("criado_por_id");
CREATE INDEX "licentia_resources_statusdoprocesso_atualizado_por_id_112eb223" ON "licentia_resources_statusdoprocesso" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusdoprocesso_criado_por_id_46af1c26" ON "licentia_resources_statusdoprocesso" ("criado_por_id");
CREATE INDEX "licentia_resources_statusdoprocessopagamento_atualizado_por_id_aef7d9dd" ON "licentia_resources_centrodecusto" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusdoprocessopagamento_criado_por_id_54747838" ON "licentia_resources_centrodecusto" ("criado_por_id");
CREATE INDEX "licentia_resources_empresa_atualizado_por_id_2d6a617f" ON "licentia_resources_empresa" ("atualizado_por_id");
CREATE INDEX "licentia_resources_empresa_criado_por_id_7c678b1c" ON "licentia_resources_empresa" ("criado_por_id");
CREATE INDEX "licentia_resources_fornecedor_atualizado_por_id_1a266ff6" ON "licentia_resources_fornecedor" ("atualizado_por_id");
CREATE INDEX "licentia_resources_fornecedor_criado_por_id_de2b3ea3" ON "licentia_resources_fornecedor" ("criado_por_id");
CREATE INDEX "licentia_resources_limitacaoedicao_atualizado_por_id_814ce9d6" ON "licentia_resources_limitacaoedicao" ("atualizado_por_id");
CREATE INDEX "licentia_resources_limitacaoedicao_criado_por_id_c89f39fc" ON "licentia_resources_limitacaoedicao" ("criado_por_id");
CREATE INDEX "licentia_resources_localizacaodorecurso_atualizado_por_id_51453029" ON "licentia_resources_localizacaodorecurso" ("atualizado_por_id");
CREATE INDEX "licentia_resources_localizacaodorecurso_criado_por_id_226790e2" ON "licentia_resources_localizacaodorecurso" ("criado_por_id");
CREATE INDEX "licentia_resources_statusanaliseautrec_atualizado_por_id_22e6eb02" ON "licentia_resources_statusanaliseautrec" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusanaliseautrec_criado_por_id_f3d4af02" ON "licentia_resources_statusanaliseautrec" ("criado_por_id");
CREATE INDEX "licentia_resources_statusanaliseeditorial_atualizado_por_id_5b091f3b" ON "licentia_resources_statusanaliseeditorial" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusanaliseeditorial_criado_por_id_39c16707" ON "licentia_resources_statusanaliseeditorial" ("criado_por_id");
CREATE INDEX "licentia_resources_statusdoorcamento_atualizado_por_id_410e6708" ON "licentia_resources_statusdoorcamento" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusdoorcamento_criado_por_id_3f5b0e8d" ON "licentia_resources_statusdoorcamento" ("criado_por_id");
CREATE INDEX "licentia_resources_statusdoorcamentoaprovacao_atualizado_por_id_294741a9" ON "licentia_resources_statusdoorcamentoaprovacao" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusdoorcamentoaprovacao_criado_por_id_1088e510" ON "licentia_resources_statusdoorcamentoaprovacao" ("criado_por_id");
CREATE INDEX "licentia_resources_statusdoprocessopagamentofornecedor_atualizado_por_id_14d72d0c" ON "licentia_resources_statusdoprocessopagamentofornecedor" ("atualizado_por_id");
CREATE INDEX "licentia_resources_statusdoprocessopagamentofornecedor_criado_por_id_8a1e3f82" ON "licentia_resources_statusdoprocessopagamentofornecedor" ("criado_por_id");
CREATE INDEX "licentia_resources_tipodetermo_atualizado_por_id_5b59cc57" ON "licentia_resources_tipodetermo" ("atualizado_por_id");
CREATE INDEX "licentia_resources_tipodetermo_criado_por_id_6348fde5" ON "licentia_resources_tipodetermo" ("criado_por_id");
CREATE INDEX "users_departamento_atualizado_por_id_3d741ece" ON "users_departamento" ("atualizado_por_id");
CREATE INDEX "users_departamento_criado_por_id_1a9bd662" ON "users_departamento" ("criado_por_id");
CREATE INDEX "users_user_departamentos_user_id_e680dba7" ON "users_user_departamentos" ("user_id");
CREATE INDEX "users_user_departamentos_departamento_id_f2f0d2d8" ON "users_user_departamentos" ("departamento_id");
CREATE INDEX "licentia_process_process_atribuido_a_process_id_a7fe17b1" ON "licentia_process_process_atribuido_a" ("process_id");
CREATE INDEX "licentia_process_process_atribuido_a_user_id_9d0df027" ON "licentia_process_process_atribuido_a" ("user_id");
CREATE INDEX "licentia_process_historicalprocess_id_df4bf4ba" ON "licentia_process_historicalprocess" ("id");
CREATE INDEX "licentia_process_historicalprocess_retranca_1f95ef80" ON "licentia_process_historicalprocess" ("retranca");
CREATE INDEX "licentia_process_historicalprocess_history_date_485b77ac" ON "licentia_process_historicalprocess" ("history_date");
CREATE INDEX "licentia_process_historicalprocess_atualizado_por_id_e4e57e59" ON "licentia_process_historicalprocess" ("atualizado_por_id");
CREATE INDEX "licentia_process_historicalprocess_centro_de_custo_id_1f3f00c9" ON "licentia_process_historicalprocess" ("centro_de_custo_id");
CREATE INDEX "licentia_process_historicalprocess_componente_id_d9a8a241" ON "licentia_process_historicalprocess" ("componente_id");
CREATE INDEX "licentia_process_historicalprocess_criado_por_id_1f16f425" ON "licentia_process_historicalprocess" ("criado_por_id");
CREATE INDEX "licentia_process_historicalprocess_empresa_id_8b739eb5" ON "licentia_process_historicalprocess" ("empresa_id");
CREATE INDEX "licentia_process_historicalprocess_fornecedor_id_ab3e52be" ON "licentia_process_historicalprocess" ("fornecedor_id");
CREATE INDEX "licentia_process_historicalprocess_history_user_id_a69022c2" ON "licentia_process_historicalprocess" ("history_user_id");
CREATE INDEX "licentia_process_historicalprocess_limitacao_edicao_id_e8ef5c01" ON "licentia_process_historicalprocess" ("limitacao_edicao_id");
CREATE INDEX "licentia_process_historicalprocess_localizacao_do_recurso_id_a03cea25" ON "licentia_process_historicalprocess" ("localizacao_do_recurso_id");
CREATE INDEX "licentia_process_historicalprocess_projeto_id_ecff3998" ON "licentia_process_historicalprocess" ("projeto_id");
CREATE INDEX "licentia_process_historicalprocess_status_analise_autrec_id_8050c62f" ON "licentia_process_historicalprocess" ("status_analise_autrec_id");
CREATE INDEX "licentia_process_historicalprocess_status_analise_editorial_id_c4299606" ON "licentia_process_historicalprocess" ("status_analise_editorial_id");
CREATE INDEX "licentia_process_historicalprocess_status_do_freela_pagamento_id_d9bfec87" ON "licentia_process_historicalprocess" ("status_do_freela_pagamento_id");
CREATE INDEX "licentia_process_historicalprocess_status_do_orcamento_id_487a5c65" ON "licentia_process_historicalprocess" ("status_do_orcamento_id");
CREATE INDEX "licentia_process_historicalprocess_status_do_processo_id_591747ad" ON "licentia_process_historicalprocess" ("status_do_processo_id");
CREATE INDEX "licentia_process_historicalprocess_status_do_processo_pagamento_fornecedor_id_357b5c59" ON "licentia_process_historicalprocess" ("status_do_processo_pagamento_fornecedor_id");
CREATE INDEX "licentia_process_historicalprocess_tipo_de_termo_id_88d02054" ON "licentia_process_historicalprocess" ("tipo_de_termo_id");
CREATE INDEX "licentia_process_historicalprocess_status_do_orcamento_aprovacao_id_57758f7e" ON "licentia_process_historicalprocess" ("status_do_orcamento_aprovacao_id");
CREATE INDEX "licentia_process_process_atualizado_por_id_d7f1969f" ON "licentia_process_process" ("atualizado_por_id");
CREATE INDEX "licentia_process_process_centro_de_custo_id_3073b769" ON "licentia_process_process" ("centro_de_custo_id");
CREATE INDEX "licentia_process_process_componente_id_14748629" ON "licentia_process_process" ("componente_id");
CREATE INDEX "licentia_process_process_criado_por_id_f8acca07" ON "licentia_process_process" ("criado_por_id");
CREATE INDEX "licentia_process_process_empresa_id_4fbef6ef" ON "licentia_process_process" ("empresa_id");
CREATE INDEX "licentia_process_process_fornecedor_id_c1c6a34e" ON "licentia_process_process" ("fornecedor_id");
CREATE INDEX "licentia_process_process_limitacao_edicao_id_47cbb415" ON "licentia_process_process" ("limitacao_edicao_id");
CREATE INDEX "licentia_process_process_localizacao_do_recurso_id_b011439e" ON "licentia_process_process" ("localizacao_do_recurso_id");
CREATE INDEX "licentia_process_process_projeto_id_95c1b048" ON "licentia_process_process" ("projeto_id");
CREATE INDEX "licentia_process_process_status_analise_autrec_id_8e903b4e" ON "licentia_process_process" ("status_analise_autrec_id");
CREATE INDEX "licentia_process_process_status_analise_editorial_id_6f9a22fa" ON "licentia_process_process" ("status_analise_editorial_id");
CREATE INDEX "licentia_process_process_status_do_freela_pagamento_id_0cd828c1" ON "licentia_process_process" ("status_do_freela_pagamento_id");
CREATE INDEX "licentia_process_process_status_do_orcamento_id_280a8aed" ON "licentia_process_process" ("status_do_orcamento_id");
CREATE INDEX "licentia_process_process_status_do_processo_id_79c8cf6f" ON "licentia_process_process" ("status_do_processo_id");
CREATE INDEX "licentia_process_process_status_do_processo_pagamento_fornecedor_id_a8b78d9d" ON "licentia_process_process" ("status_do_processo_pagamento_fornecedor_id");
CREATE INDEX "licentia_process_process_tipo_de_termo_id_50820bb0" ON "licentia_process_process" ("tipo_de_termo_id");
CREATE INDEX "licentia_process_process_status_do_orcamento_aprovacao_id_36a72c4e" ON "licentia_process_process" ("status_do_orcamento_aprovacao_id");

SET session_replication_role = 'origin';
