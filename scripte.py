import mysql.connector
while True:
    a = int(input("what you wanna do? \
                    \n 1. Add a New Product.\
                    \n 2. View All Products.\
                    \n 3. Update Prod Details.\
                    \n 4. Delete a Product.\
                    \n 5. sort \
                    \n 6. search\n"))
    mydb = mysql.connector.connect(
                    host="localhost",
                    user="user",
                    password="password",
                    database="mystore"
                )
    cursor = mydb.cursor()
    match a:
        case 1 :
            b= int(input("product id:"))
            c= str(input("product name:"))
            d= int(input("product cat id :"))
            e= int(input("product qty:"))
            f= int(input("product price:"))
            try:
                
                if mydb.is_connected():
                    cursor.execute("CREATE DATABASE IF NOT EXISTS store")
                    print("store created successfully!")
                    line="INSERT INTO mystore.product(id,prod_name,cat_id,qty,PRICE)VALUES(%s,%s,%s,%s,%s);"
                    val=(b,c,d,e,f)
                    cursor.execute(line,val)
                    mydb.commit()
                    print("product added!")

                    
            except mysql.connector.Error as e:

                print("Error: failed to cennect to data base",{e})
        case 2 :
            print("Here's a liste of all products:")
            try:
                if mydb.is_connected():
                    cursor.execute("SELECT * FROM mystore.product")
                    val=cursor.fetchall()
                    for i in val:
                        print(f"Id: {i[0]} | name: {i[1]} | category: {i[2]} | qty: {i[3]} units| price: {i[4]}$ ")
                        if i[3] <5: print(i[1],"is running low!!")
            except mysql.connector.Error as e:

                print("Error: failed to cennect to data base",{e})

        case 3 :
            prod= int(input("enter ID of product to update: "))
            table=["prod_name","cat_id","qty","PRICE"]
            b = int(input("what do you wanna update:\
                            \n 1. name\
                            \n 2. category\
                            \n 3. qty\
                            \n 4. price\n"))
            c = input("new value:")
            line="UPDATE mystore.product SET " + str(table[b-1]) + " = " + str(c) +" WHERE id =" + str(prod)
            cursor.execute(line)
            mydb.commit()
            print("info updated")

        case 4 :
            prod= int(input("enter ID of product to delete: "))
            line = "DELETE FROM mystore.product WHERE id =" +str(prod)
            cursor.execute(line)
            mydb.commit()
            print("product deleted")

        case 5:
            a=int(input("how do you wanna sort:\
                    \n 1. by qty\
                    \n 2. by price\n"))
            b=["qty","PRICE"]
            line="SELECT * FROM mystore.product ORDER BY " + str(b[a-1]) + " ASC"
            cursor.execute(line)
            val=cursor.fetchall()
            for i in val:
                print(f"Id: {i[0]} | name: {i[1]} | category: {i[2]} | qty: {i[3]} units| price: {i[4]}$ ")
        case 6:
            a= int(input("search by :\
                        \n 1. name\
                        \n 2. category\n"))
            b=str(input("Enter term to research: "))
            c=["prod_name","cat_id"]
            line="SELECT * FROM mystore.product WHERE " + str(c[a-1]) + " LIKE " + "\'%"+str(b)+"%\'"
            cursor.execute(line)
            values=cursor.fetchall()
            for i in values:
                print(f"Id: {i[0]} | name: {i[1]} | category: {i[2]} | qty: {i[3]} units| price: {i[4]}$ ")
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("connection closed")


