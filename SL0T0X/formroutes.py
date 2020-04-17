#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: PyLeet, is a modular web penetration testing interface, Made specially for private People...

"""

import os
import datetime

from flask import render_template, flash, redirect, url_for, Markup
from flask_login import login_required

from SL0T0X import app

# !/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

from SL0T0X.db import Note, Pentest, db, Persons
from SL0T0X.forms import AddPT, AddNT, EditNT, AddSE

basedir = os.path.abspath(os.path.dirname(__file__))
now = datetime.datetime.now()


@app.route('/Index/Pentest/Add', methods=['GET', 'POST'])
@login_required
def AddPentest():
    form = AddPT()
    if form.validate_on_submit():
        Add = Pentest(url=form.url.data, ipaddress=form.ipaddress.data,
                      server=form.server.data, type=form.type.data, script=form.script.data, vulns=form.vuln.data,
                      nmap=form.nmapoutput.data.filename, godirb=form.godirb.data.filename, notes=form.note.data,
                      status=form.status.data)
        db.session.add(Add)
        db.session.commit()
        if not os.path.exists(app.root_path +
                              '/static/uploads/Pentest'):
            os.mkdir(app.root_path +
                     '/static/uploads/Pentest')
        if not os.path.exists(app.root_path +
                              'static/uploads/Pentest/' +
                              str(Add.id)):
            os.mkdir(app.root_path +
                     '/static/uploads/Pentest/' +
                     str(Add.id))
        nmap = form.nmapoutput.data
        godirb = form.godirb.data
        nmap.save(os.path.join(app.root_path +
                               '/static/uploads/Pentest/' +
                               str(Add.id) +
                               '/', form.nmapoutput.data.filename))
        godirb.save(os.path.join(app.root_path +
                                 '/static/uploads/Pentest/' +
                                 str(Add.id) + '/', form.godirb.data.filename))

        if Add:
            flash("Success")
            return redirect(url_for('Index'))
        else:
            flash(f"Error")
    return render_template('addpentest.html', title="Add Pentest", form=form)


@app.route('/Notes/Add', methods=['GET', 'POST'])
@login_required
def AddNote():
    form = AddNT()
    if form.validate_on_submit():
        Add = Note(name=form.name.data, note=Markup.escape(form.note.data))
        db.session.add(Add)
        db.session.commit()
        if Add:
            flash("Success")
            return redirect(url_for('Notes'))
    return render_template('addnote.html',
                           form=form,
                           title='Add Note',
                           year=now.year)


@app.route('/Notes/Edit/<int:ID>', methods=['POST', 'GET'])
@login_required
def EditNote(ID):
    form = EditNT()
    nto = Note.query.get(ID)
    if form.validate_on_submit():
        nto.name = form.name.data
        nto.note = form.note.data
        db.session.commit()
        return redirect(url_for('Notes'))
    return render_template('editnote.html',
                           title=nto.name,
                           note=nto,
                           form=form,
                           year=now.year)


@app.route('/SE/Add', methods=['GET', 'POST'])
@login_required
def AddS():
    form = AddSE()
    if form.validate_on_submit():
        Add = Persons(name=form.name.data,
                      birthday=form.Birthday.data, email=form.emailaddress.data, pnumber=form.pnumber.data,
                      location=form.location.data,
                      accounts=form.accounts.data, note=form.note.data, avatar=form.picture.data.filename)
        db.session.add(Add)
        db.session.commit()
        if not os.path.exists(app.root_path + '/static/uploads'):
            os.mkdir(app.root_path + '/static/uploads/SE')
        if not os.path.exists(app.root_path + 'static/uploads/SE/' + str(Add.name)):
            os.mkdir(app.root_path + '/static/uploads/SE/' + str(Add.name))
        if not os.path.exists(app.root_path + 'static/uploads/SE/' + str(Add.name) + '/archive'):
            os.mkdir(app.root_path + '/static/uploads/SE/' + str(Add.name) + '/archive')

        images = form.archive.data
        if images:
            for img in images:
                file_name = str(img.filename)
                image_file = os.path.join(
                    app.root_path + '/static/uploads/SE/' + str(Add.name) + '/archive/', file_name)
                img.save(image_file)
        avatar = form.picture.data
        avatar.save(
            os.path.join(app.root_path + '/static/uploads/SE/' + str(Add.name) + '/', form.picture.data.filename))

        if Add:
            flash("Success")
            return redirect(url_for('SE'))
        else:
            flash(f"Error")
    return render_template('addSE.html',
                           form=form,
                           title='Add SE',
                           year=now.year)
