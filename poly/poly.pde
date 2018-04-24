float x;
float y;
 
int bounceCount;

void setup() {
  size(640, 640);  // Size should be the first statement
  
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
  stroke(x/width*r%g,x/width*g%b,x/width*b%r);
  line(0, y, width, height-y);
  y = y - 1; 
  if (y < 0) { 
    y = height;
    updateRGB();
    bounceCount++;
  } 
}

void drawVertLine() {
  stroke(x/width*r,x/width*g,x/width*b);
  line(x, 0, x, width);
  stroke(255-x/width*r%g,255-x/width*g%b,255-x/width*b%r);
  stroke(b, r, g);
  line(x, 0, width-x, width);
    x = x + 1; 
  if (x > width) { 
    x = 0;
    updateRGB();
    bounceCount++;
  } 
}

boolean shouldLoop = true;
void loopOnInput() {
  shouldLoop = !shouldLoop;
  if(shouldLoop) {
    loop();
  } else {
    noLoop();
  }
}

void mousePressed() {
  //loopOnInput();
  r = random(255);
  g = random(255);
  b = random(255);
}

void updateRGB() {
  r = (r+random(100))%255;
  g = (g+random(100))%255;
  b = (b+random(100))%255;
  println("r:" + r + ", g:" + g + ", b:" + b);
}

float[] rgbChanger(float r, float g, float b) {
  
  float[] rgb = new float[3];
  switch(int(random(5))) {
    case 0:
      rgb[0] = r;
      rgb[1] = g;
      rgb[2] = b;

    case 1:
      rgb[0] = g;
      rgb[1] = b;
      rgb[2] = r;
      break;
    case 2:
      rgb[0] = b;
      rgb[1] = r;
      rgb[2] = g;
      break;
    default:
      rgb[0] = r;
      rgb[1] = r;
      rgb[2] = r;
      break;
  }
  return rgb;
}

void keyPressed() {
  switch(key) {
    case ' ':
      loopOnInput();
      break;
     default:
  }
}
