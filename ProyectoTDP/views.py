from django.http import HttpResponse

def firstPage(request):
    document ="""
    <html>
        <head>
            <title>Proyect TDP</title>
        </head>
        <body>  
            <h1><center>A proxemics toolkit for F-formation patterns detection</center></h1>
            <h3>Insert your Video to process (*.mp4)</h3>
            <form action=/secondPage/ method="GET">
                <input type="file" name="upload" accept="video/mp4" />
                </br><input type="submit" value="Start">
            </form>
        </body>
    </html>"""
    return HttpResponse(document)

def secondPage(request):
    document ="""
    <html>
        <head>
            <title>Proyect TDP</title>
            <meta http-equiv="refresh" content="5;URL=/thirdPage/">
        </head>
        <body>  
                        <h1><center>A proxemics toolkit for F-formation patterns detection</center></h1>
            <h3><font size="6" color="blue">processing...</font></h3>
        </body>
    </html>"""
    return HttpResponse(document)
    
def thirdPage(request):
    document ="""
    <html>
        <head>
            <title>Proyect TDP</title>
        </head>
        <body>  
            <h1><center>A proxemics toolkit for F-formation patterns detection</center></h1>
            <h3><font size="6" color="blue">Your video was processed correctly</font></h3>
            <video width="640" height="480" controls>
                <source src="C:/Users/Hans Soto/Desktop/Movie.mp4" type="video/mp4"/>
                <source src="C:/Users/Hans Soto/Desktop/Movie.webm" type="video/webm"/>
                <source src="C:/Users/Hans Soto/Desktop/Movie.ogg" type="video/ogg"/>
                <font size="6" color="red">Your browser does not support the video tag.</font>
            </video>
        </body>
    </html>"""
    return HttpResponse(document)
