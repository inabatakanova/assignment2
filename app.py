from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
 
app = Flask(__name__)

app.secret_key = "cairocoders-ednalan"
DB_HOST = "localhost"
DB_NAME = "assignment_2"
DB_USER = "postgres"
DB_PASS = "Inabatqueen16"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://pvpygtzphxggsx:0e1a5e46375e700d5d90aa1274e8215680750a692be37fac0eb2113e23e896bd@ec2-52-3-200-138.compute-1.amazonaws.com:5432/d44818ajt6qune"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
#disease_type
@app.route('/')
#disease_type
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    dt = "SELECT * FROM disease_type"
    cur.execute(dt)
    list_disease_types= cur.fetchall()

    c = "SELECT * FROM country"
    cur.execute(c)
    list_countries = cur.fetchall()

    d = "SELECT * FROM disease"
    cur.execute(d)
    list_disease = cur.fetchall()


    dis = "SELECT * FROM discover"
    cur.execute(dis)
    list_discover = cur.fetchall()

    users= "SELECT * FROM users"
    cur.execute(users)
    list_users = cur.fetchall()

    ps= "SELECT * FROM public_servant"
    cur.execute(ps)
    list_ps = cur.fetchall()


    doctor= "SELECT * FROM doctor"
    cur.execute(doctor)
    list_doctor = cur.fetchall()

    spec= "SELECT * FROM specialize"
    cur.execute(spec)
    list_spec = cur.fetchall()

    record= "SELECT * FROM record"
    cur.execute(record)
    list_record = cur.fetchall()

    
    return render_template('index.html', list_disease_types = list_disease_types, 
    list_countries=list_countries, 
    list_disease=list_disease,
    list_discover=list_discover,
    list_users=list_users,
    list_ps=list_ps,
    list_doctor=list_doctor,
    list_spec=list_spec,
    list_record=list_record)


 
@app.route('/add_disease_type', methods=['POST'])
def add_disease_type():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        id = request.form['id']
        description = request.form['description']
        #email = request.form['email']
        cur.execute("INSERT INTO disease_type (id, description) VALUES (%s,%s)", (id, description))
        conn.commit()
        flash('Disease_Type Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_disease_type(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM disease_type WHERE id = %s', (id,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', disease_type = data[0])
 
@app.route('/update/<id>', methods=['POST'])
def update_disease_type(id):
    if request.method == 'POST':
        id = request.form['id']
        description = request.form['description']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE disease_type
            SET description = %s
            WHERE id = %s
        """, (description, id))
        flash('Disease_Type Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_disease_type(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM disease_type WHERE id = {0}'.format(id))
    conn.commit()
    flash('Disease_Type Removed Successfully')
    return redirect(url_for('Index'))
def delete_country(cname):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM country WHERE cname = {0}'.format(cname))
    conn.commit()
    flash('Country Removed Successfully')
    return redirect(url_for('Index'))


#country

@app.route('/add_country', methods=['POST'])
def add_country():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        cname = request.form['cname']
        population = request.form['population']
        #email = request.form['email']
        cur.execute("INSERT INTO country (cname, population) VALUES (%s,%s)", (cname, population))
        conn.commit()
        flash('Country Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<cname>', methods = ['POST', 'GET'])
def get_country(cname):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM country WHERE cname = %s', (cname,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_country.html', country = data[0])
 
@app.route('/update/<cname>', methods=['POST'])
def update_country(cname):
    if request.method == 'POST':
        cname = request.form['cname']
        population = request.form['population']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE country
            SET cname = %s,
                population = %s,
            WHERE cname = %s
        """, (cname, population))
        flash('Country Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/country/<string:cname>', methods = ['POST','GET'])
def delete_country(cname):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM country WHERE cname = {0}'.format(cname))
    conn.commit()
    flash('Country Removed Successfully')
    return redirect(url_for('Index'))



#disease

@app.route('/add_disease', methods=['POST'])
def add_disease():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        disease_code = request.form['disease_code']
        pathogen = request.form['pathogen']
        description = request.form['description']
       
        cur.execute("INSERT INTO disease (disease_code, pathogen, description) VALUES (%s,%s, %s)", (disease_code, pathogen, description))
        conn.commit()
        flash('Disease Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/disease/<disease_code>', methods = ['POST', 'GET'])
def get_disease(disease_code):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM disease WHERE disease_code = %s', (disease_code))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', disease = data[0])
 
@app.route('/update/<disease_code>', methods=['POST'])
def update_disease(disease_code):
    if request.method == 'POST':
        pathogen = request.form['pathogen']
        description = request.form['description']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE disease
            SET pathogen = %s,
                description = %s,
            WHERE disease_code = %s
        """, (pathogen, description, id))
        flash('Disease Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/disease_type/<string:disease_code>', methods = ['POST','GET'])
def delete_disease(disease_code):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM country WHERE disease_code = {0}'.format(disease_code))
    conn.commit()
    flash('Disease Removed Successfully')
    return redirect(url_for('Index'))


#discover

@app.route('/add_discover', methods=['POST'])
def add_discover():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        cname = request.form['cname']
        disease_code = request.form['disease_code']
        first_enc_date= request.form['first_enc_date']
        #email = request.form['email']
        cur.execute("INSERT INTO discover (cname, disease_code, first_enc_date) VALUES (%s,%s, %s)", (cname, disease_code, first_enc_date))
        conn.commit()
        flash('Discovery Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<cname>', methods = ['POST', 'GET'])
def get_discover(cname):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM discover WHERE cname = %s', (cname,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', discover = data[0])
 
@app.route('/update/discover/<cname>', methods=['POST'])
def update_discover(cname):
    if request.method == 'POST':
        cname = request.form['cname']
        disease_code = request.form['disease_code']
        first_enc_date= request.form['first_enc_date']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE discover
            SET disease_code = %s,
                first_enc_date = %s,
            WHERE cname = %s
        """, (cname, disease_code, first_enc_date))
        flash('Discover Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:cname>', methods = ['POST','GET'])
def delete_discover(cname):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM discover WHERE cname = {0}'.format(cname))
    conn.commit()
    flash('Discover Removed Successfully')
    return redirect(url_for('Index'))





#users

@app.route('/add_users', methods=['POST'])
def add_users():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        surname =request.form['surname']
        salary = request.form['salary']
        phone = request.form['phone']
        cname = request.form['cname']
        
        #email = request.form['email']
        cur.execute("INSERT INTO users (email, name, surname, salary, phone, cname) VALUES (%s,%s, %s, %s,%s, %s)", (email, name, surname, salary, phone, cname))
        conn.commit()
        flash('User Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<email>', methods = ['POST', 'GET'])
def get_user(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM users WHERE email = %s', (email,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', users = data[0])
 
@app.route('/update/<email>', methods=['POST'])
def update_users(cname):
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        surname =request.form['surname']
        salary = request.form['salary']
        phone = request.form['phone']
        cname = request.form['cname']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE users
            SET name = %s,
                surname = %s,
                salary = %s,
                phone = %s,
                cname = %s,
            WHERE email= %s
        """, (name, surname, salary, phone, cname, email))
        flash('Users Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:email>', methods = ['POST','GET'])
def delete_users(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM users WHERE email = {0}'.format(email))
    conn.commit()
    flash('Users Removed Successfully')
    return redirect(url_for('Index'))




#public_servant

@app.route('/add_public_servant', methods=['POST'])
def add_public_servant():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        department = request.form['department']
       
        cur.execute("INSERT INTO public_servant (email, department) VALUES (%s,%s)", (email, department))
        conn.commit()
        flash('Public servant Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<email>', methods = ['POST', 'GET'])
def get_public_servant(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM public_servant WHERE email = %s', (email,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', public_servant = data[0])
 
@app.route('/update/public_servant/<email>', methods=['POST'])
def update_public_servant(email):
    if request.method == 'POST':
        email = request.form['email']
        department = request.form['department']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE public_servant
            SET department = %s
            WHERE email = %s
        """, (department, email))
        flash('Public Servant Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:email>', methods = ['POST','GET'])
def delete_public_servant(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM public_servant WHERE email = {0}'.format(email))
    conn.commit()
    flash('Public servant Removed Successfully')
    return redirect(url_for('Index'))
def delete_public_servant(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM public_servant WHERE email = {0}'.format(email))
    conn.commit()
    flash('Public servant Removed Successfully')
    return redirect(url_for('Index'))


#doctor

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        degree = request.form['degree']
       
        cur.execute("INSERT INTO doctor (email, degree) VALUES (%s,%s)", (email, degree))
        conn.commit()
        flash('Doctor Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<email>', methods = ['POST', 'GET'])
def get_doctor(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM doctor WHERE email = %s', (email,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', doctor = data[0])
 
@app.route('/update/doctor/<email>', methods=['POST'])
def update_doctor(email):
    if request.method == 'POST':
        email = request.form['email']
        degree = request.form['degree']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE doctor
            SET degree = %s
            WHERE email = %s
        """, (degree, email))
        flash('Doctor Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:email>', methods = ['POST','GET'])
def delete_doctor(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM doctor WHERE email = {0}'.format(email))
    conn.commit()
    flash('Doctor Removed Successfully')
    return redirect(url_for('Index'))




#specialize

@app.route('/add_specialize', methods=['POST'])
def add_specialize():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
       
        cur.execute("INSERT INTO specialize (id, email) VALUES (%s,%s)", (id, email))
        conn.commit()
        flash('Specialization Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<email>', methods = ['POST', 'GET'])
def get_specialization(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM specialize WHERE email = %s', (email,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_specialize.html', specialize = data[0])
 
@app.route('/update/<email>', methods=['POST'])
def update_specialize(email):
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE specialize
            SET id = %s
            WHERE email = %s
        """, (id, email))
        flash('Specialize Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:email>', methods = ['POST','GET'])
def delete_specialize(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM specialize WHERE email = {0}'.format(email))
    conn.commit()
    flash('Specialize Removed Successfully')
    return redirect(url_for('Index'))



#record

@app.route('/add_record', methods=['POST'])
def add_record():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        email = request.form['email']
        cname = request.form['cname']
        disease_code =request.form['disease_code']
        total_deaths =request.form['total_deaths']
        total_patients =request.form['total_patients']
       
        cur.execute("INSERT INTO record (email, cname, disease_code, total_deaths, total_patients) VALUES (%s,%s, %s,%s,%s)", (email, cname, disease_code, total_deaths, total_patients))
        conn.commit()
        flash('Record Added successfully')
        return redirect(url_for('Index'))
 
@app.route('/edit/<email>', methods = ['POST', 'GET'])
def get_record(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM record WHERE email = %s', (email,))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', record = data[0])
 
@app.route('/update/<email>', methods=['POST'])
def update_record(email):
    if request.method == 'POST':
        email = request.form['email']
        cname = request.form['cname']
        disease_code =request.form['disease_code']
        total_deaths =request.form['total_deaths']
        total_patients =request.form['total_patients']
        
         
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE record
            SET cname = %s,
            disease_code = %s,
            total_deaths = %s,
            total_patients = %s
            WHERE email = %s
        """, (cname, disease_code, total_deaths, total_patients, email))
        flash('Record Updated Successfully')
        conn.commit()
        return redirect(url_for('Index'))
 
@app.route('/delete/<string:email>', methods = ['POST','GET'])
def delete_record(email):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('DELETE FROM record WHERE email = {0}'.format(email))
    conn.commit()
    flash('Record Removed Successfully')
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)

#</string:id></id>

