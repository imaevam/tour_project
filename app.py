from flask import Flask, abort, render_template
import data

app = Flask(__name__)


@app.route('/')
def render_main():
    length = sum([len(i) for i in data.tours.values()])
    prices = sorted([j['price'] for i in data.tours.values() for j in i])
    nights = sorted([j['nights'] for i in data.tours.values() for j in i])
    return render_template('start.html',
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description,
                           tours=data.tours,
                           departures=data.departures,
                           cities=cities,
                           length=length,
                           prices=prices,
                           nights=nights)


@app.route('/departures/<departure>/')
def render_departures(departure):
    prices = sorted([i['price'] for i in data.tours[departure]])
    nights = sorted([i['nights'] for i in data.tours[departure]])
    return render_template('departure.html',
                           title=data.title,
                           departure=departure,
                           tours=data.tours,
                           departures=data.departures,
                           cities=cities,
                           prices=prices,
                           nights=nights)


@app.route('/tour/<int:tour_id>')
def render_tours(tour_id):
    ids = [j['id'] for i in data.tours.values() for j in i]
    if tour_id in ids:
        return render_template('tour.html',
                               title=data.title,
                               tours=data.tours,
                               tour_id=tour_id,
                               departures=data.departures,
                               cities=cities)
    return abort(404)


if __name__ == "__main__":
    # cities = list(set([i for i in data.tours]))
    cities = ['msk', 'spb', 'kazan', 'ekb', 'nsk']
    app.run(debug=True)
