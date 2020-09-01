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
    public partial class Weekly_Updates : UserControl
    {
        // Global variable
        string Club;

        public Weekly_Updates(string clubname)
        {
            InitializeComponent();

            // set global variable
            Club = clubname;
        }

        // Display Date and Time
        private void Update_Club_Load(object sender, EventArgs e)
        {
            // Get current date and display it
            string datenow = DateTime.UtcNow.ToString("MM-dd-yyyy");
            Date.Text = "Today's date: " + datenow;

            // Get current time and display it
            string timenow = DateTime.Now.ToString("t");
            Time.Text = "Current time: " + timenow;
        }

        // Checks for Invalid Input and then shows a message box on success
        private void Submit_Click(object sender, EventArgs e)
        {
            if (tbWK.Text == "")
            {
                MessageBox.Show("Please enter an Update", "Invalid Field");
            }
            else
            {
                MessageBox.Show("Successful notified and updated", "Success");

                // Get date and time
                string datetime = DateTime.UtcNow.ToString();

                // Open connection
                Classes.SqlDBConnect con = new Classes.SqlDBConnect();

                /* Update Clubs table */

                // Query the database
                con.SqlQuery("UPDATE Clubs SET LastUpdated=@datetime WHERE ClubName=@clubname;");

                // Fill in
                con.cmd.Parameters.AddWithValue("@datetime", datetime);
                con.cmd.Parameters.AddWithValue("@clubname", Club.Trim());

                // Run
                con.NonQueryEx();

                /* Add to Activity table */

                // Get the category
                con.SqlQuery("SELECT cat FROM Clubs WHERE ClubName=@clubname;");
                con.cmd.Parameters.AddWithValue("@clubname", Club.Trim());

                string cat = "";
                foreach (DataRow dr in con.QueryEx().Rows)
                {
                    cat = dr["cat"].ToString();
                }


                // Query the database
                con.SqlQuery("INSERT INTO Activities VALUES (@club, @cat, @activity, @datetime);");

                // Fill in
                con.cmd.Parameters.AddWithValue("@club", Club);
                con.cmd.Parameters.AddWithValue("@cat", cat);
                con.cmd.Parameters.AddWithValue("@activity", tbWK.Text);
                con.cmd.Parameters.AddWithValue("@datetime", datetime);


                // Run
                con.NonQueryEx();

                // Close Connection
                con.con.Close();
            }
        }
    }
}
