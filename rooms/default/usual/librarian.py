from localizations import locale_manager
from localizations import locale_manager
from constants import *

name = locale_manager.get('rooms.default.usual.librarian.phrase_1')

room_type = 'other'

def get_actions(user):
	return [ locale_manager.get('rooms.default.usual.librarian.phrase_2'), locale_manager.get('rooms.default.usual.librarian.phrase_3'), locale_manager.get('rooms.default.usual.librarian.phrase_101') ]

def enter(user, reply):
	reply(locale_manager.get('rooms.default.usual.librarian.phrase_102'), photo='BQADAgAD4QgAAmrZzgf86MI3ztAEQwI')

def action(user, reply, text):
	actions = get_actions(user)

	if text == actions[0]:
		user.throw_dice(reply, 'derp')
	elif text == actions[1]:
		user.mana_damage += 5
		reply(locale_manager.get('rooms.default.usual.librarian.phrase_4'))
		if not user.paid(50):
			reply(locale_manager.get('rooms.default.usual.librarian.phrase_5'))
			user.make_damage(40, 60, reply, name=name)
		user.leave(reply)
	else:
		if user.has_item('necromicrone'):
			usr_name = user.name.lower()
			user.leave(reply)
			reply(locale_manager.get('rooms.default.usual.librarian.phrase_103').format(usr_name))
		else:
			usr_name = user.name.lower()
			if (locale_manager.get('rooms.default.usual.librarian.phrase_6')in usr_name) or ('book worm' in usr_name) or (locale_manager.get('rooms.default.usual.librarian.phrase_6')in usr_name):
				reply(locale_manager.get('rooms.default.usual.librarian.phrase_8'))
				user.leave(reply)
			else:
				reply(locale_manager.get('rooms.default.usual.librarian.phrase_105') .format(usr_name))


def dice(user, reply, result, subject='derp'):
	if result > DICE_MIDDLE:
		reply(locale_manager.get('rooms.default.usual.librarian.phrase_9'))
		user.leave(reply)
	else:
		reply(locale_manager.get('rooms.default.usual.librarian.phrase_106'))
		user.leave(reply)