namespace calculate_distance
{
    partial class btnClear
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
            this.lblspeed = new System.Windows.Forms.Label();
            this.lblTime = new System.Windows.Forms.Label();
            this.lblDistance = new System.Windows.Forms.Label();
            this.lblAnswer = new System.Windows.Forms.Label();
            this.tbSpeed = new System.Windows.Forms.TextBox();
            this.tbTime = new System.Windows.Forms.TextBox();
            this.btnCalculate = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblspeed
            // 
            this.lblspeed.AutoSize = true;
            this.lblspeed.Location = new System.Drawing.Point(27, 63);
            this.lblspeed.Name = "lblspeed";
            this.lblspeed.Size = new System.Drawing.Size(38, 13);
            this.lblspeed.TabIndex = 0;
            this.lblspeed.Text = "Speed";
            // 
            // lblTime
            // 
            this.lblTime.AutoSize = true;
            this.lblTime.Location = new System.Drawing.Point(27, 95);
            this.lblTime.Name = "lblTime";
            this.lblTime.Size = new System.Drawing.Size(30, 13);
            this.lblTime.TabIndex = 1;
            this.lblTime.Text = "Time";
            // 
            // lblDistance
            // 
            this.lblDistance.AutoSize = true;
            this.lblDistance.Location = new System.Drawing.Point(15, 141);
            this.lblDistance.Name = "lblDistance";
            this.lblDistance.Size = new System.Drawing.Size(49, 13);
            this.lblDistance.TabIndex = 2;
            this.lblDistance.Text = "Distance";
            // 
            // lblAnswer
            // 
            this.lblAnswer.AutoSize = true;
            this.lblAnswer.Location = new System.Drawing.Point(91, 141);
            this.lblAnswer.Name = "lblAnswer";
            this.lblAnswer.Size = new System.Drawing.Size(0, 13);
            this.lblAnswer.TabIndex = 3;
            // 
            // tbSpeed
            // 
            this.tbSpeed.Location = new System.Drawing.Point(94, 60);
            this.tbSpeed.Name = "tbSpeed";
            this.tbSpeed.Size = new System.Drawing.Size(76, 20);
            this.tbSpeed.TabIndex = 4;
            // 
            // tbTime
            // 
            this.tbTime.Location = new System.Drawing.Point(94, 92);
            this.tbTime.Name = "tbTime";
            this.tbTime.Size = new System.Drawing.Size(75, 20);
            this.tbTime.TabIndex = 5;
            // 
            // btnCalculate
            // 
            this.btnCalculate.Location = new System.Drawing.Point(30, 195);
            this.btnCalculate.Name = "btnCalculate";
            this.btnCalculate.Size = new System.Drawing.Size(63, 26);
            this.btnCalculate.TabIndex = 6;
            this.btnCalculate.Text = "Calculate";
            this.btnCalculate.UseVisualStyleBackColor = true;
            this.btnCalculate.Click += new System.EventHandler(this.btnCalculate_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(122, 195);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(64, 26);
            this.button1.TabIndex = 7;
            this.button1.Text = "clear";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // btnClear
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(247, 313);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.btnCalculate);
            this.Controls.Add(this.tbTime);
            this.Controls.Add(this.tbSpeed);
            this.Controls.Add(this.lblAnswer);
            this.Controls.Add(this.lblDistance);
            this.Controls.Add(this.lblTime);
            this.Controls.Add(this.lblspeed);
            this.Name = "btnClear";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblspeed;
        private System.Windows.Forms.Label lblTime;
        private System.Windows.Forms.Label lblDistance;
        private System.Windows.Forms.Label lblAnswer;
        private System.Windows.Forms.TextBox tbSpeed;
        private System.Windows.Forms.TextBox tbTime;
        private System.Windows.Forms.Button btnCalculate;
        private System.Windows.Forms.Button button1;
    }
}

