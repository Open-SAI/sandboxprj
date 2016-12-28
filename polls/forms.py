from django import forms
from django.core.exceptions import ValidationError

from .models import Question, Choice

from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

#from bootstrap3_datetime.widgets import DateTimePicker

#class DatePicker(forms.DateInput):
#    template_name = 'date'

class QuestionForm(forms.ModelForm):
#    pub_date = forms.DateField(required=False, input_formats=['%d-%m-%Y'])
    class Meta:
        model = Question 
        fields = '__all__'
#        fields['pub_date'].widget.format = '%d/%m/%Y'
#        widgets = { 'pub_date': forms.DateInput(format=['%m/%d/%Y'], attrs={'class':'datepicker'} )} 
#        widgets = { 'pub_date': forms.DateInput(attrs={'class':'datepicker'} )} 
        widgets = { 'pub_date': forms.DateInput(attrs={'id':'id_pub_date'} )} 
#        pub_date = forms.DateTimeField(widget=DateTimePicker())
#        date_available = forms.DateField(widget=forms.widgets.DateInput(format="%d-%m-%Y"))
#        widgets = { 'pub_date': forms.DateInput(attrs={'class':'datepicker'},format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',) }
#        fields['pub_date'] = forms.DateField(initial=pub_date.today(), widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
#        widgets = {
#            'pub_date': DateTimeWidget(attrs={'id':"id_pub_date"}, usel10n = True, bootstrap_version=3)
#        }

#    def __init__(self, *args, **kwargs):
#        super(QuestionForm, self).__init__(*args, **kwargs)
#        self.fields['pub_date'].widget.format = '%d/%m/%Y'

# at the same time, set the input format on the date field like you want it:
#        self.fields['pub_date'].input_formats = ['%d/%m/%Y']
