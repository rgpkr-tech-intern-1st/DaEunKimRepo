from django.test import TestCase
from django.shortcuts import reverse
from django.utils import timezone

from ..models import Restaurant


class RestaurantDefaultListViewTests(TestCase):

    def test_default_list_view_should_return_restaurants_with_local_postal_code_when_request_without_postal_code(self):
        pass

    def test_default_list_view_should_only_return_restaurants_with_same_postal_code_when_request_with_postal_code(self):
        # Given
        postal_code = '01234'
        different_postal_code_restaurant = Restaurant.objects.create(
            is_franchise=True,
            name='요기짜장-서초점',
            address='서울시 요기구 기요동',
            postal_code='01233',
            minimum_order_price=14000,
            open_time=timezone.localtime().min.strftime('%H:%M:%S'),
            close_time=timezone.localtime().max.strftime('%H:%M:%S'),
        )
        same_postal_code_restaurant = Restaurant.objects.create(
            is_franchise=True,
            name='요기치킨-강남점',
            address='서울시 요기구 요기동',
            postal_code='01234',
            minimum_order_price=14000,
            open_time=timezone.localtime().min.strftime('%H:%M:%S'),
            close_time=timezone.localtime().max.strftime('%H:%M:%S'),
        )

        # When
        response = self.client.get(reverse('restaurant:default_list', kwargs={
            'postal_code': postal_code,
        }))

        # Then
        self.assertQuerysetEqual(
            response.context['restaurants'], [
                f'<Restaurant: {same_postal_code_restaurant}>',
            ],
        )

    def test_default_list_view_should_only_return_opened_restaurants_when_compared_to_present_time(self):
        # Given
        postal_code = '01234'
        present_time = timezone.localtime()
        earlier_time = present_time - timezone.timedelta(minutes=1)
        later_time = present_time + timezone.timedelta(minutes=1)
        not_yet_opened_restaurant = Restaurant.objects.create(
            is_franchise=True,
            name='요기피자-서초점',
            address='서울시 요기구 기요동',
            postal_code='01234',
            minimum_order_price=14000,
            open_time=later_time.strftime('%H:%M:%S'),
            close_time=timezone.localtime().max.strftime('%H:%M:%S'),
        )
        already_closed_restaurant = Restaurant.objects.create(
            is_franchise=True,
            name='요기카페-서초점',
            address='서울시 요기구 기요동',
            postal_code='01234',
            minimum_order_price=14000,
            open_time=timezone.localtime().min.strftime('%H:%M:%S'),
            close_time=earlier_time.strftime('%H:%M:%S'),
        )
        opened_restaurant = Restaurant.objects.create(
            name='요기버거-서초점',
            address='서울시 요기구 기요동',
            postal_code='01234',
            minimum_order_price=14000,
            open_time=earlier_time.strftime('%H:%M:%S'),
            close_time=later_time.strftime('%H:%M:%S'),
        )

        # When
        response = self.client.get(reverse('restaurant:default_list', kwargs={
            'postal_code': postal_code,
        }))

        # Then
        self.assertQuerysetEqual(
            response.context['restaurants'], [
                f'<Restaurant: {opened_restaurant}>',
            ],
        )

    def test_default_list_view_should_return_empty_when_restaurants_do_not_exists(self):
        # Given
        postal_code = '01234'

        # When
        response = self.client.get(reverse('restaurant:default_list', kwargs={
            'postal_code': postal_code,
        }))

        # Then
        self.assertQuerysetEqual(
            response.context['restaurants'], [
            ],
        )
        self.assertContains(
            response,
            '주문가능한 음식점이 제공되지 않습니다.',
        )
