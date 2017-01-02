from django.conf import settings
from django.views.generic import TemplateView
import stripe

stripe.api_key = settings.TEST_SECRET_KEY


class Donate(TemplateView):
    template_name = 'donate/donate.html'

    public_key = settings.TEST_PUBLISHABLE_KEY

    def post(self, request, *args, **kwargs):
        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        #Create a charge: this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency="usd",
                source=token,
                description="Example charge"
            )
        except stripe.error.CardError as e:
            # The card has been declined
            pass
        context = super(Donate, self).get_context_data(**kwargs)
        context['public_key'] = self.public_key
        return self.render_to_response(context)
