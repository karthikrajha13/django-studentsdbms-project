from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

        labels = {
            "name": "Student Name",
            "email": "Email Address",
            "age": "Student Age",
            "course": "Course Name",
        }

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Student Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email"
            }),

            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Age"
            }),

            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Course"
            }),

        }
    def clean_name(self):
        name = self.cleaned_data["name"]

        if len(name) < 3:
            raise forms.ValidationError(
                "Name must contain at least 3 characters."
            )

        return name