from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag,  Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                if is_main:
                    raise ValidationError('Уже существует is_main')
                else:
                    is_main = True
        if not is_main:
            raise ValidationError('Нет is_main')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    verbose_name_plural = "Тематики статьи"
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    pass
