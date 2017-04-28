from MusicianModels.models import Tag
from ajax_select import register, LookupChannel

@register('tag')
class ThingsLookup(LookupChannel):

    model = Tag

    def get_query(self, q, request):
          return self.model.objects.filter(title__icontains=q).order_by('tag_type')