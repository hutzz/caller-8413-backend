from index import app
from flask import request, jsonify
from errno import errorcode
from flask_mysqldb import MySQL
from app import media, abbie, ram #, xi

mysql = MySQL(app)

try:
    @app.route('/')
    def index():
        return abbie.count(mysql)
    @app.route('/addjob', methods = ['POST'])
    def add_job():
        data = request.get_json()
        return abbie.increment(mysql, data)
    @app.route('/deletejob', methods = ['POST'])
    def remove_job():
        data = request.get_json()
        return abbie.decrement(mysql, data)
    @app.route('/mp4', methods = ['POST'])
    def dl_mp4():
        url = request.get_json()
        dl = media.mp4(url)
        if not dl: return jsonify('h')
        return jsonify(dl)
    @app.route('/mp3', methods = ['POST'])
    def dl_mp3():
        url = request.get_json()
        dl = media.mp3(url)
        if not dl: return jsonify('h')
        return jsonify(dl)
    @app.route('/rammap', methods = ['POST'])
    def rammap():
        data = request.get_json()
        mt1,mt2,cas1,cas2 = data 
        mt1,mt2,cas1,cas2 = int(mt1),int(mt2),int(cas1),int(cas2)
        return jsonify(ram.rammap(ram.megatransfers(mt1,mt2),ram.cas_latency(cas1,cas2)))
    # @app.route('/xi')
    # def iswinnie():
    #     if xi.is_winnie_the_pooh():
    #         return jsonify('0')
    #     return jsonify('1')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database connection failure")
    else:
        print('Something went wrong:', err)