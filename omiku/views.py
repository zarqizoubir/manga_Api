from django.contrib.auth.models import User


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response


class RegisterUser(APIView):
    model = User

    def get(self, request: HttpRequest):
        return Response({"message": "Send The Cridentials Using a POST method"})

    def post(self, request: HttpRequest):
        data = request.data
        try:
            username = data["username"]
            email = data["email"]
            password = data["password"]
            confirmpassword = data["confirmpassword"]
            if User.objects.all().filter(username=username):
                return Response({"message": "User already exist"}, status=status.HTTP_400_BAD_REQUEST)

            if password != confirmpassword:
                return Response({"message": "The passwords does't match"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            # return Response({"message": "Navigate to token/ route to get your token"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Enter the Data with a valid format"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "User Created", "user_credentials": {"username": username, "email": email, "password": password}}, status=status.HTTP_201_CREATED)
