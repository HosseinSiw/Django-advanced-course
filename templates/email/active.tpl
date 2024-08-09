{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}


{% block html %}
Hello <strong>Hossein</strong>. <br/>
Activation URL -->  https://127.0.0.1/users/api/v1/activation/confirm/{{ token }}/
{% endblock %}