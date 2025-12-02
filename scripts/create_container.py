from azure.storage.blob import BlobServiceClient

connection = BlobServiceClient(
    account_url="http://localhost:10000/devstoreaccount1",
    credential="Eby8vdM02xNOcqFEYpYJys2OV8I6r9Q1qho="
)

container_name = "datalake"
connection.create_container(container_name)
print("Container criado: ", container_name)