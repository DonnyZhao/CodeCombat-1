#http://codecombat.com/play/level/extra-extrapolation
shellAirTime = 3.4;  // in seconds

ogre = self.getNearestEnemy();
if(ogre):
    self.attackXY(ogre.pos.x, ogre.pos.y);

