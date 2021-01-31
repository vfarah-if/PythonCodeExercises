from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput

from meetings.models import Meeting


# REMARKS: Build component types for form HTML
class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "15", "max": "1440"}),
        }

    def clean_date(self):
        date = self.cleaned_data.get("date")
        if date < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return date
