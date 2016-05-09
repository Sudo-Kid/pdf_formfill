import os
import tempfile
import subprocess

from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from . import forms


def gen_xfdf(datas={}):
    ''' Generates a temp XFDF file suited for fill_form function, based on dict input data '''
    fields = []
    for key, value in datas.items():
        fields.append('<field name="%s"><value>%s</value></field>' % (key, value))
    tpl = """<?xml version="1.0" encoding="UTF-8"?>
    <xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">
        <fields>
            %s
        </fields>
    </xfdf>""" % "\n".join(fields)
    handle, out_file = tempfile.mkstemp()
    f = open(out_file, 'w')
    f.write(tpl)
    f.close()
    return out_file


def fill_form(pdf_path, datas={}, out_file=None):
    '''
        Fills a PDF form with given dict input data.
        Return temp file if no out_file provided.
    '''
    tmp_fdf = gen_xfdf(datas)
    subprocess.run(['pdftk', pdf_path, 'fill_form', tmp_fdf, 'output', out_file], stdout=subprocess.PIPE)
    os.remove(tmp_fdf)


class Index(View):
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
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        appl = forms.ApplForm()
        return render(request, self.template_name, {'appl': appl})

    def post(self, request, *args, **kwargs):
        appl = forms.ApplForm(request.POST)
        if appl.is_valid():
            new_appl = appl.save(commit=False)
            form_data = {
                'appl.name': new_appl.name,
                'appl.addressL1': new_appl.addressL1,
                'appl.addressL2': new_appl.addressL2,
                'appl.city': new_appl.city,
                'appl.deduct_fee_yes': 'CHECKED' if new_appl.deduct_fee_yes else 'UNCHECKED'
            }
            base_pdf = settings.BASE_DIR + '/home/templates/home/form_b.pdf'
            filled_pdf = settings.BASE_DIR + '/home/templates/home/filled_b.pdf'
            generated_pdf = fill_form(base_pdf, datas=form_data, out_file=filled_pdf)
            new_appl.save()
            appl = forms.ApplForm()

        return render(request, self.template_name, {'appl': appl})
