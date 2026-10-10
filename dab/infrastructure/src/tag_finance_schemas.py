# Databricks notebook source
dbutils.widgets.text("catalog", "")
dbutils.widgets.text("erp_bronze_schema", "")
dbutils.widgets.text("erp_silver_schema", "")
dbutils.widgets.text("erp_gold_schema", "")

catalog = dbutils.widgets.get("catalog")
erp_bronze_schema = dbutils.widgets.get("erp_bronze_schema")
erp_silver_schema = dbutils.widgets.get("erp_silver_schema")
erp_gold_schema = dbutils.widgets.get("erp_gold_schema")

spark.sql(f"ALTER SCHEMA {catalog}.{erp_bronze_schema} SET TAGS ('Finance')")
spark.sql(f"ALTER SCHEMA {catalog}.{erp_silver_schema} SET TAGS ('Finance')")
spark.sql(f"ALTER SCHEMA {catalog}.{erp_gold_schema} SET TAGS ('Finance')")
