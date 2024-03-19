import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from django.core.files.storage import FileSystemStorage
from django.db.models import Q, Avg, Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Epharma.models import *

# ijvk fiyj dnfk uuqg

systempath = r"C:\Users\Riss Technology\Downloads\untitled\untitled\Epharma\static\medicine photo\\"


def log(request):
    return render(request, "index.html")


def landingpage(request):
    return render(request, "loginindex.html")


def about_us(request):
    return render(request, 'about.html')


def logpost(request):
    un = request.POST['textfield2']
    p = request.POST['textfield']
    l = login.objects.filter(username=un, password=p)
    if l.exists():
        l = l[0]
        request.session['lid'] = l.id
        request.session['lin'] = "1"
        request.session['h'] = ""
        if l.usertype == 'admin':
            return HttpResponse("<script>alert('Welcome admin home');window.location='/Adminhome'</script>")
        elif l.usertype == 'pharmacy':
            request.session['pid'] = pharmacy.objects.get(LOGIN=l.id).id

            return HttpResponse("<script>alert('Welocome home');window.location='/Home'</script>")
        elif l.usertype == 'user':
            request.session['uid'] = user.objects.get(LOGIN=l.id).id
            request.session['cartcount'] = cart.objects.filter(USER=request.session['uid']).count()
            return HttpResponse("<script>alert('Welocome home');window.location='/home'</script>")
        else:
            return HttpResponse("<script>alert('Wait for verification');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('doesnt exist');window.location='/'</script>")


def addmedicine(request):
    request.session['h'] = "ADD MEDICINE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "admin/ADD.html")


def medicinepost(request):
    name = request.POST['textfield']
    Type = request.POST['textfield2']
    if Medicine.objects.filter(name=name).exists():
        return HttpResponse("<script>alert('Already added');window.location='/addmedicine#services'</script>")

    mobj = Medicine()
    mobj.name = name
    mobj.type = Type
    mobj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/addmedicine#services'</script>")


def feedback(request):
    request.session['h'] = "VIEW FEEDBACK"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = Feedback.objects.all()
    return render(request, "admin/Feedback.html", {"data": data})


def rating(request, id):
    request.session['h'] = "VIEW RATING"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = Rating.objects.filter(PHARMACY=id)
    da = []

    for im in data:
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        ar = []
        a = float(im.userrating)

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]


        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]


        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]


        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]


        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]


        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]


        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]


        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]


        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]


        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]

        da.append({
            'userrating': ar,
            'review': im.review,
            'date': im.date,
            'USER': im.USER,
            'PHARMACY': im.PHARMACY
        })

    return render(request, "admin/Rating.html", {"data": da})


def users(request):
    request.session['h'] = "VIEW USER"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = user.objects.all()
    arr = []
    for i in data:
        ad = address.objects.filter(USER=i.id)
        arr.append({"name": i.name,
                    "email": i.email,
                    "phone": i.phone,
                    "Housename": ad[0].Housename,
                    "place": ad[0].place,
                    "post": ad[0].post,
                    "pin": ad[0].pin})
    return render(request, "admin/user.html", {"data": arr})


def viewpharma1(request):
    request.session['h'] = "VIEW PHARMA1"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = pharmacy.objects.filter(LOGIN__usertype='pharmacy')
    return render(request, "admin/view pharma 1.html", {"data": data})


def viewpharma(request):
    request.session['h'] = "VIEW PHARMA"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    data = pharmacy.objects.filter(LOGIN__usertype='pending')
    return render(request, "admin/view pharma.html", {"data": data})


def pharmaaccept(request, id, em):
    request.session['h'] = "ACCEPT PHARMACY"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    login.objects.filter(id=id).update(usertype='pharmacy')

    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)

        gmail.ehlo()

        gmail.starttls()

        gmail.login('epharmacy377@gmail.com', 'ijvk fiyj dnfk uuqg')

    except Exception as e:
        print("Couldn't setup email!!" + str(e))

    msg = MIMEText("your verification succesfuly completed")

    msg['Subject'] = 'Verification'

    msg['To'] = em

    msg['From'] = 'epharmacy377@gmail.com'

    try:

        gmail.send_message(msg)

    except Exception as e:

        print("COULDN'T SEND EMAIL", str(e))
    return HttpResponse("<script>alert('accept successfully');window.location='/viewpharma#services'</script>")


def pharmareject(request, id, em):
    request.session['h'] = "REJECT PHARMACY"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    login.objects.get(id=pharmacy.objects.get(id=id).LOGIN.id).delete()
    try:
        gmail = smtplib.SMTP('smtp.gmail.com', 587)

        gmail.ehlo()

        gmail.starttls()

        gmail.login('epharmacy377@gmail.com', 'ijvk fiyj dnfk uuqg')

    except Exception as e:
        print("Couldn't setup email!!" + str(e))

    msg = MIMEText("your verification rejected")

    msg['Subject'] = 'Verification'

    msg['To'] = em

    msg['From'] = 'epharmacy377@gmail.com'

    try:

        gmail.send_message(msg)

    except Exception as e:

        print("COULDN'T SEND EMAIL", str(e))
    return HttpResponse("<script>alert('rejected successfully');window.location='/viewpharma#services'</script>")


def view1(request):
    request.session['h'] = "VIEW"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = Medicine.objects.all()
    return render(request, "admin/view1.html", {"data": data})


def deletemedicine(request, id):
    request.session['h'] = "DELETE MEDICINE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    Medicine.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/view1#services'</script>")


def password(request):
    request.session['h'] = "CHANGE PASSWORD"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "admin/password.html")


def passwordpost(request):
    cp = request.POST['textfield']
    chp = request.POST['textfield2']
    np = request.POST['textfield3']
    if login.objects.filter(usertype='admin', password=cp).exists():
        if cp == chp:
            return HttpResponse("<script>alert('same password');window.location='/password'</script>")
        if chp == np:
            login.objects.filter(usertype='admin').update(password=chp)
            return HttpResponse("<script>alert('password changed successfully');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('password incorrect');window.location='/password'</script>")
    else:
        return HttpResponse("<script>alert('current password incorrect');window.location='/password'</script>")


def Adminhome(request):
    request.session['h'] = "ADMIN HOME"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "admin/index.html")


def view_complaints(request):
    request.session['h'] = "COMPLAINTS"
    obj = complaints.objects.all().order_by('-id')
    return render(request, "admin/view_complaints.html", {"data": obj})


def send_reply(request, id):
    request.session['h'] = "REPLY"
    return render(request, 'admin/send_reply.html', {"id": id})


def send_reply_post(request, id):
    reply = request.POST['reply']
    complaints.objects.filter(id=id).update(reply=reply, rdate=datetime.now().strftime("%Y-%m-%d"))
    return HttpResponse("<script>alert('Successfully Sent');window.location='/view_complaints#service'</script>")


# ==========================================================================================================================================================================


def Registration(request):
    request.session['h'] = "REGISTRATION"
    return render(request, "pharmacy/Registration.html")


def Registrationpost(request):
    n = request.POST['textfield']
    e = request.POST['textfield3']
    p = request.POST['textfield4']
    la = request.POST['textfield5']
    lo = request.POST['textfield6']
    pas = request.POST['textfield7']
    lobj = login()
    lobj.username = e
    lobj.password = pas
    lobj.usertype = 'pending'
    lobj.save()
    dobj = pharmacy()
    dobj.name = n
    dobj.email = e
    dobj.phone = p
    dobj.latitude = la
    dobj.longitude = lo
    dobj.LOGIN = lobj
    dobj.save()
    return HttpResponse("<script>alert('registered successfully');window.location='/'</script>")


def viewprofile(request):
    request.session['h'] = "PROFILE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = pharmacy.objects.get(id=request.session['pid'])
    return render(request, "pharmacy/view profile and update.html", {"data": data})


def profilepost(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    n = request.POST['textfield']
    e = request.POST['textfield2']
    p = request.POST['textfield5']
    la = request.POST['textfield3']
    lo = request.POST['textfield4']
    pharmacy.objects.filter(id=request.session['pid']).update(name=n, email=e, phone=p, latitude=la, longitude=lo)
    return HttpResponse("<script>alert('updated successfully');window.location='viewprofile'</script>")


def viewmedicine(request):
    request.session['h'] = "VIEW MEDICINE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    mid = []
    for i in Medicine.objects.all():
        if stock.objects.filter(Q(PHARMACY=request.session['pid']), MEDICINE=i.id).exists():
            pass
        else:
            mid.append(
                {
                    'id': i.id,
                    'name': i.name,
                    'type': i.type,
                }
            )
    return render(request, "pharmacy/view medicine.html", {"data": mid})


def stockupdate(request, id):
    request.session['h'] = "STOCK UPDATE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "pharmacy/stock update.html", {"id": id})


def stockupdatepost(request, id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    n = request.POST['textfield']
    s = request.POST['textfield2']
    price = request.POST['price']
    f = request.FILES['f']
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    fs = FileSystemStorage()
    fs.save(systempath + d + '.jpg', f)
    sobj = stock()
    sobj.MEDICINE_id = id
    sobj.quantity = n
    sobj.size = s
    sobj.price = price
    sobj.file = '/static/medicine photo/' + d + '.jpg'
    sobj.PHARMACY_id = request.session['pid']
    sobj.save()
    return HttpResponse("<script>alert('stock updated successfully');window.location='/viewstock'</script>")


def viewstock(request):
    request.session['h'] = "VIEW STOCK"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = stock.objects.filter(PHARMACY=request.session['pid'])
    return render(request, "pharmacy/view stock.html", {"data": data})


def deletestock(request, id):
    request.session['h'] = "DELETE STOCK"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    stock.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted successfully');window.location='/viewstock'</script>")


def viewbooking(request):
    request.session['h'] = "VIEW BOOKING"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "pharmacy/view booking.html")


def previous(request):
    request.session['h'] = "VIEW PREVIOUS"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = purchase.objects.filter(PHARMACY=request.session['pid'], status='completed').order_by('id')
    arr = []
    for i in data:
        add = address.objects.get(id=i.ADDRESS_id)
        amount = 0
        des = purchasehub.objects.filter(PURCHASE=i)
        for j in des:
            amount += float(j.quantity) * float(j.STOCK.price)
        arr.append({"ADDRESS": add,
                    "id": i.id,
                    "USER": i.USER,
                    "status": i.status,
                    "purchase": i.purchase,
                    "amount": str(amount)})
    return render(request, "pharmacy/previous booking.html", {"data": arr})


def vieworderitem(request, id):
    request.session['h'] = "VIEW ORDER"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = purchasehub.objects.filter(PURCHASE=id)
    data2 = []
    for i in data:
        data2.append({
            'id': i.id,
            'STOCK': i.STOCK,
            'quantity': i.quantity,
            'PURCHASE': i.PURCHASE,
            'price': int(i.quantity) * int(i.STOCK.price),

        })
    return render(request, "pharmacy/view order item.html", {"data": data2})


def verify(request):
    request.session['h'] = "VERIFY"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = purchase.objects.filter(PHARMACY=request.session['pid'], status__in=['pending', 'paid', 'approved', 'paid'])
    arr = []
    for i in data:
        add = address.objects.get(id=i.ADDRESS_id)
        amount = 0
        des = purchasehub.objects.filter(PURCHASE=i)
        for j in des:
            amount += float(j.quantity) * float(j.STOCK.price)
        arr.append({"ADDRESS": add,
                    "id": i.id,
                    "USER": i.USER,
                    "status": i.status,
                    "purchase": i.purchase,
                    "amount": str(amount)})
    return render(request, "pharmacy/verify.html", {"data": arr})


def vaccept(request, id):
    request.session['h'] = "ACCEPT"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    if purchase.objects.get(id=id).purchase == "offline":
        purchase.objects.filter(id=id).update(status='approved')
    else:
        purchase.objects.filter(id=id).update(status='paid')
    # Stock Update

    obj = purchasehub.objects.filter(PURCHASE=id)

    for i in obj:
        cstock = int(i.STOCK.quantity)
        qty = int(i.quantity)
        updated = cstock - qty
        stock.objects.filter(id=i.STOCK).update(quantity=str(updated))

    return HttpResponse("<script>alert('approved successfully');window.location='/verify#service'</script>")


def accept_cash(request, id):
    purchase.objects.filter(id=id).update(status="paid")
    return HttpResponse("<script>alert('Cash Accepted');window.location='/verify#service'</script>")


def vreject(request, id):
    request.session['h'] = "REJECT"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, 'pharmacy/reject_reason.html', {"id": id})


def vreject_post(request, id):
    reason = request.POST['reason']
    purchase.objects.filter(id=id).update(status=reason)
    return HttpResponse("<script>alert('rejected');window.location='/verify#service'</script>")


def set_delivered(request, id):
    purchase.objects.filter(id=id).update(status="completed")
    return HttpResponse("<script>alert('Delivered Successfully');window.location='/verify#service'</script>")


def phrating(request):
    request.session['h'] = "PHARMACY RATING"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = Rating.objects.filter(PHARMACY=request.session['pid'])
    da = []

    for im in data:
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        ar = []
        a = float(im.userrating)

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]


        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]


        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]


        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]


        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]


        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]


        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]


        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]


        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]


        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]

        da.append({
            'userrating': ar,
            'review': im.review,
            'date': im.date,
            'USER': im.USER,
            'PHARMACY': im.PHARMACY
        })

    return render(request, "pharmacy/Rating.html", {"data": da})


def phchangepass(request):
    request.session['h'] = "CHANGE PASSWORD"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "pharmacy/password.html")


def phchangepasspost(request):
    cp = request.POST['textfield']
    chp = request.POST['textfield2']
    np = request.POST['textfield3']
    if login.objects.filter(usertype='pharmacy', password=cp, id=request.session['lid']).exists():
        if cp == chp:
            return HttpResponse("<script>alert('same password');window.location='/phchangepass'</script>")
        if chp == np:

            login.objects.filter(usertype='pharmacy', id=request.session['lid']).update(password=chp)
            return HttpResponse("<script>alert('password changed successfully');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('password incorrect');window.location='/phchangepass'</script>")
    else:
        return HttpResponse("<script>alert('current password incorrect');window.location='/phchangepass'</script>")


def Home(request):
    request.session['h'] = "HOME"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "pharmacy/Home.html")


def stockupdate2(request, id):
    request.session['h'] = "STOCK UPDATE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = stock.objects.get(id=id)
    return render(request, "pharmacy/stock update2.html", {"id": id, "data": data})


def stockupdate2post(request, id):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    q = request.POST['textfield']
    s = request.POST['textfield2']
    price = request.POST['price']

    if 'f' in request.FILES:
        f = request.FILES['f']
        d = datetime.now().strftime("%Y%m%d%H%M%S")
        fs = FileSystemStorage()
        fs.save(systempath + d + '.jpg', f)
        file = '/static/medicine photo/' + d + '.jpg'
        stock.objects.filter(id=id).update(file=file)
    stock.objects.filter(id=id).update(size=s, quantity=q, price=price)
    return HttpResponse("<script>alert('stock updated successfully');window.location='/viewstock'</script>")


# =========================================================================================================================================


def Addqua(request, id, pid, q):
    request.session['h'] = "ADD QUANTITY"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")
    return render(request, "user/Add quantity.html", {"id": id, "pid": pid, "q": q})


def Addquapost(request, id, pid):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    qty = request.POST['textfield']
    a = cart.objects.filter(USER_id=request.session['uid'], STOCK_id=id)
    if a.exists():
        q = int(a[0].quantity) + int(qty)
        a.update(quantity=q)
    else:
        uobj = cart()
        uobj.USER_id = request.session['uid']
        uobj.PHARMACY_id = pid
        uobj.STOCK_id = id
        uobj.quantity = qty
        uobj.save()
    request.session['cartcount'] = cart.objects.filter(USER=request.session['uid']).count()
    return HttpResponse("<script>alert('added to cart successfully');window.location='/viewcart'</script>")


def ufeedback(request):
    request.session['h'] = "USER FEEDBACK"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "user/feedback.html")


def ufeedbackpost(request):
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    fd = request.POST['textarea']
    ufd = Feedback()
    ufd.USER_id = request.session['uid']
    ufd.feedback = fd
    ufd.date = datetime.now().date()
    ufd.save()

    return HttpResponse("<script>alert('feedback sended successfully');window.location='/home'</script>")


def register(request):
    request.session['h'] = "REGISTER"
    return render(request, "user/Register.html")


def registerpost(request):
    n = request.POST['textfield']
    e = request.POST['textfield2']
    p = request.POST['textfield3']
    ha = request.POST['textfield4']
    lo = request.POST['textfield5']
    po = request.POST['textfield6']
    pi = request.POST['textfield7']
    pas = request.POST['textfield8']
    lobj = login()
    lobj.username = e
    lobj.password = pas
    lobj.usertype = 'user'
    lobj.save()

    dobj = user()
    dobj.name = n
    dobj.email = e
    dobj.phone = p
    dobj.Housename = ha
    dobj.place = lo
    dobj.post = po
    dobj.pin = pi
    dobj.LOGIN = lobj
    dobj.save()
    return HttpResponse("<script>alert('registered successfully');window.location='/'</script>")


def viewcart(request):
    request.session['h'] = "VIEW CART"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = cart.objects.filter(USER=request.session['uid'])
    data2 = []
    for i in data:
        if int(i.quantity) <= int(i.STOCK.quantity):
            data2.append({
                'id': i.id,
                'USER': i.USER,
                'PHARMACY': i.PHARMACY,
                'STOCK': i.STOCK,
                'quantity': i.quantity,
                'price': int(i.quantity) * int(i.STOCK.price),
                'status': '1'
            })
        else:
            data2.append({
                'id': i.id,
                'USER': i.USER,
                'PHARMACY': i.PHARMACY,
                'STOCK': i.STOCK,
                'quantity': i.quantity,
                'price': int(i.quantity) * int(i.STOCK.price),
                'status': '0'
            })

    return render(request, "user/view cart.html", {"data": data2})


def deletecart(request, id):
    request.session['h'] = "DELETE CART"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    cart.objects.get(id=id).delete()
    return HttpResponse("<script>alert('removed successfully');window.location='/viewcart'</script>")


def viewitem(request, id):
    request.session['h'] = "VIEW ITEM"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = purchasehub.objects.filter(PURCHASE=id)
    data2 = []
    for i in data:
        data2.append({
            'id': i.id,
            'STOCK': i.STOCK,
            'PURCHASE': i.PURCHASE,
            'quantity': i.quantity,
            'price': int(i.quantity) * int(i.STOCK.price),
        })
    return render(request, "user/view item medicine.html", {"data": data2})


def viewmed(request):
    request.session['h'] = "VIEW MEDICINE"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = Medicine.objects.all()

    return render(request, "user/view medicine.html", {"data": data})


def viewmed_search(request):
    request.session['h'] = "MEDICINE SEARCH"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = Medicine.objects.filter(Q(name__icontains=request.POST['s']) | Q(type__icontains=request.POST['s']))
    return render(request, "user/view medicine.html", {"data": data})


def vieworder(request):
    request.session['h'] = "VIEW ORDER"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = purchase.objects.filter(USER=request.session['uid'], date=datetime.now().date())

    return render(request, "user/view orders.html", {"data": data})


def viewphar(request, id):
    request.session['h'] = "VIEW PHARMACY"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = stock.objects.filter(MEDICINE=id)
    da = []
    for im in data:
        fs = "/static/star/full.jpg"
        hs = "/static/star/half.jpg"
        es = "/static/star/empty.jpg"
        ar = []

        data = Rating.objects.filter(PHARMACY=request.session['pid']).aggregate(Avg('userrating'))
        print(data)

        if data['userrating__avg'] is not None:
            a = float(data['userrating__avg'])
            if a >= 0.0 and a < 0.4:
                print("eeeee")
                ar = [es, es, es, es, es]


            elif a >= 0.4 and a < 0.8:
                print("heeee")
                ar = [hs, es, es, es, es]

            elif a >= 0.8 and a < 1.4:
                print("feeee")
                ar = [fs, es, es, es, es]


            elif a >= 1.4 and a < 1.8:
                print("fheee")
                ar = [fs, hs, es, es, es]


            elif a >= 1.8 and a < 2.4:
                print("ffeee")
                ar = [fs, fs, es, es, es]


            elif a >= 2.4 and a < 2.8:
                print("ffhee")
                ar = [fs, fs, hs, es, es]


            elif a >= 2.8 and a < 3.4:
                print("fffee")
                ar = [fs, fs, fs, es, es]


            elif a >= 3.4 and a < 3.8:
                print("fffhe")
                ar = [fs, fs, fs, hs, es]


            elif a >= 3.8 and a < 4.4:
                print("ffffe")
                ar = [fs, fs, fs, fs, es]


            elif a >= 4.4 and a < 4.8:
                print("ffffh")
                ar = [fs, fs, fs, fs, hs]


            elif a >= 4.8 and a <= 5.0:
                print("fffff")
                ar = [fs, fs, fs, fs, fs]

            da.append({
                'id': im.id,
                'userrating': ar,
                'PHARMACY': im.PHARMACY,
                'quantity': im.quantity,
                'price': im.price,
                'file': im.file
            })
        else:
            da.append({
                'id': im.id,
                'userrating': [es, es, es, es, es],
                'PHARMACY': im.PHARMACY,
                'quantity': im.quantity,
                'price': im.price,
                'file': im.file
            })
    return render(request, "user/view pharmacy.html", {"data": da})


def viewprev(request, ):
    request.session['h'] = "VIEW PREVIOUS ORDER"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = purchase.objects.filter(USER=request.session['uid'], status='approved', date__lte=datetime.now().date())
    return render(request, "user/view previous medicine.html", {"data": data})


def home(request):
    request.session['h'] = "HOME"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "user/Home.html")


def upass(request):
    request.session['h'] = "PASSWORD"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "user/upassword.html")


def upasspost(request):
    cp = request.POST['textfield']
    chp = request.POST['textfield2']
    np = request.POST['textfield3']
    if login.objects.filter(usertype='user', password=cp, id=request.session['lid']).exists():
        if cp == chp:
            return HttpResponse("<script>alert('same password');window.location='/upass'</script>")
        if chp == np:
            login.objects.filter(usertype='user', id=request.session['lid']).update(password=chp)
            return HttpResponse("<script>alert('password changed successfully');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('password incorrect');window.location='/upass'</script>")
    else:
        return HttpResponse("<script>alert('current password incorrect');window.location='/upass'</script>")


def buynow(request):
    request.session['h'] = "BUY NOW"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    data = cart.objects.filter(USER=request.session['uid'])
    for i in data:
        pobj = purchase.objects.filter(USER=request.session['uid'], PHARMACY=i.PHARMACY_id, status='pending')
        if pobj.exists():
            if int(i.STOCK.quantity) < int(i.quantity):
                pass
            else:

                q = stock.objects.filter(id=i.STOCK.id)
                cs = int(q[0].quantity) - int(i.quantity)
                q.update(quantity=cs)
                amnt = int(pobj[0].purchase) + (int(i.quantity) * int(i.STOCK.price))
                pobj.update(purchase=amnt)
                psub = purchasehub()
                psub.STOCK_id = i.STOCK.id
                psub.quantity = i.quantity
                psub.PURCHASE_id = pobj[0].id
                psub.save()
        else:
            if int(i.STOCK.quantity) < int(i.quantity):
                pass
            else:
                p = purchase()
                p.date = datetime.now().date()
                p.purchase = int(i.quantity) * int(i.STOCK.price)
                p.Delievery = 'pending'
                p.USER_id = request.session['uid']
                p.latitude = 0
                p.longitude = 0
                p.PHARMACY_id = i.PHARMACY_id
                p.save()
                psub = purchasehub()
                psub.STOCK_id = i.STOCK.id
                psub.quantity = i.quantity
                psub.PURCHASE_id = p.id
                psub.save()
                q = stock.objects.filter(id=i.STOCK.id)
                cs = int(q[0].quantity) - int(i.quantity)
                q.update(quantity=cs)

    return HttpResponse(
        "<script>alert('Please choose a delivery option for convenient delivery.');window.location='/option#service'</script>")


def option(request):
    request.session['h'] = "VIEW OPTION"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "user/chooseoption.html")


def option_post(request):
    d = request.POST['textfield']
    lt = request.POST['textfield5']
    lg = request.POST['textfield6']
    l = purchase.objects.filter(status='pending', USER=request.session['uid'])
    if l.exists():
        l.update(latitude=lt, longitude=lg, Delievery=d)
        data = cart.objects.filter(USER=request.session['uid']).delete()
    request.session['cartcount'] = cart.objects.filter(USER=request.session['uid']).count()
    return HttpResponse(
        "<script>alert('Your order has been successfully placed.');window.location='/viewcart'</script>")


def sendra(request, id):
    request.session['h'] = "SEND RATING"
    if request.session['lin'] == '0':
        return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")

    return render(request, "user/rate.html", {"id": id})


def sendrapost(request, id):
    r = request.POST['star']
    us = Rating()
    us.USER_id = request.session['uid']
    us.PHARMACY_id = id
    us.date = datetime.now().date()
    us.userrating = r
    us.review = request.POST['re']
    us.save()
    return HttpResponse("<script>alert('rating sended successfully ');window.location='/home'</script>")


def logout(request):
    request.session['h'] = "LOGOUT"
    request.session['lin'] = "0"
    return HttpResponse("<script>alert('Your session has expired');window.location='/'</script>")


def profile(request):
    request.session['h'] = "VIEW PROFILE"
    q = user.objects.get(id=request.session['uid'])
    return render(request, "user/profile.html", {"data": q})


def uprofilepost(request):
    n = request.POST['textfield']
    e = request.POST['textfield6']
    p = request.POST['textfield7']
    ha = request.POST['textfield2']
    lo = request.POST['textfield3']
    po = request.POST['textfield4']
    pi = request.POST['textfield5']

    dobj = user.objects.get(id=request.session['uid'])
    dobj.name = n
    dobj.email = e
    dobj.phone = p
    dobj.Housename = ha
    dobj.place = lo
    dobj.post = po
    dobj.pin = pi
    dobj.save()
    return HttpResponse("<script>alert('updated successfully');window.location='/profile#service'</script>")


def and_connect(request):
    return JsonResponse({"status": "ok"})


def and_login(request):
    username = request.POST['username']
    password = request.POST['password']

    obj = login.objects.filter(username=username, password=password, usertype="user")
    if obj.exists():
        obj = obj[0]
        lid = obj.id
        name = user.objects.get(LOGIN=obj).name
        return JsonResponse({"status": "ok", "lid": lid, "name": name})
    else:
        return JsonResponse({"status": "no"})


def and_search_medicine(request):
    s = request.POST['search']

    obj = stock.objects.filter(MEDICINE__name__icontains=s, quantity__gte=0)
    arr = []
    for i in obj:
        rating = "0"
        res = Rating.objects.filter(PHARMACY=i.PHARMACY)
        if res.exists():
            rating = res.aggregate(Avg('userrating'))['userrating__avg']
        arr.append({"name": i.MEDICINE.name,
                    "price": i.price,
                    "stock": i.quantity,
                    "file": i.file,
                    "id": i.id,
                    "size": i.size,
                    "type": i.MEDICINE.type,
                    "pharmacyname": i.PHARMACY.name,
                    "rating": rating,
                    "latitude": i.PHARMACY.latitude,
                    "longitude": i.PHARMACY.longitude})
    print(arr)
    return JsonResponse({"status": "ok", "data": arr})


def and_add_to_cart(request):
    lid = request.POST['lid']
    sid = request.POST['id']
    quantity = request.POST['quantity']

    obj = cart.objects.filter(USER__LOGIN=lid, STOCK=sid)
    if obj.exists():
        cquantity = int(obj[0].quantity)
        updated = cquantity + int(quantity)
        print("updates", updated)
        print("stock", stock.objects.get(id=sid).quantity)

        if int(stock.objects.get(id=sid).quantity) < updated or updated > 10:
            return JsonResponse({"status": "out"})

        obj.update(quantity=updated)
    else:
        obj = cart()
        obj.quantity = quantity
        obj.USER = user.objects.get(LOGIN=lid)
        obj.STOCK_id = sid
        obj.save()
    return JsonResponse({"status": "ok"})


def and_view_cart(request):
    lid = request.POST['lid']
    obj = cart.objects.filter(USER__LOGIN=lid)
    arr = []
    total = 0
    for i in obj:
        tprice = float(i.quantity) * float(i.STOCK.price)
        total += tprice
        stockcount = "False"
        if int(stock.objects.get(id=i.STOCK_id).quantity) < int(i.quantity):
            stockcount = "True"
        arr.append({"name": i.STOCK.MEDICINE.name,
                    "image": i.STOCK.file,
                    "quantity": i.quantity,
                    "isStock": stockcount,
                    "id": i.id,
                    "tprice": tprice,
                    })
    print(arr)
    return JsonResponse({"status": "ok", "data": arr, "total": total})


def and_update_cart(request):
    cartid = request.POST['id']
    quantity = request.POST['quantity']
    cart.objects.filter(id=cartid).update(quantity=quantity)
    return JsonResponse({"status": "ok"})


def and_delete_cart(request):
    cartid = request.POST['id']
    cart.objects.filter(id=cartid).delete()
    return JsonResponse({"status": "ok"})


def and_view_complaints(request):
    lid = request.POST['lid']
    obj = complaints.objects.filter(USER__LOGIN=lid).order_by('-id')
    arr = []
    for i in obj:
        arr.append({"complaint": i.complaint,
                    "cdate": i.cdate,
                    "reply": i.reply,
                    "rdate": i.rdate})
    return JsonResponse({"status": "ok", "data": arr})


def and_view_payment_history(request):
    lid = request.POST['lid']
    type = request.POST['type']
    if type == "today":
        obj = purchase.objects.filter(USER__LOGIN=lid, date=datetime.now().strftime("%Y-%m-%d")).order_by('-id')
    else:
        obj = purchase.objects.filter(USER__LOGIN=lid, date__lt=datetime.now().strftime("%Y-%m-%d")).order_by('-id')
    arr = []
    for i in obj:
        total = 0
        for j in purchasehub.objects.filter(PURCHASE=i):
            total += float(j.STOCK.price) * float(j.quantity)
        arr.append({"date": i.date,
                    "status": i.status,
                    "id": i.id,
                    "purchase": i.purchase,
                    "phname": i.PHARMACY.name,
                    "total": str(total)})
    print(arr)
    return JsonResponse({"status": "ok", "data": arr})


def and_view_address(request):
    lid = request.POST['lid']
    obj = address.objects.filter(USER__LOGIN=lid, status="active").order_by('-id')
    arr = []
    for i in obj:
        arr.append({"house": i.Housename,
                    "place": i.place,
                    "pin": i.pin,
                    "post": i.post,
                    "id": i.id})

    return JsonResponse({"status": "ok", "data": arr})


def and_payment(request):
    lid = request.POST['lid']
    adrs = request.POST['address']
    method = request.POST['method']

    cart_list = cart.objects.filter(USER__LOGIN=lid)
    pharmacy_list = []

    for i in cart_list:
        if i.STOCK.PHARMACY_id not in pharmacy_list:
            pharmacy_list.append(i.STOCK.PHARMACY_id)

    for i in pharmacy_list:
        q = purchase()
        q.date = datetime.now().strftime("%Y-%m-%d")
        q.purchase = method
        q.PHARMACY_id = i
        q.ADDRESS_id = adrs
        q.USER = user.objects.get(LOGIN=lid)
        q.save()

        res = cart.objects.filter(USER__LOGIN=lid, STOCK__PHARMACY=i)
        for k in res:
            obj = purchasehub()
            obj.STOCK = k.STOCK
            obj.quantity = k.quantity
            obj.PURCHASE = q
            obj.save()
    cart.objects.filter(USER__LOGIN=lid).delete()
    return JsonResponse({"status": "ok"})


def and_send_complaint(request):
    lid = request.POST['lid']
    complaint = request.POST['complaint']
    obj = complaints()
    obj.USER = user.objects.get(LOGIN=lid)
    obj.complaint = complaint
    obj.reply = "pending"
    obj.rdate = "pending"
    obj.cdate = datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return JsonResponse({"status": "ok"})


def and_view_items(request):
    reqid = request.POST['reqid']
    obj = purchasehub.objects.filter(PURCHASE=reqid)
    arr = []
    for i in obj:
        arr.append({"name": i.STOCK.MEDICINE.name,
                    "quantity": i.quantity,
                    "image": i.STOCK.file,
                    "price": i.STOCK.price})

    return JsonResponse({"status": "ok", "data": arr})


def and_send_review(request):
    review = request.POST['review']
    rating = request.POST['rating']
    purchaseid = request.POST['purchaseid']
    lid = request.POST['lid']
    pharmacyid = purchase.objects.get(id=purchaseid).PHARMACY_id

    obj = Rating()
    obj.userrating = rating
    obj.review = review
    obj.PHARMACY_id = pharmacyid
    obj.USER = user.objects.get(LOGIN=lid)
    obj.date = datetime.now().strftime("%Y-%m-%d")
    obj.save()
    return JsonResponse({"status": "ok"})


def and_cart_check(request):
    lid = request.POST['lid']
    if cart.objects.filter(USER__LOGIN=lid).exists():
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "no"})


def and_view_review(request):
    medid = request.POST['medid']
    pharmacyid = stock.objects.get(id=medid).PHARMACY_id

    obj = Rating.objects.filter(PHARMACY=pharmacyid).order_by('-id')
    arr = []
    for i in obj:
        arr.append({"name": i.USER.name,
                    "date": i.date,
                    "rating": i.userrating,
                    "review": i.review})
    return JsonResponse({"status": "ok", "data": arr})


def and_register(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    house = request.POST['house']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']

    if login.objects.filter(username=email).exists():
        return JsonResponse({"status": "exists"})

    obj = login()
    obj.username = email
    obj.usertype = "user"
    obj.password = password
    obj.save()
    obj1 = user()
    obj1.name = name
    obj1.email = email
    obj1.phone = phone
    obj1.LOGIN = obj
    obj1.save()
    obj2 = address()
    obj2.Housename = house
    obj2.place = place
    obj2.post = post
    obj2.pin = pin
    obj2.USER = obj1
    obj2.save()

    return JsonResponse({"status": "ok"})


def and_address_add(request):
    house = request.POST['house']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    lid = request.POST['lid']
    address(Housename=house, place=place, post=post, pin=pin, USER=user.objects.get(LOGIN=lid)).save()
    return JsonResponse({"status": "ok"})


def and_delete_address(request):
    addid = request.POST['id']
    address.objects.filter(id=addid).update(status="inactive")
    return JsonResponse({"status": "ok"})
