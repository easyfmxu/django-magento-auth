from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError


from madjango.db.models.products import MagentoProduct
from madjango.utils import MagentoAPILazyObject
from madjango import forms


class MagentoIntegerField(models.IntegerField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(MagentoIntegerField, self).__init__(*args, **kwargs)
    #     self.

    def to_python(self, value):

        if self.is_magento_object(value):
            return value

        # We allow null=True for this field, so we have a couple
        # options, casting None to int() will raise a TypeError
        # everythign else will raise a ValueError.
        try:
            value = int(value)
        except ValueError:
            raise ValidationError(
                'Invalid input for \'%s\' instance. '
                'Received \'%s\' but expected int' %
                self.__class__.__name__, value)
        except TypeError:
            pass

        return self.magento_model(value)
        #return self.lazy_magento_model(value)

    def is_magento_object(self, value):
        raise NotImplementedError('is_magento_object')

    def magento_model(self, value):
        raise NotImplementedError('magento_model')

    def lazy_magento_model(self, value):
        raise NotImplementedError('lazy_magento_model')

    def get_prep_value(self, value):
        # value here will be a MagentoProduct as to_python
        # above returns that. We are extending an IntegerField,
        # so we just pass back the id of the product.
        return value.id

    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': forms.ProductField}
        defaults.update(kwargs)

        return super(MagentoIntegerField, self).formfield(**defaults)



class MagentoProductField(MagentoIntegerField):
    description = _('Magento Product Id')

    def __init__(self, *args, **kwargs):
        super(MagentoProductField, self).__init__(*args, **kwargs)

    def is_magento_object(self, value):

        # The SimpleLazyObject subclass
        # this 'value' might be will trigger it's
        # _setup on just about any check, including
        # isinstance(value, MagentoAPILazyObject)
        # we don't want that, so we go about the the long
        # way, and a bit of duck typing.
        try:
            value._setupfunc == MagentoAPILazyObject
            return True
        except AttributeError:
            pass

        # important that this goes second,
        # we do not want to call isinstance on
        # a MagentoAPILazyObject or it will trigger
        # the XMLRPC call to load the data
        # if we got to this point, our check above failed
        # so we should be safe.
        if isinstance(value, MagentoProduct):
            return True

        return False

        # return isinstance(value, MagentoProduct) or \
        #        isinstance(value, MagentoAPILazyObject)

    def magento_model(self, value):
        obj = MagentoProduct()
        obj.id = value
        return obj

    def lazy_magento_model(self, value):
        return MagentoAPILazyObject(MagentoProduct, id=value)
