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
    def with_ratio(self):
        # returns annotated ratio property
        return self.annotate(
            upvote_count=Count('upvotes'),
            downvote_count=Count('downvotes'),
            ratio=F('upvote_count') - F('downvote_count'),
        )

    def with_scores(self):
        "generalized function with most used annotatations"
        return self.filter(type='PUBLIC').annotate(
            vote_score=Count('upvotes') - Count('downvotes'),
            comment_score=Count('comments') * 0.5,
            score=F('vote_score') + F('comment_score'),
        )

    def sorted_by(self, decay_factor: float, offset: float):
        """
        generalized sorting function to compute scores with time decay.
        - `decay_factor`: controls how quickly older posts lose rank.
        - `offset`: prevents zero-division and smooths early rankings.
        """
        return (
            self.with_scores()
            .annotate(
                # hours since post creation
                hours_elapsed=ExpressionWrapper(
                    ExtractHour(Now() - F('created_at')), output_field=FloatField()
                ),
                # avoid zero division
                adjusted_hours_elapsed=ExpressionWrapper(
                    Coalesce(NullIf(F('hours_elapsed'), 0) + Value(offset), Value(1.0)),
                    output_field=FloatField(),
                ),
                # final score
                final_score=ExpressionWrapper(
                    F('score') / (F('adjusted_hours_elapsed') ** decay_factor),
                    output_field=FloatField(),
                ),
            )
            .order_by('-final_score')
        )

    def hot(self):
        "returns posts ordered by hot score"
        return self.sorted_by(decay_factor=1.8, offset=2.0)

    def best(self):
        "returns posts ordered by best score"
        return self.with_scores().order_by('-score')

    def new(self):
        "returns latest posts ordered by timestamp"
        return self.filter(type='PUBLIC').order_by('-created_at')

    def top(self):
        "returns posts ordered by top score"
        return self.sorted_by(decay_factor=1.5, offset=5.0)
