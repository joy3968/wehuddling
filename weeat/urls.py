from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_veiw = get_schema_view(
    openapi.Info(
        title='weeat API',
        default_version='v1',
        descriptions='사용자페이지 API 입니다.',
        contact = openapi.Contact(email='sayo1z2@naver.com'),
        license = openapi.License(name='SSAFY License')
    )
)

app_name = 'weeat'

urlpatterns = [
    # 메인 화면
    path('', views.main, name='main'),
    # 메뉴 주문
    path('menu', views.menu, name='menu'),
    # 주문 목록
    path('order_list', views.order_list, name='order_list'),
    # 로그아웃
    path('logout', views.user_logout, name='logout'),
]