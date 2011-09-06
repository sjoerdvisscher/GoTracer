function Preview(cvs)
{
  this.canvas = cvs;
  this.ctx = this.canvas.getContext('2d');
  this.backgroundImage = new Image();
  this.backgroundImage.src = "/images/blank_board.png";
}

Preview.prototype = {
  update: function(goTracer) {
    this.clear();
    this.draw(goTracer.blackSet.points, "black");
    this.draw(goTracer.whiteSet.points, "white");
  },
  clear: function()
  {
    this.ctx.clearRect(0,0,this.canvas.width, this.canvas.height);
  },
  draw: function(points, color)
  {
    this.ctx.fillStyle = color == "white" ? "rgb(255,255,255)" : "rgb(0,0,0)";
    for ( var p=0 ; p<points.length ; p++ )
    {
      this.drawStone(points[p]);
    }
  },
  
  // point here is anything with a .x and a .y, like a PointSet
  drawStone: function(point)
  {
    var x = 10 + 10.46*(point.coord[1].charCodeAt(0) - 97) -4;
    var y = 10 + 10.46*(point.coord[2].charCodeAt(0) - 97) -4;
    var r = 5;
    
    this.ctx.beginPath();
    this.ctx.arc(x, y, r, 0, 2*Math.PI, 0)
    this.ctx.fill();
    this.ctx.closePath();
  }
};

