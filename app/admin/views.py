from . import admin
from flask import *
from app import db
from flask import render_template, redirect, request, url_for
from flask_login import login_required
from .forms import LoginForm, EditProfileParkingForm
from app import models
from ..decorators import admin_required


@admin.route('/parking/id/<id>')
@login_required
@admin_required
def admin_parking_panel(id):
    parking = models.Parking.query.filter_by(user_id=id).first_or_404()

    x = {
        "id": parking.id,
        "user_id": parking.user_id,
        "adress": parking.adress,
        "localisation": parking.localisation,
        "name": parking.name,
        "description": parking.description,
        "number_of_parkings": parking.number_of_parkings,
        "numer_of_free_parking": parking.number_of_free_parkings
    }
    return jsonify(x)


@admin.route('/user/id/<users_id>')
@login_required
@admin_required
def admin_user_panel(users_id):
    users = models.User.query.filter_by(id=users_id).first_or_404()
    print(users)
    x = {
        "id": users.id,
        "email": users.email,
        "username": users.username,
        "subname": users.subname,
        "numerphone": users.numerphone,
        "nrrej": users.nrrej,
        "role_id": users.role_id,

    }
    return jsonify(x)


@admin.route('/')
@login_required
@admin_required
def admin_panel():
    x = models.Parking.query.all()
    list = []
    list2 = []
    for i in x:
        name = models.User.query.filter_by(id=i.user_id).first()
        list.append(name.username)
        list2.append(name.subname)
    return render_template('panelAdminParkingList.html', people=x, list=list, list2=list2)


@admin.route('/parking/create/', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_create_parking_panel():
    form = LoginForm()
    if request.method == 'POST':
        parking = models.Parking(user_id=form.user_id.data, adress=form.adress.data,
                                 number_of_parkings=form.number_of_parkings.data,
                                 name=form.name.data, description=form.description.data,
                                 localisation=form.localisation.data, number_of_free_parkings=0)
        db.session.add(parking)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_parking.html', form=form)


@admin.route('/managerlist/')
@login_required
@admin_required
def admin_manager_list():
    return render_template('panelAdminManagerList.html', people=models.User.query.filter_by(role_id=3))


@admin.route('/parking/<id>/', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_one_parking(id):
    parking = models.Parking.query.get_or_404(id)
    form = EditProfileParkingForm(user=parking)
    if request.method == 'POST':
        if not request.form['name'] == '':
            parking.name = request.form['name']
        if not request.form['adress'] == '':
            parking.adress = request.form['adress']
        if not request.form['number_of_parkings'] == '':
            parking.number_of_parkings = request.form['number_of_parkings']
        if request.form['owner'] == '' or not models.Parking.validate_user_id(request.form['owner']):
            print(models.Parking.validate_user_id(request.form['owner']))
        else:
            print(models.Parking.validate_user_id(request.form['owner']))
            parking.user_id = request.form['owner']
        if not request.form["description"] == '':
            parking.description = request.form["description"]
        if not request.form['position'] == "":
            parking.localisation = request.form['position']
        db.session.add(parking)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('Panel_admin_one_parking.html', parking=parking)


@admin.route('/delete/<id>')
@login_required
@admin_required
def admin_delete_parking(id):
    x = models.Parking.delete_parking(id)
    if not x:
        print(False)
    else:
        return redirect(url_for("admin.admin_panel"))


@admin.route('/userlist/')
@login_required
@admin_required
def admin_user_list():
    return render_template('panelUserList.html', people=models.User.query.filter_by(role_id=1))


@admin.route('/manager/<id>', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_manager_one(id):
    manager = models.User.query.get_or_404(id)
    if request.method == 'POST':
        print(models.User.verify_email(request.form['email']))
        print(request.form['email'])
        if models.User.verify_email(request.form['email']):
            manager.email = request.form['email']
        elif not request.form['email'] == '':
            manager.email = request.form['email']
        if not request.form['username'] == '':
            manager.username = request.form['username']
        if not request.form['subname'] == '':
            manager.subname = request.form['subname']
        if not request.form['numerphone'] == '':
            manager.numerphone = request.form['numerphone']
        if not request.form['nrrej'] == '':
            manager.nrrej = request.form['nrrej']
        db.session.add(manager)
        db.session.commit()
        return redirect(url_for('main.admin_manager_one'))
    return render_template('Panel_admin_one_manger.html', user=manager,
                           parking=models.Parking.query.filter_by(user_id=id))
