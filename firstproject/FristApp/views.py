from django.shortcuts import render
from django.http  import HttpResponse;
# Create your views here.
def display(request):
    #ss---->multi-line-str with html-data/code
    print("welcome/url is request &display() is executed")
    ss = '''
            <center>
                <h2 style="color:Blue;">
                Hello User,welcome to Django Frist-Project
                Frist-App
                </h2>
                <hr />
                </center>
         ''';
    return HttpResponse(ss); #s1=Student(1001,"sai",6.2)
    
    
def show(request):
    ss='''
    <!--
 html webpage to display "welcome-message" with different Headings
 -->
<html>
<head>
<title>welcome-page </title>
<style>
h1{
color:blue;
}
h2{
color:green;
}
h3{
color:green;
}
h4{
color:pink;
}
h5{
color:red;
}
h6{
color:black;
}
h1,h2,h3{
 background-color:yellow;
 border:2px solid rgb(123,124,125);
 }
 h4,h5,h6{
 background-color:blue;
 border:2px solid rgb(125,126,127);
 }

</style>
</head>
<body>
<center>

<h1>welcome to django html page</h1>
<hr color="brown" width="95%">
<h2> welcome to django html page</h2>
<hr color ="brown" width="85%">
<h3>welcome to django html page</h3>
<hr color="brown" width="75%">
<h4>welcome to django html page</h4>
<hr color="brown" width="65%">
<h5>welcome to django html page</h5>
<hr color="brown" width="55%">
<h6>welcome to django html page</h6>
<hr color="brown" width="45%">


<center>
</body>
</html>
    ''';
    return HttpResponse(ss);
    
    
    
    
def hello(request):
    ss='''
    <html>
<head>
<title>hello webapage</title>
<style>
h1{
color:yellow;
width:90%;
border:2px solid rgb(123,124,125);
}

h2{
color:green;
width:80%;
border:2px solid rgb(123,124,125);
}

h3{
color:blue;
width:70%;
border:2px solid rgb(123,124,125);
}

</style>
<body>
<center>
<h1>hello user</h1>
<hr color:"brown" width="80%"/>
<h2>welcome to django</h2>
<hr color:"brown" width="60%"/>
<h3>have a nice day</h3>
<hr color:"brown" width="40%"/>
</center>
</body>
</html>
    ''';
    return HttpResponse(ss);
    
    
    
    
    
#single-view & multiple-urls
def demo(request):
    print("multiple-Request-URLs same response");
    htmldata='''<center>
    <h1>welcome demo user!!!</h1>
    <h2> This is same-output for diff-mulitple-Requests-URLs</h2><hr/>
    <h3>have a  great day...</h3>
    </center>''';
    return HttpResponse(htmldata);
#default-url-request-views-func
def homepage(request):
    htmldata='''<center>
    <h1>welcome to DEFAULT Home-page!!!</h1><hr/>
    <h2>your Request page is Not-Found...</h2><hr/>
    <h3>piz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);
    
        