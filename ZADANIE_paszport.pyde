add_library('pdf')

def setup():
    id_photo = loadImage("paszport.jpg")
    size(413,531)
    global id_photo
    beginRecord (PDF, "id_photo_z_record.pdf")
def draw():
    global id_photo
    image(id_photo, 0, 0,)
    endRecord()
    s= createShape()
    s.beginShape()
    s.fill(0)
    s.noStroke()
    s.vertex(90, 203)
    s.vertex(165, 215)
    s.vertex(163, 230)
    s.vertex(94, 234)    
    s.endShape(CLOSE)
    shape(s,0,0)
    print (mouseX, mouseY)
    s= createShape()
    s.beginShape()
    s.fill(0)
    s.noStroke()
    s.vertex(300, 201)
    s.vertex(305, 223)
    s.vertex(224, 228)
    s.vertex(225, 211)    
    s.endShape(CLOSE)
    shape(s,0,0)
    
    if keyPressed:
        if key == 's':
            s= createShape()
            s.beginShape()
            s.fill(0)
            s.noStroke()
            s.vertex(134, 388)
            s.vertex(257, 387)
            s.vertex(241, 344)
            s.vertex(151, 342)    
            s.endShape(CLOSE)
            shape(s,0,0)
    
            s= createShape()
            s.beginShape()
            s.fill(255,78,135)
            s.noStroke()
            s.vertex(210, 367)
            s.vertex(174, 367)
            s.vertex(164, 385)
            s.vertex(220, 385)    
            s.endShape(CLOSE)
            shape(s,0,0)
    
            s= createShape()
            s.beginShape()
            s.fill(255)
            s.noStroke()
            s.vertex(143, 360)
            s.vertex(245, 360)
            s.vertex(241, 344)
            s.vertex(151, 342)    
            s.endShape(CLOSE)
            shape(s,0,0)
    
            loop()
        
    

    
