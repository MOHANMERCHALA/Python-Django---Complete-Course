from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        # To show all the fields
        #fields='__all__'

        # To show only the specific fields
        fields = ['title','description','demo_link','source_link','tags']