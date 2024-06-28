import os
import fastavro
from avro_util import create_avro_files
from explode_avro_data import explode_data

# Diretórios
avro_dir = 'avro_files'
parquet_dir = 'parquet_files'
os.makedirs(avro_dir, exist_ok=True)
os.makedirs(parquet_dir, exist_ok=True)

def avro_to_parquet_exploded():
    for avro_file in os.listdir(avro_dir):
        avro_path = os.path.join(avro_dir, avro_file)
        with open(avro_path, 'rb') as fo:
            reader = fastavro.reader(fo)
            records = [record for record in reader]
            print(f'Conteúdo dos arquivo Avro \n')
            print(f'{records}\n')

            df_parquet = explode_data(records, avro_file, parquet_dir)

            print(f'Conteúdo dos arquivo Parquet:\n')
            print(df_parquet)    

if __name__ == "__main__":
    # Criar arquivos Avro
    create_avro_files()
    avro_to_parquet_exploded()
