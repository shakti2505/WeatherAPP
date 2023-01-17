from django import forms


class WeatherForm(forms.Form):
    city_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'weather'}), label='Enter City Name', initial="Search City....")

    

