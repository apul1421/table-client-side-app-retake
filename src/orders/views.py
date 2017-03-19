from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
# Create your views here.
from .mixins import CartOrderMixin, LoginRequiredMixin
from .models import UserCheckout, Order

class OrderDetail(DetailView):
	model = Order

	def dispatch(self, request, *args, **kwargs):
		try:
			user_check_id = self.request.session.get("user_checkout_id")
			user_checkout = UserCheckout.objects.get(id=user_check_id)
		except UserCheckout.DoesNotExist:
			user_checkout = request.user.usercheckout
		except:
			user_checkout = None

		obj = self.get_object()
		if obj.user == user_checkout and user_checkout is not None:
			return super(OrderDetail, self).dispatch(request, *args, **kwargs)
		else:
			raise Http404




class OrderList(LoginRequiredMixin, ListView):
	queryset = Order.objects.all()

	def get_queryset(self):
		user_check_id = self.request.user.email
		template_name = 'orders/order_list.html'
		print user_check_id
		user_checkout = UserCheckout.objects.get(email=user_check_id)
		print user_checkout
		return super(OrderList, self).get_queryset().filter(user=user_checkout)
		


#######CHEF SIDE######	
class ChefList(ListView):
	model = Order
	queryset = Order.objects.filter(status ='completed')
	queryset = Order.objects.all
	template_name = 'orders/chef_list.html'

	