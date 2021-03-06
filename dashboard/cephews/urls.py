# Copyright 2015 Cisco Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import url

from .views import login, logout, overview, osd_status, pool, crush_rule
from .views import distribution, json_response

urlpatterns = [
    url(r'^$', overview, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^overview$', overview, name='overview'),
    url(r'^osd_status$', osd_status, name='osd_status'),
    url(r'^pool$', pool, name='pool'),
    url(r'^crush_rule$', crush_rule, name='crush_rule'),
    url(r'^distribution$', distribution, name='distribution'),
    url(r'^json$', json_response, name='json'),
]
