from typing import Dict

class DjangoRepository(object):
    _model = None

    def _find_one_by(self, *args, **kwargs):
        return self._model.objects.get(*args, **kwargs)

    def _find_by(self, *args, **kwargs):
        return self._model.objects.filter(*args, **kwargs)

    def _find_all(self):
        return self._model.objects.all()

    def _sql(self, query: str, name_map: Dict):
        return self._model.objects.raw(query, translations=name_map)

    def _persist(self, model):
        model.save()

    def _remove(self, model):
        model.delete()
