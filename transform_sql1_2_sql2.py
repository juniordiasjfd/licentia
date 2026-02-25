import re
import os

def limpar_para_postgres(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8') as f_out:
        
        # Desativa checks de integridade para facilitar o restore inicial
        f_out.write("SET session_replication_role = 'replica';\n")
        
        for linha in f_in:
            # Remove comandos específicos do SQLite
            if any(x in linha for x in ['BEGIN TRANSACTION', 'COMMIT', 'sqlite_sequence', 'CREATE UNIQUE INDEX']):
                continue
            
            # Substitui AUTOINCREMENT por SERIAL (ajuste manual se necessário no pgAdmin)
            linha = linha.replace('AUTOINCREMENT', '')
            
            # Troca aspas duplas de strings para aspas simples (se houver)
            # Nota: O Postgres usa " para nomes de tabelas/colunas e ' para valores
            
            f_out.write(linha)
            
        f_out.write("\nSET session_replication_role = 'origin';\n")

limpar_para_postgres(os.path.join(os.getcwd(),'base_sqlite3.sql'), os.path.join(os.getcwd(),'base_preparada_para_postgre.sql'))
print("Arquivo pronto para o pgAdmin!")