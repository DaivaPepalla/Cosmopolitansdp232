from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Menu,Items,Nonveg,Veg,Beverages,Desserts,Gallery1,Gallery2,Contactus,allItems,Order,Check,Pay,RoomOrder,RoomCheck,Room
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *
from .contactus import *
from .utils import *
from rsome import ro
from rsome import grb_solver as grb
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def menudeffunc(request):
    return {
        'menu' : Menu.objects.all()
    }


def homefunc(request):
    print(request.user.id)
    request.session['roomcart'] = {}
    request.session['cart'] = {}
    return render(request, 'home.html')

def loginfunc(request):
    return_url = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("/")
        else:
            msg = "**incorrect credentials**"
            return render(request, 'signup.html',{'msg':msg})
    else:
        loginfunc.return_url=request.GET.get('return_url')  
        return render(request, 'login.html')

def logoutfunc(request):
    auth.logout(request)
    return redirect("/")

def aboutfunc(request):
    return render(request, 'aboutus.html')

def signupfunc(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                msg = "----username exixts-----"
                return render(request, 'signup.html',{'msg':msg})
            elif User.objects.filter(email=email).exists():
                msg = "------email taken------"
                return render(request, 'signup.html',{'msg':msg})
            else:
                form = SignupForm(request.POST)
                if form.is_valid():
                    user = User.objects.create_user(username=username,password=password1,email=email)
                    user.save()
                    subject = 'Successful Registration'
                    message = "Welcome To Cosmopolitan '"+username+"' . ThankYou for Signing up to our website! Explore it make use of it's services"
                    recipient = email
                    send_mail(subject,
                          message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
                    print("--------user created---------")
                    return render(request, 'login.html')
                else:
                    print("---django form validation didn't work---")
                    return render(request, 'signup.html')
        else:
            msg = "**failed to save user**"
            print("failed to save user")
            return render(request, 'signup.html',{'msg':msg})
    else:
        return render(request, 'signup.html')

def menufunc(request):
    items = Items.objects.all()
    menu = Menu.objects.all()
    return render(request, 'menu.html',{'items':items,'menu':menu})

def galleryfunc(request):
    gal1 = Gallery1.objects.all()
    gal2 = Gallery2.objects.all()
    return render(request, 'gallery.html',{'gal1':gal1,'gal2':gal2})

@login_required(redirect_field_name='next')
def contactusfunc(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        form = ContactusForm(request.POST)
        if form.is_valid():
            sent = Contactus(name=name,email=email,message=message)
            sent.save()
            subject = 'Resolve Issue'
            message = "ThankYou for contacting us '"+name+"' . We will make sure to resolve your issue as soon as possible and get back to you soon."
            recipient = email
            send_mail(subject,
                          message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            msg = "message sent"
            print("message saved-------------------------")
            return render(request, 'contact.html',{'msg':msg})
        else:
            msg = "inalid credentials"
            print("enter valid credentials-----------")
            return render(request, 'contact.html',{'msg':msg})
    else:
        return render(request, 'contact.html')



@login_required(redirect_field_name='next')
def eachitemfunc(request,item_slug):
    item_n = Nonveg.objects.filter(slug = item_slug)
    item_v = Veg.objects.filter(slug = item_slug)
    item_b = Beverages.objects.filter(slug = item_slug)
    item_d = Desserts.objects.filter(slug = item_slug)
    if item_n:
        if request.method == 'POST':
            item = get_object_or_404(Nonveg, slug=item_slug)
            items = request.POST.get('items')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(items)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(items)
                        else:
                            cart[items] = quantity - 1
                    else:
                        cart[items] = quantity + 1

                else:
                    cart[items] = 1
            else:
                cart = {}
                cart[items] = 1
            request.session['cart'] = cart

            return render(request, 'item.html', {'item': item})

        else:
            item = get_object_or_404(Nonveg, slug=item_slug)
            rating = allItems.objects.values_list('rating',flat=True).get(name=item)
            return render(request, 'item.html', {'item': item,'rating':rating})
    if item_v:
        if request.method == 'POST':
            item = get_object_or_404(Veg, slug=item_slug)
            items = request.POST.get('items')
            remove = request.POST.get('remove')

            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(items)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(items)
                        else:
                            cart[items] = quantity - 1
                    else:
                        cart[items] = quantity + 1

                else:
                    cart[items] = 1
            else:
                cart = {}
                cart[items] = 1
            request.session['cart'] = cart

            return render(request, 'item.html', {'item': item})
        else:
            item = get_object_or_404(Veg, slug=item_slug)
            rating = allItems.objects.values_list('rating',flat=True).get(name=item)
            return render(request, 'item.html', {'item': item,'rating':rating})
    if item_b:
        if request.method == 'POST':
            item = get_object_or_404(Beverages, slug=item_slug)
            items = request.POST.get('items')
            remove = request.POST.get('remove')

            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(items)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(items)
                        else:
                            cart[items] = quantity - 1
                    else:
                        cart[items] = quantity + 1

                else:
                    cart[items] = 1
            else:
                cart = {}
                cart[items] = 1
            request.session['cart'] = cart

            return render(request, 'item.html', {'item': item})
        else:
            item = get_object_or_404(Beverages, slug=item_slug)
            rating = allItems.objects.values_list('rating',flat=True).get(name=item)
            return render(request, 'item.html', {'item': item,'rating':rating})
    if item_d:
        if request.method == 'POST':
            item = get_object_or_404(Desserts, slug=item_slug)
            items = request.POST.get('items')
            remove = request.POST.get('remove')

            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(items)
                if quantity:
                    if remove:
                        if quantity <= 1:
                            cart.pop(items)
                        else:
                            cart[items] = quantity - 1
                    else:
                        cart[items] = quantity + 1

                else:
                    cart[items] = 1
            else:
                cart = {}
                cart[items] = 1
            request.session['cart'] = cart

            return render(request, 'item.html', {'item': item})
        else:
            item = get_object_or_404(Desserts, slug=item_slug)
            rating = allItems.objects.values_list('rating',flat=True).get(name=item)
            return render(request, 'item.html', {'item': item,'rating':rating})


@login_required(redirect_field_name='next')
def categorymenufunc(request,menu_slug):
    category = get_object_or_404(Menu,slug=menu_slug)
    items = Items.objects.filter(menu=category)
    if menu_slug == "non-veg":
        nv = Nonveg.objects.all()
        return render(request, 'category.html',{'category':category,'nv':nv}) 
    elif menu_slug == "veg" :
        nv = Veg.objects.all()
        return render(request, 'category.html',{'category':category,'nv':nv})
    elif menu_slug == "beverages":
        nv = Beverages.objects.all()
        return render(request, 'category.html',{'category':category,'nv':nv})
    elif menu_slug == "desserts" :
        nv = Desserts.objects.all()
        return render(request, 'category.html',{'category':category,'nv':nv})
    else:
        return render(request, 'category.html',{'category':category,'items':items})


@login_required(redirect_field_name='next')
def search(request):
    query_name = request.GET.get('q')
    if not query_name:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    elif Veg.objects.filter(name__icontains=query_name):
        results = Veg.objects.filter(name__icontains=query_name)
        return render(request, 'category.html', {"results": results})
    elif Nonveg.objects.filter(name__icontains=query_name):
        results = Nonveg.objects.filter(name__icontains=query_name)
        return render(request, 'category.html', {"results": results})
    elif Beverages.objects.filter(name__icontains=query_name):
        results = Beverages.objects.filter(name__icontains=query_name)
        return render(request, 'category.html', {"results": results})
    elif Desserts.objects.filter(name__icontains=query_name):
        results = Desserts.objects.filter(name__icontains=query_name)
        return render(request, 'category.html', {"results": results})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(redirect_field_name='next')
def cart(request):
    ids=list(request.session.get('cart').keys())
    print(list(request.session.get('cart').keys()))
    print(request.user.username)
    items=allItems.get_products_by_id(ids)
    return render(request,'cart.html',{'cart':items})


@login_required(redirect_field_name='next')
def orders(request):
        user=request.user.username
        orders=Order.get_orders_by_customer(user)
        rate2 = request.POST.get('rating[rating]')
        oid=request.POST.get('item')
        rate=request.POST.get('rate')
        itemname=request.POST.get('itemname')
        if request.method == 'POST':
            rate1 = allItems.objects.values_list('rating',flat=True).get(name=itemname)
            res = (int(rate1)+int(rate2))/2
            s = allItems.objects.get(name=itemname)
            s.rating = res
            s.save()
        return render(request,'orders.html',{'orders':orders})


@login_required(redirect_field_name='next')
def Checkout(request):
    if request.method == 'POST':
        user=request.user.username
        comment=request.POST.get('comment')
        streetaddress=request.POST.get('streetaddress')
        locality=request.POST.get('locality')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        phone=request.POST.get('phonenumber')
        cart=request.session.get('cart')
        orders=Order.get_orders_by_customer(user)
        request.session['streetaddress']=streetaddress
        request.session['locality']=locality
        request.session['city']=city
        request.session['pincode']=pincode
        request.session['comment'] = comment
        request.session['phone']=phone
        products=allItems.get_products_by_id(list(cart.keys()))

        print(user,phone,cart,products,orders)
        if len(str(pincode))==6 and len(str(phone))==10:
                check=Check(username=User(id=user),
                            comment=comment,
                            streetaddress=streetaddress,
                            locality=locality,
                            city=city,
                            pincode=pincode,
                            phone=phone)
                check.save()
                return redirect('store:pay')
        else:
            messages.warning(request, ("Fill the details correctly"))
            return render(request,'checkout.html')
    else:
        return render(request,'checkout.html')


@login_required(redirect_field_name='next')
def payment(request):
    if request.method == 'POST':
        user=request.user.username
        cardname=request.POST.get('cardname')
        cardnumber=request.POST.get('cardnumber')
        cvv=request.POST.get('cvv')
        month = request.POST.get('cc_exp_mm')
        year = request.POST.get('cc_exp_yyyy')
        cart=request.session.get('cart')
        streetaddress = request.session['streetaddress']
        locality = request.session['locality']
        city = request.session['city']
        pincode = request.session['pincode']
        phone=request.session['phone']
        comment = request.session['comment']
        products=allItems.get_products_by_id(list(cart.keys()))
        print(user,month,year,cardnumber,cardname,cvv)
        print(streetaddress,locality,city,pincode,phone)

        if (len(str(cardnumber))>=8 and len(str(cardnumber))<=16) and len(str(cvv))==3:
            pay= Pay(name=user,
                     cardno=cardnumber,
                     cardname=cardname,
                     cvv=cvv,
                     expmonth=month,
                     expyr=year)
            pay.save()
            for product in products:
                print(product)
                order = Order(item=product,
                              username=user,
                              quantity=cart.get(str(product.name)),
                              comment=comment,
                              price=product.price,
                              streetaddress=streetaddress,
                              locality=locality,
                              city=city,
                              pincode=pincode,
                              phone=phone,
                              total=product.price * int((cart.get(str(product.name)))))
                order.placeOrder()
                subject = 'Your Order'
                message = 'Hey there! Your order got delivered. Hope you enjoy your meal!!.  check your status at  http://127.0.0.1:8000/orders/  and dont forget to rate the food, That helps us to improve its quality.'
                recipient = request.user.email
                send_mail(subject,
                          message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            request.session['cart'] = {}
            return redirect('store:orders')
        else:
            messages.warning(request, ("Fill the details correctly"))
            return render(request,'pay.html')

    else:
        if not get_referer(request):
            return redirect('store:home')
        return render(request,'pay.html')


def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer



@login_required(redirect_field_name='next')
def visualize(request):
    sale = Items.objects.all()
    allitems = allItems.objects.all()
    x=[x.item_name for x in sale]
    y=[y.price for y in sale]
    z=[z.rating for z in allitems]
    chart1 = get_plot1(x, y)
    chart2 = get_plot2(x, y)
    chart3 = get_plot3(x,y,z)
    chart4 = get_plot4(x,y,z)
    chart5 = get_plot5(x,y,z)
    chart6 = get_plot6(x,y,z)
    chart7 = get_plot7(x,y,z)
    chart8 = get_plot8(x,y,z)
    chart9 = get_plot9(x,y,z)
    return render(request, 'visualize.html' , {'chart1':chart1,'chart2':chart2,'chart3':chart3,'chart4':chart4,'chart5':chart5,'chart6':chart6,'chart7':chart7,'chart8':chart8,'chart9':chart9})



@login_required(redirect_field_name='next')
def optimize(request):
    if request.method == 'POST':
        model = ro.Model('LP model')
        x = model.dvar()
        y = model.dvar()
        x_coff = int(request.POST.get('x'))
        y_coff = int(request.POST.get('y'))
        budget = int(request.POST.get('z'))
        res = ((x_coff+y_coff)*5)/2
        model.max(x_coff*x + y_coff*y)
        model.st(7*x + 3*y <= budget)
        model.st(abs(x)<=x_coff)
        model.st(abs(y)<=100)
        model.solve(grb)
        # model.st(2.5*x +y <=20)
        # model.st(5 *x +3*y<=30)
        # model.st(x +2*y<=16)
        # model.st(abs(y)<=2)
        # model.solve(grb)
        # print('x:', x.get())
        # print('y:', y.get())
        opt = model.get()
        # print('Objective:', opt)
        # formula = model.do_math()
        # print(formula)
        val = max(x.get(),y.get())
        return render(request,'optimize.html',{'val':val,'opt':opt})
    else:
        return render(request,'optimize.html')



@login_required(redirect_field_name='next')
def room(request):
    if request.method == 'POST':
        chin = request.POST.get('checkin')
        out = request.POST.get('daycount')
        room = request.POST.get('product')
        roomcart = request.session.get('roomcart')
        print(chin, out, room)
        print(roomcart)
        if roomcart:
            roomcart[room] = 1
            print(roomcart)
        else:
            roomcart = {}
            roomcart[room] = 1
            print(roomcart)
        request.session['roomcart'] = roomcart
        return redirect('store:rooms')

    else:
        rooms = Room.get_all_rooms()
        return render(request, 'bookings.html', {'Rooms': rooms})


@login_required(redirect_field_name='next')
def roomcart(request):
    ids = list(request.session.get('roomcart').keys())
    print(list(request.session.get('roomcart').keys()))
    print(request.user.username)
    items = Room.get_products_by_id(ids)
    print(items)
    return render(request, 'roomcart.html', {'cart': items})



def search_product(request):
    """ search function  """
    query_name = request.GET.get('q')
    a = request.GET.get('checkin')
    b = request.GET.get('daycount')
    c = request.GET.get('childrencount')
    print(a, b, c)
    results = Room.objects.filter(adult__icontains=query_name)
    return render(request, 'bookings.html', {"results": results})


@login_required(redirect_field_name='next')
def roomcheckout(request):
    if request.method == 'POST':
        user = request.user.username
        roomcart = request.session.get('roomcart')
        checkin = request.POST.get('checkin')
        days = request.POST.get('daycount')
        children = request.POST.get('children')
        adults = request.POST.get('Adult')
        rstreetaddress = request.POST.get('rstreetaddress')
        rlocality = request.POST.get('locality')
        rcity = request.POST.get('city')
        rpincode = request.POST.get('pincode')
        rphone = request.POST.get('phonenumber')
        request.session['checkin'] = checkin
        request.session['days'] = days
        request.session['children'] = children
        request.session['rstreetaddress'] = rstreetaddress
        request.session['rlocality'] = rlocality
        request.session['rcity'] = rcity
        request.session['rpincode'] = rpincode
        request.session['adults'] = adults
        request.session['rphone'] = rphone
        if len(str(rpincode)) == 6 and len(str(rphone)) == 10:
            check = RoomCheck(username=User(id=user),
                              streetaddress=rstreetaddress,
                              locality=rlocality,
                              city=rcity,
                              pincode=rpincode,
                              phone=rphone)
            check.save()
            return redirect('store:roompay')
        else:
            messages.warning(request, ("Fill the details correctly"))
            return render(request, 'roomcheckout.html')
    else:
        return render(request, 'roomcheckout.html')



@login_required(redirect_field_name='next')
def Roompayment(request):
    if request.method == 'POST':
        user = request.user.username
        cardname = request.POST.get('cardname')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        month = request.POST.get('cc_exp_mm')
        year = request.POST.get('cc_exp_yyyy')
        roomcart = request.session.get('roomcart')

        checkin = request.session['checkin']
        days = request.session['days']
        children = request.session['children']
        adults = request.session['adults']
        rstreetaddress=request.session['rstreetaddress']
        rlocality = request.session['rlocality']
        rcity = request.session['rcity']
        rpincode = request.session['rpincode']
        rphone = request.session['rphone']

        print(user, month, year, cardnumber, cardname, cvv)
        rooms = Room.get_products_by_id(list(roomcart.keys()))
        if (len(str(cardnumber)) >= 8 and len(str(cardnumber)) <= 16) and len(str(cvv)) == 3:
            pay = Pay(name=user,
                      cardno=cardnumber,
                      cardname=cardname,
                      cvv=cvv,
                      expmonth=month,
                      expyr=year)
            pay.save()
            for product in rooms:
                print(product)
                order = RoomOrder(item=product,
                                  username=user,
                                  checkin=checkin,
                                  price=product.price,
                                  days=days,
                                  adult=adults,
                                  children=children,
                                  streetaddress=rstreetaddress,
                                  locality=rlocality,
                                  city=rcity,
                                  pincode=rpincode,
                                  phone=rphone,
                                  total=product.price)
                order.save()
                subject = 'Your Booking'
                message = 'Hey there! Your room booking is done. Hope you enjoy our service!!.  check your status at  http://127.0.0.1:8000/rorders/  and dont forget to rate the service, That helps us to improve its quality.'
                recipient = request.user.email
                send_mail(subject,
                          message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            request.session['roomcart'] = {}
            return redirect('store:roomorders')
        else:
            messages.warning(request, ("Fill the details correctly"))
            return render(request, 'roompay.html')

    else:
        if not get_referer(request):
            return redirect('store:home')
        return render(request, 'roompay.html')



@login_required(redirect_field_name='next')
def roomorders(request):
    user = request.user.username
    roomname = request.POST.get('roomname')
    print(roomname)
    roooms = RoomOrder.get_Roomorders_by_customer(user)
    rate = request.POST.get('rate')
    stars = request.POST.get('rating[rating]')
    if request.method == 'POST':
        s = Room.objects.get(name=roomname)
        s.stars = float(stars)
        s.save()
    itemname = request.POST.get('itemname')
    return render(request, 'roomorders.html', {'orders': roooms})

def rating(request):
    if request.method == 'POST':
        tab = allItems.objects.values_list('rating',flat=True).get(name='Chicken Fry Piece Biryani')
        rate = request.POST['rate']
        res = (int(tab)+int(rate))/2
        s = allItems.objects.get(name='Chicken Fry Piece Biryani')
        s.rating = res
        s.save()
        msg = allItems.objects.values_list('rating',flat=True).get(name='Chicken Fry Piece Biryani')
        return render(request,'rate.html',{'msg':msg})
    else:
        return render(request,'rate.html')