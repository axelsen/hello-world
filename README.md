# hello-world
~ The initiation of food for the hungry

I am all about aboutness and the gooditude of latitude, longtiude, solitude and sociatude.


@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    if form.validate_on_submit():
        models.LunchOrder.create()
        g.user = current_user
    return render_template('lunch.html')
