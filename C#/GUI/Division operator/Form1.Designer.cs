namespace Division_operator
{
    partial class Form1
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
            this.label1 = new System.Windows.Forms.Label();
            this.tb5digits = new System.Windows.Forms.TextBox();
            this.btnSubmit = new System.Windows.Forms.Button();
            this.a = new System.Windows.Forms.Button();
            this.b = new System.Windows.Forms.Button();
            this.c = new System.Windows.Forms.Button();
            this.d = new System.Windows.Forms.Button();
            this.ed = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(20, 48);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(68, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Enter 5 digits";
            // 
            // tb5digits
            // 
            this.tb5digits.Location = new System.Drawing.Point(94, 45);
            this.tb5digits.Name = "tb5digits";
            this.tb5digits.Size = new System.Drawing.Size(100, 20);
            this.tb5digits.TabIndex = 1;
            // 
            // btnSubmit
            // 
            this.btnSubmit.Location = new System.Drawing.Point(205, 43);
            this.btnSubmit.Name = "btnSubmit";
            this.btnSubmit.Size = new System.Drawing.Size(75, 23);
            this.btnSubmit.TabIndex = 2;
            this.btnSubmit.Text = "Submit";
            this.btnSubmit.UseVisualStyleBackColor = true;
            this.btnSubmit.Click += new System.EventHandler(this.btnSubmit_Click);
            // 
            // a
            // 
            this.a.Enabled = false;
            this.a.Location = new System.Drawing.Point(30, 109);
            this.a.Name = "a";
            this.a.Size = new System.Drawing.Size(34, 38);
            this.a.TabIndex = 3;
            this.a.UseVisualStyleBackColor = true;
            // 
            // b
            // 
            this.b.Enabled = false;
            this.b.Location = new System.Drawing.Point(79, 109);
            this.b.Name = "b";
            this.b.Size = new System.Drawing.Size(34, 38);
            this.b.TabIndex = 3;
            this.b.UseVisualStyleBackColor = true;
            // 
            // c
            // 
            this.c.Enabled = false;
            this.c.Location = new System.Drawing.Point(130, 109);
            this.c.Name = "c";
            this.c.Size = new System.Drawing.Size(34, 38);
            this.c.TabIndex = 3;
            this.c.UseVisualStyleBackColor = true;
            // 
            // d
            // 
            this.d.Enabled = false;
            this.d.Location = new System.Drawing.Point(184, 109);
            this.d.Name = "d";
            this.d.Size = new System.Drawing.Size(34, 38);
            this.d.TabIndex = 3;
            this.d.UseVisualStyleBackColor = true;
            // 
            // ed
            // 
            this.ed.Enabled = false;
            this.ed.Location = new System.Drawing.Point(236, 109);
            this.ed.Name = "ed";
            this.ed.Size = new System.Drawing.Size(34, 38);
            this.ed.TabIndex = 3;
            this.ed.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(309, 204);
            this.Controls.Add(this.ed);
            this.Controls.Add(this.d);
            this.Controls.Add(this.c);
            this.Controls.Add(this.b);
            this.Controls.Add(this.a);
            this.Controls.Add(this.btnSubmit);
            this.Controls.Add(this.tb5digits);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tb5digits;
        private System.Windows.Forms.Button btnSubmit;
        private System.Windows.Forms.Button a;
        private System.Windows.Forms.Button b;
        private System.Windows.Forms.Button c;
        private System.Windows.Forms.Button d;
        private System.Windows.Forms.Button ed;
    }
}

