import stripe
import json
from docassemble.base.util import word, get_config, action_argument, DAObject, prevent_going_back
from docassemble.base.standardformatter import BUTTON_STYLE, BUTTON_CLASS
def check_coupon(coupon_code):
  # check if the coupon code is valid
  return stripe.Coupon.retrieve(coupon_code)

class CheckoutFlow(DAObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set your stripe secret key
        stripe.api_key = 'sk_test_51KbgkpSDtFmq7yIYzw8zNwiG6Pl13RuwYyMeQ506l7Fw9Jgd2QM9qz50NzAe9s4AFXCVJm6azuPqK4Ta0RJUEgNu00v6U8xFyz'

    def create_payment_intent(self, amount):
        # Create a PaymentIntent
        return stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            metadata={'integration_check': 'accept_a_payment'},
        )

    def create_payment(self, payment_intent_id, payment_method_id):
        # Confirm the PaymentIntent
        return stripe.PaymentIntent.confirm(payment_intent_id, payment_method_id)


    def process_payment(self, card_info, coupon_code=None):
        # process the card payment and coupon code
        amount = 100 # set the amount here
        # create the payment intent
        payment_intent = self.create_payment_intent(amount)
        # check if the coupon code is valid
        if coupon_code:
            coupon = self.check_coupon(coupon_code)
            if coupon:
                # apply the coupon to the payment intent
                payment_intent.coupon = coupon.id
                payment_intent.save()
                amount = payment_intent.amount
            else:
                return 'Invalid Coupon Code'
        # create the payment with the card information and the payment intent
        payment = self.create_payment(payment_intent.id, card_info)
        if payment.status == 'succeeded':
            return f'Payment of {amount/100} USD was successful'
        else:
            return 'Payment failed'

    

