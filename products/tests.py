from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import UnifiedProduct, PriceUpdateLog

class UnifiedProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_product_sets_default_price_signal(self):
        # Trigger Django signal (default price = 0)
        product = UnifiedProduct.objects.create(name="Signal Test Product", price=None)
        self.assertEqual(product.price, 0)

    def test_update_product_logs_price_change_signal(self):
        product = UnifiedProduct.objects.create(name="Signal Log Test", price=100.00)
        product.price = 150.00
        product.save()

        logs = PriceUpdateLog.objects.filter(product=product)
        self.assertEqual(logs.count(), 1)
        self.assertEqual(float(logs.first().old_price), 100.00)
        self.assertEqual(float(logs.first().new_price), 150.00)

    def test_rest_api_create_product(self):
        response = self.client.post('/api/products/', {
            'name': 'API Created',
            'price': 321.99
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UnifiedProduct.objects.count(), 1)
        self.assertEqual(UnifiedProduct.objects.first().name, 'API Created')

    def test_rest_api_update_logs_trigger_or_signal(self):
        product = UnifiedProduct.objects.create(name="API Update", price=999.99)
        response = self.client.put(f'/api/products/{product.id}/', {
            'name': 'API Update',
            'price': 888.88
        }, format='json')
        self.assertEqual(response.status_code, 200)

        logs = PriceUpdateLog.objects.filter(product=product)
        self.assertEqual(logs.count(), 1)
        self.assertEqual(float(logs.first().old_price), 999.99)
        self.assertEqual(float(logs.first().new_price), 888.88)

    def test_price_not_logged_if_same(self):
        product = UnifiedProduct.objects.create(name="No Change", price=50.00)
        product.price = 50.00
        product.save()
        logs = PriceUpdateLog.objects.filter(product=product)
        self.assertEqual(logs.count(), 0)
