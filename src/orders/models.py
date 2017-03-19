from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save

# Create your models here.
from carts.models import Cart

import braintree

if settings.DEBUG:
	braintree.Configuration.configure(braintree.Environment.Sandbox,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC,
        private_key=settings.BRAINTREE_PRIVATE)





class UserCheckout(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
	email = models.EmailField(unique=True) #--> required
	braintree_id = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self): #def __str__(self):
		return self.email

	@property
	def get_braintree_id(self):
		instance = self
		if not instance.braintree_id:
			#update it
			result = braintree.Customer.create({
			    
			    "email": instance.email,
			   
			})
			if result.is_success:
				instance.braintree_id = result.customer.id
				instance.save()
		return instance.braintree_id

	def get_client_token(self):
		customer_id = self.get_braintree_id
		if customer_id:
			client_token = braintree.ClientToken.generate({
				"customer_id": customer_id
			})	
			return client_token
		return None


def update_braintree_id(sender, instance, *args, **kwargs):
	if not instance.braintree_id:
		instance.get_braintree_id


post_save.connect(update_braintree_id, sender=UserCheckout)



ORDER_STATUS_CHOICES = (
		('created', 'Created'),
		('completed', 'Completed')
	)		

class Order(models.Model):
	status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default ='created')
	cart = models.ForeignKey(Cart)
	user = models.ForeignKey(UserCheckout, null=True)
	#shipping_address = models.ForeignKey
	#final_total_price = models.DecimalField(default=)
	order_total = models.DecimalField(max_digits=50, decimal_places=2,)
	order_id = models.CharField(max_length=20, null=True, blank=True)
	def __unicode__(self):
		return str(self.cart.id)

	def mark_completed(self, order_id=None):
		self.status = "completed"
		if order_id and not self.order_id:
			self.order_id = order_id
		self.save() 	

def order_pre_save(sender, instance, *args, **kwargs):
	cart_total = instance.cart.total
	order_total = Decimal(cart_total)
	instance.order_total = order_total

pre_save.connect(order_pre_save, sender=Order)





