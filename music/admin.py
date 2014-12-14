
from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline
from forms import ReleaseForm
from models import *


class PersonAdmin(AjaxSelectAdmin):

    pass

admin.site.register(Person, PersonAdmin)


class LabelAdmin(AjaxSelectAdmin):
    """ to get + popup buttons, subclass AjaxSelectAdmin

        multi-inheritance is also possible if you have an Admin class you want to inherit from:

        class PersonAdmin(YourAdminSuperclass, AjaxSelectAdmin):

        this acts as a MixIn to add the relevant methods
    """
    # this shows a ForeignKey field

    # create an ajax form class using the factory function
    #                     model, fieldlist,   [form superclass]
    form = make_ajax_form(Label, {'owner': 'person'})

admin.site.register(Label, LabelAdmin)


class GroupAdmin(AjaxSelectAdmin):

    # this shows a ManyToMany field
    form = make_ajax_form(Group, {'members': 'person'})

admin.site.register(Group, GroupAdmin)


class SongAdmin(AjaxSelectAdmin):

    form = make_ajax_form(Song, {'group': 'group', 'title': 'cliche'})

admin.site.register(Song, SongAdmin)


class ReleaseAdmin(AjaxSelectAdmin):

    # specify a form class manually (normal django way)
    # see forms.py
    form = ReleaseForm

admin.site.register(Release, ReleaseAdmin)


class BookInline(AjaxSelectAdminTabularInline):

    # AjaxSelectAdminTabularInline enables the + add option

    model = Book
    form = make_ajax_form(Book, {
                'about_group': 'group',
                'mentions_persons': 'person'
                },
                show_help_text=True)
    extra = 2

    # to enable the + add option
    # instead of your inline inheriting from AjaxSelectAdminTabularInline
    # you could implement this
    # def get_formset(self, request, obj=None, **kwargs):
    #     from ajax_select.fields import autoselect_fields_check_can_add
    #     fs = super(BookInline, self).get_formset(request, obj,**kwargs)
    #     autoselect_fields_check_can_add(fs.form, self.model, request.user)
    #     return fs


class AuthorAdmin(AjaxSelectAdmin):

    inlines = [
        BookInline,
    ]

admin.site.register(Author, AuthorAdmin)
