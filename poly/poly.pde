float x;
float y;
 
int bounceCount;

void setup() {
  size(640, 360);  // Size should be the first statement
  noLoop();
  
  x = width * 0.5;
  y = height * 0.5;
  
  bounceCount = 1;
 
}

float r = 0;
float g = 127;
float b = 255;

void draw() { 
  float colorVal = 255*(y/height);
  //background(255-colorVal, 255-colorVal, 255-colorVal);
  stroke(colorVal, colorVal, colorVal);
  drawHoriLine();
  drawVertLine();

}

void drawHoriLine() {
  stroke(255-x/width*r,255-x/width*g,255-x/width*b);
  line(0, y, width, y);
  stroke(x/width*r,x/width*g,x/width*b);
  line(0, y, width, height-y);
  y = y - 1; 
  if (y < 0) { 
    y = height;
    updateRGB();
    bounceCount++;
    if(bounceCount%7 == 0) {
      background(r,g,b);
    }
  } 
}

void drawVertLine() {
  stroke(x/width*r,x/width*g,x/width*b);
  line(x, 0, x, width);
  stroke(255-x/width*r,255-x/width*g,255-x/width*b);
  line(x, 0, width-x, width);
    x = x + 1; 
  if (x > width) { 
    x = 0;
    updateRGB();
    bounceCount++;
    if(bounceCount%7 == 0) {
      background(r,g,b);
    }
  } 
}

boolean shouldLoop = false;
void mousePressed() {
  shouldLoop = !shouldLoop;
  if(shouldLoop) {
    loop();
  } else {
    noLoop();
  }
}

void updateRGB() {
  r = (r+random(100))%255;
  g = (g+random(100))%255;
  b = (b+random(100))%255;
  println("r:" + r + ", g:" + g + ", b:" + b);
}
