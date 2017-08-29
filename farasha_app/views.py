# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os import listdir
import re
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

from constants import ADV_CAROUSEL_STATIC_IMAGES_PATH



def index(request):
    template = loader.get_template('farasha_app/index.html')
    context = dict()
    adv_images_list = [carousel_img for carousel_img in  listdir(ADV_CAROUSEL_STATIC_IMAGES_PATH)
                       if re.search('adv_', carousel_img)]
    carousel_list = list()
    is_one_iteration = False
    for adv_image in adv_images_list:
        if not is_one_iteration:
            carousel_list.append((adv_image, "active"))
            is_one_iteration = True
        else:
            carousel_list.append((adv_image, ""))
    context['carousel_image_list'] = carousel_list
    return HttpResponse(template.render(context, request))


def about(request, user_name="Isham"):
    return HttpResponse("Hi {}, \n Welcome to the about page.".format(user_name))
