from django.contrib import admin
from app.models import Company, Promotion, Guest, Visit, PromoCode

admin.site.register(Company)
admin.site.register(Promotion)
admin.site.register(Guest)
admin.site.register(Visit)
admin.site.register(PromoCode)