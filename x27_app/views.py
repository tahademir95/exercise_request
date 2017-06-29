import logging

from django.shortcuts import render

logging.basicConfig(filename="test.log", level=logging.DEBUG)


# Create your views here.

def Index(request):
    print(request)
    return render(request, "index.html")


def ekle(request):
    logging.debug("REQUEST İçindeyim  {}".format(request))
    print(request)
    da = "mesut"
    return render(request, "ekle.html", {"da": "mesut"})


def gonder(request):
    logging.debug("Gonderdim {}".format(request))
    return render(request, "d.html")


def yaz(request):
    logging.debug("Yazdım {}".format(request))
    return render(request, "abc.html")


def halil(request):
    logging.debug("Halil e gelenler {}".format(request))
    json_data = {"name": "Halil e gelenler"}
    return render(request, "halil.html", json_data)
