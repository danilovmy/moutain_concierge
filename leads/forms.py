from django import forms

from .models import Lead


NEED_CHOICES = Lead.Need.choices


class LeadForm(forms.ModelForm):
    needs = forms.MultipleChoiceField(
        choices=NEED_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Что нужно',
    )

    class Meta:
        model = Lead
        fields = [
            'guest_name',
            'contact',
            'source_type',
            'source_text',
            'needs',
            'date_from',
            'date_to',
            'status',
            'comment',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # When editing, initialize needs from JSON list
        if self.instance and self.instance.pk and isinstance(self.instance.needs, list):
            self.initial.setdefault('needs', self.instance.needs)

    def clean_needs(self):
        data = self.cleaned_data.get('needs') or []
        # Ensure JSON serializable list
        return list(data)

