import pandas as pd
import codecs


df = pd.read_excel("./Resultados_MEGASENA.xlsx")

# NOME DAS COLUNAS
# Concurso
# Data do Sorteio
# Coluna1
# Coluna2
# Coluna3
# Coluna4
# Coluna5
# Coluna6
# Ganhadores Faixa 1
# Ganhadores Faixa 2
# Ganhadores Faixa 3
# Rateio Faixa 1
# Unnamed: 12
# Rateio Faixa2
# Rateio Faixa 3
# Cidade
# Valor Arrecadado
# Estimativa para o próximo concurso
# Valor Acumulado Próximo Concurso  
# Acumulado
# Sorteio Especial
# Observação


df = df.fillna('NULL')

def format_string(value):
    if value != 'NULL':
        value = value.replace("'","").replace("`","")
        return "\'" + str(value) + "\'"
    else: 
        return 'NULL'
    
def format_money(value):
    if value != 'NULL':
        return str(value).replace("R$","").replace(".","").replace(",",".")
    else: 
        return 'NULL'


c = 0
num = 1
file = f"output{num}.txt"
f = codecs.open(file, "x", "utf-8")

for ind in df.index:
    insert_string = "INSERT INTO MEGASENA VALUES ("
    insert_string += str(df['Concurso'][ind]) + ","
    insert_string += "TO_DATE(\'" + str(df['Data do Sorteio'][ind].strftime("%d/%m/%Y")) + "\','DD/MM/YYYY\')" + ","
    insert_string += str(df['Coluna1'][ind]) + ","
    insert_string += str(df['Coluna2'][ind]) + ","
    insert_string += str(df['Coluna3'][ind]) + ","
    insert_string += str(df['Coluna4'][ind]) + ","
    insert_string += str(df['Coluna5'][ind]) + ","
    insert_string += str(df['Coluna6'][ind]) + ","
    insert_string += str(df['Ganhadores Faixa 1'][ind]) + ","
    insert_string += str(df['Ganhadores Faixa 2'][ind]) + ","
    insert_string += str(df['Ganhadores Faixa 3'][ind]) + ","
    insert_string += format_money(df['Rateio Faixa 1'][ind]) + "," 
    insert_string += format_money(df['Rateio Faixa2'][ind]) + "," 
    insert_string += format_money(df['Rateio Faixa 3'][ind]) + "," 
    insert_string += format_string(df['Cidade'][ind]) + ","
    insert_string += format_money(df['Valor Arrecadado'][ind]) + "," 
    insert_string += format_money(df['Valor Arrecadado'][ind]) + "," 
    insert_string += format_money(df['Valor Acumulado Próximo Concurso'][ind]) + "," 
    insert_string += format_string(df['Acumulado'][ind]) + ","
    insert_string += format_string(df['Sorteio Especial'][ind]) + ","
    insert_string += format_string(df['Observação'][ind])
    insert_string += ");"
    
    print(insert_string)
    f.write(insert_string + '\n')
    c+=1

    if (c % 100) == 0:
        num+=1
        f.close()
        file = f"output{num}.txt"
        f = codecs.open(file, "x", "utf-8")


f.close()
