from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.vietnam.special.icecream.phrase_1')

room_type = 'other'
actions = [ locale_manager.get('rooms.vietnam.special.icecream.phrase_2'), locale_manager.get('rooms.vietnam.special.icecream.phrase_3'), locale_manager.get('rooms.vietnam.special.icecream.phrase_4') ]

def get_actions(user):
	return actions

def dice(user, reply, result, subject=None):
	if result > DICE_MIDDLE:
		reply(locale_manager.get('rooms.vietnam.special.icecream.phrase_5'))
	else:
		reply(locale_manager.get('rooms.vietnam.special.icecream.phrase_6'))

		if user.has_item('scissors'):
			user.remove_items_with_tag('scissors')
			reply(locale_manager.get('rooms.vietnam.special.icecream.phrase_7'))

		user.make_damage(20, 30, reply, death=False)
	user.leave(reply)

def enter(user, reply):
	msg = locale_manager.get('rooms.vietnam.special.icecream.phrase_8')
	reply(msg)

def action(user, reply, text):
	if text == actions[0]:
		reply(locale_manager.get('rooms.vietnam.special.icecream.phrase_9'))

		user.add_item('special', 'icecream')
	elif text == actions[1]:
		if user.gods_level[BUDDHA_NUM] > 0:
			reply(locale_manager.get('rooms.vietnam.special.icecream.phrase_10'))
			user.gods_level[BUDDHA_NUM] = 0
		else:
			reply(locale_manager.get('rooms.vietnam.special.icecream.phrase_11'))
			user.make_damage(1, 5, reply, death=False)
	else:
		user.leave(reply)