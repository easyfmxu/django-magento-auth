Django Magento Auth Middleware
=============

## Django Magento access

[![ScreenShot](http://img.youtube.com/vi/Ve9F4NJjIIM/hqdefault.jpg)](http://youtu.be/Ve9F4NJjIIM)


## Magento authentication middleware
[![ScreenShot](http://img.youtube.com/vi/k7OhiNBZ2o0/hqdefault.jpg)](http://youtu.be/k7OhiNBZ2o0)

view repo [here](https://github.com/blitzagency/django-magento-auth)

default username is set in www/project/settings/local.py
ex:  
	
	MAGENTO_URL = 'http://127.0.0.1:8001'
	MAGENTO_USERNAME = 'foobar'
	MAGENTO_PASSWORD = 'foobar'

**If you set the magento username and password as something different, make sure you have that represented here or the middleware won't work**

About
-----
This works in tandom with madjango agency template.  

Using Madjango
-------------------------------

1. install madjango

pip install -e git+https://github.com/blitzagency/django-magento-auth.git#egg=madjango


2. Edit `settings.py` 

        # settings.py
        ...
        
        MAGENTO_URL = 'http://127.0.0.1:8001'
        MAGENTO_USERNAME = 'foobar'
        MAGENTO_PASSWORD = 'foobar'
        
        ...
        MIDDLEWARE_CLASSES = (
        ...
        'madjango.middleware.MadjangoAuthenticationMiddleware',
        ...
        }


License (MIT)
=============

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
