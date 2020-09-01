using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Club_GUI
{
    public partial class Update_Club_Description : UserControl
    {
        // Global variable
        string Club;

        public Update_Club_Description(string clubname)
        {
            InitializeComponent();

            // set global variable
            Club = clubname;
        }

        // Display current date and time
        private void Update_Club_Load(object sender, EventArgs e)
        {
            // Get current date and display it
            string datenow = DateTime.UtcNow.ToString("MM-dd-yyyy");
            Date.Text = "Today's date: " + datenow; ;

            // Get current time and display it
            string timenow = DateTime.Now.ToString("t");
            Time.Text = "Current time: " + timenow;
        }

        // Lets the user pick an image
        private void Browse_Click(object sender, EventArgs e)
        {
            OpenFileDialog opf = new OpenFileDialog();

            opf.Filter = "Choose Image(*.jpg;*.png;*.gif;*.ico)| *.jpg;*.png;*.gif;*.ico";
            
            if (opf.ShowDialog() == DialogResult.OK)
            {
                pbLogo.Image = Image.FromFile(opf.FileName);
            }
        }

        // Updates database
        private void Submit_Click(object sender, EventArgs e)
        {
            if (tbUD.Text == "")
            {
                MessageBox.Show("Please enter an Update", "Invalid Field");
            }
            else
            {
                MessageBox.Show("Successful updated", "Success");

                // Get date and time
                string datetime = DateTime.UtcNow.ToString();

                // Open connection
                Classes.SqlDBConnect con = new Classes.SqlDBConnect();

                // Query the database
                con.SqlQuery("UPDATE Clubs SET LastUpdated=@datetime, Description=@des WHERE ClubName=@clubname;");

                // Fill in
                con.cmd.Parameters.AddWithValue("@datetime", datetime);
                con.cmd.Parameters.AddWithValue("@des", tbUD.Text);
                con.cmd.Parameters.AddWithValue("@clubname", Club.Trim());

                // Run
                con.NonQueryEx();

                // Close Connection
                con.con.Close();
            }
        }
    }
}
