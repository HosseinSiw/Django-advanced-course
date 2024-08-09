{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}


{% block html %}
Hello <strong>Hossein</strong>. <br/>
This is an <strong>html</strong> part.
{% endblock %}