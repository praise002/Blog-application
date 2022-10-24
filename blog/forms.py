from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, 
                        help_text='25 characters max.', 
                        error_messages={'required': 'Please enter your name.'})  #type='text'
    email = forms.EmailField(initial='example@gmail.com')  #type='email', value='example.com'
    to = forms.EmailField(help_text='A valid email address please.')
    comments = forms.CharField(required=False, widget=forms.Textarea)  #<textarea></textarea>