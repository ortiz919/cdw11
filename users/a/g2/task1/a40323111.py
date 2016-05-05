# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
a40323111 = Blueprint('a40323111', __name__, url_prefix='/a40323111', template_folder='templates')

@a40323111.route('/task1')
def task1():
    #return "ag100 task1"
    return render_template('task1.html', var1="來自 ag100 的 task1 變數")

# 展示傳回 Brython 程式
@a40323111.route('/task2')
def task2():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 700, 700) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0,0)
    
    basic2 = cmbr.dup()
    basic2.rotate(165)
    basic2.translate(0,0)
    
    basic3 = cmbr.dup()
    basic3.rotate(165)
    basic3.translate(20*math.cos(75*deg), 20*math.sin(75*deg))
    
    basic4 = cmbr.dup()
    basic4.rotate(165)
    basic4.translate(40*math.cos(75*deg), 40*math.sin(75*deg))
    
    basic5 = cmbr.dup()
    basic5.rotate(90)
    basic5.translate(60*math.cos(75*deg), 60*math.sin(75*deg))
    
    basic6 = cmbr.dup()
    basic6.rotate(15)
    basic6.translate(60*math.cos(75*deg)+20, 60*math.sin(75*deg))
    
    basic7 = cmbr.dup()
    basic7.rotate(15)
    basic7.translate(40*math.cos(75*deg)+30.5, 40*math.sin(75*deg))
    
    basic8 = cmbr.dup()
    basic8.rotate(15)
    basic8.translate(20*math.cos(75*deg)+41, 40*math.sin(75*deg)-19)
    
    basic9 = cmbr.dup()
    basic9.rotate(0)
    basic9.translate(51.5, 0)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(20*math.cos(75*deg), 20*math.sin(75*deg))
    
    basic11 = cmbr.dup()
    basic11.rotate(90)
    basic11.translate(20*math.cos(75*deg)+21.2, 20*math.sin(75*deg))
    
    basic12 = cmbr.dup()
    basic12.rotate(0)
    basic12.translate(80,0)
    
    basic13 = cmbr.dup()
    basic13.rotate(165)
    basic13.translate(80,0)
    
    basic14 = cmbr.dup()
    basic14.rotate(165)
    basic14.translate(20*math.cos(75*deg)+80, 20*math.sin(75*deg))
    
    basic15 = cmbr.dup()
    basic15.rotate(165)
    basic15.translate(40*math.cos(75*deg)+80, 40*math.sin(75*deg))
    
    basic16 = cmbr.dup()
    basic16.rotate(90)
    basic16.translate(60*math.cos(75*deg)+80, 60*math.sin(75*deg))
    
    basic17 = cmbr.dup()
    basic17.rotate(15)
    basic17.translate(60*math.cos(75*deg)+100, 60*math.sin(75*deg))
    
    basic18 = cmbr.dup()
    basic18.rotate(15)
    basic18.translate(40*math.cos(75*deg)+110.5, 40*math.sin(75*deg))
    
    basic19 = cmbr.dup()
    basic19.rotate(15)
    basic19.translate(20*math.cos(75*deg)+121, 40*math.sin(75*deg)-19)
    
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(131.5, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(90)
    basic21.translate(20*math.cos(75*deg)+80, 20*math.sin(75*deg))
    
    basic22 = cmbr.dup()
    basic22.rotate(90)
    basic22.translate(20*math.cos(75*deg)+101.2, 20*math.sin(75*deg))
    
    basic23 = cmbr.dup()
    basic23.rotate(0)
    basic23.translate(160,0)
    
    basic24 = cmbr.dup()
    basic24.rotate(165)
    basic24.translate(160,0)
    
    basic25 = cmbr.dup()
    basic25.rotate(165)
    basic25.translate(20*math.cos(75*deg)+160, 20*math.sin(75*deg))
    
    basic26 = cmbr.dup()
    basic26.rotate(165)
    basic26.translate(40*math.cos(75*deg)+160, 40*math.sin(75*deg))
    
    basic27 = cmbr.dup()
    basic27.rotate(90)
    basic27.translate(60*math.cos(75*deg)+160, 60*math.sin(75*deg))
    
    basic28 = cmbr.dup()
    basic28.rotate(15)
    basic28.translate(60*math.cos(75*deg)+180, 60*math.sin(75*deg))
    
    basic29 = cmbr.dup()
    basic29.rotate(15)
    basic29.translate(40*math.cos(75*deg)+190.5, 40*math.sin(75*deg))
    
    basic30 = cmbr.dup()
    basic30.rotate(15)
    basic30.translate(20*math.cos(75*deg)+201, 40*math.sin(75*deg)-19)
    
    basic31 = cmbr.dup()
    basic31.rotate(0)
    basic31.translate(211.5, 0)
    
    basic32 = cmbr.dup()
    basic32.rotate(90)
    basic32.translate(20*math.cos(75*deg)+160, 20*math.sin(75*deg))
    
    basic33 = cmbr.dup()
    basic33.rotate(90)
    basic33.translate(20*math.cos(75*deg)+181.2, 20*math.sin(75*deg))
    
    basic34 = cmbr.dup()
    basic34.rotate(0)
    basic34.translate(240,0)
    
    basic35 = cmbr.dup()
    basic35.rotate(165)
    basic35.translate(240,0)
    
    basic36 = cmbr.dup()
    basic36.rotate(165)
    basic36.translate(20*math.cos(75*deg)+240, 20*math.sin(75*deg))
    
    basic37 = cmbr.dup()
    basic37.rotate(165)
    basic37.translate(40*math.cos(75*deg)+240, 40*math.sin(75*deg))
    
    basic38 = cmbr.dup()
    basic38.rotate(90)
    basic38.translate(60*math.cos(75*deg)+240, 60*math.sin(75*deg))
    
    basic39 = cmbr.dup()
    basic39.rotate(15)
    basic39.translate(60*math.cos(75*deg)+260, 60*math.sin(75*deg))
    
    basic40 = cmbr.dup()
    basic40.rotate(15)
    basic40.translate(40*math.cos(75*deg)+270.5, 40*math.sin(75*deg))
    
    basic41 = cmbr.dup()
    basic41.rotate(15)
    basic41.translate(20*math.cos(75*deg)+281, 40*math.sin(75*deg)-19)
    
    basic42 = cmbr.dup()
    basic42.rotate(0)
    basic42.translate(291.5, 0)
    
    basic43 = cmbr.dup()
    basic43.rotate(90)
    basic43.translate(20*math.cos(75*deg)+240, 20*math.sin(75*deg))
    
    basic44 = cmbr.dup()
    basic44.rotate(90)
    basic44.translate(20*math.cos(75*deg)+261.2, 20*math.sin(75*deg))
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)
    cmbr.appendPath(basic43)
    cmbr.appendPath(basic44)
   
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 2 倍
    cgo.render(cmbr, x, y, 1.2, rot)

O(0, 0, 0, 0, 0, "green", True, 4)
</script>
<!-- 以協同方式加上 ag100 的 task3 程式碼 -->
<script type="text/python" src="/ag100/task3"></script>
<!-- 以協同方式加上 bg99 的 task3 程式碼 -->
<script type="text/python" src="/bg99/task3"></script>
</body>
</html>
'''
    return outstring
    
# 展示傳回 Brython 程式
# 展示傳回 Brython 程式
@a40323111.route('/task3')
def task3():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 700, 700) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
   #B
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0,0)
    
    basic2 = cmbr.dup()
    basic2.rotate(180)
    basic2.translate(0,0)
    
    basic3 = cmbr.dup()
    basic3.rotate(180)
    basic3.translate(0, 20)
    
    basic4 = cmbr.dup()
    basic4.rotate(180)
    basic4.translate(0, 40)
    
    basic5 = cmbr.dup()
    basic5.rotate(90)
    basic5.translate(0, 60)
    
    basic6 = cmbr.dup()
    basic6.rotate(60)
    basic6.translate(20, 60)
    
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(20*math.sin(60*deg)+20, -20*math.cos(60*deg)+60)
    
    basic8 = cmbr.dup()
    basic8.rotate(90)
    basic8.translate(0, 20)
    
    basic9 = cmbr.dup()
    basic9.rotate(120)
    basic9.translate(20, 20)
    
    basic10 = cmbr.dup()
    basic10.rotate(60)
    basic10.translate(20,20)
    
    basic11 = cmbr.dup()
    basic11.rotate(90)
    basic11.translate(0,-20)
    
    basic41 = cmbr.dup()
    basic41.rotate(120)
    basic41.translate(20,-20)
    
    basic42 = cmbr.dup()
    basic42.rotate(180)
    basic42.translate(20+20*math.cos(30*deg),-20+20*math.sin(30*deg))
   
   #A
    basic12 = cmbr.dup()
    basic12.rotate(0)
    basic12.translate(80,0)
    
    basic13 = cmbr.dup()
    basic13.rotate(165)
    basic13.translate(80,0)
    
    basic14 = cmbr.dup()
    basic14.rotate(165)
    basic14.translate(20*math.cos(75*deg)+80, 20*math.sin(75*deg))
    
    basic15 = cmbr.dup()
    basic15.rotate(165)
    basic15.translate(40*math.cos(75*deg)+80, 40*math.sin(75*deg))
    
    basic16 = cmbr.dup()
    basic16.rotate(90)
    basic16.translate(60*math.cos(75*deg)+80, 60*math.sin(75*deg))
    
    basic17 = cmbr.dup()
    basic17.rotate(15)
    basic17.translate(60*math.cos(75*deg)+100, 60*math.sin(75*deg))
    
    basic18 = cmbr.dup()
    basic18.rotate(15)
    basic18.translate(40*math.cos(75*deg)+110.5, 40*math.sin(75*deg))
    
    basic19 = cmbr.dup()
    basic19.rotate(15)
    basic19.translate(20*math.cos(75*deg)+121, 40*math.sin(75*deg)-19)
    
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(131.5, 0)
    
    basic21 = cmbr.dup()
    basic21.rotate(90)
    basic21.translate(20*math.cos(75*deg)+80, 20*math.sin(75*deg))
    
    basic22 = cmbr.dup()
    basic22.rotate(90)
    basic22.translate(20*math.cos(75*deg)+101.2, 20*math.sin(75*deg))
    
    #D
    basic23 = cmbr.dup()
    basic23.rotate(0)
    basic23.translate(160,0)
    
    basic24 = cmbr.dup()
    basic24.rotate(180)
    basic24.translate(160,0)
    
    basic25 = cmbr.dup()
    basic25.rotate(180)
    basic25.translate(160, 20)
    
    basic26 = cmbr.dup()
    basic26.rotate(180)
    basic26.translate(160, 40)
    
    basic27 = cmbr.dup()
    basic27.rotate(90)
    basic27.translate(160, 60)
    
    basic28 = cmbr.dup()
    basic28.rotate(60)
    basic28.translate(180, 60)
    
    basic29 = cmbr.dup()
    basic29.rotate(30)
    basic29.translate(20*math.cos(30*deg)+180, 60-20*math.sin(30*deg))
   
    basic30 = cmbr.dup()
    basic30.rotate(90)
    basic30.translate(160, -20)
    
    basic31 = cmbr.dup()
    basic31.rotate(120)
    basic31.translate(180, -20)
    
    basic32 = cmbr.dup()
    basic32.rotate(150)
    basic32.translate(20*math.cos(30*deg)+180, -20+20*math.sin(30*deg))
    
    basic33 = cmbr.dup()
    basic33.rotate(0)
    basic33.translate(208, 31)
    
    #C
    basic34 = cmbr.dup()
    basic34.rotate(90)
    basic34.translate(270,-20)
    
    basic35 = cmbr.dup()
    basic35.rotate(-120)
    basic35.translate(270,-20)
    
    basic36 = cmbr.dup()
    basic36.rotate(-165)
    basic36.translate(-20*math.cos(30*deg)+270, -20+20*math.sin(30*deg))
    
    basic37 = cmbr.dup()
    basic37.rotate(180)
    basic37.translate(247, 12)
    
    basic38 = cmbr.dup()
    basic38.rotate(165)
    basic38.translate(247, 32)
    
    basic39 = cmbr.dup()
    basic39.rotate(120)
    basic39.translate(252,51)
    
    basic40 = cmbr.dup()
    basic40.rotate(90)
    basic40.translate(270, 61)
    
    
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)

   
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 2 倍
    cgo.render(cmbr, x, y, 1.2, rot)

O(0, 0, 0, 0, 0, "green", True, 4)
</script>
<!-- 以協同方式加上 ag100 的 task3 程式碼 -->
<script type="text/python" src="/ag100/task3"></script>
<!-- 以協同方式加上 bg99 的 task3 程式碼 -->
<script type="text/python" src="/bg99/task3"></script>
</body>
</html>
'''
    return outstring
    
# 展示傳回 Brython 程式
# 展示傳回 Brython 程式
@a40323111.route('/task4')
def task4():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-100, -300, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 1500, 0, 1500, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
   #B
    basic1 = cmbr.dup()
    basic1.rotate(0)
    basic1.translate(0,0)
    
    basic2 = cmbr.dup()
    basic2.rotate(180)
    basic2.translate(0,0)
    
    basic3 = cmbr.dup()
    basic3.rotate(180)
    basic3.translate(0, 20)
    
    basic4 = cmbr.dup()
    basic4.rotate(180)
    basic4.translate(0, 40)
    
    basic5 = cmbr.dup()
    basic5.rotate(90)
    basic5.translate(0, 60)
    
    basic6 = cmbr.dup()
    basic6.rotate(60)
    basic6.translate(20, 60)
    
    basic7 = cmbr.dup()
    basic7.rotate(0)
    basic7.translate(20*math.sin(60*deg)+20, -20*math.cos(60*deg)+60)
    
    basic8 = cmbr.dup()
    basic8.rotate(90)
    basic8.translate(0, 20)
    
    basic9 = cmbr.dup()
    basic9.rotate(120)
    basic9.translate(20, 20)
    
    basic10 = cmbr.dup()
    basic10.rotate(60)
    basic10.translate(20,20)
    
    basic11 = cmbr.dup()
    basic11.rotate(90)
    basic11.translate(0,-20)
    
    basic41 = cmbr.dup()
    basic41.rotate(120)
    basic41.translate(20,-20)
    
    basic42 = cmbr.dup()
    basic42.rotate(180)
    basic42.translate(20+20*math.cos(30*deg),-20+20*math.sin(30*deg))
   
   #A
    basic12 = cmbr.dup()
    basic12.rotate(0)
    basic12.translate(0,100)
    
    basic13 = cmbr.dup()
    basic13.rotate(165)
    basic13.translate(0,100)
    
    basic14 = cmbr.dup()
    basic14.rotate(165)
    basic14.translate(20*math.cos(75*deg), 100+20*math.sin(75*deg))
    
    basic15 = cmbr.dup()
    basic15.rotate(165)
    basic15.translate(40*math.cos(75*deg), 100+40*math.sin(75*deg))
    
    basic16 = cmbr.dup()
    basic16.rotate(90)
    basic16.translate(60*math.cos(75*deg), 100+60*math.sin(75*deg))
    
    basic17 = cmbr.dup()
    basic17.rotate(15)
    basic17.translate(60*math.cos(75*deg)+20, 100+60*math.sin(75*deg))
    
    basic18 = cmbr.dup()
    basic18.rotate(15)
    basic18.translate(40*math.cos(75*deg)+30.5, 100+40*math.sin(75*deg))
    
    basic19 = cmbr.dup()
    basic19.rotate(15)
    basic19.translate(20*math.cos(75*deg)+41, 81+40*math.sin(75*deg))
    
    basic20 = cmbr.dup()
    basic20.rotate(0)
    basic20.translate(51.5, 100)
    
    basic21 = cmbr.dup()
    basic21.rotate(90)
    basic21.translate(20*math.cos(75*deg), 100+20*math.sin(75*deg))
    
    basic22 = cmbr.dup()
    basic22.rotate(90)
    basic22.translate(20*math.cos(75*deg)+21.2, 100+20*math.sin(75*deg))
    
    #D
    basic23 = cmbr.dup()
    basic23.rotate(0)
    basic23.translate(0,-210)
    
    basic24 = cmbr.dup()
    basic24.rotate(180)
    basic24.translate(0,-210)
    
    basic25 = cmbr.dup()
    basic25.rotate(180)
    basic25.translate(0, -190)
    
    basic26 = cmbr.dup()
    basic26.rotate(180)
    basic26.translate(0, -170)
    
    basic27 = cmbr.dup()
    basic27.rotate(90)
    basic27.translate(0, -150)
    
    basic28 = cmbr.dup()
    basic28.rotate(60)
    basic28.translate(20, -150)
    
    basic29 = cmbr.dup()
    basic29.rotate(30)
    basic29.translate(20*math.cos(30*deg)+20, -150-20*math.sin(30*deg))
   
    basic30 = cmbr.dup()
    basic30.rotate(90)
    basic30.translate(0, -230)
    
    basic31 = cmbr.dup()
    basic31.rotate(120)
    basic31.translate(20, -230)
    
    basic32 = cmbr.dup()
    basic32.rotate(150)
    basic32.translate(20*math.cos(30*deg)+20, -230+20*math.sin(30*deg))
    
    basic33 = cmbr.dup()
    basic33.rotate(0)
    basic33.translate(48, -179)
    
    #C
    basic34 = cmbr.dup()
    basic34.rotate(90)
    basic34.translate(23,-121)
    
    basic35 = cmbr.dup()
    basic35.rotate(-120)
    basic35.translate(23,-121)
    
    basic36 = cmbr.dup()
    basic36.rotate(-165)
    basic36.translate(-20*math.cos(30*deg)+23, -121+20*math.sin(30*deg))
    
    basic37 = cmbr.dup()
    basic37.rotate(180)
    basic37.translate(0, -89)
    
    basic38 = cmbr.dup()
    basic38.rotate(165)
    basic38.translate(0, -70)
    
    basic39 = cmbr.dup()
    basic39.rotate(120)
    basic39.translate(6,-50)
    
    basic40 = cmbr.dup()
    basic40.rotate(90)
    basic40.translate(25, -40)
    
    
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    cmbr.appendPath(basic13)
    cmbr.appendPath(basic14)
    cmbr.appendPath(basic15)
    cmbr.appendPath(basic16)
    cmbr.appendPath(basic17)
    cmbr.appendPath(basic18)
    cmbr.appendPath(basic19)
    cmbr.appendPath(basic20)
    cmbr.appendPath(basic21)
    cmbr.appendPath(basic22)
    cmbr.appendPath(basic23)
    cmbr.appendPath(basic24)
    cmbr.appendPath(basic25)
    cmbr.appendPath(basic26)
    cmbr.appendPath(basic27)
    cmbr.appendPath(basic28)
    cmbr.appendPath(basic29)
    cmbr.appendPath(basic30)
    cmbr.appendPath(basic31)
    cmbr.appendPath(basic32)
    cmbr.appendPath(basic33)
    cmbr.appendPath(basic34)
    cmbr.appendPath(basic35)
    cmbr.appendPath(basic36)
    cmbr.appendPath(basic37)
    cmbr.appendPath(basic38)
    cmbr.appendPath(basic39)
    cmbr.appendPath(basic40)
    cmbr.appendPath(basic41)
    cmbr.appendPath(basic42)

   
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 2 倍
    cgo.render(cmbr, x, y, 1.2, rot)

O(0, 0, 0, 0, 0, "green", True, 4)
</script>
<!-- 以協同方式加上 ag100 的 task3 程式碼 -->
<script type="text/python" src="/ag100/task3"></script>
<!-- 以協同方式加上 bg99 的 task3 程式碼 -->
<script type="text/python" src="/bg99/task3"></script>
</body>
</html>
'''
    return outstring    
