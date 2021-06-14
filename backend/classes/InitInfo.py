from backend.classes.Common import *

class InitInfo():

	def init(request):
		print('inside init')
		user_id = request.user.id
		# print('user_id:: ', user_id)

		user_id_partner_code_dict = Common.user_id_partner_code_dict

		partner_code = user_id_partner_code_dict[user_id] if user_id in user_id_partner_code_dict else 0
		print('user_id:: ', user_id)
		print('partner_code:: ', partner_code)
		
		return {
			'partner_code': partner_code
		}