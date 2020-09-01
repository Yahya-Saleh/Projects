namespace Club_GUI
{
    partial class Student
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Student));
            this.guna2Elipse1 = new Guna.UI2.WinForms.Guna2Elipse(this.components);
            this.panelcontrol = new System.Windows.Forms.Panel();
            this.pictureBox5 = new System.Windows.Forms.PictureBox();
            this.Search = new Guna.UI2.WinForms.Guna2Button();
            this.pb = new System.Windows.Forms.PictureBox();
            this.exit = new Guna.UI2.WinForms.Guna2Button();
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.guna2GradientPanel1 = new Guna.UI2.WinForms.Guna2GradientPanel();
            this.Register = new Guna.UI2.WinForms.Guna2Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panelcontrol.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pb)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.guna2GradientPanel1.SuspendLayout();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // guna2Elipse1
            // 
            this.guna2Elipse1.BorderRadius = 18;
            this.guna2Elipse1.TargetControl = this;
            // 
            // panelcontrol
            // 
            this.panelcontrol.Controls.Add(this.pictureBox5);
            this.panelcontrol.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panelcontrol.Location = new System.Drawing.Point(108, 0);
            this.panelcontrol.Name = "panelcontrol";
            this.panelcontrol.Size = new System.Drawing.Size(727, 577);
            this.panelcontrol.TabIndex = 3;
            // 
            // pictureBox5
            // 
            this.pictureBox5.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox5.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox5.Image")));
            this.pictureBox5.Location = new System.Drawing.Point(738, 16);
            this.pictureBox5.Name = "pictureBox5";
            this.pictureBox5.Size = new System.Drawing.Size(38, 44);
            this.pictureBox5.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox5.TabIndex = 2;
            this.pictureBox5.TabStop = false;
            // 
            // Search
            // 
            this.Search.BackColor = System.Drawing.Color.Transparent;
            this.Search.BorderColor = System.Drawing.Color.Aqua;
            this.Search.BorderRadius = 24;
            this.Search.BorderThickness = 1;
            this.Search.ButtonMode = Guna.UI2.WinForms.Enums.ButtonMode.RadioButton;
            this.Search.Checked = true;
            this.Search.CheckedState.Parent = this.Search;
            this.Search.CustomImages.Parent = this.Search;
            this.Search.FillColor = System.Drawing.Color.Aqua;
            this.Search.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.Search.ForeColor = System.Drawing.Color.White;
            this.Search.HoverState.BorderColor = System.Drawing.Color.White;
            this.Search.HoverState.CustomBorderColor = System.Drawing.Color.White;
            this.Search.HoverState.FillColor = System.Drawing.Color.White;
            this.Search.HoverState.Image = ((System.Drawing.Image)(resources.GetObject("Search.HoverState.Image")));
            this.Search.HoverState.Parent = this.Search;
            this.Search.Image = ((System.Drawing.Image)(resources.GetObject("Search.Image")));
            this.Search.ImageSize = new System.Drawing.Size(30, 30);
            this.Search.Location = new System.Drawing.Point(17, 141);
            this.Search.Name = "Search";
            this.Search.ShadowDecoration.Parent = this.Search;
            this.Search.Size = new System.Drawing.Size(60, 50);
            this.Search.TabIndex = 0;
            this.Search.UseTransparentBackground = true;
            this.Search.Click += new System.EventHandler(this.Search_Click);
            // 
            // pb
            // 
            this.pb.BackColor = System.Drawing.Color.Transparent;
            this.pb.Image = ((System.Drawing.Image)(resources.GetObject("pb.Image")));
            this.pb.Location = new System.Drawing.Point(21, 95);
            this.pb.Name = "pb";
            this.pb.Size = new System.Drawing.Size(141, 153);
            this.pb.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pb.TabIndex = 1;
            this.pb.TabStop = false;
            // 
            // exit
            // 
            this.exit.BackColor = System.Drawing.Color.Transparent;
            this.exit.BorderColor = System.Drawing.Color.Aqua;
            this.exit.BorderRadius = 24;
            this.exit.BorderThickness = 1;
            this.exit.ButtonMode = Guna.UI2.WinForms.Enums.ButtonMode.RadioButton;
            this.exit.CheckedState.Parent = this.exit;
            this.exit.CustomImages.Parent = this.exit;
            this.exit.FillColor = System.Drawing.Color.MintCream;
            this.exit.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.exit.ForeColor = System.Drawing.Color.White;
            this.exit.HoverState.BorderColor = System.Drawing.Color.White;
            this.exit.HoverState.CustomBorderColor = System.Drawing.Color.White;
            this.exit.HoverState.FillColor = System.Drawing.Color.White;
            this.exit.HoverState.Image = ((System.Drawing.Image)(resources.GetObject("exit.HoverState.Image")));
            this.exit.HoverState.Parent = this.exit;
            this.exit.Image = ((System.Drawing.Image)(resources.GetObject("exit.Image")));
            this.exit.Location = new System.Drawing.Point(21, 489);
            this.exit.Name = "exit";
            this.exit.ShadowDecoration.Parent = this.exit;
            this.exit.Size = new System.Drawing.Size(60, 50);
            this.exit.TabIndex = 0;
            this.exit.UseTransparentBackground = true;
            this.exit.Click += new System.EventHandler(this.exit_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox2.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox2.Image")));
            this.pictureBox2.Location = new System.Drawing.Point(18, 15);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(66, 77);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox2.TabIndex = 2;
            this.pictureBox2.TabStop = false;
            // 
            // guna2GradientPanel1
            // 
            this.guna2GradientPanel1.BorderRadius = 18;
            this.guna2GradientPanel1.Controls.Add(this.pictureBox2);
            this.guna2GradientPanel1.Controls.Add(this.exit);
            this.guna2GradientPanel1.Controls.Add(this.Register);
            this.guna2GradientPanel1.Controls.Add(this.Search);
            this.guna2GradientPanel1.Controls.Add(this.pb);
            this.guna2GradientPanel1.FillColor = System.Drawing.Color.Aqua;
            this.guna2GradientPanel1.FillColor2 = System.Drawing.Color.DarkTurquoise;
            this.guna2GradientPanel1.Location = new System.Drawing.Point(9, 10);
            this.guna2GradientPanel1.Name = "guna2GradientPanel1";
            this.guna2GradientPanel1.ShadowDecoration.Parent = this.guna2GradientPanel1;
            this.guna2GradientPanel1.Size = new System.Drawing.Size(101, 551);
            this.guna2GradientPanel1.TabIndex = 0;
            // 
            // Register
            // 
            this.Register.BackColor = System.Drawing.Color.Transparent;
            this.Register.BorderColor = System.Drawing.Color.Aqua;
            this.Register.BorderRadius = 24;
            this.Register.BorderThickness = 1;
            this.Register.ButtonMode = Guna.UI2.WinForms.Enums.ButtonMode.RadioButton;
            this.Register.CheckedState.Image = ((System.Drawing.Image)(resources.GetObject("guna2Button3.CheckedState.Image")));
            this.Register.CheckedState.Parent = this.Register;
            this.Register.CustomImages.Parent = this.Register;
            this.Register.FillColor = System.Drawing.Color.Aqua;
            this.Register.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.Register.ForeColor = System.Drawing.Color.White;
            this.Register.HoverState.BorderColor = System.Drawing.Color.White;
            this.Register.HoverState.CustomBorderColor = System.Drawing.Color.White;
            this.Register.HoverState.FillColor = System.Drawing.Color.White;
            this.Register.HoverState.Image = ((System.Drawing.Image)(resources.GetObject("guna2Button3.HoverState.Image")));
            this.Register.HoverState.Parent = this.Register;
            this.Register.Image = ((System.Drawing.Image)(resources.GetObject("Register.Image")));
            this.Register.ImageSize = new System.Drawing.Size(30, 30);
            this.Register.Location = new System.Drawing.Point(21, 239);
            this.Register.Name = "Register";
            this.Register.ShadowDecoration.Parent = this.Register;
            this.Register.Size = new System.Drawing.Size(60, 50);
            this.Register.TabIndex = 0;
            this.Register.UseTransparentBackground = true;
            this.Register.Click += new System.EventHandler(this.Register_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.guna2GradientPanel1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(108, 577);
            this.panel1.TabIndex = 2;
            // 
            // Student
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(835, 577);
            this.Controls.Add(this.panelcontrol);
            this.Controls.Add(this.panel1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "Student";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Student";
            this.panelcontrol.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox5)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pb)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.guna2GradientPanel1.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private Guna.UI2.WinForms.Guna2Elipse guna2Elipse1;
        private System.Windows.Forms.Panel panelcontrol;
        private System.Windows.Forms.PictureBox pictureBox5;
        private Guna.UI2.WinForms.Guna2Button Search;
        private System.Windows.Forms.PictureBox pb;
        private Guna.UI2.WinForms.Guna2Button exit;
        private System.Windows.Forms.PictureBox pictureBox2;
        private Guna.UI2.WinForms.Guna2GradientPanel guna2GradientPanel1;
        private Guna.UI2.WinForms.Guna2Button Register;
        private System.Windows.Forms.Panel panel1;
    }
}