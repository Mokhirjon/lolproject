from rest_framework.generics import CreateAPIView
from .models import Customuser
from .serializers import CustomuserSerializers

# Create your views here.

class SignupUserview(CreateAPIView):
    queryset = Customuser.objects.all()
    serializer_class = CustomuserSerializers