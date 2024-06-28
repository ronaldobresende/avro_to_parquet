
Criar o ambiente virtual:

cd R:\python\avro_to_parquet
python -m venv avro_to_parquet

Ativar o ambiente
avro_to_parquet\Scripts\activate

Instalar libs
pip install -r requirements.txt

Para rodar local: 
python avro_to_parquet

O arquivo que tem a função de explodir é o explode_avro_data.py
Dentro do lambda_package.zip tem o lambda_function.py que eu usei

