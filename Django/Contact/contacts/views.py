from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .models import Contact
from django.db.models import Q
from .serializers import ContactSerializer
from .schemas import *

class CreateContactView(APIView):
    serializer_class = ContactSerializer
    @create_contact_schema
    def post(self, request):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'message': 'Contact created successfully',
            'data': serializer.data
            }, status=201)
        else:
            return Response({
            "error":"Conta1ct with similar details already exists",
            "data": serializer.errors
            }, status=400)

class GetContactView(APIView):
    serializer_class = ContactSerializer
    @get_contact_schema
    def get(self, request, id=None):
        if id:
            contact = get_contact_by_id(id)
            if contact:
                serializer = self.serializer_class(contact)
                return Response(serializer.data, status=200)
            else:
                return Response({"error": "Contact not found"}, status=404)
        else:
            contacts = Contact.objects.all()
            serializer = self.serializer_class(contacts, many=True)
            return Response(serializer.data, status=200)

class UpdateContactView(APIView):
    serializer_class = ContactSerializer
    @update_contact_schema
    def patch(self, request, id):
        contact= get_contact_by_id(id)
        if contact:
            serializer= self.serializer_class(contact, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response({"error": "Contact not found"}, status=404)

class DeleteContactView(APIView):
    serializer_class = ContactSerializer
    @delete_contact_schema
    def delete(self, request, id):
        contact = get_contact_by_id(id)
        if contact:
            contact.delete()
            return Response({"message": "Contact deleted"}, status=200)
        else:
            return Response({"error": "Contact not found"}, status=404)

def get_contact_by_id(id):
    return Contact.objects.filter(
        Q(firstname__icontains=id) |
        Q(middlename__icontains=id) |
        Q(lastname__icontains=id) |
        Q(nickname__icontains=id) |
        Q(phone__icontains=id) |
        Q(phone_2__icontains=id) |
        Q(phone_3__icontains=id) |
        Q(email__icontains=id)
    ).first()

