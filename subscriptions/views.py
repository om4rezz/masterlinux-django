from django.shortcuts import render, HttpResponseRedirect

from .forms import EmailForm, SubscriptionForm
from .models import Subscription

import uuid

# Create your views here.

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''
    return ip

def get_subscription_ref_id():
    subscription_ref_id = str(uuid.uuid4())[:12].replace('-', '').lower()
    try:
        id_exists = Subscription.objects.get(ref_id=subscription_ref_id)
        # have to do something to regenerate another one
        get_subscription_ref_id()
    except:
        return subscription_ref_id

def share(request, subscription_ref_id):
    print subscription_ref_id
    context = {"ref_id": subscription_ref_id}
    template = 'share.html'
    return render(request, template, context)

def home(request):
    print request.META.get("REMOTE_ADDR")
    print request.META.get("HTTP_X_FORWARDED_FOR")

    # this is regular django form >>>>>

    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data['email']
    #     new_subscription, created = Subscription.objects.get_or_create(email=email)
    #     print new_subscription, created
    #     print new_subscription.timestamp
    #     if created:
    #         print "this object was created!"

    # end django form

    #
    # And this is using Model forms >>>>
    #
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        new_subscription = form.save(commit=False)
        # i set commit to be (((false))) because we might do something here
        email = form.cleaned_data['email']
        new_subscription_old, created = Subscription.objects.get_or_create(email=email) # i recommend not entering any emails from admin because this line may give an error if it returned any multiples
        if created:
            print "this object was created!"
            new_subscription_old.ref_id = get_subscription_ref_id()
            new_subscription_old.ip_address = get_ip(request)
            new_subscription_old.save()

        # redirect here
        return HttpResponseRedirect('%s' % (new_subscription_old.ref_id))

        # new_subscription.ip_address = get_ip(request)
        # new_subscription.save() # this might give a lot of multiples , so i used get_or_create method

    context = {'form': form}
    template = 'home.html'
    return render(request, template, context)