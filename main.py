import random
hp1=5
kill=0
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
			print('Вы бросаете кости')
			print(eniv+' бросает кости')
			pc = random.randint(1, 6)
			ec = random.randint(1, 6)
			print('Счёт-'+str(pc)+':'+str(ec))
			if pc>ec:
				if pc>=5:
					print('Враг получил критический урон')
				print('Вы победили!')
				print('Можно продолжить путь')
				return 1
				break
			else:
				print('Вы проиграли этот раунд')
				print('- 1 сердце')
				print('У вас осталось '+str(hp)+' сердец')
				hp=hp-1
				round+=1
kill+=pve(hp1,'Гоблин')
a=input('Нажмите Enter, чтобы продолжить')
kill+=pve(hp1,'Гоблин')
a=input('Нажмите Enter, чтобы продолжить')
kill+=pve(hp1,'Гоблин')
a=input('Нажмите Enter, чтобы продолжить')
kill+=pve(hp1,'Гоблин')
a=input('Нажмите Enter, чтобы продолжить')
print('Вы совершили '+str(kill)+' убийств')				
	
	
	