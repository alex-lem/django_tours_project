import random

from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.views import View

from . import data


class MainView(View):

    def get(self, request):
        dep_menu = data.departures
        few_tours = dict(random.sample(list(data.tours.items()), 6))
        return render(request, 'tours/index.html', context={'dep_menu': dep_menu, 'few_tours': few_tours})


class DepartureView(View):

    def get(self, request, departure='msk'):
        dep_menu = data.departures
        tour_departure = {}
        nights = []
        prices = []
        tours_count = 0
        if departure not in data.departures:
            raise Http404
        for tour_id, tour in data.tours.items():
            if tour['departure'] == departure:
                tour_departure[tour_id] = tour
                nights.append(tour['nights'])
                prices.append(tour['price'])
                tours_count += 1
        return render(request, 'tours/departure.html', context={'dep_menu': dep_menu,
                                                                'tour_departure': tour_departure,
                                                                'departure': data.departures[departure],
                                                                'nights': sorted(nights),
                                                                'prices': sorted(prices),
                                                                'tours_count': tours_count})


class TourView(View):

    def get(self, request, tour_id=1):
        dep_menu = data.departures
        if tour_id not in data.tours:
            raise Http404
        single_tour = data.tours[tour_id]
        return render(request, 'tours/tour.html', context={'dep_menu': dep_menu,
                                                           'single_tour': single_tour,
                                                           'departure': data.departures[single_tour['departure']]})


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, страница не найдена!')


def custom_handler505(request, exception):
    return HttpResponseServerError('Ой, сервер поломался!')
