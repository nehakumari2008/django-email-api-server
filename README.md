# django-email-api-server

Django based email API Server with following end points:

* /api/mail/send: Sends Email
* /api/server/detect: Detects transaction values sent in the email.

It is using sendgrid to send emails.

## API Contracts

>POST api/mail/send/
>Content-Type: application/json
`
{
  "username": "username",
  "send_to": "myuser@gmail.com"
}
`

>POST pi/server/detect/
>Content-Type: application/json
`
{
  "text": "You have purchased ABC for Rs 1000. The remaining balance in your account is Rs 15,345.00"
}
`
>
`{
"status": "ok",
"count": 2,
"amount": [
"Rs 1000",
"Rs 15,345.00"
]
}
`
