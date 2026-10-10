# Databricks notebook source
dbutils.widgets.text("catalog", "")
dbutils.widgets.text("crm_bronze_schema", "")
dbutils.widgets.text("crm_silver_schema", "")
dbutils.widgets.text("crm_gold_schema", "")

catalog = dbutils.widgets.get("catalog")

spark.sql(f"ALTER SCHEMA {catalog}.{dbutils.widgets.get('crm_bronze_schema')} SET TAGS ('Finance')")
spark.sql(f"ALTER SCHEMA {catalog}.{dbutils.widgets.get('crm_silver_schema')} SET TAGS ('Finance')")
spark.sql(f"ALTER SCHEMA {catalog}.{dbutils.widgets.get('crm_gold_schema')} SET TAGS ('Finance')")
