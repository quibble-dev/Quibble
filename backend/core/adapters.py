from allauth.account.adapter import DefaultAccountAdapter
from asgiref.sync import sync_to_async
from django.contrib.sites.shortcuts import get_current_site


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom django-allauth account adapter for async mail sending function.
    Mainly for serverless platforms.
    """

    async def send_mail(self, template_prefix: str, email: str, context: dict) -> None:
        request = context.get('request')
        if not request:
            raise ValueError('request object not found in context.')

        ctx = {
            "request": request,
            "email": email,
            "current_site": get_current_site(request),
        }
        ctx.update(context)
        msg = self.render_mail(template_prefix, email, ctx)
        await sync_to_async(msg.send)()

    def sync_send_mail(self, template_prefix: str, email: str, context: dict) -> None:
        """
        A synchronous wrapper for the asynchronous send_mail method.
        This is needed because some parts of Django Allauth are synchronous.
        """

        import asyncio

        asyncio.run(self.send_mail(template_prefix, email, context))

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        """
        Override the send_confirmation_mail method to use sync_send_mail.
        type: CODE
        """

        ctx = {
            'request': request,
            'user': emailconfirmation.email_address.user,
        }
        ctx.update({"code": emailconfirmation.key})
        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation"

        # use sync_send_mail instead of send_mail
        self.sync_send_mail(email_template, emailconfirmation.email_address.email, ctx)
