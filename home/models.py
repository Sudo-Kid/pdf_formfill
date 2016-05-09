from django.db import models


class Appl(models.Model):
    """
    FieldName: appl.name
    FieldName: appl.addressL1
    FieldName: appl.addressL2
    FieldName: appl.city
    FieldName: appl.province
    FieldName: appl.postal
    FieldName: appl.additionalInfo
    FieldName: appl.sub_mgr_acct_id_label
    FieldName: appl.sub_mgr_acct_id
    FieldName: appl.deduct_fee_yes
    """
    name = models.CharField(max_length=254)
    addressL1 = models.CharField(max_length=254)
    addressL2 = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    province = models.CharField(max_length=254)
    postal = models.CharField(max_length=254)
    additionalInfo = models.CharField(max_length=254) # Switch to text area
    sub_mgr_acct_id_label = models.CharField(max_length=254)
    deduct_fee_yes = models.BooleanField(default=False)

    def __str__(self):
        return self.name


"""
FieldName: legal.undiv
FieldName: legal.PID
FieldName: legal.description
FieldName: legal.b.final_stc_yes
FieldName: legal.pickup_stc_name
FieldName: legal.RefPlanField
FieldName: legal.RefPlanText
FieldName: legal.SavedPID
FieldName: legal.insertNOPIDNUMBR
FieldName: transferee.1_name_occ
FieldName: transferee.2_name_occ
FieldName: transferee.address
FieldName: transferee.city
FieldName: transferee.prov
FieldName: transferee.postal_cd
FieldName: transferee.addl_info
FieldName: transferee.corp_type
FieldName: transferee.corp_num
FieldName: transferee.country
FieldName: lender.1_name_occ
FieldName: lender.text
FieldName: lender.address
FieldName: lender.city
FieldName: lender.prov
FieldName: lender.postal_cd
FieldName: lender.addl_info
FieldName: lender.corp_type
FieldName: lender.corp_num
FieldName: lender.country
FieldName: pay.a_principal
FieldName: pay.b_int_rate
FieldName: pay.c_dt_info
FieldName: pay.c_dt_yy
FieldName: pay.c_dt_mm
FieldName: pay.c_dt_dd
FieldName: pay.d_int_calc_period
FieldName: pay.e_payment_dates
FieldName: pay.f_dt_info
FieldName: pay.f_dt_yy
FieldName: pay.f_dt_mm
FieldName: pay.f_dt_dd
FieldName: pay.g_amount
FieldName: pay.h_int_rate
FieldName: pay.i_dt_info
FieldName: pay.i_dt_yy
FieldName: pay.i_dt_mm
FieldName: pay.i_dt_dd
FieldName: pay.j_rent_ref
FieldName: pay.k_place
FieldName: pay.l_dt_info
FieldName: pay.l_dt_yy
FieldName: pay.l_dt_mm
FieldName: pay.l_dt_dd
FieldName: pay.j_rent_yes
FieldName: pay.j_rent_no
FieldName: doc.ctl.e
FieldName: doc.ctl.e7
FieldName: doc.ctl.e2
FieldName: doc.ctl.d1
FieldName: doc.ctl.e12
FieldName: doc.ctl.e11
FieldName: doc.ctl.b
FieldName: doc.declar.attached
FieldName: doc
FieldName: lto.fee_collected
FieldName: lto.stc_fee_collected
FieldName: lto.rcvd_caption
FieldName: lto.rcvd_date
FieldName: lto.rcvd_time
FieldName: lto.appllno_from
FieldName: lto.appllno_to
FieldName: lto.package.n
FieldName: lto.package.of
FieldName: lto.package.m
FieldName: lto.package.dec
FieldName: agent_set_final
FieldName: lock.refno
FieldName: lock
FieldName: appendForm.E
FieldName: appendForm.D
FieldName: appendForm.E7
FieldName: appendForm.E2
FieldName: appendForm.e
FieldName: appendForm.E11
FieldName: appendForm.E12
FieldName: form_B1.pageNum
FieldName: form_B1.numpages
FieldName: sig.1
FieldName: sig.b_info2
FieldName: sig.b_info1
FieldName: pickup_stc
FieldName: agent_import_profile
FieldName: mtge.8_interest_ot_info
FieldName: mtge.9_terms_f_docno
FieldName: mtge.10_addl_terms
FieldName: mtge.11_encumbrances
FieldName: mtge.6_charge_yes
FieldName: mtge.6_charge_no
FieldName: mtge.7_account_yes
FieldName: mtge.7_account_no
FieldName: mtge.8_interest_fh
FieldName: mtge.8_interest_ot
FieldName: mtge.9_terms_p
FieldName: mtge.9_terms_f
FieldName: mtge.9_terms_x
FieldName: officer.wdate_dd
FieldName: officer.wdate_mm
FieldName: officer.wdate_yy
FieldName: officer.officer_name
FieldName: officer.officer_professional_capacity
FieldName: officer.officer_address
FieldName: borr1_save
FieldName: borr2_save
FieldName: lend1_save
FieldName: lend2_save
"""
