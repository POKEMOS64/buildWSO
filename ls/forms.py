from django import forms


class LkInduc(forms.Form):
    id_ls = forms.CharField(label='Лицевой номер', max_length=15)
    name_dom = forms.CharField(label='Номер дома', max_length=10)
    name_kv = forms.CharField(label='Номер квартиры', max_length=10)

    class Meta:
        fields = ('id_ls', 'name_kv')


class ProfileUser(forms.Form):
    id_ls = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)

    name_dom = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)

    name_kv = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)

    codsch_hv1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    hv1_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsh_gv1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    gv1_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsch_hv2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    hv2_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsch_gv2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    gv2_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsch_hv3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    hv3_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsch_gv3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    gv3_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsch_hv4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    hv_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    codsh_gv4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)
    gv4_data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form_first_name', 'readonly': True}), required=False)

    class Meta:
        fields = ('id_ls', 'name_dom', 'name_kv', 'codsch_hv1', 'hv1_data', 'codsh_gv1', 'gv1_data', 'codsch_hv2', 'hv2_data',
                  'codsch_gv2', 'gv2_data', 'codsch_hv3', 'hv3_data', 'codsch_gv3', 'gv3_data', 'codsch_hv4', 'hv_data', 'codsh_gv4', 'gv4_data')
