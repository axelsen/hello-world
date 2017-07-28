@app.route('/taco', methods=("GET", "POST"))
@login_required
def taco():
    form = forms.TacoForm()
    if form.validate_on_submit():
        models.Taco.create(
        protein=form.protein.data,
        cheese=form.cheese.data,
        shell=form.shell.data,
        extras=form.extras.data,
        user=g.user.id
    )
        flash("A taco has been born.", "success")
        return redirect(url_for('index'))
    return render_template('taco.html', form=form)
