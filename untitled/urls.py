"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Epharma import views

urlpatterns = [
    path('',views.landingpage),
    path('about_us', views.about_us),
    path('logout',views.logout),
    path('addmedicine',views.addmedicine),
    path('viewmed_search',views.viewmed_search),
    path('feedback',views.feedback),
    path('rating/<id>',views.rating),
    path('user',views.users),
    path('viewpharma1',views.viewpharma1),
    path('pharmaaccept',views.pharmaaccept),
    path('pharmaaccept/<id>/<em>',views.pharmaaccept),
    path('pharmareject/<id>/<em>',views.pharmareject),
    path('view1',views.view1),
    path('deletemedicine/<id>',views.deletemedicine),
    path('password',views.password),
    path('Adminhome',views.Adminhome),
    path('viewpharma',views.viewpharma),
    path('logpost',views.logpost),
    path('medicinepost',views.medicinepost),
    path('passwordpost',views.passwordpost),
    # ================================================================================================================
    path('Registration', views.Registration),
    path('Registrationpost',views.Registrationpost),
    path('viewprofile', views.viewprofile),
    path('viewmedicine', views.viewmedicine),
    path('stockupdate/<id>', views.stockupdate),
    path('stockupdatepost/<id>', views.stockupdatepost),
    path('viewstock', views.viewstock),
    path('deletestock/<id>', views.deletestock),
    path('viewbooking', views.viewbooking),
    path('vieworderitem/<id>', views.vieworderitem),
    path('verify', views.verify),
    path('vaccept/<id>', views.vaccept),
    path('vreject/<id>', views.vreject),
    path('phrating', views.phrating),
    path('phchangepasspost', views.phchangepasspost),
    path('phchangepass', views.phchangepass),
    path('Home', views.Home),
    path('previous', views.previous),
    path('profilepost', views.profilepost),
    path('view_complaints', views.view_complaints),
    path('send_reply/<id>', views.send_reply),
    path('send_reply_post/<id>', views.send_reply_post),

    path('vreject_post/<id>', views.vreject_post),
    path('accept_cash/<id>', views.accept_cash),
    path('set_delivered/<id>', views.set_delivered),


# ====================================================================================================================
    path('Addqua/<id>/<pid>/<q>',views.Addqua),
    path('Addquapost/<id>/<pid>',views.Addquapost),
    path('ufeedback', views.ufeedback),
    path('ufeedbackpost', views.ufeedbackpost),
    path('register', views.register),
    path('registerpost', views.registerpost),
    path('viewcart', views.viewcart),
    path('deletecart/<id>', views.deletecart),
    path('viewitem/<id>', views.viewitem),
    path('viewmed', views.viewmed),
    path('vieworder', views.vieworder),
    path('viewphar/<id>', views.viewphar),
    path('viewprev', views.viewprev),
    path('home', views.home),
    path('buynow', views.buynow),
    path('upass', views.upass),
    path('upasspost', views.upasspost),
    path('sendra/<id>', views.sendra),
    path('sendrapost/<id>', views.sendrapost),
    path('stockupdate2/<id>', views.stockupdate2),
    path('stockupdate2post/<id>', views.stockupdate2post),
    path('option', views.option),
    path('option_post', views.option_post),
    path('profile', views.profile),
    path('uprofilepost', views.uprofilepost),

    # ---------------------------------------Android----------------------------------------

    path('and_connect', views.and_connect),
    path('and_login', views.and_login),
    path('and_search_medicine', views.and_search_medicine),
    path('and_add_to_cart', views.and_add_to_cart),
    path('and_view_cart', views.and_view_cart),
    path('and_update_cart', views.and_update_cart),
    path('and_delete_cart', views.and_delete_cart),
    path('and_view_payment_history', views.and_view_payment_history),
    path('and_view_complaints', views.and_view_complaints),
    path('and_view_address', views.and_view_address),
    path('and_send_complaint', views.and_send_complaint),
    path('and_payment', views.and_payment),
    path('and_view_items', views.and_view_items),
    path('and_send_review', views.and_send_review),
    path('and_register', views.and_register),
    path('and_cart_check', views.and_cart_check),
    path('and_view_review', views.and_view_review),
    path('and_address_add', views.and_address_add),
    path('and_delete_address', views.and_delete_address),

]
