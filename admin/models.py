from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

# 유저모델 확장
class customer_tbl(AbstractUser):

    # 이름
    c_name = models.CharField(max_length=100, null=True, blank=True)
    # 휴대폰 번호
    c_phone = models.CharField(max_length=100, null=True, blank=True)
    # 우편번호
    c_zip_code = models.CharField(max_length=100, null=True, blank=True)
    # 신주소
    c_new_address = models.CharField(max_length=200, null=True, blank=True)
    # 구주소
    c_old_address = models.CharField(max_length=200, null=True, blank=True)
    # 상세주소
    c_address_detail = models.CharField(max_length=200, null=True, blank=True)
    # 가입일
    c_join = models.DateField(auto_now_add=True, null=True, blank=True)

# 거래처 테이블
class company_tbl(models.Model):
    # 거래처 일련번호
    cp_no = models.AutoField(primary_key=True)
    # 거래처명
    cp_name = models.CharField(max_length=100 , null=True, blank=True)
    # 거래처 번호
    cp_phone = models.CharField(max_length=20, null=True, blank=True)
    # 거래처 이미지
    cp_img = models.ImageField(upload_to='company/', blank=True, null=True)
    # 거래처 등록일(현재 날짜 자동 생성)
    cp_join = models.DateField(auto_now_add=True)

    # 거래처의 이름이 보이게(상품 등록에서 이용)
    def __str__(self):
        return self.cp_name

# 상품 테이블
class goods_tbl(models.Model):
    # 상품 일련번호
    gd_no = models.AutoField(primary_key=True)
    # 카테고리 Choice - 콤보박스로 받기 위함.
    category = (('밥류','밥류'),('샌드위치류','샌드위치류'),('샐러드류','샐러드류'),('누들류','누들류'),('기타','기타'))
    # 상품 카테고리
    gd_category = models.CharField(max_length=100 , null=True, blank=True, choices=category)
    # 상품 명
    gd_name = models.CharField(max_length=100 , null=True, blank=True)
    # 상품 가격
    gd_price = models.IntegerField(null=True, blank=True)
    # 상품 재고
    gd_stock = models.IntegerField(null=True, blank=True)
    # 상품 이미지
    gd_img = models.ImageField(upload_to='goods/', blank=True, null=True)
    # 상품 설명
    gd_desc = models.TextField(max_length=500, null=True, blank=True)
    # 상품 등록일
    gd_join = models.DateField(auto_now_add=True)
    # 거래처 일련번호(관계키-거래처 테이블)
    cp_no = models.ForeignKey(company_tbl, on_delete=models.CASCADE)

# 배송인 테이블
class shipper_tbl(models.Model):
    # 배송인 일련번호
    sp_no = models.AutoField(primary_key=True)
    # 배송인 이름
    sp_name = models.CharField(max_length=100 , null=True, blank=True)
    # 배송인 휴대폰번호
    sp_phone = models.CharField(max_length=100 , null=True, blank=True)
    # 담당 시
    sp_city= models.CharField(max_length=100 , null=True, blank=True)
    # 담당 구
    sp_borough = models.CharField(max_length=100, null=True, blank=True)
    # 등록일
    sp_join = models.DateField(auto_now_add=True)

# 주문 테이블
class order_tbl(models.Model):
    # 주문 일련번호
    od_no = models.AutoField(primary_key=True)
    # 주문 번호(같은 주문 세트일 경우 같은 주문번호)
    od_number = models.IntegerField(null=True, blank=True)
    # 주문 접수시간(현재시간 자동등록)
    od_join = models.DateField(auto_now_add=True)
    # 배송지 우편번호
    od_zip_code = models.CharField(max_length=100, null=True, blank=True)
    # 배송지 주소
    od_address = models.CharField(max_length=200, null=True, blank=True)
    # 배송지 상세 주소
    od_address_detail = models.CharField(max_length=200, null=True, blank=True)
    # 배송 완료여부
    od_state = models.BooleanField(null=True, blank=True)
    # 회원 번호(외래키)
    customer = models.ForeignKey(customer_tbl, on_delete=models.CASCADE)
    # 상품 번호(외래키)
    gd_no = models.ForeignKey(goods_tbl, on_delete=models.CASCADE)
    # 배송인 일련번호(외래키)
    sp_no = models.ForeignKey(shipper_tbl, on_delete=models.CASCADE, null=True, blank=True)



