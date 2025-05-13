import pandas as pd
import numpy as np
from tabulate import tabulate


file_path = 'data/fbref_28_4_25.csv'  # Путь к вашим данным
df = pd.read_csv(file_path)

# Фильтрация DataFrame
#'Squad'=='Manchester Utd' если нужны только игроки МЮ
poisk = df[(df['Min'] > 900) & (df['Squad']=='Manchester Utd')]

#сюда пишем 
stats=["Player","xG", "Gls"]

#Сюда пишем название столбцов в таблице если хотим поменять
head=['Name','PSxG', 'PSxG +']

mas=[]
# Проверка, найдены ли записи
if not poisk.empty:
    # 
    for index, row in poisk.iterrows():
        player_name = row['Player']  # Замените на название колонки с именем игрока
        temp=[]
        for i in range(len(stats)):
        	temp.append(row[stats[i]])        
        mas.append(temp)
        
else:
    print("Игрок не найден.")

print ('\n')

#вместо stats пишем head если хотим изменить название столбцов
print(tabulate(mas, tablefmt='pipe', stralign='center',headers=stats))

print ('\n')
