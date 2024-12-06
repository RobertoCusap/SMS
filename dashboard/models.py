from django.db import models
from twilio.rest import Client

class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = 'AC03d5363f36bf90e4500e9dc92d221936'
        auth_token = '23d1ee8216d1b91927b05e2f8fb91400'
        client = Client(account_sid, auth_token)

        try:
            if self.score >= 70:
                message = client.messages.create(
                    body=f"Congratulations {self.name} your score is {self.score}.",
                    from_="+16812412441",
                    to="+639687209150",
                )
            else:
                message = client.messages.create(
                    body=f"Sorry {self.name} your score is {self.score}. Try again.",
                    from_="+16812412441",
                    to="+639687209150",
                )

            print(message.body)
        except Exception as e:
            print(f"Failed to send message: {e}")

        return super().save(*args, **kwargs)
