import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import  getch


from tabulate import tabulate
from matplotlib.colors import LinearSegmentedColormap


fig = plt.figure(figsize=(13,9))
ax = plt.axes()
# Загрузка данных из 

file_path = 'data.csv'  # Путь к вашему файлу
df = pd.read_csv(file_path)



#nm='Name,'
#stroka=nm+''
#st=stroka.split(',')


# Фильтрация DataFrame для игроков Manchester United
#man_utd_players = df[df['Squad'].str.contains('Manchester Utd', case=False, na=False)]
#if  df[(df['Pos']=='FW') or (df['Pos']=='MF,FW') or (df['Pos']=='FW,MF')]:
#    df['Pos']=True
poisk = df[(df['Min'] > 900) & (df['PSxG+/-']>=0) & (df['Stp%']>=7)]

mas=[]
fix=[]
head=['Name','PSxG', 'PSxG +','Cr.Stp%','%усп.длин.передач']

stats=["Player","PSxG", "PSxG+/-"]
z=0
# Проверка, найдены ли записи
if not poisk.empty:
    # 
    for index, row in poisk.iterrows():
        player_name = row['Player']  # Замените на название колонки с именем игрока
        temp=[]
        for i in range(len(stats)):
        	temp.append(row[stats[i]])
        
        """
        psxg=row['PSxG']
        age=row['Age']
        pm=row['PSxG+/-']
        #team=row['Squad']'
        cross=row['Stp%']
        vper=row['Cmp%_stats_keeper_adv']
        #if minutes_played>0:  # Замените
        mas.append([player_name,psxg,pm,cross,vper])
        """
        print(temp)
        mas.append(temp)
        z=z+1
        
else:
    print("Игрок не найден.")

fam=[]
for i in range(len(mas)):
    fam.append(mas[i][0])




final=[]



print ('\n')

print(tabulate(mas, tablefmt='pipe', stralign='center',headers=stats))



print ('\n')


"""
print (final)
# Генерируем случайные индексы для выбора цветов

colors = [
    (1.0, 0.34, 0.2),   # Оранжевый
    (0.5, 0.0, 0.5),    # Фиолетовый вместо зеленого
    (0.2, 0.34, 1.0),   # Синий
    (1.0, 0.2, 0.63),   # Розовый
]

fix_c=[
(0.5, 0.0, 0.5),    # Фиолетовый вместо зеленого
(0.2, 0.34, 1.0)]   # Синий

colors_cmap = [
    "#FF6347",  # Томатный (более красный)
    "#FFA07A",  # Светло-оранжевый
    "#FFFFFF",  # Белый
    "#D3F9D8",  # Бледно-зеленый
    "#90EE90",   # Светло-зеленый
    "#32CD32"   # Светло-зеленый
]

positions_cmap = [0, 0.1, 0.5, 0.7, 0.85, 1]

# Создаем собственную палитру
custom_cmap = LinearSegmentedColormap.from_list("custom_palette", list(zip(positions_cmap, colors_cmap)))

# Генерируем случайные индексы для выбора цветов

col = np.random.choice(len(colors), size=len(mas))

"""


"""

plt.axvline(x=0,ls=":",c='#696969')
#plt.axhline(y=0,ls=":",c='#696969')
gradient = np.linspace(0, 0.2, 256)  # Градиент от 0 до 1
gradient = np.vstack((gradient, gradient))  # Дублируем для создания 2D массива
ax.imshow(gradient, aspect='auto', extent=[-14.2, 12, 8, 56], origin='lower', cmap=custom_cmap,alpha=1)

new_fam = []

for name in fam: 
	if name=='Nico Williams':
		new_fam.append('N. Williams')
	else:
		words = name.split()  # Разбиваем строку на слова
		if len(words) > 1:  # Проверяем, больше ли одно слово
			new_name = ' '.join(words[1:])  # Удаляем первое слово
			new_fam.append(new_name)
		else:
			new_fam.append(name)  # Оставляем без изменений

#new_fam=fam
mank=[]
#'#343434'

for i in range(len(mas)):
    if mas[i][3]=='Manchester Utd':
        mank.append(i)

    else:
        #if (mas[i][2]>=5) | (mas[i][3]>=1.3):
        plt.text(mas[i][2]+0.1, mas[i][1]+0.15, new_fam[i],color=colors[col[i]],bbox=dict(facecolor='white', alpha=0.6, boxstyle='round,pad=0.05'))
        #plt.text(mas[i][2]+0.1, mas[i][1]+0.15, new_fam[i],color=colors[col[i]])
        
        plt.scatter(mas[i][2], mas[i][1], facecolor=colors[col[i]],alpha=1)


mup=[]
for i in mank:
    plt.scatter(mas[i][2], mas[i][1], facecolor='red')
    #plt.text(mas[i][3]-0.13, mas[i][2]+0.05, new_fam[i],color='red',bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.1'), fontsize=13)
    plt.text(mas[i][2]+0.1, mas[i][1]+0.15, new_fam[i],color='red',fontsize=13,bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.1'))
        
    mup.append(mas[i])



        


""" 
"""
for i in range(len(mas)):
    mas[i].pop(3)
print ('\n')

"""
"""

#print(tabulate(smas, tablefmt="grid"))
#head=['Игрок','Голы','xG','Разница']
#print(tabulate(mas, tablefmt='pipe', stralign='center',headers=head))
#print(tabulate(mas1, tablefmt='pipe', stralign='center',headers=head1))
#print(tabulate(smas, tablefmt='pipe', stralign='center',headers=head))
print ('\n')
plt.ylabel("PSxG",size=15)
plt.xlabel("PSxG +/-",size=15)

fig.text(
    0.515, 0.89, '2024-2025 Big 5 European Leagues', size=13,
    ha="center", color="black"
)
fig.text(
    0.515, 0.93, 'Goalkeeping. PSxG. 900+ min', size=15,
    ha="center", color="black"
)

#rodri_filt='* Min > 1000\nPrgP per 90 > 4\nTackles per 90 > 1.5\nWin Tackles> 50%,\nInterceptions per 90 >  0.7\nWin Aerial Duels >50%\nvs Drib Duels >50%'
rodri_filt=''
fig.text(
    0.88, 0.68, rodri_filt, size=10,
    ha="right", color="black"
)
fig.text(
    0.255, 0.89, f"t.me/ne_dan_ton", size=10,
    ##fontproperties=font_italic.prop, color="#F2F2F2",
    color="black",
    ha="right",
    linespacing=1.7
)
fig.text(
    0.84, 0.94, f"Data: FBref (Opta)", size=9,
    ##fontproperties=font_italic.prop, color="#F2F2F2",
    color="black",
    ha="center"
)
print (mank)
#fm=os.path.basename(__file__)
#plt.savefig('test'+'.png', dpi=400, bbox_inches = "tight")
print ('F')
#plt.show()

"""

