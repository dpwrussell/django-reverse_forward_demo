django-reverse_forward_demo
===========================

Demo django project to demonstrate inefficient querying when
doing a reverse and then a forward lookup with the built-in
lookups.

DemoCarView
===========
Inefficient querying view.
Uses HTML: car_detail.html
At URL:  demo/car/1

DemoCarViewPreload
==================
Efficient querying view, but loses some benefits of using generic views
Uses HTML: car_detail_preload.html
At URL:  demo/carpreload/1
