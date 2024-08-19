from flask import Flask, render_template, render_template_string

app = Flask(__name__)


template_str = """
{% if yes_check_result %}
    {% for item in yes_check_result %}
        {{ item }}
        {% if not loop.last %}
            ,
        {% endif %}
    {% endfor %}
{% endif %}
<h3>==========</h3>
{% if no_check_result %}
    {% for item in no_check_result %}
        {{ item }}
        {% if not loop.last %}
            ,
        {% endif %}
    {% endfor %}
{% endif %}
"""


@app.route('/')
def index():
    yes_check_result = ['item1', 'item2', 'item3']
    # no_check_result = ['item11', 'item12', 'item13', 'item14', 'item15']
    return render_template('index.html', yes_check_result=yes_check_result)
    # return render_template('index.html', yes_check_result=yes_check_result, no_check_result=no_check_result)



# @app.route('/')
# def index():
#     yes_check_result = ['item4', 'item5', 'item6']
#     no_check_result = ['item11', 'item12', 'item13', 'item14', 'item15']
#     #return render_template_string(template_str, yes_check_result=yes_check_result)
#     return render_template_string(template_str, yes_check_result=yes_check_result, no_check_result=no_check_result)

if __name__ == '__main__':
    app.run()