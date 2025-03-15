from typing import TYPE_CHECKING

from django.db.models import (
    Count,
    ExpressionWrapper,
    F,
    FloatField,
    Manager,
    Value,
)
from django.db.models.functions import Coalesce, ExtractHour, Now, NullIf


class PostManager(Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                ratio=Count('upvotes') - Count('downvotes'),
            )
        )

    def with_scores(self):
        "Generalized function with most used annotations"
        return self.filter(type='PUBLIC').annotate(
            comment_score=Count('comments') * 0.5,
            score=F('ratio') + F('comment_score'),
        )

    def sorted_by(self, decay_factor: float, offset: float):
        """
        Generalized sorting function to compute scores with time decay.
        """
        return (
            self.with_scores()
            .annotate(
                hours_elapsed=ExpressionWrapper(
                    ExtractHour(Now() - F('created_at')), output_field=FloatField()
                ),
                adjusted_hours_elapsed=ExpressionWrapper(
                    Coalesce(NullIf(F('hours_elapsed'), 0) + Value(offset), Value(1.0)),
                    output_field=FloatField(),
                ),
                final_score=ExpressionWrapper(
                    F('score') / (F('adjusted_hours_elapsed') ** decay_factor),
                    output_field=FloatField(),
                ),
            )
            .order_by('-final_score')
        )

    def hot(self):
        return self.sorted_by(decay_factor=1.8, offset=2.0)

    def best(self):
        return self.with_scores().order_by('-score')

    def new(self):
        return self.filter(type='PUBLIC').order_by('-created_at')

    def top(self):
        return self.sorted_by(decay_factor=1.5, offset=5.0)
