import imp
from backend.classes.Common import *
from backend.dao.PartnersDAO import PartnersDAO

class InitInfo():

	def init(request):

		user_id = request.user.id
		email_id = request.user.email
		partner_code, msm_obj_slave, msm_obj_master = None,None,None
		master_slave_email_ids = []
		is_master_user = False
		is_payment_link_generation_partner = False
		#This code block will check the User is Slave and assign Partner Code
		# msm => Master Slave Mapping
		msm_obj_slave = PartnersDAO.get_msm(condition={'msm_slave_email':email_id}) 
		print('msm_obj_slave:: ', msm_obj_slave)
		msm_obj_slave = msm_obj_slave if len(msm_obj_slave) > 0 else None
		if msm_obj_slave is not None:
			print('msm_obj_slave:: ',msm_obj_slave)
			partner_code = msm_obj_slave[0]['msm_partner_code']
		
		if partner_code is None:
			partners_code = PartnersDAO.get_partners('partners_code',condition={'partners_mis_userid':user_id})
			partner_code = str(partners_code[0]['partners_code'])
			
	
		#This code block will check the User is Master and get all the Slave User Email Id
		if msm_obj_slave is None:
			msm_obj_master = PartnersDAO.get_msm(condition={'msm_master_email':email_id})
			if len(msm_obj_master) > 0:
				for msm in msm_obj_master:
					master_slave_email_ids.append(msm['msm_slave_email'])
			
			is_master_user = True if len(master_slave_email_ids) > 0 else False

		is_payment_link_generation_partner = True if partner_code in Common.payment_link_generation_partners else False
		
		return {
			'partner_code': partner_code,
			'user_id': user_id,
			'is_master_user': is_master_user,
			'is_payment_link_generation_partner': is_payment_link_generation_partner,
			'host_url': Common.host_url
		}