import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table():
	c.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INTEGER PRIMARY KEY,
    ticket_number TEXT,
    ticket_creation_date TEXT,
    client_name TEXT,
    ticket_assigned TEXT,
    ticket_description TEXT,
    ticket_deadline TEXT,
    ticket_status TEXT
);
''')


def add_data(ticket_number,ticket_creation_date,client_name,ticket_assigned,ticket_Discription,ticket_deadline,ticket_satatus):
	c.execute('''
        INSERT INTO tickets (ticket_number,ticket_creation_date,client_name,ticket_assigned,ticket_description,ticket_deadline,ticket_status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ticket_number,ticket_creation_date,client_name,ticket_assigned,ticket_Discription,ticket_deadline,ticket_satatus))

	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM tickets')
	data = c.fetchall()
	return data

def view_all_task_names():
	c.execute('SELECT DISTINCT task FROM tickets')
	data = c.fetchall()
	return data

def get_task(task):
	c.execute('SELECT * FROM tickets WHERE task="{}"'.format(task))
	data = c.fetchall()
	return data

def get_task_by_status(task_status):
	c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
	data = c.fetchall()


def edit_task_data(new_task,new_task_status,new_task_date,task,task_status,task_due_date):
	c.execute("UPDATE taskstable SET task =?,task_status=?,task_due_date=? WHERE task=? and task_status=? and task_due_date=? ",(new_task,new_task_status,new_task_date,task,task_status,task_due_date))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(task):
	c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
	conn.commit()