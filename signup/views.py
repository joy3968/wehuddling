from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import *

# 회원가입
def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            # 회원 객체 생성
            customer = customer_tbl.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            customer.c_name = request.POST['c_name']
            customer.c_phone = request.POST['c_phone']
            # 우편번호
            customer.c_zip_code = request.POST['addr1']
            # 신주소
            customer.c_new_address = request.POST['addr2']
            # 주소 상세
            customer.c_address_detail = request.POST['addr3']
            customer.save()

            # 회원가입 완료되었다는 메세지를 보낸 후 메인 페이지로 이동.
            return HttpResponse('<script type="text/javascript"> alert("회원가입이 완료되었습니다."); location.href = "/";</script>')

    # 폼 불러오기
    user_form = UserForm()

    context = {'user_form': user_form}
    return render(request, 'signup/signup.html', context)
# Create your views here.
