from backend.dao.PartnersDAO import *

def set_partner_code(request):
	print('set_partner_code')

	error = None
	user_id = request.user.id
	parnter_obj = PartnersDAO.get_partners(condition={'partners_mis_userid':user_id})
	error = "Invalid User id" if len(parnter_obj) == 0 else None

	if error is None:
		print('set_partner_code  1111111')
		parnter_obj = parnter_obj[0]
		request.session.modified = True
		request.session['partner_code'] = parnter_obj['partners_code']


