import pandas as pd
#Dados da base do TSE:
dados_tse = "https://cdn.tse.jus.br/estatistica/sead/odsele/arquivos_gerados/resultados/20221115/682c812ccb32e42937205141b45d9fcf/votacao_candidato.csv.zip"
df = pd.read_csv(filepath_or_buffer=dados_tse,  sep=';', encoding='latin1')

#Array dos estados basileiros:
uf = df.sg_uf.unique()

#Loop para separar as informações por estado e gravar os dados em CSV:
for i in uf:
  df_uf = df.query(f'sg_uf == "{i}"')
  df_uf.to_csv(path_or_buf=f'./dados/{i}.zip',sep=';',index=False, compression={'method': 'zip', 'archive_name': f'{i}.csv'})

  
