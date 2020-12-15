from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_veiw = get_schema_view(
    openapi.Info(
        title='admin API',
        default_version='v1',
        descriptions='관리자 API 입니다.',
        contact = openapi.Contact(email='sayo1z2@naver.com'),
        license = openapi.License(name='SSAFY License')
    )
)


app_name = 'admin'

urlpatterns = [
    # 메인 화면
    path('', views.index, name='index'),
    # 로그인(관리자)
    path('login', views.login_admin, name='login_admin'),
    # 로그아웃(관리자)
    path('logout', views.logout_admin, name='logout_admin'),
    # 거래처 등록
    path('cp_enroll', views.cp_enroll, name='cp_enroll'),
    # 상품 등록
    path('gd_enroll', views.gd_enroll, name='gd_enroll'),
    # 배송인 등록
    path('sp_enroll', views.sp_enroll, name='sp_enroll'),
    # 주문 목록
    path('order_list', views.order_list, name='order_list'),
    # 상품 목록
    path('goods_list', views.goods_list, name='goods_list'),
    # 배송인 목록
    path('shipper_list', views.shipper_list, name='shipper_list'),
    # 거래처 목록
    path('company_list', views.company_list, name='company_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)