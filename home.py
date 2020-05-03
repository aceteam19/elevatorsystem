#!C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python.exe

import cgi

#header 
print("Content-Type: text/html \n\n\n")


#main page 
print("Welcome ACE Team 19")


print("""
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>

<script>
$(function(){
    $("#DivContent").load("dashboard.html");
});
</script>

<div id="DivContent"></div>

""")
