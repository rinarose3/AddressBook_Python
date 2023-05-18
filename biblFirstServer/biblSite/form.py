from django import forms
from .models import AddressBook


class AddressBookForm(forms.ModelForm):
    objects = None

    class Meta:
        model = AddressBook
        fields = "__all__"
        labels = {
            "name": "Имя",
            "fam": "Фамилия",
            "tel": "Телефон",
            "mail": "Почта",
            "note": "Заметки",

        }
