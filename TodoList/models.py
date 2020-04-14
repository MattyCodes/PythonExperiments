from database import db, ma

# Todo-item model-class.
class TodoItem(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))

    def __init__(self, description):
        self.description = description

# Todo-item schema (for serialization).
class TodoItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description')
