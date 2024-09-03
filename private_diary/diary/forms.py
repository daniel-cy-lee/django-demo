from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=30) 
    email = forms.EmailField(label="信箱")
    title = forms.CharField(label="主旨", max_length=50)
    message = forms.CharField(label="內容", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

        self.fields["name"].widget_attrs["class"] = "form_control"
        self.fields["name"].widget_attrs["placeholder"] = "請輸入您的姓名"


        self.fields["email"].widget_attrs["class"] = "form_control"
        self.fields["email"].widget_attrs["placeholder"] = "請輸入您的信箱"

        self.fields["title"].widget_attrs["class"] = "form_control"
        self.fields["title"].widget_attrs["placeholder"] = "請輸入信件主旨"

        self.fields["message"].widget_attrs["class"] = "form_control"
        self.fields["message"].widget_attrs["placeholder"] = "請輸入信件內容"
