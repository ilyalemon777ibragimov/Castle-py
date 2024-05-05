import random

print('  _____          _   _                ')
print(' / ____|        | | | |             ')
print('| |     __ _ ___| |_| | ___   _ __   _   _ ')
print("| |    / _` / __| __| |/ _ \ | '_ \ | | | |")
print('| |___| (_| \__ \ |_| |  __/_| |_) || |_| |')
print(' \_____\__,_|___/\__|_|\___(_) .__/  \__, |')
print('                             | |      __/ |')
print('                             |_|     |___ /')


hp1=5
kill=0
krit=0
pvekol=int(input('Введите количество pve >>> '))
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
			print('Счёт-'+str(pc)+':'+str(ec))
			
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
	
	
	