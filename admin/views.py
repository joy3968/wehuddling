from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# 메인 페이지
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def index(request):
    # 거래처 목록을 불러 옵니다.
    company_list = company_tbl.objects.all()
    context = {'company_list': company_list}

    return render(request, 'admin/main.html', context)

# 로그인
def login_admin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate 함수를 사용하여 인증과정을 거칩니다. 인증이 되지 않으면 None을 리턴합니다.
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)

            # 관리자일 경우 관리자 페이지로 이동
            if user.is_superuser == 1:
                return redirect('/admin/')
            else:
                # 그렇지 않을 경우 사용자 페이지로 이동
                return redirect('/')
        # 정보가 틀렸을 시 새로운 스크립트에 메세지를 띄우고 확인 시 원래창으로 돌아오기
        else:
            return HttpResponse('<script type="text/javascript"> alert("입력하신 정보가 틀렸습니다. 다시 입력해 주세요."); history.back();</script>' )

    return render(request, 'admin/login.html')

# 로그아웃
def logout_admin(request):
    logout(request)

    return redirect('/admin/login')

# 거래처 관리(거래처 등록)
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def cp_enroll(request):
    if request.method == 'POST':
        # 거래처 객체 생성
        company = company_tbl.objects.create(cp_name=request.POST['cp_name'], cp_phone=request.POST['cp_phone'], cp_img=request.FILES['cp_img'])
        # DB에 저장
        company.save()

        return redirect('/admin')

    return render(request, 'admin/cp_enroll.html')

# 상품 등록
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def gd_enroll(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST)
        goods_tbl = form.save(commit=False)
        goods_tbl.gd_img = request.FILES['gd_img']
        # DB저장
        goods_tbl.save()

        # 메인으로 이동
        return redirect('admin:index')

    # 폼을 불러옵니다.
    form = GoodsForm()
    context = {'form' : form}

    return render(request, 'admin/gd_enroll.html', context)

# 배송인 등록
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def sp_enroll(request):
    if request.method == 'POST':

        # 이미 해당 구역에 등록된 배송 기사가 있으면 새로 에러 메세지를 띄웁니다.
        try:
            shipper_tbl.objects.get(sp_city=request.POST['sp_city'], sp_borough=request.POST['sp_borough'])
            return HttpResponse('<script type="text/javascript"> alert("해당 구역에 등록된 배송 기사가 있습니다."); history.back();</script>' )

        except:

            # 해당 구역에 등록된 기사가 없을 경우만 새로운 객체를 생성
            form = ShipperForm(request.POST)
            shipper_form = form.save(commit=False)
            # DB저장
            shipper_form.save()

            # 메인으로 이동
            return redirect('admin:index')

    # 폼을 불러옵니다.
    form = ShipperForm()
    context = {'form' : form}

    return render(request, 'admin/sp_enroll.html', context)

# 주문 목록
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def order_list(request):
    # 주문 목록 리스트를 불러옵니다.
    order_list = order_tbl.objects.all()
    context = {'order_list': order_list}

    if request.method == "POST":
        # 주문 일련번호
        od_no = request.POST['od_no']
        # 주문 객체를 불러 옵니다.
        order = order_tbl.objects.get(od_no=od_no)
        # 배송 완료 여부 속성을 True로 변경
        order.od_state = True
        # 변경된 속성을 DB에 저장
        order.save()

        return render(request, 'admin/order_list.html', context)


    return render(request, 'admin/order_list.html', context)

# 상품 목록
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def goods_list(request):
    # 상품 목록 리스트를 불러옵니다.
    goods_list = goods_tbl.objects.all()
    context = {'goods_list' : goods_list
               }
    return render(request, 'admin/goods_list.html', context)

# 배송인 목록
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def shipper_list(request):
    # 배송인 목록 리스트를 불러 옵니다.
    shipper_list = shipper_tbl.objects.all()
    context = {'shipper_list': shipper_list}

    return render(request, 'admin/shipper_list.html', context)

# 거래처 목록
@user_passes_test(lambda u: u.is_superuser, login_url='admin:login_admin')
def company_list(request):
    # 거래처 목록을 불러 옵니다.
    company_list = company_tbl.objects.all()
    context = {'company_list' : company_list}

    return render(request, 'admin/company_list.html', context)
