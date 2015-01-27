BEGIN;
CREATE TABLE "auth_user" ("id" serial NOT NULL PRIMARY KEY, "password" varchar(128) NOT NULL, "last_login" timestamp with time zone NOT NULL, "is_superuser" boolean NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" boolean NOT NULL, "is_active" boolean NOT NULL, "date_joined" timestamp with time zone NOT NULL);
CREATE TABLE "auth_group" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_permission" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "codename" varchar(100) NOT NULL, "content_type_id" integer NOT NULL);
ALTER TABLE "auth_permission" ADD CONSTRAINT auth_permission_content_type_id_cf901bb0fdd2ad0_uniq UNIQUE ("content_type_id", "codename");
CREATE TABLE "auth_group_permissions" ("id" serial NOT NULL PRIMARY KEY, "group_id" integer NOT NULL, "permission_id" integer NOT NULL, UNIQUE ("group_id", "permission_id"));
CREATE INDEX auth_permission_417f1b1c ON "auth_permission" ("content_type_id");
ALTER TABLE "auth_permission" ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX auth_group_permissions_0e939a4f ON "auth_group_permissions" ("group_id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX auth_group_permissions_8373b171 ON "auth_group_permissions" ("permission_id");
ALTER TABLE "auth_group_permissions" ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED;

COMMIT;
