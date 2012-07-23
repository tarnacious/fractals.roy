set_fillStyle = function(context, style) {
    context.fillStyle = style
}

to_rgb = function(r, g, b) {
    return "rgb(" + Math.round(r).toString() + "," + Math.round(g).toString() + "," + Math.round(b).toString() + ")"
}

window.onload = function() 
{
    start();
}
