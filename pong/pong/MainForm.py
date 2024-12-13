﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.R = System.Random()
        self.ballup = 0
        self.balld = 0
        self.flagleft = False
        self.flagright = False
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        self._lbltitle = System.Windows.Forms.Label()
        self._leftscore = System.Windows.Forms.Label()
        self._rightscore = System.Windows.Forms.Label()
        self._lblball = System.Windows.Forms.Label()
        self._lblleft = System.Windows.Forms.Label()
        self._lblright = System.Windows.Forms.Label()
        self._TimerDummy = System.Windows.Forms.Timer(self._components)
        self._Timerboolean = System.Windows.Forms.Timer(self._components)
        self._timerright = System.Windows.Forms.Timer(self._components)
        self._timerleft = System.Windows.Forms.Timer(self._components)
        self._timerballtick = System.Windows.Forms.Timer(self._components)
        self._timermulti = System.Windows.Forms.Timer(self._components)
        self.SuspendLayout()
        # 
        # lbltitle
        # 
        self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._lbltitle.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._lbltitle.Location = System.Drawing.Point(12, 25)
        self._lbltitle.Name = "lbltitle"
        self._lbltitle.Size = System.Drawing.Size(958, 52)
        self._lbltitle.TabIndex = 0
        self._lbltitle.Text = "Press enter to start or M to start multiplayer"
        self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # leftscore
        # 
        self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._leftscore.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._leftscore.Location = System.Drawing.Point(78, 96)
        self._leftscore.Name = "leftscore"
        self._leftscore.Size = System.Drawing.Size(166, 109)
        self._leftscore.TabIndex = 1
        self._leftscore.Text = "0"
        self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # rightscore
        # 
        self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._rightscore.ForeColor = System.Drawing.SystemColors.ButtonFace
        self._rightscore.Location = System.Drawing.Point(734, 96)
        self._rightscore.Name = "rightscore"
        self._rightscore.Size = System.Drawing.Size(166, 109)
        self._rightscore.TabIndex = 2
        self._rightscore.Text = "0"
        self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # lblball
        # 
        self._lblball.BackColor = System.Drawing.SystemColors.ButtonFace
        self._lblball.Location = System.Drawing.Point(479, 304)
        self._lblball.Name = "lblball"
        self._lblball.Size = System.Drawing.Size(20, 20)
        self._lblball.TabIndex = 3
        self._lblball.Click += self.LblballClick
        # 
        # lblleft
        # 
        self._lblleft.BackColor = System.Drawing.SystemColors.ButtonFace
        self._lblleft.Location = System.Drawing.Point(12, 246)
        self._lblleft.Name = "lblleft"
        self._lblleft.Size = System.Drawing.Size(20, 100)
        self._lblleft.TabIndex = 4
        # 
        # lblright
        # 
        self._lblright.BackColor = System.Drawing.SystemColors.ButtonFace
        self._lblright.Location = System.Drawing.Point(950, 246)
        self._lblright.Name = "lblright"
        self._lblright.Size = System.Drawing.Size(20, 100)
        self._lblright.TabIndex = 5
        # 
        # timerright
        # 
        self._timerright.Tick += self.TimerrightTick
        # 
        # timerleft
        # 
        self._timerleft.Tick += self.TimerleftTick
        # 
        # timerballtick
        # 
       
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaptionText
        self.ClientSize = System.Drawing.Size(988, 607)
        self.Controls.Add(self._lblright)
        self.Controls.Add(self._lblleft)
        self.Controls.Add(self._lblball)
        self.Controls.Add(self._rightscore)
        self.Controls.Add(self._leftscore)
        self.Controls.Add(self._lbltitle)
        self.Name = "MainForm"
        self.Text = "pong"
        self.Load += self.MainFormLoad
        self.SizeChanged += self.MainFormSizeChanged
        self.KeyDown += self.MainFormKeyDown
        self.ResumeLayout(False)


    def TimerballTick(self, sender, e):
        pass

    def MainFormKeyDown(self, sender, e):
        tball  = self._timerballtick
        tdum   = self._TimerDummy
        tbool  = self._Timerboolean
        tmult  = self._timermulti
        tleft  = self._timerleft
        tright = self._timerright
        bl     = self._lblball
        lpdl   = self._lblleft
        rpdl   = self._lblright
        title  = self._lbltitle
        
        def reset():
            title.Visible = True
            title.Text = "Press enter to start or M for Multiplay!"
            self._leftscore.Text = "0"
            self._rightscore.Text = "0"
            tball.Enabled = False
            tdum.Enabled =  False
            tbool.Enabled =  False
            tmult.Enabled =  False
            tleft.Enabled =  False
            tright.Enabled =  False
            bl.Left = self.Width // 2
            bl.Right = self.Height // 2
            lpdl.Top = (self.Height // 2) - 50 + lpdl.Height
            rpdl.Top = (self.Height // 2) - 50 + rpdl.Height
            
            bl.BackColor = Color.White
            
        if e.KeyCode == Keys.R:
            reset()
            
        if e.KeyCode == Keys.Enter:
            tball.Enabled = True
            tdum.Enabled = True
            tbool.Enabled = not tmult.Enabled
            title.Visible = False
            
        if e.KeyCode == Keys.M:
            reset()
            title.Visible = True
            Title.Text = "UUse W and S to move the left paddle; hit Enter to Start"
            tmult.Enabled = True
            
        if tdum.Enabled:
            if e.KeyCode == Keys.Up:
                self.flagright = False
                tright.Enabled = True
            elif e.KeyCode == Keys.Down:
                self.flagright = True
                tright.Enabled = True
                
        if tmult.Enabled and tball.Enabled:
            if e.Keycode == Keys.W:
                pass
                
            elif e.KeyCode == Keys.S:
                pass 
         
        
        
    def MainFormLoad(self, sender, e):
        """ TODO: ADD 3 UNIQUE SECRETS/CHEATS/EASTER EGGS
        IN TOTAL & FINISH MULTIPLAYER & SCOREBOARD & DUMMY AI """
        self.balld = 1
        self.ballup = self.R.Next(-4, 5)
    
    def pdlTick(self, pdl, flagd, tmr):
        if flagd == True:
            pdl.Top += 5
        else:
            pdl.Top -= 5
        if pdl.Top <= 10 or pdl.Bottom >= self.Height - 50:
            tmr.Enabled = False

    def TimerleftTick(self, sender, e):
        self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

    def TimerrightTick(self, sender, e):
        self.pdlTick(self._lblright, self.flagright, self._timerright)

    def LblballClick(self, sender, e):
        self._lblball.BackColor = Color.Red
        self.BackColor = Color.Green  # Form BG Color
        """ TODO: PUT MORE EASTER EGGS LATER """

    def MainFormSizeChanged(self, sender, e):
        self._lblright.Left = self.Width - 25 - self._lblright.Width
        self._rightscore.Left = self.Width - 75 - self._rightscore.Width
        self._lbltitle.Width = self.Width - 25
        self._lblball.Left = self.Width // 2
        self._lblball.Top = self.Height // 2