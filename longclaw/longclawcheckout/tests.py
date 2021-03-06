from django.test.client import RequestFactory
from longclaw.tests.utils import LongclawTestCase, BasketItemFactory
from longclaw.longclawcheckout.utils import create_order
from longclaw.longclawbasket.utils import basket_id


class CheckoutTest(LongclawTestCase):

    def setUp(self):
        self.addresses = {
            'shipping_name': '',
            'shipping_address_line1': '',
            'shipping_address_city': '',
            'shipping_address_zip': '',
            'shipping_address_country': '',
            'billing_name': '',
            'billing_address_line1': '',
            'billing_address_city': '',
            'billing_address_zip': '',
            'billing_address_country': ''
        }
        self.email = "test@test.com"
        request = RequestFactory().get('/')
        request.session = {}
        self.basket_id = basket_id(request)

    def test_create_order(self):
        shipping_rate = 0
        basket_items = [BasketItemFactory(basket_id=self.basket_id),
                        BasketItemFactory(basket_id=self.basket_id)]
        order = create_order(basket_items, self.addresses,
                             self.email, shipping_rate)
        self.assertIsNotNone(order)
        self.assertEqual(self.email, order.email)
        self.assertEqual(order.items.count(), 2)

    def test_checkout(self):
        """
        Test api endpoint checkout/
        """
        BasketItemFactory(basket_id=self.basket_id)
        BasketItemFactory(basket_id=self.basket_id)
        data = {
            'address': self.addresses,
            'email': self.email,
            'shipping_rate': 0
        }
        self.post_test(data, 'longclaw_checkout', format='json')

    def test_checkout_prepaid(self):
        """
        Test api endpoint checkout/prepaid/
        """
        BasketItemFactory(basket_id=self.basket_id)
        data = {
            'address': self.addresses,
            'email': self.email,
            'shipping_rate': 3.95,
            'transaction_id': 'blahblah'
        }
        self.post_test(data, 'longclaw_checkout_prepaid', format='json')

    def test_create_token(self):
        """
        Test api endpoint checkout/token/
        """
        self.get_test('longclaw_checkout_token')
