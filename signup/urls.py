from django.urls import path
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_veiw = get_schema_view(
    openapi.Info(
        title='signup API',
        default_version='v1',
        descriptions='회원가입 API 입니다.',
        contact = openapi.Contact(email='sayo1z2@naver.com'),
        license = openapi.License(name='SSAFY License')
    )
)


app_name = 'signup'

urlpatterns = [
    # 회원가입
    path('', views.signup, name='signup'),

]