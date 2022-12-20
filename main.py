# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_a = 'Ruud Gullit'
scorer_b = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers =  f'{scorer_a} {str(goal_0)}, {scorer_b} {str(goal_1)}'
report = f'{scorer_a} scored in the {goal_0}nd minute\n{scorer_b} scored in the {goal_1}th minute'
player = 'Ruud Gullit'
first_name_find = player[player.find('')]
first_name_slice = slice(1,4)
first_name = first_name_find + player[first_name_slice]
last_name_find = player[player.find('')+5]
last_name_slice = slice(6,11)
last_name_len = len(player[5:])
last_name = last_name_find + player[last_name_slice]
name_short = f'{player[0]}. {player[5:]}'
chant = f'{first_name}! {first_name}! {first_name}! {first_name}!'
good_chant = chant != chant[-1]
print(last_name)