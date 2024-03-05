from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
import mysql.connector


# FUNCTION DECLARATIONS

def add_data():
    if t1 == "" or t2 == "" or t3 == "" or t4 == "" or t5 == "":
        msg.showerror("Error", "All fields are required")
    else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='Ke200207@', database='Customer')
            my_cursor = conn.cursor()
            my_cursor.execute('insert into customer values(%s,%s,%s,%s,%s)',
                              (t1.get(), t2.get(), t3.get(), t4.get(), t5.get()))
            conn.commit()
            fetch_data()
            conn.close()
            msg.showinfo('Success', 'Customer Data has been Added', parent=root)
        except Exception as e:
            msg.showerror('Error', f"Due To:{str(e)}", parent=root)


def fetch_data():
    conn = mysql.connector.connect(host='localhost', username='root', password='Ke200207@', database='Customer')
    my_cursor = conn.cursor()
    my_cursor.execute('select * from customer')
    data = my_cursor.fetchall()
    if len(data) != 0:
        customer_table.delete(*customer_table.get_children())
        for i in data:
            customer_table.insert('', END, values=i)
        conn.commit()
    conn.close()


def get_cursor(event=''):
    cursor_row = customer_table.focus()
    content = customer_table.item(cursor_row)
    data = content['values']

    t1.set(data[0])
    t2.set(data[1])
    t3.set(data[2])
    t4.set(data[3])
    t5.set(data[4])


def update_data():
    if t1 == "" or t2 == "" or t3 == "" or t4 == "" or t5 == "":
        msg.showerror("Error", "All fields are required")
    else:
        try:
            update = msg.askyesno('Update', 'Are you update this customer data')
            if update > 0:
                conn = mysql.connector.connect(host='localhost', username='root', password='Ke200207@',
                                               database='Customer')
                my_cursor = conn.cursor()
                my_cursor.execute(
                    'update customer set Customer_Name=%s,Phone_No=%s,Problem=%s,Gadget=%s where Customer_ID=%s',
                    (t2.get(), t3.get(), t4.get(), t5.get(), t1.get()))
            else:
                if not update:
                    return
            conn.commit()
            fetch_data()
            conn.close()
            msg.showinfo('Success', 'Customer Successfully updated', parent=root)

        except Exception as e:
            msg.showerror('Error', f'Due To:{str(e)}', parent=root)


def delete_data():
    if t1.get() == '':
        msg.showerror('Error', 'All fields are required')
    else:
        try:
            Delete = msg.askyesno('Delete', 'Are you sure delete this customer', parent=root)
            if Delete > 0:
                conn = mysql.connector.connect(host='localhost', username='root', password='Ke200207@',
                                               database='Customer')
                my_cursor = conn.cursor()
                sql = 'delete from customer where Customer_ID=%s'
                value = (t1.get(),)
                my_cursor.execute(sql, value)
            else:
                if not Delete:
                    return
            conn.commit()
            fetch_data()
            conn.close()
            msg.showinfo('Delete', 'Customer Successfully Deleted', parent=root)
        except Exception as e:
            msg.showerror('Error', f'Due To:{str(e)}', parent=root)


def reset_data():
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t1.set("")


# search
def search_data():
    if q.get() == '':
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='Ke200207@',
                                           database='Customer')
            my_cursor = conn.cursor()
            my_cursor.execute("select *from customer")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                customer_table.delete(*customer_table.get_children())
                for i in rows:
                    customer_table.insert("", END, values=i)
            conn.commit()
            conn.close()
        except Exception as e:
            msg.showerror('Error', f'Due To:{str(e)}', parent=root)
    else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='Ke200207@',
                                           database='Customer')
            my_cursor = conn.cursor()
            my_cursor.execute("select *from customer where Customer_Name LIKE '%" + str(q.get()) + "%'")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                customer_table.delete(*customer_table.get_children())
                for i in rows:
                    customer_table.insert("", END, values=i)
            conn.commit()
            conn.close()
        except Exception as e:
            msg.showerror('Error', f'Due To:{str(e)}', parent=root)


root = Tk()
root.title("Customer Care")
root.geometry("800x500")
root.resizable(False, False)
lbl_title = Label(root, text="CUSTOMER CARE", font=("Arial", 37, "bold"), fg="White")
lbl_title.place(x=0, y=0, width=800, height=50)

wrapper1 = LabelFrame(root, text="Customer Data")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Customer Information")
wrapper1.pack(fill=BOTH, expand=False, padx=20, pady=(60, 0))
wrapper2.pack(fill=BOTH, expand=False, padx=20, pady=(0, 10))
wrapper3.pack(fill=BOTH, expand=False, padx=20, pady=(0, 10))

# User Data Section
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()

opt = ["Mobile",
       "Laptop",
       "Tablet",
       "Desktop",
       "Other"]

t4.set("Gadgets")

l1 = Label(wrapper1, text="Customer ID", font="Helvetica 13")
l2 = Label(wrapper1, text="Customer Name", font="Helvetica 13")
l3 = Label(wrapper1, text="Phone No", font="Helvetica 13")
l4 = Label(wrapper1, text="Gadget", font="Helvetica 13")
l5 = Label(wrapper1, text="Problem", font="Helvetica 13")

l1.grid(row=0, column=0, padx=5, pady=5, sticky=W)
l2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
l3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
l4.grid(row=4, column=0, padx=5, pady=5, sticky=W)
l5.grid(row=3, column=0, padx=5, pady=5, sticky=W)

e1 = ttk.Entry(wrapper1, textvariable=t1, width=30)
e2 = ttk.Entry(wrapper1, textvariable=t2, width=30)
e3 = ttk.Entry(wrapper1, textvariable=t3, width=30)
e5 = ttk.Entry(wrapper1, textvariable=t5, width=30)

someStyle = ttk.Style()
someStyle.configure('my.TMenubutton', font='Helvetica')

e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)
e3.grid(row=2, column=1, padx=5, pady=5)
drop = ttk.OptionMenu(wrapper1, t4, "Mobile", *opt, style='my.TMenubutton')
drop.grid(row=4, column=1, padx=5, pady=5, ipadx=10, ipady=10, sticky="w")
e5.grid(row=3, column=1, padx=5, pady=5)

insert_btn = Button(wrapper1, text="Add Customer", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue",
                    fg="Blue", command=add_data)
update_btn = Button(wrapper1, text="Update Customer", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue",
                    fg="Blue", command=update_data)
delete_btn = Button(wrapper1, text="Delete Customer", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue",
                    fg="Blue", command=delete_data)
reset_btn = Button(wrapper1, text="Clear", font="times 12", borderwidth=3, relief=RAISED, bg="salmon", fg="Blue",
                   command=reset_data)

insert_btn.grid(row=0, column=2, padx=35, pady=3, ipadx=19, sticky='nsew')
update_btn.grid(row=1, column=2, padx=35, pady=3, ipadx=10, sticky='nsew')
delete_btn.grid(row=2, column=2, padx=35, pady=3, ipadx=13, sticky='nsew')
reset_btn.grid(row=3, column=2, padx=35, pady=3, ipadx=48, sticky='nsew')

# Search Section
q = StringVar()

l1 = Label(wrapper2, text="Search", font="Helvetica 15")
l1.pack(side=tk.LEFT, padx=10)

e1 = ttk.Entry(wrapper2, textvariable=q, width=30)
e1.pack(side=tk.LEFT, padx=10)

b1 = Button(wrapper2, text="Search", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="blue",
            command=search_data)
b2 = Button(wrapper2, text="Show All", font="times 12", borderwidth=3, relief=RAISED, bg="steel blue", fg="blue",
            command=search_data)
b1.pack(side=tk.LEFT, padx=10)
b2.pack(side=tk.LEFT, padx=10)

# TABLE
scroll_x = ttk.Scrollbar(wrapper3, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(wrapper3, orient=VERTICAL)

customer_table = ttk.Treeview(wrapper3, columns=(0, 1, 2, 3, 4), show="headings", height=6,
                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_y.pack(side=RIGHT, fill=Y)

scroll_x.config(command=customer_table.xview)
scroll_y.config(command=customer_table.yview)
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 13))

# Define the columns for your customer table
customer_table.column(0, width=10, anchor=CENTER)
customer_table.column(1, width=100, anchor=CENTER)
customer_table.column(2, width=50, anchor=CENTER)
customer_table.column(3, width=50, anchor=CENTER)
customer_table.column(4, width=150, anchor=CENTER)

# Define headings for each column in your customer table
customer_table.heading(0, text="ID")
customer_table.heading(1, text="Name")
customer_table.heading(2, text="Phone")
customer_table.heading(3, text="Gadget")
customer_table.heading(4, text="Problem")

# Now, pack the customer_table after configuring the scrollbars
customer_table.pack(fill=BOTH, expand=True, padx=(5, 5))
fetch_data()
customer_table.bind('<ButtonRelease>', get_cursor)

root.mainloop()
