#!C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python.exe

import cgi
import database_requests


if __name__ in "__main__":

    form = cgi.FieldStorage()

    #header 
    print("Content-Type: text/html \n\n\n")

    if form:

        print("""Form was submitted""")

        retrieved_parameter = form['parameter1'].value

        print("""
        <br>
        <br>
        Value is: %s 
        """ %str(retrieved_parameter))
    
    else:

        #main page 
        print("""Welcome ACE Team 19 <br>
              <br>""")

        #1. retrieve data
        #all_items = get_all_items()
        all_items = ['dummy variable']
        
        #2. place data in javascript variables
        print("""
        <script>
            var all_items = %s; 
        </script>
        """ %json.dumps(all_items))

        #3. display the html page (which includes vue)
        #demonstrating of displaying a page 
        print("""
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>

        <script>
        $(function(){
            $("#DivContent").load("dashboard.html");
        });
        </script>

        <div id="DivContent"></div>

        """)

