from currency.models import ContactUs, Rate, Source

from django.contrib import admin


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        'source',
        'created',
    )
    search_fields = (
        'type',
        'source',
    )
    readonly_fields = (
        'buy',
        'sale',
    )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
    )


admin.site.register(Source, SourceAdmin)


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message',
        'created',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ContactUs, ContactUsAdmin)
