import os
import pandas as pd

def explode_data(conteudo_avro, avro_file, parquet_dir):

    # Converter para DataFrame Pandas
    df = pd.DataFrame(conteudo_avro)

    # Explodir os campos aninhados
    df_flat = pd.concat([df.drop(['data'], axis=1), df['data'].apply(pd.Series)], axis=1)

    # Converter para Parquet
    parquet_path = os.path.join(parquet_dir, avro_file.replace('.avro', '.parquet'))
    df_flat.to_parquet(parquet_path)

    # Ler o arquivo parquet para um data frame
    df_exploded = pd.read_parquet(parquet_path)

    #Retorna um dataframe
    return df_exploded
