from index import app
import mysql.connector
from flask import request, jsonify
import re
from pytube import YouTube
from moviepy.editor import *
from errno import errorcode
from flask_mysqldb import MySQL

mysql = MySQL(app)

try:
    @app.route('/')
    def index():
        cur = mysql.connection.cursor()
        cur.execute("SELECT job_count FROM abbie")
        fetchdata = cur.fetchone()
        for f in fetchdata: return str(f)
    @app.route('/addjob', methods = ['POST'])
    def add_job():
        cur1 = mysql.connection.cursor()
        cur2 = mysql.connection.cursor()
        data = request.get_json()
        try:
            cur1.execute(f"UPDATE abbie SET job_count = job_count + {data}")
            cur2.execute("SELECT job_count FROM abbie")
            mysql.connection.commit()
            print('jobs added')
            fetchdata = cur2.fetchone()
        except:
            mysql.connection.rollback()
        finally:
            cur1.close()
            cur2.close()
        for f in fetchdata: return str(f)
    @app.route('/deletejob', methods = ['POST'])
    def remove_job():
        cur1 = mysql.connection.cursor()
        cur2 = mysql.connection.cursor()
        data = request.get_json()
        try:
            cur1.execute(f"UPDATE abbie SET job_count = job_count - {data}")
            cur2.execute("SELECT job_count FROM abbie")
            mysql.connection.commit()
            print('jobs removed')
            fetchdata = cur2.fetchone()
        except:
            mysql.connection.rollback()
        finally:
            cur1.close()
            cur2.close()
        for f in fetchdata: return str(f)
    @app.route('/mp4', methods = ['POST'])
    def mp4():
        url = request.get_json()
        yt = YouTube(url)
        print(yt.streams.get_highest_resolution().filesize)
        if (yt.streams.get_highest_resolution().filesize) > 7900000:
            return jsonify('h')
        stream = yt.streams.filter(progressive=True).order_by('resolution').last()
        stream.download()
        regex = r'[#%{}/<>*?/$\'":+`|=,.]'
        title = re.sub(regex, '', yt.title)
        print(title)
        return jsonify(f'../caller-8413-data-server/{title}.mp4')
    @app.route('/mp3', methods = ['POST'])
    def mp3():
        url = request.get_json()
        yt = YouTube(url)
        print(yt.streams.get_highest_resolution().filesize)
        if (yt.streams.get_highest_resolution().filesize) > 50000000:
            return jsonify('h')
        stream = yt.streams.filter(progressive=True).order_by('resolution').last()
        stream.download()
        regex = r'[#%{}/<>*?/$\'":+`|=,.]'
        title = re.sub(regex, '', yt.title)
        print(title)
        mp4 = VideoFileClip(title + '.mp4')
        mp3 = mp4.audio
        mp3.write_audiofile(title + '.mp3')
        mp4.close()
        mp3.close()
        os.remove(title + '.mp4')
        if (os.path.getsize(title + '.mp3') > 7900000):
            os.remove(title + '.mp3')
            return jsonify('h')
        return jsonify(f'../caller-8413-data-server/{title}.mp3')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database connection failure")
    else:
        print('Something went wrong:', err)