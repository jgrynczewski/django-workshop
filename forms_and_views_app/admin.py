#https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
from django.contrib import admin
from django.utils import timezone

from forms_and_views_app.models import Message, Ticket, Person

# # prosta rejestracja
# admin.site.register(Message)

# Ticket wprowadzam do admina, po podstawowym omówieniu Message
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    ...

# TabularInline (tabelaryczne) vs StackedInline (w wierszu)
class TicketInline(admin.TabularInline):
    model = Ticket

# Akcje
@admin.action(description="Reset the time of the message")
def reset_message_time(modeladmin, request, queryset):
    queryset.update(time=timezone.now())

# modyfikacje
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # class Media:
    #     css = {
    #         "all": ["admin_style.css"]
    #     }
    #     js = ["admin_script.js"]

    list_display = ['name', 'email', 'subject', 'time']  # wybrane kolumna na widoku listy
    # fields = [('name', 'email'), 'subject']  # pola formularza (ew. exclude)
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             "fields": ["name", "email", "subject"],
    #             "description": "Opcje podstawowe"
    #         },
    #     ),
    #     (
    #         "Advanced options",
    #         {
    #             "classes": ["collapse"],  # wide, collapse
    #             "fields": ["category", "body", "date", "time"],
    #             "description": "Opcje zaawansowane"
    #         },
    #     ),
    # ]  # fieldset
    list_filter = ('email', 'added')  # filtry
    search_fields = ["subject", "body"] # wyszukiwarka
    inlines = [TicketInline]  # edycja z poziomu rodzica
    actions = [reset_message_time]

admin.site.register(Person)