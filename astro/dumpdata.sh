#! /bin/bash

function dumpData() {
    python manage.py dumpdata -o data.json faq.AstroPoint faq.Rule faq.Resource polls.Question polls.Choice auth.User;
}

dumpData