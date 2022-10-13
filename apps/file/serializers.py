# Rest framework
from rest_framework import serializers

# Project
from file.models import File
from file.service import thumbnail_files


class FileFieldSerializer(serializers.FileField):

    def __init__(self, context, *args, **kwargs):
        super(FileFieldSerializer, self).__init__(*args, **kwargs)
        self.request = context['request']
        self.width = self.request.GET.get('width')
        self.height = self.request.GET.get('height')

    def to_representation(self, instance):
        url = thumbnail_files(instance, self.width, self.height)
        return self.request.build_absolute_uri(url)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'id',
            'file',
            'format',
            'name',
            'ordering'
        ]

    def __init__(self, *args, **kwargs):
        super(FileSerializer, self).__init__(*args, **kwargs)
        self.request = self.context['request']
        if getattr(self.request, 'method', None) == 'GET':
            self.fields['file'] = FileFieldSerializer(context=self.context)