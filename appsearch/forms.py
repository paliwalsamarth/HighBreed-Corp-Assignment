from django import forms


class AppSearchForm(forms.Form):
    CHOICES = [("android", "Google Play Store"), ("apple", "Apple App Store")]
    storeName = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect, required=True
    )
    appID = forms.CharField(required=False)
    appName = forms.CharField(required=False)

    def clean_appID(self):
        appID = self.cleaned_data.get("appID", False)
        if appID is False:
            raise forms.ValidationError("AppID is a required field.")
        return appID

    def clean_appName(self):
        storeName = self.cleaned_data.get("storeName")
        appName = self.cleaned_data.get("appName", False)
        if storeName == "apple" and appName is False:
            raise forms.ValidationError("AppName is a required field.")
        return appName
