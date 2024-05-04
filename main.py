import random
hp1=5
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
			if pc>=ec:
				print('Вы победили!')
				print('Можно продолжить путь')
				break
			else:
				print('Вы проиграли этот раунд')
				print('- 1 сердце')
				hp=hp-1
				round+=1
pve(hp1,'Тест')
				
	
	
	