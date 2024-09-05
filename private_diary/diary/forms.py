import os
from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=30)
    email = forms.EmailField(label="信箱")
    title = forms.CharField(label="主旨", max_length=50)
    message = forms.CharField(label="內容", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form_control"
        self.fields["name"].widget.attrs["placeholder"] = "請輸入您的姓名"


        self.fields["email"].widget.attrs["class"] = "form_control"
        self.fields["email"].widget.attrs["placeholder"] = "請輸入您的信箱"

        self.fields["title"].widget.attrs["class"] = "form_control"
        self.fields["title"].widget.attrs["placeholder"] = "請輸入信件主旨"

        self.fields["message"].widget.attrs["class"] = "form_control"
        self.fields["message"].widget.attrs["placeholder"] = "請輸入信件內容"

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        title = self.cleaned_data["title"]
        message = self.cleaned_data["message"]

        subject = "[聯繫我們]{}".format(title)
        message = "寄件者:{}\n信箱:{}\n主旨:{}\n信件內容:{}\n".format(name, email,subject, message)
        from_email = os.environ.get("FROM_EMAIL")
        to_list = [
            os.environ.get("FROM_EMAIL")
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()
