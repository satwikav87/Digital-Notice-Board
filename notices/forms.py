from django import forms
from .models import Institution,Notice
class NoticeForm(forms.ModelForm):
 publish_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}),input_formats=["%Y-%m-%dT%H:%M"])
 expiry_date=forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={"type":"datetime-local"}),input_formats=["%Y-%m-%dT%H:%M"])
 class Meta:
  model=Notice
  fields=["title","content","category","department","audience","priority","image","attachment","is_published","is_pinned","publish_date","expiry_date"]
  widgets={"content":forms.Textarea(attrs={"rows":8})}
 def clean(self):
  data=super().clean(); p=data.get("publish_date"); e=data.get("expiry_date")
  if p and e and e<=p: self.add_error("expiry_date","Expiry must be later than publish date.")
  return data
class InstitutionForm(forms.ModelForm):
 class Meta:
  model=Institution
  fields="__all__"
  widgets={"address":forms.Textarea(attrs={"rows":3}),"primary_color":forms.TextInput(attrs={"type":"color"})}
