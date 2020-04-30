from . import ma

class TodoSchema(ma.Schema):
    class Meta:
        fields = ("_id", "name", "status")