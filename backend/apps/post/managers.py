from django.db.models import Count, ExpressionWrapper, F, FloatField, Manager, Value
from django.db.models.functions import Coalesce, ExtractHour, Now, NullIf


class PostManager(Manager):
    def with_scores(self):
        return self.filter(type='PUBLIC').annotate(
            vote_score=Count('upvotes') - Count('downvotes'),
            comment_score=Count('comments') * 0.5,
            score=F('vote_score') + F('comment_score'),
        )

    def hot(self):
        "returns posts ordered by hot score"
        return (
            self.with_scores()
            .annotate(
                # hours since post creation
                hours_elapsed=ExpressionWrapper(
                    ExtractHour(Now() - F('created_at')), output_field=FloatField()
                ),
                # avoid zero division
                adjusted_hours=ExpressionWrapper(
                    Coalesce(NullIf(F('hours_elapsed'), 0) + Value(2.0), Value(1.0)),
                    output_field=FloatField(),
                ),
                # final hot score
                hot_score=ExpressionWrapper(
                    F('score') / (F('adjusted_hours') ** 1.8), output_field=FloatField()
                ),
            )
            .order_by('-hot_score')
        )

    def best(self):
        "returns posts ordered by best score"
        return self.with_scores().order_by('-score')

    def new(self):
        "returns latest posts ordered by timestamp"
        return self.filter(type='PUBLIC').order_by('-created_at')

    def top(self):
        "returns posts ordered by top score"
        return (
            self.with_scores()
            .annotate(
                hours_elapsed=ExpressionWrapper(
                    ExtractHour(Now() - F('created_at')), output_field=FloatField()
                ),
                adjusted_hours=ExpressionWrapper(
                    Coalesce(NullIf(F('hours_elapsed'), 0) + Value(5.0), Value(1.0)),
                    output_field=FloatField(),
                ),
                top_score=ExpressionWrapper(
                    F('score') / (F('adjusted_hours') ** 1.5), output_field=FloatField()
                ),
            )
            .order_by('-top_score')
        )
