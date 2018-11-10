from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for

eq_solver = Blueprint('solver', __name__, url_prefix='/solve')

