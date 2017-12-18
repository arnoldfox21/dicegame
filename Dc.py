import random

def throw(val):
	dice = val
	if 6 in dice and 1 in dice:
		winner = dice.index(6)
		dice.remove(6)
	elif 6 in dice:
		winner = dice.index(6)
		dice.remove(6)
	elif 1 in dice:
		winner = dice.index(1)
		dice.remove(1)
	else:
		winner = 'nothing'
		dice = dice
	result = [dice, winner]
	return result
def roll(number):

	NO =[1, 2, 3, 4, 5, 6]
	res = []
	for i in range(0, number):
		res.append(random.choice(NO))

	return res

choice = input('type the number of 0 to throw dice : ')

if choice == 0:
	d = roll(4)
	print 'result of dice : %s'%(d)
	res = throw(d)
	print 'dice remaining is %s with number %s'%(len(res[0]), res[0])

	if len(res) == 4:
		print 'the winner is nothing'
		print 'game was reset'
	else:
		choice2 = input('type the number of 0 to throw dice again : ')	
			
	if choice2 == 0:
		dc = roll(3)
		print 'result of dice : %s'%(dc)
		rest = throw(dc)
		print rest[0]
		if len(rest) == 3
			print 'the winner is player number %s'% (int(res[1])+1)
			print 'game over'
		else:
			choice2 = input('type the number of 0 to throw dice again : ')
		if choice2 == 0:
			d3 = roll(2)
			print 'result of dice : %s'%(d3)
			rest3 = throw(d3)
			print rest3[0]
			print 'the winner is player number %s'% (int(res[1])+1)
		else:
			print 'unknow command'
	else:
		print 'unknow command'
      
else:
	print 'unknow command'
   
   
