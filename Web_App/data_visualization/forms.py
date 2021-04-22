from django import forms


class ChooseMeasurement(forms.Form):
    name_measurement = forms.CharField(label="Measurement", max_length=30)


class ChooseCountry(forms.Form):
    name_country = forms.CharField(label="Country", max_length=30)

