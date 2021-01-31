from django import forms
class feedbackForm(forms.Form):
        option = (
            ("1", "Comments"),
            ("2", "Suggestions"),
            ("3", "Questions")
        )
        feedback = forms.ChoiceField(choices=option)
        fname = forms.CharField(max_length=20)
        lname = forms.CharField(max_length=20)
        email = forms.EmailField()

