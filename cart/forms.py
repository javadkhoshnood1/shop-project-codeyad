from django import forms


class CheckOutForm(forms.Form):
    phone = forms.CharField(label="شماره تماس", widget=forms.TextInput(attrs={"class": "form-control mt-3"}))
    first_name = forms.CharField(label="نام",
                                 widget=forms.TextInput(attrs={"class": "form-control mt-3", "type": "text"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control mt-3", "type": "text"}),
                                label="نام خانوادگی")
    address = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control mt-3", "type": "text", "placeholder": "بادرود خیابان امام"}), label="ادرس شما")
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control mt-3", "placeholder": "javadkho@gmail.com"}),
        label="ادرس شما")
    discription = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mt-3", "placeholder": "توضیحات اضافی", "type": "text","cols" : "30","rows":"11"}),
        label="توضیحات خرید")
