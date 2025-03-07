from tinydb import TinyDB


db = TinyDB("pedidos.json")


def inserDB(data:dict) -> bool:
    TinyDB.default_table_name = "pedidos"
    if len(data) > 0:
        insert = db.insert(data)
    else:
        insert = None
    return True if isinstance(insert,int) else False

def get_all_pedidosDB() -> dict:
    TinyDB.default_table_name = "pedidos"
    return db.all()


if __name__ == "__main__":
    dados = get_all_pedidosDB() 
    for dado in dados:
        print(dado["idd"])


