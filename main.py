# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_a = 'Ruud Gullit'
scorer_b = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers =  scorer_a + ' ' + str(goal_0) + ',' + ' ' + scorer_b + ' ' + str(goal_1)
report = f'{scorer_a} scored in the {goal_0}nd minute\n{scorer_b} scored in the {goal_1}th minute'

player = 'Ruud Gullit'

first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:]
last_name_len = len(last_name)
name_short = f'{player[0]}. { last_name}'

chant_space = f'{first_name}! ' *len(first_name)
chant = chant_space[:-1]
good_chant = chant[-1] != ' '
print(good_chant)
print(last_name_len)