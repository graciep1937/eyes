function Blink () {
    scene.setBackgroundImage(assets.image`Eyes`)
    pause(100)
    scene.setBackgroundImage(assets.image`Blink1`)
    pause(100)
    scene.setBackgroundImage(assets.image`Blink2`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes`)
}
function LookLeft () {
    scene.setBackgroundImage(assets.image`Eyes4`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes3`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes2`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes`)
}
function LookRight () {
    scene.setBackgroundImage(assets.image`Eyes`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes2`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes3`)
    pause(100)
    scene.setBackgroundImage(assets.image`Eyes4`)
}
forever(function () {
    LookRight()
    pause(1000)
    LookLeft()
    pause(1000)
    Blink()
    pause(1000)
})
