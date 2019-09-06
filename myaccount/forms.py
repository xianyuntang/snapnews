from django import forms


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='名', max_length=50, required=False,
                                 widget=forms.TextInput(attrs={"autocomplete": "off"}))
    last_name = forms.CharField(label='姓', max_length=50, required=False,
                                widget=forms.TextInput(attrs={"autocomplete": "off"}))
    org = forms.CharField(label='公司', max_length=50, required=False,
                          widget=forms.TextInput(attrs={"autocomplete": "off"}))
    telephone = forms.CharField(label='電話', max_length=50, required=False,
                                widget=forms.TextInput(attrs={"autocomplete": "off"}))
    email_address = forms.CharField(label="電子信箱", max_length=100, required=False,
                                    widget=forms.TextInput(attrs={"autocomplete": "off"}))
    line_api_key = forms.CharField(label='Line api key', max_length=100, required=False,
                                   widget=forms.TextInput(attrs={"autocomplete": "off"}))


class KeywordForm(forms.Form):
    keyword_list = forms.CharField(label='關鍵字清單', required=False,
                                   widget=forms.Textarea(attrs={"class": "form-control keyword-area"}))
