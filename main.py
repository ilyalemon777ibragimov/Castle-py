import random

print('Чтение  сохранений после последних сессий... Пожалуйста подождите')
print(' ')
hp1=5

save=open("save.txt")
kills=int(save.readline())
krits=int(save.readline())
pvekols=int(save.readline())
save.close()

s=input('Чтение заершено. Ведите 1, если хотите чтобы игра продолжилась         ')
if s=="1":
        print("Отлично, продолжим игру через \n 3 \n 2 \n 1....")
        kill=kills
        krit=krits
else:
        print("Отлично, начнём игру через \n 3 \n 2 \n 1....")
        kill=0
        krit=0
print('\n \n \n')
print(' ')
print(' ')


print('  _____          _   _                ')
print(' / ____|        | | | |             ')
print('| |     __ _ ___| |_| | ___   _ __   _   _ ')
print("| |    / _` / __| __| |/ _ \ | '_ \ | | | |")
print('| |___| (_| \__ \ |_| |  __/_| |_) || |_| |')
print(' \_____\__,_|___/\__|_|\___(_) .__/  \__, |')
print('                             | |      __/ |')
print('                             |_|     |___ /')




print("Главное меню")
e=input("Нажмите Enter, чтобы начать играть. Для просмотра статистики введите stat           ")
if e=="stat":
        print("Вы совершили "+str(kills)+" убийств")
        print("Критический урон был нанесён "+str(krits)+" раз")
        print("Последний цикл - "+str(pvekols)+" PVE")
        a=input('Нажмите Enter, чтобы начать играть')
if e=="ыефе":
        print("Это надо было сделать с английской раскладкой... но видимо вам как и мне на это плевать.")
        print("Вы совершили "+str(kills)+" убийств")
        print("Критический урон был нанесён "+str(krits)+" раз")
        print("Последний цикл - "+str(pvekols)+" PVE")
        a=input('Нажмите Enter, чтобы начать играть')
pvekol=int(input('Введите количество PVE >>> '))
pvekolsave=pvekol
def pve(hp,eniv):
	print('На вас напал '+eniv)
	pc=0
	ec=0
	round=1
	while True:
		if hp<=0:
			print('Вы протерпели поражение. Игра окончена')
			break
		else:
			print('Раунд '+str(round))
			a=input('Нажмите Enter, чтобы бросить кости')
			print('Вы бросаете кости')
			print(eniv+' бросает кости')

			pc = random.randint(1, 6)
			ec = random.randint(1, 6)
			print('Счёт '+str(pc)+':'+str(ec))
			
			if pc>=ec:
				if pc>=5:
					print('Ваше оружие в огне!!!')
					a=input('Нажмите Enter, чтобы использовать оружие')
					print('Враг получил критический урон')
					if hp < 5:
						print('Ваши сердца востановленны')
					print('Можно продолжить путь')
					a=input('Нажмите Enter, чтобы продолжить')
					return 2
				else:
					a=input('Нажмите Enter, чтобы использовать оружие')
					print('Вы победили!')
					if hp < 5:
						print('Ваши сердца востановленны')
					print('Можно продолжить путь')
					a=input('Нажмите Enter, чтобы продолжить')
					return 1
			else:
				print('Вы проиграли этот раунд')
				print(eniv+' атакует')
				print('- 1 сердце')
				hp=hp-1
				print('У вас осталось '+str(hp)+' сердец')
				round+=1
				a=input('Нажмите Enter, чтобы продолжить')
while pvekol>0:
	res=pve(hp1,'Гоблин')
	if res==2:
		krit+=1
		kill+=1
	elif res==1:
		kill+=1
	pvekol+=-1


print('Вы совершили '+str(kill)+' убийств')	
print('Вы нанесли кретический урон '+str(krit)+' раз')
print('Происходит запись сохранения...')
print('Не закрывайте игру до конца сохранения, чтобы не повредить файл сохранений')
save=open("save.txt", "w")
save.write("{0}\n".format(kill))
save.write("{0}\n".format(krit))
save.write("{0}\n".format(pvekolsave))
save.close()
print('Сохранение завершено, можно закрыть игру')
	
	
	
