from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Create your views here.

# 사용자 메인페이지
def main(request):
    return render(request, 'mainpage/introduce.html')

# 메뉴
def menu(request):

    # 로그인을 하지 않았을 시 로그인이 필요하다는 메세지를 보여줍니다.
    if request.user.id == None:
        return HttpResponse(
            '<script type="text/javascript"> alert("로그인이 필요합니다."); location.href = "/" </script>')

    if request.method == "POST":
        # QueryDict 를 딕셔너리로 변환.(상품 일련번호를 리스트로 가져오기 위함)
        mydict = dict(request.POST)

        # 상품을 선택하지 않고 주문하기를 눌렀을 경우 예외처리
        try:
            # 상품 일련번호 리스트
            gd_no_list = mydict['gd_no']
        except:
            return HttpResponse(
                '<script type="text/javascript"> alert("상품을 선택하신 후 주문하기를 눌러주세요."); location.href = "/menu";</script>')

        try:
            # 마지막 주문 객체
            last_order = order_tbl.objects.last()
            # 마지막 주문 객체의 주문번호
            pre_od_number = last_order.od_number
            # 이전 주문 번호에 1을 더한 값을 주문번호로 합니다.
            od_number = pre_od_number + 1
        except:
            # 이전 주문이 없을 경우 1부터 시작
            od_number = 1

        # 주소 등록이 되어있지 않은 경우 오류 메세지를 보여준 후 메인 페이지로 돌아갑니다.
        try:
            new_address = request.user.c_new_address.split(' ')
        except:
            return HttpResponse(
                '<script type="text/javascript"> alert("주소 등록이 필요합니다."); location.href = "/";</script>')

        # 시,도
        city = new_address[0]

        # ~시(ex 성남시)
        borough = new_address[1]


        # 배송 담당자 객체를 불러 옵니다
        try:
            shipper = shipper_tbl.objects.get(sp_city=city, sp_borough=borough)
        except:
            # 배송 담당자가 없을 경우 배송할 수 없는 지역이라는 문구를 띄웁니다.
            return HttpResponse(
                '<script type="text/javascript"> alert("배송할 수 없는 지역입니다."); location.href = "/";</script>')



        # for문을 통해 주문 객체 생성
        for gd_no in gd_no_list:
            # 주문 객체를 생성
            order_tbl.objects.create(od_number=od_number, od_state=False, customer_id=request.user.id, gd_no_id=gd_no, od_zip_code=request.user.c_zip_code,
                                     od_address=request.user.c_new_address, od_address_detail=request.user.c_address_detail,sp_no_id=shipper.sp_no)

            # 상품 객체를 가져 옵니다.
            goods = goods_tbl.objects.get(gd_no=gd_no)
            # 상품을 주문 했으므로 상품의 재고를 1개 차감.
            goods.gd_stock = goods.gd_stock - 1
            # DB에 저장(수정)
            goods.save()

        return HttpResponse(
                '<script type="text/javascript"> alert("상품 주문이 완료 되었습니다."); location.href = "/";</script>')


    # 밥류 리스트
    rice_list = goods_tbl.objects.filter(gd_category='밥류')
    # 샌드위치류 리스트
    sandwich_list = goods_tbl.objects.filter(gd_category='샌드위치류')
    # 샐러드류 리스트
    salad_list = goods_tbl.objects.filter(gd_category='샐러드류')
    # 누들류 리스트
    noodle_list = goods_tbl.objects.filter(gd_category='누들류')
    # 기타
    etc_list = goods_tbl.objects.filter(gd_category='기타')

    context = {'rice_list' : rice_list, 'sandwich_list' : sandwich_list, 'salad_list' : salad_list, 'noodle_list' : noodle_list, 'etc_list' : etc_list}
    return render(request, 'mainpage/menu.html', context)

# 주문 목록
def order_list(request):

    # 로그인을 하지 않았을 시 로그인이 필요하다는 메세지를 보여줍니다.
    if request.user.id == None:
        return HttpResponse(
            '<script type="text/javascript"> alert("로그인이 필요합니다."); location.href = "/" </script>')

    # 접속한 고객의 주문 목록 리스트를 불러옵니다.
    order_list = order_tbl.objects.filter(customer_id=request.user.id)
    context = {'order_list' : order_list}

    return render(request, 'mainpage/order_list.html', context)

# 로그아웃
def user_logout(request):
    logout(request)

    return redirect('/')
