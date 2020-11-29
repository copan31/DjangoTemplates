from django import forms

class FileUpLdForm(forms.Form):
    upfile = forms.FileField()

class ConfirmForm(forms.Form):
    filename = forms.CharField(
        max_length=100,
    )
    choice1 = forms.fields.ChoiceField(
        choices = (
            ('conv_a', '変換a'),
            ('conv_b', '変換b'),
        ),
        required=True,
        widget=forms.widgets.Select
    )