# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bissexto, sendo que nesses casos Fevereiro terá 29 dias.

# def data(dataNum):
#      dic_datas = {'01':'Janeiro', '02':'Fevereiro', '03':'Março', '04':'Abril', '05':'Maio', '06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}
#      if dataNum[3:5] == dic_datas['01']:
#          return dic_datas.values()
#      elif dataNum[3:5] == dic_datas['02']:
#          return dic_datas.values()