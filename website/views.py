from flask import Blueprint, render_template, redirect, url_for

main_views = Blueprint("main_views", __name__)

@main_views.route("/templates/index.html")
def Home_Page():
  return render_template("index.html")



@main_views.route("/")
def root():
  return redirect(url_for("main_views.Home_Page"))