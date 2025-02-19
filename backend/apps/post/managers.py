from django.db.models import Count, ExpressionWrapper, F, FloatField, Manager
from django.db.models.functions import ExtractHour, Now


class PostManager(Manager):
    def hot(self):
        "returns posts ordered by hot score"
        return (
            self.filter(type="PUBLIC")
            .annotate(
                # vote score
                vote_score=Count("upvotes") - Count("downvotes"),
                # comment engagement score
                comment_score=Count("comments") * 0.5,
                # combined score
                score=F("vote_score") + F("comment_score"),
                # hours since post creation
                hours_elapsed=ExpressionWrapper(
                    ExtractHour(Now() - F("created_at")), output_field=FloatField()
                ),
            )
            .annotate(
                # final hot score
                hot_score=ExpressionWrapper(
                    F("score") / (F("hours_elapsed") + 2) ** 1.8, output_field=FloatField()
                )
            )
            .order_by("-hot_score")
        )

    def best(self):
        "returns posts ordered by best score"
        return (
            self.filter(type="PUBLIC")
            .annotate(
                # vote score
                vote_score=Count("upvotes") - Count("downvotes"),
                # comment engagement score
                comment_score=Count("comments") * 0.5,
                # final best score
                best_score=F("vote_score") + F("comment_score"),
            )
            .order_by("-best_score")
        )

    def new(self):
        "returns latest posts ordered by timestamp"
        return self.filter(type="PUBLIC").order_by("-created_at")
