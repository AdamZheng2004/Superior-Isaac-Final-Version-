screen gameTimeline():
    if Lightbox_image != "":
        $ lb_image = im.Scale(Lightbox_image + ".png", 1280, 720)
        imagebutton:
            idle lb_image
            hover lb_image
            xalign 0.5
            yalign 0.5
            focus_mask True
            action SetVariable("Lightbox_image", "")
    else:
        frame:
            xpos 250
            ypos 100
            background None
            side ("r"):
                area(-65, 100, 1280, 720)
                viewport id "timeline":
                    draggable True mousewheel True
                    vpgrid:
                        cols 3
                        spacing 20

                        if persistent.affection >= 10 and persistent.affection < 20:
                            for q in timeline1:
                                $ qimage = q + ".png"
                                $ lb_image = im.Scale(qimage, 320, 180)
                                imagebutton:
                                    idle lb_image
                                    hover lb_image
                                    action SetVariable("Lightbox_image", q) 
                                    activate_sound "audio/Noah/" + q + ".mp3"

                        if persistent.affection >= 20 and persistent.affection < 30:
                            for q in timeline2:
                                $ qimage = q + ".png"
                                $ lb_image = im.Scale(qimage, 320, 180)
                                imagebutton:
                                    idle lb_image
                                    hover lb_image
                                    action SetVariable("Lightbox_image", q)
                                    activate_sound "audio/Noah/" + q + ".mp3"

                        if persistent.affection >= 30 and persistent.affection < 40:
                            for q in timeline3:
                                $ qimage = q + ".png"
                                $ lb_image = im.Scale(qimage, 320, 180)
                                imagebutton:
                                    idle lb_image
                                    hover lb_image
                                    action SetVariable("Lightbox_image", q)
                                    activate_sound "audio/Noah/" + q + ".mp3"

                        if persistent.affection >= 40 and persistent.affection < 50:
                            for q in timeline4:
                                $ qimage = q + ".png"
                                $ lb_image = im.Scale(qimage, 320, 180)
                                imagebutton:
                                    idle lb_image
                                    hover lb_image
                                    action SetVariable("Lightbox_image", q)
                                    activate_sound "audio/Noah/" + q + ".mp3"

                        if persistent.affection >= 50 and persistent.affection < 60:
                            for q in timeline5:
                                $ qimage = q + ".png"
                                $ lb_image = im.Scale(qimage, 320, 180)
                                imagebutton:
                                    idle lb_image
                                    hover lb_image
                                    action SetVariable("Lightbox_image", q)
                                    activate_sound "audio/Noah/" + q + ".mp3"

                        if persistent.affection >= 60:
                            for q in timeline6:
                                $ qimage = q + ".png"
                                $ lb_image = im.Scale(qimage, 320, 180)
                                imagebutton:
                                    idle lb_image
                                    hover lb_image
                                    action SetVariable("Lightbox_image", q)
                                    activate_sound "audio/Noah/" + q + ".mp3"
