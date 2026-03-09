import pandas as pd
import sqlalchemy

server = "sql-tristan-customer.database.windows.net"
database = "customer_analysis_db"
username = "sqladmin"
password = "Yloha*0602"

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}:1433/{database}"
    "?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no"
)

engine = sqlalchemy.create_engine(connection_string)

customer_agg = pd.read_csv("data_export:/customer_aggregates.csv")
rfm = pd.read_csv("data_export:/rfm_clients.csv")

customer_agg.to_sql("customer_aggregates", engine, if_exists="append", index=False)
rfm.to_sql("rfm_clients", engine, if_exists="append", index=False)

print("Import terminé 🚀")