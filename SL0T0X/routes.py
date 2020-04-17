#!/usr/bin/env python3

"""

   [#] Author: 0m4rS3c
   [#] Email: 0m4rS3c[at]Gmail.com
   [#] Description: SL0T0X, is a modular web penetration testing interface, Made specially for private People...

"""

import datetime
import os
import markdown2

from flask import render_template, redirect, flash, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from SL0T0X import app, crypt
from SL0T0X.db import User, Note, Pentest, db, Persons
from SL0T0X.forms import LoginForm, Settings

now = datetime.datetime.now()


@app.route('/')
@login_required
def home():
    return redirect('/Index')


@app.route('/Index')
@login_required
def Index():
    page = request.args.get('page', 1, type=int)
    Pt = Pentest.query.order_by(Pentest.date.desc()).paginate(page=page, per_page=app.config['PERPAGE'])
    next = url_for('Index', page=Pt.next_num) \
        if Pt.has_next else None
    prev = url_for('Index', page=Pt.prev_num) \
        if Pt.has_prev else None
    return render_template('index.html', title="Dashboard", pt=Pt, next=next, prev=prev, year=now.year)


@app.route('/Notes')
@login_required
def Notes():
    page = request.args.get('page', 1, type=int)
    nt = Note.query.order_by(Note.date.desc()).paginate(page=page, per_page=app.config['PERPAGE'])
    next = url_for('Notes', page=nt.next_num) \
        if nt.has_next else None
    prev = url_for('Notes', page=nt.prev_num) \
        if nt.has_prev else None
    return render_template('notes.html', title='Notes', nt=nt, next=next, prev=prev, year=now.year)


@app.route('/Notes/<int:Nid>')
@login_required
def ShowNotes(Nid):
    nt = Note.query.get(Nid)
    mark = markdown2.markdown(nt.note)
    return render_template('shownote.html',
                           title=nt.name,
                           note=nt,
                           mark=mark,
                           year=now.year)


@app.route('/Notes/Delete/<int:nid>', methods=['GET'])
@login_required
def DelNote(nid):
    nt = Note.query.filter_by(id=nid).delete()
    db.session.commit()
    if nt:
        return redirect(url_for('Notes'))


@app.route('/Index/Pentest/Delete/<int:nid>', methods=['GET'])
@login_required
def DelPentest(nid):
    nt = Pentest.query.filter_by(id=nid).delete()
    db.session.commit()
    if nt:
        return redirect(url_for('Index'))


@app.route('/Pentest/<int:Pid>')
@login_required
def ShowPentest(Pid):
    pt = Pentest.query.get(Pid)
    nmapfile = open(app.root_path + '/static/uploads/Pentest/' + str(pt.id) + '/' + pt.nmap, 'r')
    godirb = open(app.root_path + '/static/uploads/Pentest/' + str(pt.id) + '/' + pt.godirb, 'r')
    return render_template('showpentest.html',
                           title=pt.url,
                           pt=pt,
                           np=nmapfile.read(),
                           godirb=godirb.read(),
                           year=now.year)


@app.route('/SE')
@login_required
def SE():
    page = request.args.get('page', 1, type=int)
    PT = Persons.query.order_by(Persons.date.desc()).paginate(page=page, per_page=10)
    next = url_for('SE', page=PT.next_num) \
        if PT.has_next else None
    prev = url_for('SE', page=PT.prev_num) \
        if PT.has_prev else None
    pics = []
    for PTS in PT.items:
        pics = os.listdir(app.root_path + '/static/uploads/SE/' + PTS.name + '/archive')
        pics.append(pics)
    return render_template('SE.html',
                           PT=PT,
                           next=next,
                           prev=prev,
                           title='Social Engineering',
                           archive=pics,
                           year=now.year)


@app.route('/SE/<int:Pid>')
@login_required
def ShowPerson(Pid):
    pr = Persons.query.get(Pid)
    avatar = os.path.join(app.config['UPLOAD_FOLDER'] + '/SE/' + str(pr.name) + '/', pr.avatar)
    folderarchive = os.listdir(app.root_path + '/static/uploads/SE/' + pr.name + '/archive')
    file_count = len(folderarchive)
    return render_template('showperson.html',
                           pr=pr,
                           len=file_count,
                           avatar=avatar,
                           year=now.year)


@app.route('/SE/Delete/<int:nid>', methods=['GET'])
@login_required
def DelSE(nid):
    nt = Persons.query.filter_by(id=nid).delete()
    db.session.commit()
    if nt:
        return redirect(url_for('SE'))


@app.route('/Settings', methods=['GET', 'POST'])
@login_required
def Sett():
    form = Settings()
    nto = User.query.get(1)
    if form.validate_on_submit():
        nto.password = crypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.commit()
        flash(f"Password Changed!")
        return redirect(url_for('Sett'))
    return render_template('settings.html',
                           title='Settings',
                           form=form,
                           sett=nto,
                           year=now.year)


@app.route('/About')
@login_required
def About():
    return render_template('about.html',
                           title='About',
                           year=now.year)


@app.route('/License')
@login_required
def License():
    return render_template('license.html',
                           title='License',
                           year=now.year)


@app.route('/SE/Archive/<int:CID>')
@login_required
def arc(CID):
    pt = Persons.query.get(CID)
    folderarchive = os.listdir(app.root_path + '/static/uploads/SE/' + pt.name + '/archive')
    folderarchive.sort()
    return render_template('showarchive.html',
                           title='Archive',
                           pt=pt,
                           archive=folderarchive,
                           year=now.year)


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect('Index')
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and crypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('Index'))
            else:
                flash('Invalid Username/Password!')
        return render_template('login.html', form=form, title='Login', year=now.year)


@app.route('/Logout')
def Logout():
    logout_user()
    return redirect(url_for('Login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
