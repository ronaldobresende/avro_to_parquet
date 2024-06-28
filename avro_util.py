import os
import fastavro

# Diretórios
avro_dir = 'avro_files'
os.makedirs(avro_dir, exist_ok=True)

# Função para criar arquivos Avro (Exemplo)
def create_avro_files():
    schema = {
        "type": "record",
        "name": "Event",
        "fields": [
            {"name": "anomesdia", "type": "string"},
            {"name": "data", "type": {
                "type": "record",
                "name": "Data",
                "fields": [
                    {"name": "codigo_contrato", "type": "string"},
                    {"name": "codigo_produto", "type": "string"},
                    {"name": "codigo_garantia", "type": "int"},
                    {"name": "data_hora_evento", "type": "string"}
                ]
            }}
        ]
    }

    records = [
        {"anomesdia": "20240627", "data": {
            "codigo_contrato": "123",
            "codigo_produto": "456",
            "codigo_garantia": 800,
            "data_hora_evento": "2024-06-27T12:00:00"
        }},
        {"anomesdia": "20240627", "data": {
            "codigo_contrato": "789",
            "codigo_produto": "012",
            "codigo_garantia": 50,
            "data_hora_evento": "2024-06-27T13:00:00"
        }}
    ]

    file_path = os.path.join(avro_dir, '20240627.avro')
    with open(file_path, 'wb') as out:
        fastavro.writer(out, schema, records)
