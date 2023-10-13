def Blink():
    scene.set_background_image(assets.image("""
        Eyes
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Blink1
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Blink2
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes
    """))
def LookLeft():
    scene.set_background_image(assets.image("""
        Eyes4
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes3
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes2
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes
    """))
def LookRight():
    scene.set_background_image(assets.image("""
        Eyes
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes2
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes3
    """))
    pause(100)
    scene.set_background_image(assets.image("""
        Eyes4
    """))

def on_forever():
    LookRight()
    pause(1000)
    LookLeft()
    pause(1000)
    Blink()
    pause(1000)
forever(on_forever)
