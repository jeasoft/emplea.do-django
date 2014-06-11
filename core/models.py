#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Los modelos creados!

from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

from tinymce.models import HTMLField

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categorías"

    name = models.CharField(max_length=30, verbose_name="nombre")
    slug = models.SlugField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ("category/%s" % self.slug)

@python_2_unicode_compatible
class Job(models.Model):
    name = models.CharField(max_length=200, verbose_name="nombre del trabajo")
    category = models.ForeignKey(Category, verbose_name="categoría")
    place = models.CharField(max_length=200, verbose_name="lugar")
    description = HTMLField(verbose_name="Perfil de puesto")
    application = HTMLField(verbose_name="Como aplicar?")
    pub_date = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=200, verbose_name="nombre de compañía")
    url = models.URLField(blank=True, null=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to="images/logos", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ("/job/%i/" % self.id)
