from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        lables ={
            'user_name' : 'Your Name',
            'rating' : 'Your Rating',
            'review_text' : 'Your Feedback',
        }
    
    

    