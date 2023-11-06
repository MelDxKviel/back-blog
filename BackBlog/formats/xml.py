from django.utils.translation import gettext_lazy as _

import dicttoxml
from import_export.formats.base_formats import Format


class XML(Format):

    def get_title(self):
        return _('xml')

    def is_binary(self):
        """
        Returns if this format is binary.
        """
        return False

    def get_extension(self):
        """
        Returns extension for this format files.
        """
        return ".xml"

    def get_content_type(self):
        return 'application/xml'

    def can_import(self):
        return True

    def can_export(self):
        return True

    def export_data(self, dataset, **kwargs):
        """
        Returns format representation for given dataset.
        """
        kwargs.setdefault('attr_type', False)
        return dicttoxml.dicttoxml(dataset.dict, attr_type=False)

    def create_dataset(self, in_stream):
        print(in_stream)
