import imp
from backend.classes.Common import *
from backend.dao.PartnersDAO import PartnersDAO

class InitInfo():

	def init(request):
		print('inside init')
		user_id = request.user.id
		# print('user_id:: ', user_id)

		# user_id_partner_code_dict = Common.user_id_partner_code_dict
		partners_code = PartnersDAO.get_partners('partners_code',condition={'partners_mis_userid':user_id})
		print("partners_code:: ", partners_code[0]['partners_code'])
		# user_id_partner_code_dict = str(partners_code[0]['partners_code'])

		partner_code = str(partners_code[0]['partners_code'])
		print('user_id:: ', user_id)
		print('partner_code:: ', partner_code)
		
		return {
			'partner_code': partner_code,
			'user_id': user_id
		}