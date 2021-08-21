from django import forms
from django.conf import settings
from django.core.mail import send_mail

# class SendMailForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.Form):

    name = forms.CharField(max_length=120,required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100,required=True)
    message = forms.CharField(widget=forms.Textarea)

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """

        clean_data= super().clean()

        name = clean_data.get('name').strip()
        from_email =  clean_data.get('email').strip()
        subject = clean_data.get('subject')

        message = f'{name} with email {from_email} said:'
        message += f'\n"{subject}"\n\n'
        message += clean_data.get('message')


        return subject, message


    def send(self):
        subject, message = self.get_info()


        send_mail(
            subject= subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]



        )



