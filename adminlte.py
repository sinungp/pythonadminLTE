from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='pos'
mysql=MySQL(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/masterbarang')
def masterbarang():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM masterbarang")
    barang=cur.fetchall()
    cur.close()
    return render_template('masterbarang.html', menu='master', submenu='barang', data=barang)

@app.route('/formmasterbarang')
def formmasterbarang():
    return render_template('formmasterbarang.html', menu='master', submenu='barang')

@app.route('/simpanformmasterbarang',methods=["POST"])
def simpanformmasterbarang():
    nama=request.form['nama']
    harga=request.form['harga']
    satuan=request.form['satuan']
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO masterbarang(nama,harga,satuan) VALUES(%s,%s,%s)",(nama,harga,satuan))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterbarang'))

@app.route("/mastersupplier")
def mastersupplier():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM mastersupplier")
    supplier=cur.fetchall()
    cur.close()
    return render_template('mastersupplier.html', menu='master', submenu='supplier', data=supplier)

@app.route('/formmastersupplier')
def formmastersupplier():
    return render_template('formmastersupplier.html', menu='master', submenu='supplier')

@app.route('/simpanformmastersupplier',methods=["POST"])
def simpanformmastersupplier():
    nama=request.form['nama']
    alamat=request.form['alamat']
    kota=request.form['kota']
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO mastersupplier(nama,alamat,kota) VALUES(%s,%s,%s)",(nama,alamat,kota))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('mastersupplier'))

@app.route("/masterpelanggan")
def masterpelanggan():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM masterpelanggan")
    pelanggan=cur.fetchall()
    cur.close()
    return render_template('masterpelanggan.html', menu='master', submenu='pelanggan', data=pelanggan)

@app.route('/formmasterpelanggan')
def formmasterpelanggan():
    return render_template('formmasterpelanggan.html', menu='master', submenu='pelanggan')

@app.route('/simpanformmasterpelanggan',methods=["POST"])
def simpanformmasterpelanggan():
    nama=request.form['nama']
    alamat=request.form['alamat']
    kota=request.form['kota']
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO masterpelanggan(nama,alamat,kota) VALUES(%s,%s,%s)",(nama,alamat,kota))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('masterpelanggan'))

@app.route("/formpembelian")
def formpembelian():
    return render_template('formpembelian.html', menu='pembelian', submenu='formpembelian')

@app.route("/datapembelian")
def datapembelian():
    return render_template('datapembelian.html', menu='pembelian', submenu='datapembelian')

@app.route("/formpenjualan")
def formpenjualan():
    return render_template('formpenjualan.html', menu='penjualan', submenu='formpenjualan')

@app.route("/datapenjualan")
def datapenjualan():
    return render_template('datapenjualan.html', menu='penjualan', submenu='datapenjualan')    


if __name__ == "__main__":
    app.run(debug=True)