from subscriptions.models import Subscription

class RefMiddleware():
    def process_request(self, request):
        ref_id = request.GET.get('ref')
        try:
            obj = Subscription.objects.get(ref_id = ref_id)
        except:
            obj = None

        if obj:
            request.session['subscription_id_ref'] = obj.id