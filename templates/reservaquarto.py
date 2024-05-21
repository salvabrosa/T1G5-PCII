{% extends 'base.html' %}

{% block title %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css')}}">
{% endblock %}

{% block content %}
    <div class = "dados">
        <img src="/static/images/{{cname}}.jpg" alt="{{cname}}" width="300" height="200">
        <h1>{{header}}</h1>
        <br>
        
        {% if tipou == "admin" %}
        <button id="edit" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=edit'" class="button1">Edit</button>
        <button id="delete" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=delete'" class="button1">Delete</button>
        <button id="insert" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=insert'" class="button1">Insert</button>
        <button id="save" type="submit" form="form" class = "button1" {{butedit}}>Save</button>
        <button id="cancel" type="button" {{butedit}} onclick="window.location.href = '/gform/{{cname}}?option=cancel'" class="button1">Cancel</button>
        <button id="exit" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=exit'" class="button1">Exit</button>
        {%endif%}
        <br><br>
        
            <form id="form" action="/gform/{{cname}}?option=save" method="post">
                {% for key in att %}
                  <label for="{{key}}">{{des[loop.index-1]}}:</label>
                  {% if loop.index == 1 and butedit == 'enabled' and auto_number == 1 %}
                      <input type="text" disabled id="{{key}}" name="{{key}}" value="{{obj[key]}}" size="30"/>
                  {%else%}                  
                      <input type="text" {{butedit}} id="{{key}}" name="{{key}}" value="{{obj[key]}}" size="30"/>
                  {%endif%}
                  <br><br>
                {% endfor %}
            </form>
        <br>
        {% if tipou == "admin" %}
        <button id="first" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=first'" class="button1">First</button>
        <button id="previous" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=previous'" class="button1">Previous</button>
        <button id="next" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=next'" class="button1">Next</button>
        <button id="last" type="button" {{butshow}} onclick="window.location.href = '/gform/{{cname}}?option=last'" class="button1">Last</button>
        {%endif%}    
    </div>

{% endblock %}