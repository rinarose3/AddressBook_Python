from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView


from .form import AddressBookForm
from .models import AddressBook
from .serializers import AddressBookSerializer

# Create your views here.

menu = [{"title": "home", "url_name": "main", "dis": "isEnabled", "id": "main"},
        {"title": "add", "url_name": "add", "dis": "isEnabled", "id": "add"},
        {"title": "edit-icon", "url_name": "change", "dis": "isDisabled", "id": "change"},
        {"title": "delete-icon-1", "url_name": "main", "dis": "isDisabled", "id": "delete"},
        ]


def bibl_main(request):
    bibl_list = AddressBook.objects.all()
    return render(request, "main.html", {"bibl_list": bibl_list, "menu": menu})


def bibl_add(request):
    form = AddressBookForm()
    return render(request, "add.html", {"menu": menu, "form": form})


def bibl_change(request):
    try:
        pk_cur = request.GET["pk"]
        cur = AddressBook.objects.get(pk=pk_cur)

        form = AddressBookForm(instance=cur)
        return render(request, "change.html", {"menu": menu, "pk": cur.pk, "form": form})
    except:
        return HttpResponse("Выберите запись")


class AddressBookAPIView(APIView):
    def get(self, request):
        bibl_list = AddressBook.objects.all().values()
        return Response(list(bibl_list))

    def post(self, request):
        serializer = AddressBookSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({'error': e.detail}, status=400)
        serializer.save()

        return redirect("main")

    def put(self,  request):
        pk_cur = request.data["pk"]
        cur = AddressBook.objects.get(pk=pk_cur)
        serializer = AddressBookSerializer(instance=cur, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({'error': e.detail}, status=400)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request):
        try:
            print(request.query_params["id"])
            pk_cur = request.query_params["id"]
            cur = AddressBook.objects.filter(pk=pk_cur)
            cur.delete()
            return Response("", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "No pk parameter provided"}, status=400)












